#TEAM MEMBERS
# Marwan Essam Ismail Fadel 202000417  (Team Leader)
# Hisham Ahmed Hussien 202001462  
#Farida Yasser Ali   202000177 

# Interface For A Student in College 

import tkinter as tk
from tkinter import *

#part for the name of the interface
top=tk.Tk()
top.title('NU Course Manager')
top.geometry("480x280")
top.config(background="white")#line for colour
#part for title of the window
label=tk.Label(top, text='NU',bg="white",fg="#00BFFF",font=("times", 60, "bold")).grid(row=0, column=4)
label1=tk.Label(top, text='Username:',bg="white",fg="black",font=("arial", 20, "bold")).grid(row=1,column=0)
field1=tk.Entry(top,bg="#e5e5e5",width=30)
field1.grid(row=1,column=1)
def user():
    file=open("user.txt","w")
    file.write("Username: ")
    file.write(field1.get())
    global entryString
    entryString = field1.get()
    file.flush()
    print("Username:",entryString)

def Vuser():
    if entryString !="":
        return tab2()
    else:
        Vuser=tk.Tk()
        Vuser.title('ERROR')
        Vuser.geometry("300x75")
        Vuser.config(background="white")        
        tk.Label(Vuser, text='    Please enter Username & Password!!!!',bg="white",fg="red",font=("arial", 10, "bold")).grid(row=0,column=0)
        
    
label2=tk.Label(top, text='Password:',bg="white",fg="black",font=("arial", 20, "bold")).grid(row=2,column=0)
field2=tk.Entry(top,bg="#e5e5e5",width=30).grid(row=2,column=1)


def register():
    regist=tk.Tk()
    regist.title('Register')
    regist.geometry("450x250")
    regist.config(background='#cae9f5') #line for colour
    Rbutton=tk.Button(regist, text='Submit',width=25,bg='blue',fg='white',command=subject).grid(row=7,column=1)
    #part for title of the window
    label=tk.Label(regist, text='Please Select Subjects:',bg="#cae9f5",fg="blue",font=("times", 15, "bold")).grid(row=0, sticky=W)
    global field5
    field5=tk.Entry(regist,bg="#e5e5e5")
    field5.grid(row=1,column=1,pady=3,padx=1) 
    tk.Label(regist, text='Subject 1: ',bg="#cae9f5",fg="blue",font=("times", 15, "bold")).grid(row=1, column=0)
    
    global field6
    field6=tk.Entry(regist,bg="#e5e5e5")
    field6.grid(row=2,column=1,pady=3)
    tk.Label(regist, text='Subject 2: ',bg="#cae9f5",fg="blue",font=("times", 15, "bold")).grid(row=2, column=0)
    
    global field7
    field7=tk.Entry(regist,bg="#e5e5e5")
    field7.grid(row=3,column=1,pady=3) 
    tk.Label(regist, text='Subject 3: ',bg="#cae9f5",fg="blue",font=("times", 15, "bold")).grid(row=3, column=0)
    
    global field8
    field8=tk.Entry(regist,bg="#e5e5e5")
    field8.grid(row=4,column=1,pady=3) 
    tk.Label(regist, text='Subject 4: ',bg="#cae9f5",fg="blue",font=("times", 15, "bold")).grid(row=4, column=0)
    
    global field9
    field9=tk.Entry(regist,bg="#e5e5e5")
    field9.grid(row=5,column=1,pady=3) 
    tk.Label(regist, text='Subject 5: ',bg="#cae9f5",fg="blue",font=("times", 15, "bold")).grid(row=5, column=0)
    
    global field10
    field10=tk.Entry(regist,bg="#e5e5e5")
    field10.grid(row=6,column=1,pady=3)
    tk.Label(regist, text='Subject 6: ',bg="#cae9f5",fg="blue",font=("times", 15, "bold")).grid(row=6, column=0)

def subject():    
    file=open("user.txt","a")
    file.write("\n""subject 1: ")
    file.write(field5.get())
    entryString1 = field5.get()
    file.flush()
    print("Subject1: ",entryString1)
    
    file.write("\n""subject 2: ")
    file.write(field6.get())
    entryString2 = field6.get()
    file.flush()
    print("Subject2: ",entryString2)
    
    file.write("\n""subject 3: ")
    file.write(field7.get())
    entryString3 = field7.get()
    file.flush()
    print("Subject3: ",entryString3) 
    
    file.write("\n""subject 4: ")
    file.write(field8.get())
    entryString4 = field8.get()
    file.flush()
    print("Subject4: ",entryString4)  
    
    file.write("\n""subject 5: ")
    file.write(field9.get())
    entryString5 = field9.get()
    file.flush()
    print("Subject5: ",entryString5)
    
    file.write("\n""subject 6: ")
    file.write(field10.get())
    file.write("\n""\n")
    entryString6 = field10.get()
    file.flush()
    print("Subject6: ",entryString6)    
        
grades=[]  

