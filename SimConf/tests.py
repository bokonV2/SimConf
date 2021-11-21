from simconf import SimConf
from pprint import pprint
import timeit

conf = SimConf("test1", {}, True, False)
# conf = SimConf("test1", [], True, False)

# conf.ensure_ascii = False
#
conf["arg0"] = "arg00"
conf["arg1"] = "arg1"
conf["arg2"] = "arg2"
conf["arg3"] = "arg3"
conf["arg4"] = [1,2,3]
conf["arg4"].append(4)
conf["arg4"].append(8)

# conf[3] = 5
#


# conf.append(5)
# conf.append(2)
# conf.append(3)
# conf.append(7)
#
# pprint(conf.load_conf)
# pprint(conf[1:3])
# pprint(conf.get(5))
# pprint(conf.get("arg0"))

# conf.print_all()
# conf.set_default()
# conf.print_all()

# tt = {"1":2, "3":4}
# pprint(tt.items())
# pprint("")
# pprint(tt.values())
# pprint("")
# pprint(tt.keys())
# pprint("")

# pprint(len(conf))

pprint(conf.items())
pprint("")
pprint(conf.values())
pprint("")
pprint(conf.keys())
pprint("")
#
for c in conf.values():
    print(f"{c}\t")
