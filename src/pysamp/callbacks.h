#ifndef CALLBACKSMANAGER_H
#define CALLBACKSMANAGER_H

#include <string>
#include <unordered_map>


class CallbacksManager
{
public:
	const std::string* getFormat(const std::string& name) const;
	int getBadret(const std::string& name) const;
	void addFormat(const std::string& name, const std::string& format);

private:
	static std::unordered_map<std::string, std::string> formats;
	static const std::unordered_map<std::string, bool> badrets;
};

#endif
