from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        self.root.wm_iconbitmap("face.ico")


        #variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_student_id=StringVar()
        
        self.var_name=StringVar()
        self.var_Div=StringVar()
        
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_photo1=StringVar()
        self.var_photo2=StringVar()
        

        




        img=Image.open(r"C:\Users\hp\Desktop\attendence management system\image\face-recognition.png")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)


        img1=Image.open(r"C:\Users\hp\Desktop\attendence management system\image\smart-attendance.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)


        img2=Image.open(r"C:\Users\hp\Desktop\attendence management system\image\iStock-182059956_18390_t12.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        img3=Image.open(r"C:\Users\hp\Desktop\attendence management system\image\wp2551980.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="red",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1530,height=600)

        

        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=580)


        img_left=Image.open(r"C:\Users\hp\Desktop\attendence management system\image\AdobeStock_303989091.jpeg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        #current course
        current_course_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=115)
#department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=2,pady=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"))

        course_label.grid(row=0,column=2,padx=2,pady=10,sticky=W)
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),width=20,state="readonly")
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"))
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"))

        year_label.grid(row=1,column=0,padx=2,pady=10,sticky=W)
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"))
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),width=20,state="readonly")
        year_combo["values"]=("Select Course","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester

        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"))
        semester_label.grid(row=1,column=2,padx=2,pady=10,sticky=W)
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",13,"bold"),width=20,state="readonly")
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"))
        semester_combo["values"]=("Select Semester","1","2","3","4")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class student information
        Class_student_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Class student information",font=("times new roman",12,"bold"))
        Class_student_frame.place(x=5,y=250,width=720,height=300)
#student id
        studentId_label=Label(Class_student_frame,text="StudentId:",font=("times new roman",13,"bold"))
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentId_entry=ttk.Entry(Class_student_frame,textvariable=self.var_student_id,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        studentName_label=Label(Class_student_frame,text="StudentName:",font=("times new roman",13,"bold"))
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(Class_student_frame,textvariable=self.var_name,width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class_division 
        class_division_label=Label(Class_student_frame,text="Class division:",font=("times new roman",13,"bold"))
        class_division_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        #class_division_entry=ttk.Entry(Class_student_frame,textvariable=self.var_div,width=20,font=("times new roman",13,"bold"))
        #class_division_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        class_division_combo=ttk.Combobox(Class_student_frame,textvariable=self.var_Div,font=("times new roman",13,"bold"),width=20,state="readonly")
        class_division_combo["values"]=("AA","A","B","C","D")
        class_division_combo.current(0)
        class_division_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #roll number
        rollNumber_label=Label(Class_student_frame,text="Roll Number:",font=("times new roman",13,"bold"))
        rollNumber_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        rollNumber_entry=ttk.Entry(Class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        rollNumber_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #gender
        
        gender_label=Label(Class_student_frame,text="Gender:",font=("times new roman",13,"bold"))
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        #gender_entry=ttk.Entry(Class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",13,"bold"))
        #gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        gender_combo=ttk.Combobox(Class_student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),width=20,state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female","Others","sixer")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #dob
        
        dob_label=Label(Class_student_frame,text="DOB:",font=("times new roman",13,"bold"))
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(Class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #email
        email_label=Label(Class_student_frame,text="Email Id:",font=("times new roman",13,"bold"))
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(Class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phone_number
        phone_number_label=Label(Class_student_frame,text="Phone Number:",font=("times new roman",13,"bold"))
        phone_number_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_number_entry=ttk.Entry(Class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_number_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #address
       
        address_label=Label(Class_student_frame,text="Address:",font=("times new roman",13,"bold"))
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(Class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #teacherName
     
        teacherName_label=Label(Class_student_frame,text="Teacher Name:",font=("times new roman",13,"bold"))
        teacherName_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacherName_entry=ttk.Entry(Class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        teacherName_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #Radiobutton
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(Class_student_frame,variable=self.var_radio1,text="take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)

        radiobtn2=ttk.Radiobutton(Class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No ")
        radiobtn2.grid(row=5,column=1)

        #button_frame
        btn_frame=Frame(Class_student_frame,bd=2,relief=RIDGE, bg="white")
        btn_frame.place(x=0,y=210,width=715,height=40)

        #save btn
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="aqua",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="aqua",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="aqua",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="aqua",fg="white")
        reset_btn.grid(row=0,column=3)


        btn_frame1=Frame(Class_student_frame,bd=2,relief=RIDGE, bg="white")
        btn_frame1.place(x=0,y=242,width=715,height=35)

        take_photo_sample_btn=Button(btn_frame1,command=self.generate_dataset,text="Take a Photo Sample",width=35,font=("times new roman",13,"bold"),bg="aqua",fg="white")
        take_photo_sample_btn.grid(row=0,column=0)

        update_photo_sample_btn=Button(btn_frame1,text="Update a Photo Sample",width=35,font=("times new roman",13,"bold"),bg="aqua",fg="white")
        update_photo_sample_btn.grid(row=0,column=1)
    
    
    #rightframe
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=720,height=580)

        img_right=Image.open(r"C:\Users\hp\Desktop\attendence management system\image\gettyimages-1022573162.jpg")
        img_right=img_right.resize((720,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        

        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)


        ##seaching system
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Searching System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=710,height=70)

        search_label=Label(search_frame,text="Search BY:",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)


        search_combo=ttk.Combobox(search_frame,font=("times new roman",13,"bold"),width=15,state="readonly")
        search_combo["values"]=("Select","Roll NO.","Phone No.")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=12,font=("times new roman",13,"bold"),bg="aqua",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        reset_btn=Button(search_frame,text="Show All",width=12,font=("times new roman",13,"bold"),bg="aqua",fg="white")
        reset_btn.grid(row=0,column=4,padx=4)


        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)


        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","Div","email","name","roll","gender","dob","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("Div",text="Class division")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("phone",text="Phone Number")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("Div",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)
        



        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        #function 

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_student_id.get()=="":
            messagebox.showerror("Error","All Fileds are mandatory",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="kana8989@",database="facedb1")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_student_id.get(),
                    self.var_name.get(),
                    self.var_Div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    #fetching the data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="kana8989@",database="facedb1")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from Student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
         

#get cursor

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_student_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_Div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        
        
        
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14]),


#update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_student_id.get()=="":
            messagebox.showerror("Error","All Fileds are mandatory",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="kana8989@",database="facedb1")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Name=%s,sem=%s,`Div`=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_name.get(),
                        self.var_sem.get(),
                        self.var_Div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_student_id.get()
                    ))

                else:
                    if  not Update:
                        return
                messagebox.showinfo("Success","Student details successfully update Completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

        #delete function
    def delete_data(self):
        if self.var_student_id.get()=="":
             messagebox.showerror("Error","student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this Student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="kana8989@",database="facedb1")
                    my_cursor=conn.cursor()
                    sql="delete from Student where Student_id=%s"
                    val=(self.var_student_id.get(),) # Use get() method instead of calling the variable as a function
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                         return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Succesfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)



#reset
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select year"),
        self.var_sem.set(""),
        self.var_student_id.set(""),
        self.var_name.set(""),
        self.var_Div.set("AA"),
        self.var_roll.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        
        
        
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set(""),


        
        
#Generate data set or take photo sample 
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_student_id.get()=="":
            messagebox.showerror("Error","All Fileds are mandatory",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="kana8989@",database="facedb1")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1

                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Name=%s,sem=%s,`Div`=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_name.get(),
                        self.var_sem.get(),
                        self.var_Div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_student_id.get()
                    ))


                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()

                #load predifend data on face fronntal from opencv

                    face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    def face_cropped(img):
                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor
                    #Minimum Neighbour=5

                        for (x,y,w,h) in faces:
                            face_cropped=img[y:y+h,x:x+w]
                            return face_cropped

                    cap=cv2.VideoCapture(0)
                    img_id=0
                    while True:
                        ret,myframe=cap.read()
                        if face_cropped(myframe) is not None:
                            img_id+=1
                            face=cv2.resize(face_cropped(myframe),(450,450))
                            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                            file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                            cv2.imwrite(file_name_path,face)
                            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                            cv2.imshow("Croped Face",face)

                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                    cap.release()
                    cv2.destroyAllWindows()

                    messagebox.showinfo("Result","Genrating data set compled!!!")

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


                                          
                                                                
                                                                                                              










if __name__ == "__main__":
        root=Tk()
        obj=Student(root)
        root.mainloop()