from tkinter import*
from tkinter import messagebox
import base64
import os

def decryp():
  password=code.get()
  if password=="1234":
    screen2=Toplevel(screen)
    screen2.title("decryption")
    screen2.geometry("400x200")
    screen2.configure(bg="#00bd56")
    
    mesage=text1.get(1.0,END)
    decode_mesage=mesage.encode("ascii")
    base64_bytes=base64.b64decode(decode_mesage)
    decypted=base64_bytes.decode("ascii")
    
    Label(screen2,text="encrypt",font="arial",fg="white",bg="#00bd56").place(x=10,y=0)
    text2=Text(screen2,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text2.place(x=10,y=40,width=380,height=150)
    text2.insert(END,decypted)
  elif password=="":
    messagebox.showerror("encryption","input password")
  elif password!="1234":
    messagebox.showerror("encryption","invalid password")
    
  
def encryp():
  password=code.get()
  if password=="1234":
    screen1=Toplevel(screen)
    screen1.title("encryption")
    screen1.geometry("400x200")
    screen1.configure(bg="#ed3833")
    
    mesage=text1.get(1.0,END)
    encode_mesage=mesage.encode("ascii")
    base64_bytes=base64.b64encode(encode_mesage)
    encypted=base64_bytes.decode("ascii")
    
    Label(screen1,text="encrypt",font="arial",fg="white",bg="#ed3833").place(x=10,y=0)
    text2=Text(screen1,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text2.place(x=10,y=40,width=380,height=150)
    text2.insert(END,encypted)
  elif password=="":
    messagebox.showerror("encryption","input password")
  elif password!="1234":
    messagebox.showerror("encryption","invalid password")
    
    
    
  
def main_screen():
  global screen
  global code
  global text1
  
  
  screen=Tk()
  screen.geometry("375x398")
  #icon
  global_icon = PhotoImage(file="C:/Users/sfar/Desktop/dr chuk/python/project/encdry/key.png")
  screen.iconphoto(False,global_icon)
  screen.title("encrypdcrypt")
  def rest ():
    code.set("")
    text1.delete(1.0,END)
  Label(text="Enter text for encryption and decryption",fg='black',font=("calbri",13)).place(x=10,y=10)
  text1=Text(font="Robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
  text1.place(x=10,y=50,width=355,height=100)
  Label(text="Enter secret key for encrypted and drypt ",fg='black',font=("calbri",13)).place(x=10,y=170)
  code=StringVar()
  Entry(textvariable=code,width=19,bd=0,font=("arial",25),show="*").place(x=10,y=200)
  Button(text="Encrypt",height="2",width=23,bg="#ed3833",fg="white",bd=0,command=encryp).place(x=10,y=250)
  Button(text="decrypt",height="2",width=23,bg="#00bd56",fg="white",bd=0,command=decryp).place(x=200,y=250)
  Button(text="rest",height="2",width=50,bg="#1089ff",fg="white",bd=0,command=rest).place(x=10,y=300)
  screen.mainloop()
main_screen()

