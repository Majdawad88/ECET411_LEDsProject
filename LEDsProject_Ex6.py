#  git clone https://github.com/Majdawad88/ECET411_LEDsProject.git


from tkinter import*
root = Tk()
root.title("LED Project")
root.geometry('600x400')
Count = 0

def greenClicked():
        global Count
        Count = Count +1
        CounterReminder = Count %2
        if CounterReminder == 1:
                greenLedLabel = Label(root, text = 'GREEN LED ON',fg = "white",bg = "green", )
        else:
                greenLedLabel = Label(root, text = 'GREEN LED OFF',fg = "white",bg = "green", )
        greenLedLabel.grid(row=7, column = 5)



greenLedButton = Button(root, text="GREEN",command=lambda:greenClicked(), padx = 10, pady = 0, fg = "white", bg = "green")
greenLabel = Label(root, text = "Green LED OFF", fg = "white", bg ="green")

root.columnconfigure(5, weight=1)
root.rowconfigure(7, weight = 1)
root.rowconfigure(3, weight = 1)

greenLedButton.grid(row=3, column=5)
greenLabel.grid(row=7, column=5)

root.mainloop()
