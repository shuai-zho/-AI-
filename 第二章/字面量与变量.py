# 字面量的写法
print(100)              # 整数 (int)
print(3.14)             # 浮点数 (float)
print(True)             # 布尔值 (bool)
print(False)            # 布尔值 (bool)
print("Hello Python")   # 字符串 (str)
print(None)             # 空值 (NoneType)


# 布尔类型本质也是整数类型(True - 1 ; False - 0)
print(True + 1)         # 输出 2
print(False - 1)        # 输出 -1


# 变量  ---> Pyhton是动态类型语言， 一个变量是可以存储不同类型的数据的（但是项目开发中，不建议一个变量存储不同类型的数据，推荐变量只存储一种类型的数据）
num = 1144.1
print(num)              # 输出 1144.1

num = num + 1
print(num)              # 输出 1145.1

num = 'ok'
print(num)              # 输出 ok

num = True
print(num)              # 输出 True

a = True
print(a)                # 输出 True


# 案例
# 基础播放量 = 20.7w
# 月新增播放量 = 50w
# 输出未来两个月每个月播放总量
base_views = 20.7
monthly_new_views = 50
total_views_month_1 = base_views + monthly_new_views * 1
total_views_month_2 = base_views + monthly_new_views * 2
print(f'未来第一个月播放总量: {total_views_month_1}')  # 输出 70.7
print(f'未来第二个月播放总量: {total_views_month_2}')  # 输出 120.7

# 案例- 升级:一次性可以定义多个变量
base_views,monthly_new_views = 20.7,50
print(f'未来第一个月播放总量: {total_views_month_1}')  # 输出 70.7
print(f'未来第二个月播放总量: {total_views_month_2}')  # 输出 120.7


# 标识符
true = 1
print(true)             # 输出 1

# 6name = Python
# print(6name)           # 报错，标识符不能以数字开头

'''
命名规范(命名规范是指在编程中对变量、函数、类等标识符的命名方式和规则。良好的命名规范有助于提高代码的可读性和可维护性。以下是一些常见的命名规范：
1. 驼峰命名法（CamelCase）：首字母小写，后续单词首字母大写。例如：myVariableName、calculateTotalAmount。
2. 下划线命名法（snake_case）：所有字母小写，单词之间用下划线分隔。例如：my_variable_name、calculate_total_amount。
3. 匈牙利命名法（Hungarian Notation）：在变量名前加上类型前缀。例如：strName（字符串）、intCount（整数）。
4. Pascal命名法（PascalCase）：每个单词的首字母都大写。例如：MyVariableName、CalculateTotalAmount。
在Python中，通常推荐使用下划线命名法（snake_case）来命名变量和函数，而类名则使用Pascal命名法（PascalCase）。
此外，避免使用Python的关键字作为标识符，并尽量使用有意义的名称来描述变量或函数的用途。  )
'''

# 案例：
# 需求：现有两个变量，分别为:a=10,b=20，现需要将这两个变量值交换，然后输出到控制台。

a = 10
b = 20
print(f'交换前: a = {a}, b = {b}')

# 方法一：使用临时变量
temp = a
a = b
b = temp

print(f'交换后: a = {a}, b = {b}')