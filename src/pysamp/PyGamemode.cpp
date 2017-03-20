#include "PyGamemode.h"


//see http://stackoverflow.com/questions/8032080/how-to-convert-char-to-wchar-t
const wchar_t *GetWC(const char *c)
{
	const size_t cSize = strlen(c) + 1;
	wchar_t* wc = new wchar_t[cSize];
	mbstowcs(wc, c, cSize);

	return wc;
}

//see http://stackoverflow.com/questions/3418231/replace-part-of-a-string-with-another-string
void replaceAll(std::string& str, const std::string& from, const std::string& to) {
	if (from.empty())
		return;
	size_t start_pos = 0;
	while ((start_pos = str.find(from, start_pos)) != std::string::npos) {
		str.replace(start_pos, from.length(), to);
		start_pos += to.length(); // In case 'to' contains 'from', like replacing 'x' with 'yx'
	}
}

PyGamemode::PyGamemode(const char * path)
{
	Py_Initialize();
	char cCurrentPath[FILENAME_MAX];
	GetCurrentDir(cCurrentPath, sizeof(cCurrentPath));
	char* absolute = std::strcat(cCurrentPath, path);
#ifdef WIN32
	std::string p(absolute);
	std::string from("\\");
	std::string to("\\\\");
	replaceAll(p, from, to);
	delete(absolute);
	absolute = new char[p.length() + 1];
	strcpy(absolute, p.c_str());
#endif
	PyRun_SimpleString("import sys");
	char* pyCode;
	sprintf(pyCode, "sys.path.append(\"%s\")", absolute);
	sampgdk::logprintf("Running: %s", pyCode);
	PyRun_SimpleString(pyCode);
	pName = PyUnicode_DecodeFSDefault("gamemode");
	/* Error checking of pName left out */
	pModule = PyImport_Import(pName);

	if (pModule != NULL) {
		initialized = true;
		sampgdk::logprintf("PyGamemode loaded!");
	}
	else
	{
		sampgdk::logprintf("PyGamemode::PyGamemode(%s%s) failed!", absolute, "gamemode.py");
	}
	delete(absolute);
}

PyGamemode::~PyGamemode()
{
	delete this->pDict, this->pModule, this->pName;
}

bool PyGamemode::callback(const char * name, PyObject * pArgs)
{
	sampgdk::logprintf("PyGamemode::callback(%s, ...)", name);
	PyObject* pFunc = PyObject_GetAttrString(pModule, name);

	if (pFunc && PyCallable_Check(pFunc)) 
	{
		PyObject* pValue = PyObject_CallObject(pFunc, pArgs);
		if (PyErr_Occurred())
			PyErr_Print();
		//Py_XINCREF(pValue);
		////Py_XDECREF(pValue);

		//bool ret = false;
		//if (pValue != NULL) 
		//{
		//	int tru = PyObject_IsTrue(pValue);
		//	if (tru == -1)
		//		sampgdk::logprintf("An error occured at %s in python gamemode. It doesn't return boolean.", name);
		//	else
		//		ret = tru == 1;
		//}

		//delete pValue;
		//sampgdk::logprintf("%s called with return %i", name, ret);

		//Py_XDECREF(pFunc);
		return false;
	}
	else
	{
		sampgdk::logprintf("Calling %s failed.", name);
	}
	Py_XDECREF(pFunc);
	return false;
}