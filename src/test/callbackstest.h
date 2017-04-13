#ifndef CALLBACKSTEST_H
#define CALLBACKSTEST_H

#include "Python.h"
#include "pysamp.h"
#include <iostream>

class CallbacksTest
{
private:
public:
	static bool testCallback(const char* name, const char* params);
	static void runAll();
};




#endif // !CALLBACKSTEST_H
