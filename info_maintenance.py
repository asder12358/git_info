import os

filename = "student.txt"


def save(student):
    try:
        student_txt = open(filename, "a")
    except Exception as e:
        student_txt = open(filename, "w")
    for info in student:
        student_txt.write(str(info) + "\n")
    student_txt.close()


def insert():
    studentList = []
    mark = True
    while mark:
        id = input("请输入ID(如 1001) : ")
        if not id:
            break
        name = input("请输入名字 : ")
        if not name:
            break
        try:
            english = int(input("请输入英文成绩 : "))
            python = int(input("请输入python成绩 : "))
            c = int(input("请输入C语言成绩 : "))
        except:
            print("输入无效，不是整型数值，请重新录入信息......")
            continue
        student = {"id": id, "name": name, "english": english, "python": python, "c": c}
        studentList.append(student)
        inputMark = input("是否继续添加? (y/n) : ")
        if inputMark == "y":
            mark = True
        else:
            mark = False
    save(studentList)
    print("学生信息录入完毕！！！")


def delete():
    mark = True
    while mark:
        studentID = input("请输入要删除的学生ID: ")
        if studentID is not "":
            if os.path.exists(filename):
                with open(filename, "r") as rf:
                    student_old = rf.readlines()
            else:
                student_old = []
            ifdel = False
            if student_old:
                with open(filename, "w") as wf:
                    d = {}
                    for list in student_old:
                        d = dict(eval(list))
                        if d["id"] != studentID:
                            wf.write(str(d) + "\n")
                        else:
                            ifdel = True
                    if ifdel:
                        print("ID为 %s 的学生信息已经被删除..." % studentID)
                    else:
                        print("没有找到ID为 %s 的学生信息..." % studentID)
            else:
                print("五学生信息...")
                break
            show()
            inputMark = input("是否继续删除? (y/n) : ")
            if inputMark == "y":
                mark = True
            else:
                mark = False


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, "r") as rf:
            student_old = rf.readlines()
    else:
        return
    studentID = input("请输入要修改的学生ID: ")
    with open(filename, "w") as wf:
        d = {}
        for student in student_old:
            d = dict(eval(student))
            if d["id"] == studentID:
                print("找到了该名学生，可以修改其信息！")
                while True:
                    try:
                        d["name"] = input("请输入姓名: ")
                        d["english"] = int(input("请输入英语成绩: "))
                        d["python"] = int(input("请输入python成绩: "))
                        d["c"] = int(input("请输入C语言成绩: "))
                    except:
                        print("您的输入有误，请重新输入...")
                    else:
                        break
                student = str(d)
                wf.write(student + "\n")
                print("修改成功！！！")
            else:
                wf.write(student)
    mark = input("是否继续修改其他学生信息? (y/n) : ")
    if mark == "y":
        modify()


def search():
    mark = True
    student_query = []
    while mark:
        id = ""
        name = ""
        if os.path.exists(filename):
            mode = input("按ID查询请按1，按姓名查询请按2: ")
            if mode == "1":
                id = input("请输入学生ID: ")
            elif mode == "2":
                name = input("请输入学生姓名: ")
            else:
                print("您的输入有误，请重新输入...")
                search()
            with open(filename, "r") as rfile:
                student = rfile.readlines()
                for list in student:
                    d = dict(eval(list))
                    if d is not "":
                        if d["id"] == id:
                            student_query.append(d)
                    elif name is not "":
                        if d["name"] == name:
                            student_query.append(d)
                show_student(student_query)
                student_query.clear()
                inputMark = input("是否继续查询? (y/n) : ")
                if inputMark == "y":
                    mark = True
                else:
                    mark = False
        else:
            print("未查询到数据信息...")
            return


def show_student(studentList):
    if not studentList:
        print("...无数据信息...")
        return
    format_title = "{:^6}{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^10}"
    print(format_title.format("ID", "名字", "英语成绩", "python成绩", "C语言成绩", "总成绩"))
    format_data = "{:^6}{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}"
    for info in studentList:
        print(
            format_data.format(str(info.get("id")), info.get("name"), str(info.get("english")), str(info.get("python")),
                               str(info.get("c")),
                               str(info.get("english") + info.get("python") + info.get("c")).center(12)))


def total():
    if os.path.exists(filename):
        with open(filename, "r") as rfile:
            student_old = rfile.readlines()
            if student_old:
                print("共有 %d 名学生" % len(student_old))
            else:
                print("还没有录入学生信息...")
    else:
        print("未查询到数据信息...")


def show():
    student_show = []
    if os.path.exists(filename):
        with open(filename, "r") as rfile:
            student_old = rfile.readlines()
        for list in student_old:
            student_show.append(eval(list))
        if student_show:
            show_student(student_show)
    else:
        print("未查询到数据信息...")


def sort():
