from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")

def restart_time():
    os.system("shutdown /r /t 20")

def logout():
    os.system("shutdown /l /t 0")

def shutdown():
    os.system("shutdown /s /t 0")

st = Tk()
st.title("Shutdown App")
st.geometry("450x400")
st.config(bg="sky blue")

# icon image
image_icon=PhotoImage(file="./Images/shutdown.png")
st.iconphoto(False,image_icon)

r_btn = Button(st,text="Restart",font=("Times New Roman",20,"bold"),relief=RAISED,cursor="plus",command=restart)
r_btn.place(x=50, y=100)

rt_btn = Button(st,text="Restart By Time",font=("Times New Roman",20,"bold"),relief=RAISED,cursor="plus",command=restart_time)
rt_btn.place(x=220, y=100)

l_btn = Button(st,text="Logout",font=("Times New Roman",20,"bold"),relief=RAISED,cursor="plus",command=logout)
l_btn.place(x=50, y=200)

l_btn = Button(st,text="Shutdown",font=("Times New Roman",20,"bold"),relief=RAISED,cursor="plus",command=shutdown)
l_btn.place(x=220, y=200)

st.mainloop()