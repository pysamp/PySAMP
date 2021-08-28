#include "pygamemode.h"
#include "samp.h"

std::string logprintf_buffer;

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

	PyObject *module = PyImport_ImportModule("pysamp");
	if(!module) {
		sampgdk::logprintf("Couldn't import module:");
		PyErr_Print();
	}

	for(auto item = SAMPConsts::map.begin(); item != SAMPConsts::map.end(); ++item) {
		if(PyObject_SetAttrString(
			module,
			item->first.c_str(),
			Py_BuildValue("i", item->second)
		) == -1) {
			sampgdk::logprintf("Couldn't set constants on module:");
			PyErr_Print();
			break;
		}
	}

	this->config = {
		{"encoding", Py_BuildValue("s", "cp1252")}
	};
	PyInit_setGamemode(this);
}

PyGamemode::~PyGamemode()
{
	PyInit_setGamemode(NULL);

	for(const auto item : this->config)
		Py_DECREF(item.second);

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

PyObject* PyGamemode::pyConfig(PyObject *self, PyObject *args, PyObject *kwargs)
{
	if(PyTuple_Size(args) != 0)
	{
		PyErr_SetString(
			PyExc_ValueError,
			"config() does not take any positional argument"
		);
		return NULL;
	}

	if(kwargs == NULL)
	{
		PyObject* return_value = PyDict_New();

		for(auto item : this->config)
			PyDict_SetItemString(return_value, item.first.c_str(), item.second);

		return return_value;
	}

	PyObject* items = PyDict_Items(kwargs);

	for(int i = 0; i < PyList_Size(items); ++i)
	{
		PyObject* item = PyList_GetItem(items, i);
		const char *key_name = PyUnicode_AsUTF8AndSize(
			PyTuple_GetItem(item, 0),
			NULL
		);

		if(this->config.count(key_name) < 1)
		{
			PyErr_Format(
				PyExc_ValueError,
				"config() key %s does not exist",
				key_name
			);
			return NULL;
		}

		this->config[key_name] = PyTuple_GetItem(item, 1);
	}

	Py_DECREF(items);
	Py_RETURN_NONE;
}

int PyGamemode::callback(const char * name, PyObject * pArgs, bool obtainLock)
{
	int ret = -1;
	// if Module does not exists don't forward callback to python function
	if (disabled || !pModule)
		return ret;

	PyGILState_STATE gstate;

	if (obtainLock)
		gstate = PyGILState_Ensure();

	if (!PyObject_HasAttrString(pModule, name))
		return ret;

	PyObject* pFunc = PyObject_GetAttrString(pModule, name);

	if (pFunc)
		Py_INCREF(pFunc);

	if (pArgs)
		Py_INCREF(pArgs);

	if (pFunc && PyCallable_Check(pFunc))
	{
		PyObject* pValue = PyObject_CallObject(pFunc, pArgs);

		if (PyErr_Occurred())
		{
			PyErr_Print();
			pValue = Py_None;
		}

		if (pValue != Py_None)
		{
			int truthy = PyObject_IsTrue(pValue);
			if (truthy != -1)
				ret = truthy;
			else
			{
				sampgdk::logprintf("An error occured at %s in Python gamemode.", name);
				PyErr_Print();
			}
		}

		Py_XDECREF(pValue);
		Py_XDECREF(pFunc);
		Py_XDECREF(pArgs);
	}

	if (obtainLock)
		PyGILState_Release(gstate);

	return ret;
}
