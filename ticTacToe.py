from tkinter import Button, messagebox, Tk

first = True
resultList = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]


def buttonClick(btn, column):
    global first, resultList

    if first:
        btn["text"] = "X"
        first = False
        resultList[column] = "X"
    else:
        btn["text"] = "O"
        first = True
        resultList[column] = "O"

    checkResult()


def messageInfo(winner):
    messagebox.showinfo("Result", f"Congratulations! {winner} is winner.")
    window.destroy()


def messageDraw():
    messagebox.showinfo("Result", "Match is draw.")
    window.destroy()


def checkResult():
    if len(resultList) == 9 and '-' not in resultList:
        messageDraw()
    if resultList[0:3] == ["X", "X", "X"]\
            or resultList[3:6] == ["X", "X", "X"]\
            or resultList[6:9] == ["X", "X", "X"]\
            or (resultList[0] == "X"
                and resultList[3] == "X"
                and resultList[6] == "X") \
            or (resultList[1] == "X"
                and resultList[4] == "X"
                and resultList[7] == "X") \
            or (resultList[2] == "X"
                and resultList[5] == "X"
                and resultList[8] == "X") \
            or (resultList[0] == "X"
                and resultList[4] == "X"
                and resultList[8] == "X") \
            or (resultList[2] == "X"
                and resultList[4] == "X"
                and resultList[6] == "X"):
        messageInfo("X")
    elif resultList[0:3] == ["O", "O", "O"]\
            or resultList[3:6] == ["O", "O", "O"]\
            or resultList[6:9] == ["O", "O", "O"] \
            or (resultList[0] == "O"
                and resultList[3] == "O"
                and resultList[6] == "O") \
            or (resultList[1] == "O"
                and resultList[4] == "O"
                and resultList[7] == "O") \
            or (resultList[2] == "O"
                and resultList[5] == "O"
                and resultList[8] == "O") \
            or (resultList[0] == "O"
                and resultList[4] == "O"
                and resultList[8] == "O") \
            or (resultList[2] == "O"
                and resultList[4] == "O"
                and resultList[6] == "O"):
        messageInfo("O")


window = Tk()
window.title("Tic Tac Toe")
window.geometry("150x150")
window.configure(background="#333333")

button1 = Button(window,
                 command=lambda column=0: buttonClick(button1, column),
                 highlightbackground="#333333",
                 text="-",
                 pady=10)
button1.grid(row=0, column=0)

button2 = Button(window,
                 command=lambda column=1: buttonClick(button2, column),
                 highlightbackground="#333333",
                 text="-",
                 pady=10)
button2.grid(row=0, column=1)

button3 = Button(window,
                 command=lambda column=2: buttonClick(button3, column),
                 highlightbackground="#333333",
                 text="-",
                 pady=10)
button3.grid(row=0, column=2)

button4 = Button(window,
                 command=lambda column=3: buttonClick(button4, column),
                 highlightbackground="#333333",
                 text="-",
                 pady=10)
button4.grid(row=1, column=0)

button5 = Button(window,
                 command=lambda column=4: buttonClick(button5, column),
                 highlightbackground="#333333",
                 text="-",
                 pady=10)
button5.grid(row=1, column=1)

button6 = Button(window,
                 command=lambda column=5: buttonClick(button6, column),
                 highlightbackground="#333333",
                 text="-",
                 pady=10)
button6.grid(row=1, column=2)

button7 = Button(window,
                 command=lambda column=6: buttonClick(button7, column),
                 highlightbackground="#333333",
                 text="-",
                 pady=10)
button7.grid(row=2, column=0)

button8 = Button(window,
                 command=lambda column=7: buttonClick(button8, column),
                 highlightbackground="#333333",
                 text="-",
                 pady=10)
button8.grid(row=2, column=1)

button9 = Button(window,
                 command=lambda column=8: buttonClick(button9, column),
                 highlightbackground="#333333",
                 text="-",
                 pady=10)
button9.grid(row=2, column=2)

window.mainloop()
