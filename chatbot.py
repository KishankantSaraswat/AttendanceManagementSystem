from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog 


class Chatbot:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        self.root.wm_iconbitmap("face.ico")

        title_lbl=Label(self.root,text="CHATBOT",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"C:\Users\hp\Desktop\attendence management system\image\2-AI-invades-automobile-industry-in-2019.jpeg") 
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        

        f_lbl=Label(self.root,image=self.photoimg_top) 
        f_lbl.place(x=0,y=55,width=1530,height=720)

        dev_label=Label(f_lbl,text="Email-:krishankantsaraswat830@gmial.com",font=("times new roman",32,"bold"))
        dev_label.place(x=550,y=400)

if __name__ == "__main__":
        root=Tk()
        obj=Chatbot(root)
        root.mainloop()