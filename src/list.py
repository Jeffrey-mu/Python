# 在Python中，用方括号（[]）来表示列表，并用逗号来分隔其中的元素
newList = ['xiao ming', 'xiao hong', 'xiao lan']
# 访问第一个元素 索引从0而不是1开始
print(newList[0].title())
# Python为访问最后一个列表元素提供了一种特殊语法。通过将索引指定为-1，可让Python返回最后一个列表元素:
print(newList[-1]) # 你经常需要在不知道列表长度的情况下访问最后的元素

# 修改元素
newList[0] = 'xiao zi'

# 在列表末尾添加元素
newList.append('xiao qiang')
# 在列表中插入元素 （索引，插入值）
newList.insert(0, 'xiao mi')

# 在列表中插入元素
# 使用del语句删除元素 使用del可删除任何位置处的列表元素，条件是知道其索引
del newList[0]
print(newList)
# 使用方法pop()可删除列表末尾的元素，并让你能够接着使用它
print(newList.pop()) # xiao qiang
# 弹出列表中任何位置处的元素 只需在括号中指定要删除的元素的索引即可
print(newList.pop(0)) # xiao zi
# 根据值删除元素
# 有时候，你不知道要从列表中删除的值所处的位置。如果你只知道要删除的元素的值，可使用方法remove()
print(newList.remove('xiao hong'))
print(newList)


first_list = [1, 3, 2, 4, 6, 5]
# 使用方法sort()对列表进行永久性排序
first_list.sort()
print(first_list)
# 反向排序
first_list.sort(reverse=True)
print(first_list)
# 使用函数sorted()对列表进行临时排序 支持 reverse=True 参数
print(sorted(first_list))
# reverse() 而只是反转列表元素的排列顺序 永久性地修改
first_list.reverse()
print(first_list)

# 确定列表的长度
print(len(first_list)) # 6