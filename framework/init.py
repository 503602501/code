
import  hashlib

key =globals()["key"]
account =globals()["account"]
m = hashlib.md5()
m.update(str.encode("utf8"))
file = open("/"+m.hexdigest(),'w',encoding="utf-8")
file.write(key)
file.close()


