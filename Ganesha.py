# Name   : Jeet Bhatt
# ID     : 20CP312
# Branch : Computer Engineering
    
# Language  : Python
# Library   : Tkinter
    
# Note : Download All Files (.py and .png)




from tkinter import *
from tkinter import messagebox 

root=Tk() 
root.title("Prarambh'21") 
#image


lbl1=Label(text="<===NOTE: IF YOU CAN NOT SEE THE PROPER OUTPUT, MAKE SURE YOU HAVE DOWNLOADED ALL FILES (.PNG)===>")
lbl1.grid(row=0,column=1)

pich=PhotoImage(file="human.png") 
lbl3=Label(image=pich) 
lbl3.grid(row=1,column=0)

picr=PhotoImage(file="rat.png") 
lbl4=Label(image=picr) 
lbl4.grid(row=1,column=1)

picg=PhotoImage(file="ganesha.png")
lbl2=Label(image=picg) 
lbl2.grid(row=1,column=2) 

messagebox.showinfo("Prarambh'21","Happy Ganeshoshtav 2021\nGanpati Bappa Morya...")
root.mainloop()