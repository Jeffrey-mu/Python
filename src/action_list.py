from asyncio import events
from distutils.command.build_scripts import first_line_re
from this import s


first_list = ['zhang san', 'li si', 'xiao qaing']
# 使用for循环来打印名单中的所有名字
for item in first_list:
    print(item)
#  避免缩进错误 遗漏了冒号!!!

# 创建数值列表
# 使用函数range()
for value in range(1, 5):
    # 它不会打印数字5
    print(value)

# 使用range()创建数字列表
numbers = list(range(1, 6))
print(numbers) # [1, 2, 3, 4, 5]
# 使用函数range()时，还可指定步长。例如，下面的代码打印1～10内的偶数
events_numbers = list(range(2, 11, 2))
print(events_numbers) # [2, 4, 6, 8, 10]

# 对数字列表执行简单的统计计算
# max() min() sum() 最大 最小 和
print(max(numbers))
print(min(numbers))
print(sum(numbers))
# 列表解析 在这个示例中，表达式为value**2，它计算平方值。接下来，编写一个for循环，用于给表达式提供值，再加上右方括号。在这个示例中，for循环为for value in range(1,11)，它将值1～10提供给表达式value**2。请注意，这里的for语句末尾没有冒号。
squares = [value**2 for value in range(1, 11)]
print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 使用列表的一部分 切片
print(squares[0: 3]) # 不包含 索引3
# 如果你没有指定第一个索引，Python将自动从列表开头开始：
print(squares[: 3])
# 由于没有指定起始索引，Python从列表开头开始提取：
print(squares[3])
# 要让切片终止于列表末尾，也可使用类似的语法。例如，如果要提取从第3个元素到列表末尾的所有元素，可将起始索引指定为2，并省略终止索引：
print(squares[2:])
# 切后两个
print(squares[-2:])
# 遍历切片如同遍历列表
# 复制列表
f_list = [1, 2, 3]
s_list = f_list[:]
# s_list = f_list 不是复制
# 元组
# 定义元组
dimensions = (1, 2)
print(dimensions)
# dimensions[0] = 0 TypeError: 'tuple' object does not support item assignment 试图修改元组的操作是被禁止的
# 遍历元组中的所有值像列表一样，也可以使用for循环来遍历元组中的所有值

# 虽然不能修改元组的元素，但可以给存储元组的变量赋值。因此，如果要修改前述矩形的尺寸，可重新定义整个元组
dimensions = (3, 5)
print(dimensions)
# 相比于列表，元组是更简单的数据结构。如果需要存储的一组值在程序的整个生命周期内都不变，可使用元组。