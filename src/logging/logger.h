#pragma once

#include<string>
#include<sstream>

#include <chrono>
#include <ctime>
#include <iomanip>

enum class LogLevel { TRACE = 0, DEBUG, INFO, WARN, ERROR, FATAL };
extern std::string LogLevelStrings[];

class Logger {
private:
	static LogLevel globalLevel;
	LogLevel level;
	std::string name;
	std::string prepare(LogLevel level, const char* text);
public:
	Logger(std::string name) : name(name), level(LogLevel::INFO) {};

	static void setGlobalLevel(LogLevel newLevel);
	void setLevel(LogLevel newLevel);

	void trace(const char* fmt, ...);
	void debug(const char* fmt, ...);
	void info(const char* fmt, ...);
	void warn(const char* fmt, ...);
	void error(const char* fmt, ...);
};