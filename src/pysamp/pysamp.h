#ifndef PYSAMP_H
#define PYSAMP_H

#if PY_TEST == 0
	#ifdef WIN32
	#define PYTHON_PATH "\\python"
	#else
	#define PYTHON_PATH "/python"
	#endif
#else
	#ifdef WIN32
	#define PYTHON_PATH "\\python\\test"
	#else
	#define PYTHON_PATH "/python/test"
	#endif
#endif // DEBUG


#include "pygamemode.h"
#include "timer.h"


class PyGamemode;

class PySAMP
{
private:
	static PyGamemode* gamemode;
	static TimerManager* timer_manager;
public:
	static void load();
	static void reload();
	static void unload();
	static void disable();
	static int callback(const char* name, PyObject * pArgs);
	static int callback(const char* name, PyObject * pArgs, bool obtainLock);
	static bool isInitialized();
	static bool isLoaded();
	static bool isEnabled();
	static void addTimer(Timer& timer);
	static void removeTimer(int id);
	static void processTick(unsigned int currentTick);
};



#endif // PYSAMP_H
