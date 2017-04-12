#ifndef CALLBACKSTEST_H
#define CALLBACKSTEST_H

#include "Python.h"
#include "PySAMP.h"

class CallbacksTest
{
private:
public:
	static bool testCallback(const char* name, const char* params);
};




#endif // !CALLBACKSTEST_H
