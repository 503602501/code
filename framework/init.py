
from com.util.key_util  import KeyUtil
import  hashlib
#一端认证的代码块#

#动态生成字段种包含账号和密码的加密信息

key =globals()["key"]
account =globals()["account"]

with open("../../config/"+KeyUtil.md5vale(account), "w",encoding="utf-8") as x:
    x.write(key)
