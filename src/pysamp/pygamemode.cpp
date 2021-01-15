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
	sampgdk::logprintf("PyGamemode::PyGamemode(%s)", path);
	SAMPConsts::create();
	if (PyImport_AppendInittab("pysamp", &PyInit_samp) == -1) {
		sampgdk::logprintf("Couldn't load module.");
		return;
	}

	Py_Initialize();
	char cCurrentPath[FILENAME_MAX];
	GetCurrentDir(cCurrentPath, sizeof(cCurrentPath));
	char* absolute = strcat(cCurrentPath, path);

	PyObject* sysPath = PySys_GetObject("path");

	if(!sysPath)
		sampgdk::logprintf("Setting python workspace failed.");

	PyList_Append(sysPath, PyUnicode_FromString(absolute));
}

PyGamemode::~PyGamemode()
{
	PyGamemode::unload();
}

void PyGamemode::load()
{
	pName = PyUnicode_DecodeFSDefault("gamemode");
	pModule = PyImport_Import(pName);
	Py_XINCREF(pModule);
	Py_XDECREF (pName);
	if (!pModule) 
	{
		PyErr_Print();
		sampgdk::logprintf("PyGamemode::PyGamemode(%s) failed!", "gamemode.py");
	} else {
		loaded = true;
	}
	disabled = false;
}

void PyGamemode::reload()
{
	if (pModule)
	{
		sampgdk::logprintf("PyGamemode::reload()-begin");
		PyObject* pNewModule = PyImport_ReloadModule(pModule);
		if (!pNewModule) 
		{
			PyErr_Print();
			sampgdk::logprintf("PyGamemode::PyGamemode(%s) failed!", "gamemode.py");
		} else {
			Py_XDECREF(pModule);
			Py_XINCREF(pNewModule);
			pModule = pNewModule;
		}
		sampgdk::logprintf("PyGamemode::reload()-end");
		disabled = false;
	}
}

void PyGamemode::unload()
{
	if (pModule) 
	{
		Py_XDECREF(pModule);
		Py_FinalizeEx();
	}
	loaded = false;
}

void PyGamemode::disable()
{
	disabled = true;
}

bool PyGamemode::isLoaded()
{
	return PyGamemode::loaded;
}
bool PyGamemode::isEnabled()
{
	return PyGamemode::isLoaded() && !PyGamemode::disabled;
}

bool PyGamemode::callback(const char * name, PyObject * pArgs, bool obtainLock)
{
	bool ret = false;
	// if Module does not exists don't forward callback to python function
	if (disabled || !pModule) {
		return ret;
	}

	PyGILState_STATE gstate;

	if (obtainLock)
	{
		gstate = PyGILState_Ensure();
	}

	PyObject* pFunc = PyObject_GetAttrString(pModule, name);

	if(pFunc) {
		Py_INCREF(pFunc);
	}
	
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

		ret = false;
		if (pValue) 
		{
			int tru = PyObject_IsTrue(pValue);
			if (tru == -1)
				sampgdk::logprintf("An error occured at %s in python gamemode. It doesn't return boolean.", name);
			else
				ret = tru == 1;
		}

		//Py_XDECREF(pValue);
		Py_XDECREF(pFunc);
		if (pArgs)
			Py_XDECREF(pArgs);
	}	
	
	if (obtainLock)
	{
		PyGILState_Release(gstate);
	}

	return ret;
}
