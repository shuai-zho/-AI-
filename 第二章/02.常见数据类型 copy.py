
# ===============================================目标========================================================

print('今天是2026年6月30日，我要每天坚持学习Pyhton，希望三年后能在外企大厂工作，成为一名优秀的Python开发工程师！')


# 常见数据类型  ----> type() 获取指定的字面量或者变量的数据类型
print('Hello')
print(type('Hello'))  # 输出 <class 'str'> 字符串类型
print(100)
print(type(100))      # 输出 <class 'int'> 整数类型
print(3.14)
print(type(3.14))     # 输出 <class 'float'> 浮点数
print(True)
print(type(True))     # 输出 <class 'bool'> 布尔类型
print(False)
print(type(False))    # 输出 <class 'bool'> 布尔类型
print(None)
print(type(None))     # 输出 <class 'NoneType'> 空值类型
num = -100
print(type(num))      # 输出 <class 'int'> 整数类型

# 常见数据类型 ----> isinstance(数据 , 数据类型) ---> bool值 ---> 判断指定的字面量或者变量是否是指定的数据类型, 如果是：True, 如果不是：False
print(isinstance('Hello',str))  # 输出 True
print(isinstance(num,int))      # 输出 True
print(isinstance(3.14,float))   # 输出 True
print(isinstance(True,bool))    # 输出 True
print(isinstance(False,bool))   # 输出 True
# print(isinstance(None,NoneType)) # 输出 True
# print(isinstance(num,float))     # 输出 False
# print(isinstance(num,str))       # 输出 False
# print(isinstance(num,bool))      # 输出 False
# print(isinstance(num,NoneType))  # 输出 False
# print(isinstance('Hello',int))   # 输出 False

# 字符串
# 定义字符串的三种方式
s1 = 'Hello Python' # 单引号定义
s2 = "Hello Python" # 双引号定义
s3 = '''            
Hello:
      
      学习成为一名AI Python工程师第二天
'''                 # 三引号定义 （多行字符串）
print(s1)
print(s2)
print(s3)
print(type(s1))  # 输出 <class 'str'> 字符串类型
print(type(s2))  # 输出 <class 'str'> 字符串类型
print(type(s3))  # 输出 <class 'str'> 字符串类型

# 定义字符串 ----> It's Very Good!  ---> 需要使用转义字符 \ 来转义单引号
# 转义字符 
# \' 在由单引号包裹的字符串中，直接写单引号会提前结束字符串，所以用 \' 表示一个真正的单引号字符。 
# \" 和单引号同理
# \n 换行
# \t 缩进一格 相当于按了一下tab，通常等于 4 或 8 个空格的宽度，用于对齐文本。
# \\ 反斜杠本身，因为反斜杠被用作转义前缀，要表示一个真正的反斜杠字符，就得写两个。
# \r 将光标移回当前行的行首，但不换行。ASCII 码为 13（0x0D）。这个名字来自老式打字机——"回车"就是那个把打印头推回最左边的动作。
msg = 'It\'s Very Good!'
msg2 = "It's Very Good!"
msg3 = "It's Very Good!\"Good!\""
print(msg3)  # 输出 It's Very Good!"Good!"
print(msg2)  # 输出 It's Very Good!
print(msg)  # 输出 It's Very Good!
print("\t今天是2026年6月30日，我要每天坚持学习Pyhton，\n\t希望三年后能在外企大厂工作，成为一名优秀的Python开发工程师！")
path = "C:\\Users\\张三\\文档"   # 实际值: C:\Users\张三\文档
print("abcde\r123") # 输出: 123de  解释: 先打印 abcde，然后 \r 把光标拉回行首，再打印 123 覆盖了 abc


# 字符串拼接
s1="人生苦短""我用Python","OK"
print(s1)
msg1="人生苦短"
msg2="我用Python"
print("龟叔说:" + msg1 + "," + msg2)
#案例:--->str(int数字I--->
name ="涛哥"
age = 18
pro="软件工程"
hobby = "Python、 Java"
print("大家好，我是" + name + "，今年" + str(age) + "岁，学习的专业是" + pro + "，爱好" + hobby)

'''
案例
完成如下字符串拼接的需求
根据自己的实际情况，输出个人的详细信息，具体结构如下:
"大家好，我是钟帅，今年26岁，学习的专业是计算机应用，爱好Python、AI，希望三年后能在外企大厂工作，成为一名优秀的Python开发工程师！"
'''