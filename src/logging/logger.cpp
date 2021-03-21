#include "logger.h"
#include "sampgdk.h"

LogLevel Logger::globalLevel = LogLevel::INFO;

std::string LogLevelStrings[] = {
	"TRACE",
	"DEBUG",
	"INFO",
	"WARN",
	"ERROR",
	"FATAL"
};

std::string Logger::prepare(LogLevel level, const char* text)
{
	std::stringstream stream;
	stream << LogLevelStrings[(int)level] << "::" << this->name << "::";

	auto now = std::chrono::system_clock::now();
	auto in_time_t = std::chrono::system_clock::to_time_t(now);

	stream << std::put_time(std::localtime(&in_time_t), "%Y-%m-%d %X");
	stream << "::" << text;
	return stream.str();
}

void Logger::setGlobalLevel(LogLevel newLevel)
{
	Logger::globalLevel = newLevel;
}

void Logger::setLevel(LogLevel newLevel)
{
	this->level = newLevel;
}

void Logger::trace(const char* fmt, ...)
{
	if (this->level <= LogLevel::TRACE || Logger::globalLevel <= LogLevel::TRACE)
	{
		std::string prepared = prepare(LogLevel::TRACE, fmt);
		va_list args;
		va_start(args, fmt);
		sampgdk_vlogprintf(prepared.c_str(), args);
		va_end(args);
	}
}

void Logger::debug(const char* fmt, ...)
{
	if (this->level <= LogLevel::DEBUG || Logger::globalLevel <= LogLevel::DEBUG)
	{
		std::string prepared = prepare(LogLevel::DEBUG, fmt);
		va_list args;
		va_start(args, fmt);
		sampgdk_vlogprintf(prepared.c_str(), args);
		va_end(args);
	}
}

void Logger::info(const char* fmt, ...)
{
	if (this->level <= LogLevel::INFO || Logger::globalLevel <= LogLevel::INFO)
	{
		std::string prepared = prepare(LogLevel::INFO, fmt);
		va_list args;
		va_start(args, fmt);
		sampgdk_vlogprintf(prepared.c_str(), args);
		va_end(args);
	}
}

void Logger::warn(const char* fmt, ...)
{
	if (this->level <= LogLevel::WARN || Logger::globalLevel <= LogLevel::WARN)
	{
		std::string prepared = prepare(LogLevel::WARN, fmt);
		va_list args;
		va_start(args, fmt);
		sampgdk_vlogprintf(prepared.c_str(), args);
		va_end(args);
	}
}

void Logger::error(const char* fmt, ...)
{
	if (this->level <= LogLevel::ERROR || Logger::globalLevel <= LogLevel::ERROR)
	{
		std::string prepared = prepare(LogLevel::ERROR, fmt);
		va_list args;
		va_start(args, fmt);
		sampgdk_vlogprintf(prepared.c_str(), args);
		va_end(args);
	}
}
