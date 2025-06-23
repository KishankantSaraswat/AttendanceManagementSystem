from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog 

class Chatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")
        self.root.geometry("730x620+0+0")
        self.root.bind('<Return>',self.enter_fun)

        main_frame = Frame(self.root, bd=4, bg="powder blue", width=610)
        main_frame.pack()

        img_chat = Image.open("C:/Users/hp/Desktop/attendence management system/image/chat.jpg")
        img_chat = img_chat.resize((200, 70), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img_chat)

        title_lbl = Label(main_frame, bd=3, relief=RAISED, anchor='center', width=730, compound=LEFT, 
                          image=self.photoimg, text="CHAT ME", font=("arial", 30, "bold"), bg="white", fg="green")

        title_lbl.pack(side=TOP)
        
        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=3,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()

        btn_frame=Frame(self.root,bd=4,bg='white',width=730)
        btn_frame.pack()

        label_text = Label(btn_frame, text="Type Something", font=('arial','14','bold'), fg='green', bg='white')
        label_text.grid(row=0, column=0, padx=5, sticky=W)


        #self.entry=StringVar
        self.entry=ttk.Entry(btn_frame,width=40 ,font=('arial ','14','bold'))
        self.entry.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="SEND>>",command=self.send, font=('arial','16','bold'),width=8,bg='green')
        self.send.grid(row=0, column=2, padx=5, sticky=W)
        

        self.clear=Button(btn_frame,text="Clear",font=('arial','16','bold'),width=8,bg='red',fg='white')
        self.clear.grid(row=1, column=0, padx=5, sticky=W)
        
        self.msg=''
        self.label_11 = Label(btn_frame, text=self.msg, font=('arial','14','bold'), fg='red', bg='white')
        self.label_11.grid(row=1, column=1, padx=5, sticky=W)


        #function


    def enter_fun(self,event):
        self.send.invoke()
        #self.entry1.set('')


    def send(self):
        send='\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END,'\n'+send)

    #def clear_fun(self):
        
        #self.text.delete('1.0',END)
        #self.entry.set('')


    
    

    

        if(self.entry.get()==''):
            self.msg='Please enter some input'
            self.label_11.config(text=self.msg,fg='red')
        else:
            self.msg=''
            self.label_11.config(text=self.msg,fg='red')

        if(self.entry.get()=='hello'):
            self.text.insert(END,'\n\n'+'Bot:Hi')

        elif(self.entry.get()=='Hello'):
            self.text.insert(END,'\n\n'+'Bot:Hi')

        elif(self.entry.get()=='Hello'):
            self.text.insert(END,'\n\n'+'Bot:Hi')
        
        elif(self.entry.get()=='How are you?'):
            self.text.insert(END,'\n\n'+'Bot:I am fine what about you')

        elif(self.entry.get()=='What is your name?'):
            self.text.insert(END,'\n\n'+'Bot:My name is Ismat KK')

        elif(self.entry.get()=='how many students in a section'):
            self.text.insert(END,'\n\n'+'Bot:72')

        elif(self.entry.get()=='Who develop you?'):
            self.text.insert(END,'\n\n'+'Bot:Developer Name=KK')
        
        elif(self.entry.get()=='hi'):
            self.text.insert(END,'\n\n'+'Bot:Hi')

        elif(self.entry.get()=='How many follower Coder_kk have on instagram'):
            self.text.insert(END,'\n\n'+'Bot:Recently 81 follower?')

        elif(self.entry.get()=='What are you doing?'):
            self.text.insert(END,'\n\n'+'Bot:I am chatting to you')

        elif(self.entry.get()=='Do you have girlfriend'):
            self.text.insert(END,'\n\n'+'KK:No I am single?\n if any one like me then DM on mr_pndit32')
        
        elif(self.entry.get()=='How many friends you have?'):
            self.text.insert(END,'\n\n'+'Bot:Every one is my friend\n BHAICHARA JINDABAD')

        elif(self.entry.get()=='You are indian?'):
            self.text.insert(END,'\n\n'+'Bot:Yes')

        elif(self.entry.get()=='who is your best friend'):
            self.text.insert(END,'\n\n'+'Bot:KK')

        elif(self.entry.get()=='what is  the name of your female best friend'):
            self.text.insert(END,'\n\n'+'KK:Kanishka')
        
        elif(self.entry.get()=='Log'):
            self.text.insert(END,'\n\n'+'Bot:')
                

        elif(self.entry.get()=='Hello'):
            self.text.insert(END,'\n\n'+'Bot:Hi')

        elif(self.entry.get()=='Hello'):
            self.text.insert(END,'\n\n'+'Bot:Hi')

        elif(self.entry.get()=='Hello'):
            self.text.insert(END,'\n\n'+'Bot:Hi')
        
        elif(self.entry.get()=='Hello'):
            self.text.insert(END,'\n\n'+'Bot:Hi')

        elif(self.entry.get()=='Hello'):
            self.text.insert(END,'\n\n'+'Bot:Hi')

        elif(self.entry.get()=='Hello'):
            self.text.insert(END,'\n\n'+'Bot:Hi')

        elif(self.entry.get()=='Hello'):
            self.text.insert(END,'\n\n'+'Bot:Hi')
        
        elif(self.entry.get()=='Hello'):
            self.text.insert(END,'\n\n'+'Bot:Hi')

        elif(self.entry.get()=='Hello'):
            self.text.insert(END,'\n\n'+'Bot:Hi')

        elif(self.entry.get()=='Hello'):
            self.text.insert(END,'\n\n'+'Bot:Hi')

        elif(self.entry.get()=='Hello'):
            self.text.insert(END,'\n\n'+'Bot:Hi')
        
        elif(self.entry.get()=='Hello'):
            self.text.insert(END,'\n\n'+'Bot:Hi')

        elif(self.entry.get()=='Hello'):
            self.text.insert(END,'\n\n'+'Bot:Hi')

        elif(self.entry.get()=='Hello'):
            self.text.insert(END,'\n\n'+'Bot:Hi')

        elif(self.entry.get()=='Hello'):
            self.text.insert(END,'\n\n'+'Bot:Hi')
        
        elif(self.entry.get()=='Hello'):
            self.text.insert(END,'\n\n'+'Bot:Hi')

        elif(self.entry.get()=='Hello'):
            self.text.insert(END,'\n\n'+'Bot:Hi')
        


        else:
            self.text.insert(END,'\n\n'+'Bot:Sorry,I can not get it')

        


if __name__ == "__main__":
    root = Tk()
    obj = Chatbot(root)
    root.mainloop()
