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

		_remove_timer(timer);
		break;
	}
}

void TimerManager::process_timers(unsigned int current_tick)
{
	if(disabled)
		return;

	bool did_i_break;

	do
	{
		did_i_break = false;

		for(auto timer = timers.begin(); timer != timers.end(); ++timer)
		{
			bool repeating = timer->is_repeating();

			if(!timer->process(current_tick))
				continue;

			if(!repeating)
				_remove_timer(timer);

			// XXX: Both process() and _remove_timer() could invalidate iterator
			did_i_break = true;
			break;
		}
	} while(did_i_break);
}

void TimerManager::clear_timers()
{
	for(auto timer = timers.begin(); timer != timers.end(); ++timer)
		timer = _remove_timer(timer);
}

std::deque<Timer>::iterator TimerManager::_remove_timer(std::deque<Timer>::iterator timer)
{
	return timers.erase(timer);
}
