import re
from info_maintenance import insert, search, delete, modify, sort, total, show


def main():
    crtl = True  # 标记是否退出系统
    while (crtl):
        menu()  # 显示菜单
        option = input("请选择：")
        option_str = re.sub("\D", "", option)  # 将option中的非数字替换为“”
        if option_str in ["0", "1", "2", "3", "4", "5", "6", "7"]:
            option_int = int(option_str)
            if option_int == 0:
                print("您已退出学生信息管理系统!")
                ctrl = False
            elif option_int == 1:
                insert()
            elif option_int == 2:
                search()
            elif option_int == 3:
                delete()
            elif option_int == 4:
                modify()
            elif option_int == 5:
                sort()
            elif option_int == 6:
                total()
            elif option_int == 7:
                show()


def menu():
    print('''
    1 录入学生信息
    2 查找学生信息
    3 删除学生信息
    4 修改学生信息
    5 排序
    6 统计学生总人数
    7 显示所有学生信息
    0 退出系统
    ''')


if __name__ == '__main__':
    main()
