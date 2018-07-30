from brickscript import ui, fmanager
import sys
import datetime

def fetchTODOs():
    ptpdir = fmanager.initPathToParentDir(__file__)
    fmanager.wFileData(ptpdir, "", "todoDB.txt", "", False)
    todoData = fmanager.rFileData(ptpdir, "", "todoDB.txt")
    return(todoData.split("\n")[:-1])

def writeTODOs(data):
    ptpdir = fmanager.initPathToParentDir(__file__)
    fmanager.wFileData(ptpdir, "", "todoDB.txt", data, False)

def rewriteTODOs(data):
    ptpdir = fmanager.initPathToParentDir(__file__)
    fmanager.wFileData(ptpdir, "", "todoDB.txt", data, True)

def clearTODOs():
    with open("todoDB.txt", "w") as f:
        f.write("")

def getDate(prompt):
    userInput = input(prompt).lower().split(" ")

    modifiers = {"following": 14, "next": 7}
    daynames = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    relativedays = {"today": 0, "tmr": 1, "tomorrow": 1}
    days = -1

    if userInput[-1][:3] in daynames:

        dayOfWeek = daynames.index(userInput[-1][:3])
        if datetime.date.today().weekday() > dayOfWeek:
            days = (6-datetime.date.today().weekday()) + dayOfWeek
        else:
            days = dayOfWeek - datetime.date.today().weekday()

        if userInput[0] in modifiers:
            days += modifiers[userInput[0]]
            if datetime.date.today().weekday() > dayOfWeek and userInput[0] == "next":
                days -= 7

    elif userInput[-1] in relativedays:
        days = relativedays[userInput[-1]]

    if days >= 0:
        date = datetime.date.today() + datetime.timedelta(days=days)
        return("{}/{}/{}".format(date.day, date.month, int(str(date.year)[-2:])))
    else:
        return(" ".join(userInput))

def listTODOs():
    todoData = [x.split(" • ") for x in fetchTODOs()]
    for todo in todoData:
        dateParts = todo[2].split("/")
        try:
            dateParts = list(map(int, dateParts))
        except:
            print(" • ".join(todo))
        else:
            deadline = datetime.date(2000+dateParts[2], dateParts[1], dateParts[0])
            daysToDeadline = (deadline - datetime.date.today()).days
            if daysToDeadline > 5:
                ui.colorise(" • ".join(todo), "green", True)
            elif daysToDeadline > 1:
                ui.colorise(" • ".join(todo), "yellow", True)
            else:
                ui.colorise(" • ".join(todo), "red", True)

def main():
    ui.refresh()
    print("Terminal Overlord v0.2 by Orbtial")
    print("============ //TODO ============")
    listTODOs()
    print("\n================================")
    input("Press [ENTER] to continue")
    action = ui.gList("What is your next move, Operator?", ["Add new task", "Mark as complete", "Edit a task", "Back", "Quit"], True)
    if action == 0:
        ui.refresh()
        flag = input("//FLAG: ")
        ui.refresh()
        task = input("//TASK: ")
        ui.refresh()
        date = getDate("//DEADLINE: ")
        writeTODOs("{} • {} • {}\n".format(flag, task, date))
        main()
    elif action == 1:
        ui.refresh()
        todoList = fetchTODOs()
        index = ui.gList("Complete which task?", todoList + ["Cancel operation and return"], True)
        if index == len(todoList):
            main()
        else:
            todoList.pop(index)
            if len(todoList) == 0: clearTODOs()
            else: rewriteTODOs("\n".join(todoList) + "\n")
            main()
    elif action == 2:
        ui.refresh()
        todoList = fetchTODOs()
        index = ui.gList("Edit which task?", todoList + ["Cancel operation and return"], True)
        if index == len(todoList):
            main()
        else:
            editedTask = todoList[index].strip("\n").split(" • ")
            actions = ["FLAG", "TASK", "DEADLINE"]
            action = ui.gList("What would you like to edit?", actions, True)
            ui.refresh()
            if action == 2: edited = getDate("//{}: ".format(actions[action]))
            else: edited = input("//{}: ".format(actions[action]))
            editedTask[action] = edited
            todoList[index] = " • ".join(editedTask)
            rewriteTODOs("\n".join(todoList) + "\n")
            main()
    elif action == 3:
        main()
    else:
        ui.refresh()
        sys.exit()
    
main()
