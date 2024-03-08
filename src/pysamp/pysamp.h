#ifndef PYSAMP_H
#define PYSAMP_H

#include "limited_api_python.h"
#include "timer.h"
#include "callbacks.h"


class PyGamemode;

class PySAMP
{
private:
	static PyGamemode* gamemode;
	static TimerManager* timer_manager;
	static CallbacksManager* callbacks;
public:
	static void load();
	static void reload();
	static void unload();
	static void disable();
	static bool isInitialized();
	static bool isLoaded();
	static bool isEnabled();
	static void addTimer(Timer& timer);
	static void removeTimer(int id);
	static void processTick(unsigned int currentTick);
	static int callback(const std::string& name);
	static int callback(const std::string& name, PyObject* pArgs);
	static int callback(const std::string& name, PyObject* pArgs, cell* retval, bool* stop);
	static bool onPlayerCommandText(int playerid, const char* cmdtext);
	static std::string getEncoding();
	static void registerCallback(const std::string& name, const std::string& format);
	static PyObject* pyConfig(PyObject *self, PyObject *args, PyObject *kwargs);
	static PyObject* amxParamsToTuple(AMX *amx, const std::string& callback_name, cell *params);
	static cell* tupleToAmxParams(PyObject *tuple, bool asReference = false);

	class GIL
	{
	public:
		GIL();
		~GIL();
	private:
		PyGILState_STATE gilState;
	};
};



#endif // PYSAMP_H
