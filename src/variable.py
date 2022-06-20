import this
# The Zen of Python, by Tim Peters   
# Beautiful is better than ugly.
message = "hello Python world"
print(message)
# 变量名只能包含字母、数字和下划线。变量名可以字母或下划线打头，但不能以数字打头

name = "ada lovelace"
print(name.title()) # Ada Lovelace
print(name.upper()) # 返回大写
print(name.lower()) # 返回小写
string = "hello "
print(string.rstrip() == 'hello') # 删除右侧空白 True 对应 左 lstrip 两侧 strip
print(string.rstrip() == 'hello') # 删除空白 False


# python2 中 可以直接使用 print str

#  str方法， 转换字符串 如下示例
age = 20
name = "jack"
# print(name + age) # 报错can only concatenate str (not "int") to str
print(name + str(age))

# python2 中数字运算区别 
print(3 / 2) # 1 Python返回的结果为1，而不是1.5。在Python 2中，整数除法的结果只包含整数部分，小数部分被删除。请注意，计算整数结果时，采取的方式不是四舍五入，而是将小数部分直接删除。

print(3.0 / 2) # 1.5

# 注释就是 # 符号开头 Python解释器将忽略