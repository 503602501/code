
import  hashlib

key =globals()["key"]
account =globals()["account"]
m = hashlib.md5()
m.update(str.encode("utf8"))
with open("../../config/"+m.hexdigest(), "w") as x:
    x.write(key)