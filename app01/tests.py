from django.test import TestCase

# Create your tests here.


# 当前path 如何与 paths匹配
# 不能用in   /users/delete/9
# 正则匹配


li = ['/users/', '/users/add', '/users/delete/(\\d+)', '/users/edit/(\\d+)']

c_path = "/users/delete/9"

import re

flag = False

for permission in li:
    permission = "^%s$" % permission
    ret = re.match(permission, c_path)
    if ret:
        flag = True
        break

if flag:
    print("success")

# ret = re.match("/users/", "/users/delete/9")
ret = re.match("^/users/$", "/users/delete/9")
print(ret)
