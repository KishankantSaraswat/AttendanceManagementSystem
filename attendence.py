from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog 




mydata=[]

class Attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        self.root.wm_iconbitmap("face.ico")

        #variables
        
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        


        img=Image.open(r"C:\Users\hp\Desktop\attendence management system\image\face-recognition.png")
        img=img.resize((800,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)


        img1=Image.open(r"C:\Users\hp\Desktop\attendence management system\image\smart-attendance.jpg")
        img1=img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)
#background
        img3=Image.open(r"C:\Users\hp\Desktop\attendence management system\image\wp2551980.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="red",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1530,height=600)

        #LEFT FRAME
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=580)
        img_left=Image.open(r"C:\Users\hp\Desktop\attendence management system\image\AdobeStock_303989091.jpeg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        left_inside_frame=Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        left_inside_frame.place(x=0,y=135,width=720,height=350)

        #label and entery
        #student id
        attendanceId_label=Label(left_inside_frame,text="AttendanceId:",textvariable=self.var_atten_id,font=("times new roman",13,"bold"))
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceId_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",13,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #roll
        rollLable=Label(left_inside_frame,text="Roll:",textvariable=self.var_atten_roll,bg="white",font=("conicsansns ",11,"bold"))
        rollLable.grid(row=0,column=2,padx=4,pady=8)

        atten_roll=ttk.Entry(left_inside_frame,width=22,font=("conicsansns",11,"bold"))
        atten_roll.grid(row=0,column=3,pady=8)

        #name
        nameLable=Label(left_inside_frame,text="Name:",textvariable=self.var_atten_name,bg="white",font=("conicsansns ",11,"bold"))
        nameLable.grid(row=1,column=0)

        atten_name=ttk.Entry(left_inside_frame,width=22,font=("conicsansns",11,"bold"))
        atten_name.grid(row=1,column=1,pady=8)
       #department
        depLable=Label(left_inside_frame,text="Department:",textvariable=self.var_atten_dep,bg="white",font=("conicsansns ",11,"bold"))
        depLable.grid(row=1,column=2)

        atten_dep=ttk.Entry(left_inside_frame,width=22,font=("conicsansns",11,"bold"))
        atten_dep.grid(row=1,column=3,pady=8)

        #time
         
        timeLable=Label(left_inside_frame,text="Time:",textvariable=self.var_atten_time,bg="white",font=("conicsansns ",11,"bold"))
        timeLable.grid(row=2,column=0)

        atten_time=ttk.Entry(left_inside_frame,width=22,font=("conicsansns",11,"bold"))
        atten_time.grid(row=2,column=1,pady=8)
         #date
        dateLable=Label(left_inside_frame,text="Date:",textvariable=self.var_atten_date,bg="white",font=("conicsansns ",11,"bold"))
        dateLable.grid(row=2,column=2)

        atten_date=ttk.Entry(left_inside_frame,width=22,font=("conicsansns",11,"bold"))
        atten_date.grid(row=2,column=3,pady=8)

        #attendence
         #name
        attendenceLable=Label(left_inside_frame,text="Attendance Status:",textvariable=self.var_atten_attendance,bg="white",font=("conicsansns ",11,"bold"))
        attendenceLable.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,font="conicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

         #button_frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE, bg="white")
        btn_frame.place(x=0,y=300,width=715,height=35)

        #save btn
        save_btn=Button(btn_frame,text="Import Csv",command=self.importCsv,width=17,font=("times new roman",13,"bold"),bg="aqua",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export",command=self.exportCsv,width=17,font=("times new roman",13,"bold"),bg="aqua",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="aqua",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="aqua",fg="white")
        reset_btn.grid(row=0,column=3)


        
    

      

        


        #date
        dateLable=Label(left_inside_frame,text="Date:",bg="white",font=("conicsansns ",11,"bold"))
        dateLable.grid(row=1,column=2,padx=4,pady=8)

        atten_date=ttk.Entry(left_inside_frame,width=22,font=("conicsansns",11,"bold"))
        atten_date.grid(row=1,column=3,pady=8)



    #rightframe
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=720,height=580)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE, bg="white")
        table_frame.place(x=5,y=5,width=700,height=455)
        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)


        self.AttendenceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance" ),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.yview)

        self.AttendenceReportTable.heading("id",text="Attendance ID")
        self.AttendenceReportTable.heading("roll",text="Roll")
        self.AttendenceReportTable.heading("name",text="Name")
        self.AttendenceReportTable.heading("department",text="Department")
        self.AttendenceReportTable.heading("time",text="time")
        self.AttendenceReportTable.heading("date",text="Date")
        self.AttendenceReportTable.heading("attendance",text="Attendance")
        self.AttendenceReportTable["show"]="headings"

        self.AttendenceReportTable.column("id",width=100)
        self.AttendenceReportTable.column("roll",width=100)
        self.AttendenceReportTable.column("name",width=100)
        self.AttendenceReportTable.column("department",width=100)
        self.AttendenceReportTable.column("time",width=100)
        self.AttendenceReportTable.column("date",width=100)
        self.AttendenceReportTable.column("attendance",width=100)
        self.AttendenceReportTable.pack(fill=BOTH,expand=1)

        self.AttendenceReportTable.bind("<ButtonRelease>",self.getcursor)

        #fetch data

    def fetchData(self,rows):
            self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
            for i in rows:
                self.AttendenceReportTable.insert("",END,values=i)


    def importCsv(self):
            global mydata
            mydata.clear()
            fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open Csv",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
            with open(fln) as myfile:
                csvread=csv.reader(myfile,delimiter=",")
                for i in csvread:
                    mydata.append(i)
                self.fetchData(mydata)

    #Export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("NO Data","No Data Found to Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open Csv",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Expert","Your data exported to"+os.path.basename(fln)+"  successfully")

        except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    
    def getcursor(self,event=""):
        cursor_row=self.AttendenceReportTable.focus()
        content=self.AttendenceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])



    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")

        

        
        
        
       
        

        

if __name__ == "__main__":
        root=Tk()
        obj=Attendence(root)
        root.mainloop()