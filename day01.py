name = "Deanna"
age = 26
print("你好，我是"+ name +",今年" + str(age) + "岁")
city = "上海"
print("你好，我是" + name + "，今年" + str(age) + "岁，住在" + city)
age = input("请输入你的年龄：")
age = int(age)
if age >= 18:
    print("已成年")
else:
    print("未成年")
    