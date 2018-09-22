

def qqzc():
    qq_account = input("请输入qq账号\n")
    qq_password = input("请输入qq密码\n")
    qq_name = input("请输入qq昵称\n")
    user = {"account" :qq_account ,"password" :qq_password ,"name" :qq_name}
    lists.append(user)
    return True

def qq_login():
    if lists:
        qq_account = input("请输入qq账号\n")
        qq_password = input("请输入qq密码\n")
        for sink in lists:
            if qq_account == sink["account"] and qq_password == sink["password"]:
                print("登陆成功！欢迎您：", sink["name"])
            else:
                print("用户名或密码不正确！请重新输入！")
    else:
        print("请先注册!")

lists = []

while True:
    value = input("请选择功能:1.注册 2.登陆 3.退出\n")
    if value == "1":
        result = qqzc()
        if result == True:
            print("注册成功！")
        else:
             print("注册失败！")
    elif value == "2":
        qq_login()
    elif value == "4":
        print("退出系统!!!")
        break
    else:
        print ("输入有误，请重新输入！")
