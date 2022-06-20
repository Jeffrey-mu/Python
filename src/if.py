# if 语句
num = 20
if (num == 20):
    print('num 等于 20')

if (num == 30):
    print('num 等于 30')
else:
    print('num 不等于 30')
# 检查是否相等
name = 'tome'
new_name = 'Tome'
print(name == new_name) # False
# 检查是否相等时不考虑大小写 
# 如果大小写很重要，这种行为有其优点。但如果大小写无关紧要，而只想检查变量的值，可将变量的值转换为小写，再进行比较：
print(name == new_name.lower())

# 检查是否不相等
print(name != new_name)
# 条件语句中可包含各种数学比较，如小于、小于等于、大于、大于等于：< |<= | > | >=
# 使用and检查多个条件 都为True 返回True
age = 20
print(age > 10 and age < 30)

# 使用or检查多个条件 一个True 返回True
print(age > 30 or age < 30)

# 检查特定值是否不包含在列表中
names = ['zs', 'xq']
print('zs' in names)
# 不在 not in
print('jack' not in names)

# if-elif-else    elif 可以多个
if age > 10:
    print('大于10')
elif age > 20:
    print('大于20')
else:
    print('大于其他')
# 省略else代码块