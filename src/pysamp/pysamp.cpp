#include "pysamp.h"

PyGamemode* PySAMP::gamemode = nullptr;
TimerManager* PySAMP::timer_manager = nullptr;


void PySAMP::load()
{
	sampgdk::logprintf("Loading PySAMP gamemode");
	PySAMP::gamemode = new PyGamemode(PYTHON_PATH);
	gamemode->load();
	PySAMP::timer_manager = new TimerManager();
}

void PySAMP::reload()
{
	sampgdk::logprintf("Reloading PySAMP gamemode");
	if (PySAMP::isLoaded())
	{
		PySAMP::gamemode->reload();
		PySAMP::timer_manager->enable();
		PySAMP::timer_manager->clear_timers();
	}
}

void PySAMP::disable()
{
	if (PySAMP::isLoaded())
	{
		PySAMP::gamemode->disable();
		PySAMP::timer_manager->disable();
	}
}

void PySAMP::unload()
{
	sampgdk::logprintf("Unloading PySAMP gamemode");
	delete PySAMP::gamemode;
	PySAMP::gamemode = nullptr;
	delete PySAMP::timer_manager;
	PySAMP::timer_manager = nullptr;
}

int PySAMP::callback(const char * name, PyObject * pArgs)
{
	return PySAMP::callback(name, pArgs, true);
}

int PySAMP::callback(const char * name, PyObject * pArgs, bool obtainLock)
{
	if(PySAMP::gamemode && PySAMP::gamemode->isLoaded())
		return PySAMP::gamemode->callback(name, pArgs, obtainLock);
	return 0;
}

bool PySAMP::isInitialized()
{
	return !!PySAMP::gamemode;
}

bool PySAMP::isLoaded()
{
	return PySAMP::isInitialized() && PySAMP::gamemode->isLoaded();
}

bool PySAMP::isEnabled()
{
	return PySAMP::isLoaded() && PySAMP::gamemode->isEnabled();
}

void PySAMP::addTimer(Timer& timer)
{
	PySAMP::timer_manager->add_timer(timer);
}

void PySAMP::removeTimer(int id)
{
	PySAMP::timer_manager->remove_timer(id);
}

void PySAMP::processTick(unsigned int currentTick)
{
	PySAMP::timer_manager->process_timers(currentTick);
}
