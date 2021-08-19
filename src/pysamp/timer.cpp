#include "timer.h"


int Timer::last_timer_id;

Timer::Timer(
	PyObject* function,
	PyObject* arguments,
	unsigned int interval,
	bool repeating
) :
	function(function),
	arguments(arguments),
	interval(interval),
	repeating(repeating)
{
	id = ++last_timer_id;
	last_call_tick = GetTickCount();
	Py_INCREF(function);
	Py_XINCREF(arguments);
}

Timer::~Timer()
{
	Py_DECREF(function);
	Py_XDECREF(arguments);
}

bool Timer::process(unsigned int current_tick)
{
	if((last_call_tick + interval) > current_tick)
		return false;

	last_call_tick = current_tick;
	PyObject_CallObject(function, arguments);

	if(PyErr_Occurred() != NULL)
	{
		PyErr_Print();
		return false;
	}

	return true;
}


TimerManager::TimerManager()
: disabled(false)
{
	Timer::last_timer_id = -1;
}

void TimerManager::add_timer(Timer& timer)
{
	timers.push_back(timer);
}

void TimerManager::remove_timer(int id)
{
	for(auto timer = timers.begin(); timer != timers.end(); ++timer)
	{
		if(timer->get_id() != id)
			continue;

		timers.erase(timer);
		break;
	}
}

void TimerManager::process_timers(unsigned int current_tick)
{
	if(disabled)
		return;

	for(auto timer = timers.begin(); timer != timers.end();)
	{
		int id = timer->get_id();
		bool repeating = timer->is_repeating();

		if(!timer->process(current_tick))
		{
			// Current timer wasn't processed
			++timer;
			continue;
		}

		if(
			!repeating
			&& _timer_exists(id)
		)
		{
			// Current timer was processed and doesn't repeat
			timer = timers.erase(timer);
			continue;
		}

		// Current timer was processed and repeats, process next
		++timer;
	}
}

void TimerManager::clear_timers()
{
	for(auto timer = timers.begin(); timer != timers.end();)
		timer = timers.erase(timer);
}

bool TimerManager::_timer_exists(int id)
{
	for(auto timer = timers.begin(); timer != timers.end(); ++timer)
		if(timer->get_id() == id)
			return true;

	return false;
}
