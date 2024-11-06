from tkinter import *
root=Tk()

root.geometry("600x600")
root.title("Tic tac toe Game")

frame1=Frame(root)
frame1.pack()
label1=Label(frame1,text="Tic tac toe",font=("Arial",30),bg="green")

label1.pack()



frame2=Frame(root)
frame2.pack()

turn="x"

def play(event):
    global turn
    button=event.widget
    

    if turn == "x":

        button["text"] = "X"
        turn="o"

    else:
        button["text"]="O"
        turn="x"



    

#Button 1 row

button1=Button(frame2,text="",width=6,height=2,bg="red",relief=RAISED,borderwidth=5,font=("Arial",35))
button1.grid(row=0,column=0)
button1.bind("<Button-1>",play)


button2=Button(frame2,text="",width=6,height=2,bg="red",relief=RAISED,borderwidth=5,font=("Arial",35))
button2.grid(row=0,column=1)
button2.bind("<Button-1>",play)

button3=Button(frame2,text="",width=6,height=2,bg="red",relief=RAISED,borderwidth=5,font=("Arial",35))
button3.grid(row=0,column=2)
button3.bind("<Button-1>",play)

#Button 2 row

button1=Button(frame2,text="",width=6,height=2,bg="red",relief=RAISED,borderwidth=5,font=("Arial",35))
button1.grid(row=1,column=0)
button1.bind("<Button-1>",play)

button2=Button(frame2,text="",width=6,height=2,bg="red",relief=RAISED,borderwidth=5,font=("Arial",35))
button2.grid(row=1,column=1)
button2.bind("<Button-1>",play)

button3=Button(frame2,text="",width=6,height=2,bg="red",relief=RAISED,borderwidth=5,font=("Arial",35))
button3.grid(row=1,column=2)
button3.bind("<Button-1>",play)

#Button 3 row

button1=Button(frame2,text="",width=6,height=2,bg="red",relief=RAISED,borderwidth=5,font=("Arial",35))
button1.grid(row=2,column=0)
button1.bind("<Button-1>",play)

button2=Button(frame2,text="",width=6,height=2,bg="red",relief=RAISED,borderwidth=5,font=("Arial",35))
button2.grid(row=2,column=1)
button2.bind("<Button-1>",play)

button3=Button(frame2,text="",width=6,height=2,bg="red",relief=RAISED,borderwidth=5,font=("Arial",35))
button3.grid(row=2,column=2)
button3.bind("<Button-1>",play)








root.mainloop()