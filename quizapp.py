from tkinter import *
from tkinter import ttk
i=0
note=ttk.Notebook()

frame1=ttk.Frame(note)
frame2=ttk.Frame(note)
frame3=ttk.Frame(note)
frame4=ttk.Frame(note)
frame5=ttk.Frame(note)

root=ttk.Frame(note)

def quiz(i):
    note.add(frame1,text="Qn1")
    note.add(frame2,text="Qn2")
    note.add(frame3,text="Qn3")
    note.add(frame4,text="Qn4")
    note.add(frame5,text="Qn5")
    
    Label(frame1,text="correct extension of python file is _?",font=("Arial",30,"bold")).grid(row=2,column=2)
    Button(frame1,text=".python",font=("Arial",20,"bold"),bg="blue",command=q1_wrong).grid(row=6,column=1)
    Button(frame1,text=".pl",font=("Arial",20,"bold"),bg="blue",command=q1_wrong).grid(row=6,column=2)
    Button(frame1,text=".py",font=("Arial",20,"bold"),bg="blue",command=q1_correct).grid(row=6,column=3)
    

    Label(frame2,text="what is the value of 4+3%5?",font=("Arial",30,"bold")).grid(row=2,column=2)
    Button(frame2,text="7",font=("Arial",20,"bold"),bg="blue",command=q2_correct).grid(row=3,column=1)
    Button(frame2,text="2",font=("Arial",20,"bold"),bg="blue",command=q2_wrong).grid(row=3,column=2)
    Button(frame2,text="4",font=("Arial",20,"bold"),bg="blue",command=q2_wrong).grid(row=3,column=3)
    

    Label(frame3,text="which keyword is used for function in python?",font=("Arial",30,"bold")).grid(row=2,column=2)
    Button(frame3,text="function",font=("Arial",20,"bold"),bg="blue",command=q3_wrong).grid(row=3,column=1)
    Button(frame3,text="Def",font=("Arial",20,"bold"),bg="blue",command=q3_correct).grid(row=3,column=2)
    Button(frame3,text="Fun",font=("Arial",20,"bold"),bg="blue",command=q3_wrong).grid(row=3,column=3)
    

    Label(frame4,text="which of the following is built-in function in python?",font=("Arial",30,"bold")).grid(row=2,column=2)
    Button(frame4,text="factorial()",font=("Arial",20,"bold"),bg="blue",command=q4_wrong).grid(row=3,column=1)
    Button(frame4,text="print()",font=("Arial",20,"bold"),bg="blue",command=q4_correct).grid(row=3,column=2)
    Button(frame4,text="seed()",font=("Arial",20,"bold"),bg="blue",command=q4_wrong).grid(row=3,column=3)
    

    Label(frame5,text="which is not a core data type in python?",font=("Arial",30,"bold")).grid(row=2,column=2)
    Button(frame5,text="Tuples",font=("Arial",20,"bold"),bg="blue",command=q5_wrong).grid(row=3,column=1)
    Button(frame5,text="List",font=("Arial",20,"bold"),bg="blue",command=q5_wrong).grid(row=3,column=2)
    Button(frame5,text="Class",font=("Arial",20,"bold"),bg="blue",command=q5_correct).grid(row=3,column=3)
    

def q1_correct():
    Label(frame1,text="correct !",font=("Arial",20,"bold"),bg="light green",fg="yellow").grid(row=1,column=2)
    Label(frame1,text="Your Score: +4",font=("Arial",20,"bold"),bg="black",fg="white").grid(row=1,column=3)
    
def q1_wrong():
    Label(frame1,text="wrong !",font=("Arial",20,"bold"),bg="red",fg="yellow").grid(row=1,column=2)
    Label(frame1,text="Your Score: 0",font=("Arial",20,"bold"),bg="black",fg="white").grid(row=1,column=3)

def q2_correct():
    Label(frame2,text="correct !",font=("Arial",20,"bold"),bg="light green",fg="yellow").grid(row=1,column=2)
    Label(frame2,text="Your Score: +4",font=("Arial",20,"bold"),bg="black",fg="white").grid(row=1,column=3)
    
def q2_wrong():
    Label(frame2,text="wrong !",font=("Arial",20,"bold"),bg="red",fg="yellow").grid(row=1,column=2)
    Label(frame2,text="Your Score: 0",font=("Arial",20,"bold"),bg="black",fg="white").grid(row=1,column=3)

def q3_correct():
    Label(frame3,text="correct !",font=("Arial",20,"bold"),bg="light green",fg="yellow").grid(row=1,column=2)
    Label(frame3,text="Your Score: +4",font=("Arial",20,"bold"),bg="black",fg="white").grid(row=1,column=3)
    
def q3_wrong():
    Label(frame3,text="wrong !",font=("Arial",20,"bold"),bg="red",fg="yellow").grid(row=1,column=2)
    Label(frame3,text="Your Score: 0",font=("Arial",20,"bold"),bg="black",fg="white").grid(row=1,column=3)

def q4_correct():
    Label(frame4,text="correct !",font=("Arial",20,"bold"),bg="light green",fg="yellow").grid(row=1,column=1)
    Label(frame4,text="Your Score: +4",font=("Arial",20,"bold"),bg="black",fg="white").grid(row=1,column=2)
    
def q4_wrong():
    Label(frame4,text="wrong !",font=("Arial",20,"bold"),bg="red",fg="yellow").grid(row=1,column=1)
    Label(frame4,text="Your Score: 0",font=("Arial",20,"bold"),bg="black",fg="white").grid(row=1,column=2)

def q5_correct():
    Label(frame5,text="correct !",font=("Arial",20,"bold"),bg="light green",fg="yellow").grid(row=1,column=2)
    Label(frame5,text="Your Score: +4",font=("Arial",20,"bold"),bg="black",fg="white").grid(row=1,column=3)
    
def q5_wrong():
    Label(frame5,text="wrong !",font=("Arial",20,"bold"),bg="red",fg="yellow").grid(row=1,column=2)
    Label(frame5,text="Your Score: 0",font=("Arial",20,"bold"),bg="black",fg="white").grid(row=1,column=3)


quiz(i)
note.pack()
note.mainloop()


