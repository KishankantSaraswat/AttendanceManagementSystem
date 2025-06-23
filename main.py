from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from time import strftime
from datetime import datetime
import os
import tkinter
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendence
from developer import Developer
from chatbot1 import Chatbot




class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        self.root.wm_iconbitmap("face.ico")

        img=Image.open(r"C:\Users\hp\Desktop\attendence management system\image\BestFacialRecognition.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)


        img1=Image.open(r"C:\Users\hp\Desktop\attendence management system\image\facialrecognition.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)


        img2=Image.open(r"C:\Users\hp\Desktop\attendence management system\image\images.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        #background image

        img3=Image.open(r"C:\Users\hp\Desktop\attendence management system\image\wp2551980.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        def time():
            string = strftime("%H:%M:%S %p")
            lbl. config(text=string)
            lbl.after(1000,time)

        lbl  = Label(title_lbl,font=('time new roman', '14','bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()


        img4=Image.open(r"C:\Users\hp\Desktop\attendence management system\image\gettyimages-1022573162.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=320,width=220,height=40)
#face detection
        img5=Image.open(r"C:\Users\hp\Desktop\attendence management system\image\face_detector1.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,command=self.face_data,image=self.photoimg5)
        b2.place(x=500,y=100,width=220,height=220)
        b2_2=Button(bg_img,text="Face Recognition",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_2.place(x=500,y=320,width=220,height=40)

#attendence
        img6=Image.open(r"C:\Users\hp\Desktop\attendence management system\image\report.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,command=self.Attendance,image=self.photoimg6)
        b3.place(x=800,y=100,width=220,height=220)
        b3_3=Button(bg_img,text="Attendence",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b3_3.place(x=800,y=320,width=220,height=40)
#3
        img7=Image.open(r"C:\Users\hp\Desktop\attendence management system\image\chat.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
#chatbot
        b7=Button(bg_img,image=self.photoimg7,command=self.chatbot_data,cursor="hand2")
        b7.place(x=1100,y=100,width=220,height=220)
        b7_7=Button(bg_img,text="Chat bot",command=self.chatbot_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b7_7.place(x=1100,y=320,width=220,height=40)

#train data
        img9=Image.open(r"C:\Users\hp\Desktop\attendence management system\image\Train.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        
        b9=Button(bg_img,image=self.photoimg9,command=self.train_data,cursor="hand2")
        b9.place(x=200,y=400,width=220,height=220)

        b9_9=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b9_9.place(x=200,y=620,width=220,height=40)
#photos
        img10=Image.open(r"C:\Users\hp\Desktop\attendence management system\image\opencv_face_reco_more_data.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b10=Button(bg_img,command=self.open_img,image=self.photoimg10)
        b10.place(x=500,y=400,width=220,height=220)
        b10_10=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b10_10.place(x=500,y=620,width=220,height=40)

        #developer
        img11=Image.open(r"C:\Users\hp\Desktop\attendence management system\image\Team-Management-Software-Development.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS , )
        self.photoimg11=ImageTk.PhotoImage(img11)

        b11=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.develpoer_data)
        b11.place(x=800,y=400,width=220,height=220)
        b11_11=Button(bg_img,text="Developer",command=self.develpoer_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b11_11.place(x=800,y=620,width=220,height=40)

        #exit

        img12=Image.open(r"C:\Users\hp\Desktop\attendence management system\image\exit.jpg")
        img12=img12.resize((220,220),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        b12=Button(bg_img,image=self.photoimg12,command=self.iExit,cursor="hand2")
        b12.place(x=1100,y=400,width=220,height=220)
        b12_12=Button(bg_img,text="Exit",command=self.iExit,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b12_12.place(x=1100,y=620,width=220,height=40)
    

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this Project",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return

#function buttons
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)


    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def Attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendence(self.new_window)

    def develpoer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def chatbot_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Chatbot(self.new_window)





if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()