#include "pygamemode.h"


//see http://stackoverflow.com/questions/8032080/how-to-convert-char-to-wchar-t
const wchar_t *GetWC(const char *c)
{
	const size_t cSize = strlen(c) + 1;
	wchar_t* wc = new wchar_t[cSize];
	mbstowcs(wc, c, cSize);

	return wc;
}

PyGamemode::PyGamemode(const char * path)
{
	SAMPConsts::create();
	if (PyImport_AppendInittab("pysamp", &PyInit_samp) == -1) {
		sampgdk::logprintf("Couldn't load module.");
		return;
	}
	// see 
	dlopen("libpython3.5m.so", RTLD_LAZY | RTLD_GLOBAL);
	Py_Initialize();
	char cCurrentPath[FILENAME_MAX];
	GetCurrentDir(cCurrentPath, sizeof(cCurrentPath));
	char* absolute = strcat(cCurrentPath, path);
	
	PyObject* sysPath = PySys_GetObject("path");

	if(!sysPath)
		sampgdk::logprintf("Setting python workspace failed.");

	PyList_Append(sysPath, PyUnicode_FromString(absolute));

	pName = PyUnicode_DecodeFSDefault("gamemode");
	pModule = PyImport_Import(pName);
	if (!pModule) 
	{
		PyErr_Print();
		sampgdk::logprintf("PyGamemode::PyGamemode(%s) failed!", "gamemode.py");
	}

}

PyGamemode::~PyGamemode()
{
	delete this->pDict, this->pModule, this->pName;
}

bool PyGamemode::callback(const char * name, PyObject * pArgs)
{
	PyGILState_STATE gstate;
	gstate = PyGILState_Ensure();

	// if Module does not exists don't forward callback to python function
	if (!pModule) {
		return false;
	}

	PyObject* pFunc = PyObject_GetAttrString(pModule, name);

	if(pFunc)
		Py_INCREF(pFunc);
	
	if (pArgs) {
		Py_INCREF(pArgs);
	}
	

	if (pFunc && PyCallable_Check(pFunc) == 1) 
	{
		PyObject* pValue = PyObject_CallObject(pFunc, pArgs);

		//ignore error if pFunc not available
		if (PyErr_Occurred())
			PyErr_Print();
			//PyErr_Clear();

		bool ret = false;
		if (pValue) 
		{
			int tru = PyObject_IsTrue(pValue);
			if (tru == -1)
				sampgdk::logprintf("An error occured at %s in python gamemode. It doesn't return boolean.", name);
			else
				ret = tru == 1;
		}

		//sampgdk::logprintf("%s called with return %i", name, ret);

		Py_XDECREF(pValue);
		Py_XDECREF(pFunc);
		if (pArgs)
			Py_XDECREF(pArgs);
		return ret;
	}	
	
	return false;
}