def Gcal():
    Gcal=tk.Tk()
    Gcal.title('Gpa Calculator')
    Gcal.geometry("450x250")
    Gcal.config(background='#ff4d4d')     
    tk.Label(Gcal, text='Enter your grade:',bg="#ff4d4d",fg="black",font=("times", 15, "bold")).grid(row=0,column=0)
    global field5
    field5=tk.Entry(Gcal,bg="#e5e5e5")
    field5.grid(row=0,column=1)  
    tk.Label(Gcal, text='Enter your grade:',bg="#ff4d4d",fg="black",font=("times", 15, "bold")).grid(row=1,column=0)
    global field6
    field6=tk.Entry(Gcal,bg="#e5e5e5")
    field6.grid(row=1,column=1)
    tk.Label(Gcal, text='Enter your grade:',bg="#ff4d4d",fg="black",font=("times", 15, "bold")).grid(row=2,column=0)
    global field7
    field7=tk.Entry(Gcal,bg="#e5e5e5")
    field7.grid(row=2,column=1) 
    tk.Label(Gcal, text='Enter your grade:',bg="#ff4d4d",fg="black",font=("times", 15, "bold")).grid(row=3,column=0)
    global field8
    field8=tk.Entry(Gcal,bg="#e5e5e5")
    field8.grid(row=3,column=1)  
    tk.Label(Gcal, text='Enter your grade:',bg="#ff4d4d",fg="black",font=("times", 15, "bold")).grid(row=4,column=0)
    global field9
    field9=tk.Entry(Gcal,bg="#e5e5e5")
    field9.grid(row=4,column=1)
    tk.Label(Gcal, text='Enter your grade:',bg="#ff4d4d",fg="black",font=("times", 15, "bold")).grid(row=5,column=0)
    global field10
    field10=tk.Entry(Gcal,bg="#e5e5e5")
    field10.grid(row=5,column=1)  
    def calculate():
        total=0
        for x in grades:
            if x == "A+":
                total = total + 4.0
            if x == "A":
                total = total + 4.0
            if x == "A-":
                total = total + 3.7
            if x == "B+":
                total = total + 3.3
            if x == "B":
                total = total + 3.0
            if x == "B-":
                total = total + 2.7
            if x == "C+":
                total = total + 2.3
            if x == "C":
                total = total + 2.0
            if x == "C-":
                total = total + 1.7
            if x=="D+":
                total = total + 1.3
            if x == "D":
                total = total + 1.0
            if x== "F":
                total = total + 0.0
        
        z=round(total/6,2)
        print("Your GPA Is: ",z)
        tk.Label(Gcal,text="Your GPA Is: "+str(z),fg='blue',bg="#ff4d4d",font=("arial", 12, "bold")).grid(row=7,column=1)  
    
    def gradeCal():
        grades.append(field5.get().upper())
        grades.append(field6.get().upper())
        grades.append(field7.get().upper())
        grades.append(field8.get().upper())
        grades.append(field9.get().upper())
        grades.append(field10.get().upper())
        return calculate()
    tk.Button(Gcal, text='Calculate',width=20,bg='red',fg='white',command=lambda:[gradeCal(),grades.clear()]).grid(row=6,column=1,pady=4)
    
    
def MESS():
    Mess=tk.Tk()
    Mess.title('For More Help')
    Mess.geometry("450x120") 
    labelN=tk.Label(Mess, text='Contact Your Advising Directors:',fg='blue',font=("arial", 12, "bold")).grid(row=0,sticky=W)  
    labelM=tk.Label(Mess, text='Y.Eid@nu.edu.eg\nNGamal@nu.edu.eg\nab.ali@nu.edu.eg',fg='black',font=("arial", 12, "bold")).grid(row=1,column=1)
    Button(Mess, text='Quit',width=20,bg='red', fg='WHITE',command=Mess.quit).grid(row=3, column=1, pady=4)
    
def advise():
    advise=tk.Tk()
    advise.title('Advising')
    advise.geometry("730x100") 
    advise.config(background='#90ee90') 
    #part for title of the window
    label=tk.Label(advise, text='You have to select minimum 6 Subjects, for any modification click "For More Help"',bg="#90ee90",fg="black",font=("arial", 15)).grid(row=0,column=0)
    button=tk.Button(advise, text='For More Help',width=30,bg='green', fg='WHITE',command=MESS).grid(row=1,column=0)    


def tab2():
    tab2=tk.Tk()
    tab2.title('NU browse')
    tab2.geometry("500x200")
    tab2.config(background='white') #line for colour
    #part for title of the window
    label=tk.Label(tab2, text='Welcome to NU',bg="white",fg="#00BFFF",font=("times", 20, "bold")).grid(row=0,column=0)
    Rbutton=tk.Button(tab2, text='Register',width=30,bg='blue',fg='white',pady=3,font=("arial", 10, "bold"),command= register).grid(row=2,column=1,pady=5)
    gbutton=tk.Button(tab2, text='GPA Calculator',width=30,bg='red',fg='white',pady=3,font=("arial", 10, "bold"),command=Gcal).grid(row=3,column=1,pady=5)
    Abutton=tk.Button(tab2, text='Advising',width=30,bg='green',fg='white',pady=3,font=("arial", 10, "bold"),command=advise).grid(row=1,column=1,pady=5)    
tk.Checkbutton(top,text="I'm student",onvalue=1,offvalue=0,bg="white",fg="black",font=("arial", 14, "bold")).grid(row=3, sticky=W)
button=tk.Button(top, text='Login',width=25,bg='#00BFFF', fg='WHITE',font=("arial", 10, "bold"),command=lambda:[user(),Vuser()]).grid(row=4,column=1)

top.mainloop()
