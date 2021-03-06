# Simple Config
 Simple Attribute saving manager


## Installation

```bash
pip install simconf
```

## Documentation
### Init
```python
from SimConf import SimConf
config = SimConf(filename, default_atr, ensure_ascii, load_conf)
```
#### filename
```python
filename = "filename"
  (create filename.json)

filename = "folder/filename"
  (create filename.json in folder)
```

#### default_atr
```python
default_atr = {"key0": 0, "key1": 1 ...}
default_atr = ["arg0", "arg1" ...]
default_atr = {"key": {"key": [],},} etс.
```

#### ensure_ascii
 Standard json attribute
```python
ensure_ascii = bool()
```

#### load_conf
  if true, loads values from file, if there is no file, uses default_atr,
  if false, uses default_atr
```python
load_conf = bool()
```

### Use

#### Get arg
```python
  ####Dict
arg = config["key"]
arg = config.get("key")

  ####List
arg = config[int(key)]
arg = config.get(int(key))
```

#### Set atr and create new
```python
####Dict
config["key"] = atr
config["keyNew"] = atr
config.append("key", atr)

####List
config.append(atr)
config[int(key)] = atr
```

#### Set default data
```python
config.set_default() #use default_atr
```

#### Get default data
```python
data = config.get_default()
```

#### Get data
```python
data = config.data
```

#### Print in console all saves
```python
config.print_all()
```

#### Get Len
```python
len(config)
```

#### Get Iterable items
```python
config.__iter__()
config.keys()
config.values()
config.items()
```

#### Forcibly get data
```python
data = config.load()
```

#### Forcibly save data
```python
data = config.save()
```

#### Print data in console
```python
config.print_all()
```

### Support
 - **Telegramm** https://t.me/Rahazb
 - **Email** bokon2014@yandex.ru
 - **Git issues** https://github.com/bokonV2/SimConf/issues
