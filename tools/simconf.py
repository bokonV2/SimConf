import json


class SimConf:
    """filename is used to set the name and path of saving attributes,
    example: filename= "config" or filename= "folder/config",
    standard: "config" """
    filename = "config"

    """default_atr is used to define standard values and reset to these
    values if necessary, it can only be a list or a dict and
    contain any attributes inside it,
    example: {atr: "atr", ...} or [atr, ...],
    standard: {} """
    default_atr = {}

    """ensure_ascii takes a boolean value, a standard json attribute"""
    ensure_ascii = True

    """load_conf accepts boolean values, if true, it loads values from
    a file, if there is no file, it uses default_atr, if false, it
    uses default_atr"""
    load_conf = True

    def __init__(self,
                 filename="config", default_atr={},
                 ensure_ascii=True, load_conf=True
                 ):

        self._name_property(filename)
        self._default_property(default_atr)
        self._ascii_property(ensure_ascii)

        if load_conf:
            self.data = self.load()
        else:
            self.data = self.default_atr

    def __setattr__(self, obj, val):
        super().__setattr__(obj, val)
        if obj == "filename" or obj == "default_atr" or obj == "ensure_ascii":
            return
        self.save()

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, val):
        self.data[key] = val
        self.save()

    def _name_property(self, name):
        if type(name) == type(str()):
            self.filename = name
        else:
            raise AttributeError("filename use only string")

    def _default_property(self, obj):
        if type(obj) == type(list()) or type(obj) == type(dict()):
            self.default_atr = obj
        else:
            raise AttributeError("default_atr use only dict or list")

    def _ascii_property(self, obj):
        if type(obj) == type(bool()):
            self.ensure_ascii = obj
        else:
            raise AttributeError("ensure_ascii use only bool")

    def load(self):
        try:
            with open(f"{self.filename}.json", "r", encoding="UTF-8") as file:
                data = json.load(file)
        except:
            data = self.default()
        return data

    def save(self):
        with open(f"{self.filename}.json", "w", encoding="UTF-8") as file:
            json.dump(self.data, file, ensure_ascii=self.ensure_ascii, indent=4)

    def set_default(self):
        self.data = self.default_atr

    def default(self):
        data = self.default_atr
        return data

    def print_all(self):
        if type(self.data) == type(dict()):
            for key, value in self.data.items():
                print(key, value, sep=" <===> ")
        else:
            for value in self.data:
                print(value)


if __name__ == '__main__':
    default_atr = [1,2,3]
    cnf = SimConf(filename="test", default_atr=default_atr)
    # cnf["tt"] = [1,2,3,4, {"atr": 12., "booll":False}]
    # print(cnf["tt"][-1]["booll"])
    cnf.print_all()