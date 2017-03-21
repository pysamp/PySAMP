# pySAMP
PySAMP is a SA-MP plugin that allows you to create gamemodes with the python language. All API functions and callbacks will be supported soon.

# Call-By-Reference functions

# Usage

```C
public OnGameModeInit()
{
  SetGameModeText("GameModeText");
  AddPlayerClass(0, 1958.3783, 1343.1572, 15.3746, 269.1425, 0, 0, 0, 0, 0, 0);
  AddPlayerClass(18, 1960.3783, 1343.1572, 15.3746, 269.1425, 0, 0, 0, 0, 0, 0);
  AddPlayerClass(0,1585.1819,-1674.7336,5.8949,176.0211,0,0,0,0,0,0);
  return 1;
}
```

```python
def OnGameModeInit():
  SetGameModeText("GameModeText")
  AddPlayerClass(0, 1958.3783, 1343.1572, 15.3746, 269.1425, 0, 0, 0, 0, 0, 0)
  AddPlayerClass(18, 1960.3783, 1343.1572, 15.3746, 269.1425, 0, 0, 0, 0, 0, 0)
  AddPlayerClass(0,1585.1819,-1674.7336,5.8949,176.0211,0,0,0,0,0,0)
  return 1
```
