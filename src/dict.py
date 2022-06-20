# 字典 在Python中，字典是一系列键—值对
man = {"name": "zs", "age": 20, "sing": "zs"}
# 访问
print(man["name"])
# 添加
man["sex"] = "0"
print(man)
# 修改
man["sex"] = "1"
print(man)
# 删除键—值对
del man["age"]
print(man)
# 遍历所有的键—值对
for key, value in man.items():
    print(key)
    print(value)
# 遍历所有的键
for key in man.keys():
    print(key)
# 按顺序遍历所有的键
for key in sorted(man.keys()):
    print(key)
# 遍历字典中的所有值
for value in man.values():
    print(value)
# 为剔除重复项，可使用集合（set）
for value in set(man.values()):
    print(value)

# 字典中存列表 字典中存字典
others = {"children": [1, 2, 3], "man": {"name": "jack"}}