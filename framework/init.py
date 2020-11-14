

#一端认证的代码块#

#动态生成字段种包含账号和密码的加密信息

key =globals()["key"]

message='Hello world!xxxxx'
print("key:"+key)

# 复杂运算 key 和# message ,输出data
data = message+"iiiiii"

file = open("./local_key",'w')
file.write(data+key)
file.close()

