from tkinter import *
from PIL import Image,ImageTk
from tkinter import  messagebox
import pymysql
win=Tk()
win.title('Login')
win.geometry('1350x700+0+0')
win.config(bg='#021e2F')
 

tittle1=Label(win,bg='#081923').place(x=500,y=0,relheight=1,relwidth=1)
tittle=Label(win,text="Login System",font=('times new roman',50,'bold'),bg='#04444a',fg='white').place(x=0,y=50,relwidt=1)

def regis():
    win.destroy()
    import registration


def login():
    if email_e.get()=='' or password_e.get()=='':
        messagebox.showerror('error',"fill the blank field")
    else:
        try:
            con=pymysql.connect(host="localhost",user='root',password='',database='student')
            cur=con.cursor()
            cur.execute("select * from st where email=%s and pass=%s",(email_e.get(),password_e.get())) 
            row=cur.fetchone()
            if row ==None:
             
                messagebox.showerror('Error','invalid password or email')
            else:
                messagebox.showinfo('sucess','welcome to my kingdom')
                win.destroy()
                import sms
        except :
            messagebox.showerror('error','error no account')

# ?frame
frame=Frame(win,bg='white')
frame.place(x=400,y=160,height=450,width=600)
# # pic
image = Image. open('log2.jpg')
image = image. resize((430, 380), Image. ANTIALIAS)
bg=ImageTk.PhotoImage(image)
bag=Label(win,image=bg).place(x=130,y=190)

# from
tittle3=Label(frame,text="Login Here", font=("times new roman", 50 ,'bold'),bg='white',fg='#08A3D2')
tittle3.place(x=200,y=20)

email=Label(frame,text="Email", font=("times new roman", 25 ,'bold'),bg='white',fg='grey')
email.place(x=200,y=110)
email_e=Entry(frame, font=("times new roman", 15 ),bg='lightgrey',fg='black')
email_e.place(x=205,y=150)

password=Label(frame,text="Password", font=("times new roman", 25 ,'bold'),bg='white',fg='grey')
password.place(x=200,y=190)
password_e=Entry(frame, font=("times new roman", 15 ),bg='lightgrey',fg='black')
password_e.place(x=205,y=230)
 
button=Button(frame,cursor='hand2',text="Registration New Account?",font=("times new roman", 14,'bold'),bg='white',fg='green',bd=0,command=regis)
button.place(x=200,y=260)

button1=Button(frame,cursor='hand2',text="Login",font=("times new roman", 20,'bold'),bg='green',fg='white',command=login)
button1.place(x=210,y=310)


win.mainloop()

