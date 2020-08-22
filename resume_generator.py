import tempfile
import os
from tkinter import *
import tkinter.messagebox

root=Tk()
root.title("Personal Details")
root.geometry("480x530+0+0")
root.config(bg="light grey")

name=StringVar()
email=StringVar()
mobile=StringVar()
address=StringVar()
dob=StringVar()
gender=StringVar()
choice=IntVar()

roothead=LabelFrame(root,width=350,height=400,font=('arial',20,'bold'),text="Personal Details",bg="light grey")
roothead.grid(row=0,column=0)

def expexit():
    exp.destroy()
    return
def expnext():
    global others
    others=Tk()
    others.title("Others")
    others.geometry("770x675+0+0")
    others.config(bg="light grey")
    def otherprev():
        others.destroy()
        return
    def othernext():
        global final
        final=Tk()
        final.title("Resume")
        final.geometry("850x850+0+0")
        final.config(bg="light grey")
        def fprint():
            q=res.get("1.0","end-1c")
            filename=tempfile.mktemp(".txt")
            open(filename,"w").write(q)
            os.startfile(filename,"print")
        def fexit():
            final.destroy()
        def fclear():
            res.delete(1.0,END)
        lbltit=Label(final,font=('arial',30,'bold'),text="Resume",bg="light grey")
        lbltit.pack()
        res=Text(final,bd=1,width=70,height=30,padx=10,pady=10,wrap=WORD,bg="white",font=('arial',12,'italic'))
        res.pack()

        buttonframe=Frame(final,bd=2,width=790,height=10,padx=8,pady=10,bg="light grey",relief=RIDGE)
        buttonframe.pack()
        Button(buttonframe,text="Exit",font=('arial',13),pady=5,height=1,width=28,bd=2,command=fexit).grid(row=0,column=0,sticky=W)
        Button(buttonframe,text="Print",font=('arial',13),pady=5,height=1,width=28,bd=2,command=fprint).grid(row=0,column=1,sticky=W)
        Button(buttonframe,text="Clear",font=('arial',13),pady=5,height=1,width=28,bd=2,command=fclear).grid(row=0,column=2,sticky=W)
        
        
        res.insert(1.0,nametxt.get().upper()+"\n")
        res.insert(50.0,emailtxt.get()+"\n")
        res.insert(4.0,phone_numtxt.get()+"\n")
                   
                   
        res.insert(5.0,'-----------------------------------------Career Objective------------------------------------------------------\n')
        res.insert(6.0,"\t"+cotext.get(1.0,END))
        res.insert(7.0,'---------------------------------------------------Education-------------------------------------------------------\n')
        for i in range(len(lst)):
            for j in range(1):
                res.insert(8.0,"\t"+lst[i][0].upper()+"\t|")
        res.insert(8.0,"\n")

        for i in range(len(lst)):
            for j in range(1):
                res.insert(9.0,"\t"+lst[i][1].upper()+"\t|")
        res.insert(9.0,"\n")
        for i in range(len(lst)):
            for j in range(1):
                res.insert(10.0,"\t"+lst[i][2].upper()+"\t|")
        res.insert(10.0,"\n")
        for i in range(len(lst)):
            for j in range(1):
                res.insert(11.0,"\t"+lst[i][3].upper()+"\t|")
        res.insert(11.0,"\n")
        if (len(skilltext.get(1.0,END))-1)>0:
            res.insert(12.0,'---------------------------------------------------Skills---------------------------------------------------------------\n')
            res.insert(13.0,"\t"+skilltext.get(1.0,END))
        if (len(projecttext.get(1.0,END))-1)!=0:
            res.insert(30.0,'-----------------------------------------------Projects--------------------------------------------------------------\n')
            res.insert(31.0,projecttext.get(1.0,END))
        if (len(wetext.get(1.0,END))-1)!=0:
            res.insert(45.0,'-----------------------------------------Work Experience------------------------------------------------------\n')
            res.insert(55.0,wetext.get(1.0,END))
        res.insert(56.0,'---------------------------------------------------------Personal Details---------------------------------------\n')
        res.insert(57.0,"Address         \t:\t"+addresstxt.get()+"\n")
        res.insert(61.0,"Date of Birth  \t:\t"+dobtext.get()+"\n")
        if (len(hobbytext.get(1.0,END))-1)!=0:
            res.insert(63.0,"Hobbies        \t:\t"+hobbytext.get(1.0,END))
        if (len(achievementstext.get(1.0,END))-1)!=0:
            res.insert(70.0,"Achievements\t:\t"+achievementstext.get(1.0,END))
            if choice.get()==1:
                res.insert(71.0,"Gender        \t:\tMale\n")
            elif choice.get()==2:
                res.insert(71.0,"Gender        \t:\tFemale\n")
        if (len(languagetext.get(1.0,END))-1)!=0:
            res.insert(72.0,"Languages\t:\t"+languagetext.get(1.0,END))
        res.insert(77.0,'-----------------------------------------Declaration---------------------------------------------------------------\n')
        res.insert(78.0,declarationtext.get(1.0,END))
    Label(others,font=('arial',18,'bold'),text="Others",padx=3,pady=4,bg='light grey').grid(row=0,column=0,columnspan=2,sticky=W)
    Label(others,font=('arial',15,'italic'),text="Skils:",padx=3,pady=4,bg='light grey').grid(row=1,column=0,sticky=W)
    skilltext=Text(others,width=50,height=4,bd=2,bg="white",padx=3,pady=5,wrap=WORD,font=('arial',13,'italic'))
    skilltext.grid(row=1,column=1,columnspan=2,sticky=W)
    Label(others,font=('arial',15,'italic'),text="Achievements:",padx=3,pady=4,bg='light grey').grid(row=2,column=0,sticky=W)
    achievementstext=Text(others,width=50,height=4,bd=2,bg="white",padx=3,pady=5,wrap=WORD,font=('arial',13,'italic'))
    achievementstext.grid(row=2,column=1,columnspan=2,sticky=W)
    Label(others,font=('arial',15,'italic'),text="Hobby:",padx=3,pady=4,bg='light grey').grid(row=3,column=0,sticky=W)
    hobbytext=Text(others,width=50,height=4,bd=2,bg="white",padx=3,pady=5,wrap=WORD,font=('arial',13,'italic'))
    hobbytext.grid(row=3,column=1,columnspan=2,sticky=W)
    Label(others,font=('arial',15,'italic'),text="Languages:",padx=3,pady=4,bg='light grey').grid(row=4,column=0,sticky=W)
    languagetext=Text(others,width=50,height=4,bd=2,bg="white",wrap=WORD,padx=3,pady=5,font=('arial',13,'italic'))
    languagetext.grid(row=4,column=1,columnspan=2,sticky=W)
    Label(others,font=('arial',15,'italic'),text="Declaration:",padx=3,pady=4,bg='light grey').grid(row=9,column=0,sticky=W)
    declarationtext=Text(others,width=106,height=5,bd=2,bg="white",padx=3,wrap=WORD,pady=5,font=('arial',10,'italic'))
    declarationtext.grid(row=10,column=0,columnspan=2,sticky=W,pady=2)
    declarationtext.insert(1.0,"I solemnly declare that all the information furnished in this document is free of errors to the best of my knowledge\n")
    
    Button(others,font=('arial',13,'italic'),text="Previous",padx=3,pady=5,height=1,width=73,bd=3,command=otherprev).grid(row=11,column=0,columnspan=2,pady=2)
    Button(others,font=('arial',13,'italic'),text="Continue",padx=3,pady=5,height=1,width=73,bd=3,command=othernext).grid(row=12,column=0,columnspan=2,pady=2)

#root functions
def rootnext():
    if len(nametxt.get())>0 and len(emailtxt.get())>0 and len(phone_numtxt.get())>0 and len(addresstxt.get())>0 and len(dobtext.get())>0 and choice.get()>0 and (len(cotext.get(1.0,END))-1)>0:
        global edu
        global coursetxt
        global institutetxt
        global boardtxt
        global yoptxt
        global markstxt
        global lst


        edu=Tk()
        edu.title("Educational Details")
        edu.geometry("450x350+0+0")
        edu.config(bg="light grey")
        
        
        def prev():
            edu.destroy()
            
            return
        
        lst=[]
        #edu functions
        def eduadd():
            if len(institutetxt.get())>0 and len(coursetxt.get())>0 and len(markstxt.get())>0 and len(yoptxt.get())>0:
                lst.append((institutetxt.get(),coursetxt.get(),markstxt.get(),yoptxt.get()))
                institutetxt.delete(0,END)
                coursetxt.delete(0,END)
                markstxt.delete(0,END)
                yoptxt.delete(0,END)
                
            else:
                tkinter.messagebox.showinfo("Warning!!!","All field are mandatory")
                

        def edunext():
            if len(lst)>0:
                global exp
                global projecttext
                global wetext
                exp=Tk()
                exp.title("Projct and Work Experience")
                exp.geometry("575x415+0+0")
                exp.config(bg="light grey")
                #exphead=LabelFrame(exp,width=440,height=400,font=('arial',20,'bold'),text="Personal Details",bg="light grey").grid(row=0,column=0)
                explabel=Label(exp,font=('arial',18,'bold'),text="Projects and Workexperience",padx=3,pady=4,bg='light grey').grid(row=0,column=0,sticky=E)
                projectlabel=Label(exp,font=('arial',15,'italic'),text="Projects:",padx=3,pady=4,bg='light grey').grid(row=1,column=0,sticky=W)
                projecttext=Text(exp,width=77,height=5,bd=3,bg="white",padx=3,pady=5,font=('arial',10,'italic'))
                projecttext.grid(row=2,column=0,columnspan=2,sticky=W)
                welabel=Label(exp,font=('arial',15,'italic'),text="Work Experiance:",padx=3,pady=4,bg='light grey').grid(row=3,column=0)
                wetext=Text(exp,width=77,height=5,bd=3,bg="white",padx=3,pady=5,font=('arial',10,'italic'))
                wetext.grid(row=4,column=0,columnspan=2,sticky=W)
                Button(exp,font=('arial',13,'italic'),text="Previous",padx=3,pady=5,height=1,width=53,bd=3,command=expexit).grid(row=5,column=0,columnspan=2,pady=2)
                Button(exp,font=('arial',13,'italic'),text="Save & Continue",padx=3,pady=5,height=1,width=53,bd=3,command=expnext).grid(row=6,column=0,columnspan=2,pady=2)
            else:
                tkinter.messagebox.showinfo("Warning!!!","All field are mandatory")            

            
        eduhead=LabelFrame(edu,width=500,height=350,font=('arial',20,'bold'),text="Educatonal Qualification",bg="light grey")
        eduhead.grid(row=0,column=0)
        institutelabel=Label(eduhead,font=('arial',15,'italic'),text="Institute:",padx=3,pady=4,bg='light grey').grid(row=0,column=0,sticky=W)
        institutetxt=Entry(eduhead,font=('arial',15,'italic'),width=25,bg='ghost white')
        institutetxt.grid(row=0,column=1,sticky=W)
        courselabel=Label(eduhead,font=('arial',15,'italic'),text="Course:",padx=3,pady=4,bg='light grey').grid(row=1,column=0,sticky=W)
        coursetxt=Entry(eduhead,font=('arial',15,'italic'),width=25,bg='ghost white')
        coursetxt.grid(row=1,column=1,sticky=W)
        #boardlabel=Label(eduhead,font=('arial',15,'italic'),text="Board:",padx=3,pady=4,bg='light grey').grid(row=2,column=0,sticky=W)
        #boardtxt=Entry(eduhead,font=('arial',15,'italic'),width=25,bg='ghost white')
        #boardtxt.grid(row=2,column=1,sticky=W)
        markslabel=Label(eduhead,font=('arial',15,'italic'),text="Marks Obtained:",padx=3,pady=4,bg='light grey').grid(row=3,column=0,sticky=W)
        markstxt=Entry(eduhead,font=('arial',15,'italic'),width=25,bg='ghost white')
        markstxt.grid(row=3,column=1,sticky=W)
        yoplabel=Label(eduhead,font=('arial',15,'italic'),text="Year of Passing:",padx=3,pady=4,bg='light grey').grid(row=4,column=0,sticky=W)
        yoptxt=Entry(eduhead,font=('arial',15,'italic'),width=25,bg='ghost white')
        yoptxt.grid(row=4,column=1,sticky=W)
        Button(eduhead,font=('arial',13,'italic'),text="Previous",padx=3,pady=5,height=1,width=43,bd=1,command=prev).grid(row=5,column=0,columnspan=2)
        edunextbtn=Button(eduhead,text="Save&Continue",font=('arial',13,"italic"),padx=3,pady=5,height=1,width=43,bd=1,command=edunext).grid(row=6,column=0,columnspan=2,pady=3)
        eduaddtbtn=Button(eduhead,text="add",font=('arial',13,"italic"),padx=3,pady=5,height=1,width=43,bd=1,command=eduadd).grid(row=7,column=0,columnspan=2,pady=3)
        #Button(eduhead,text="sample",command=display).grid(row=8,column=0)
    else:
        tkinter.messagebox.showinfo("Warning!!!","All field are mandatory")
    
def iexit():
    root.destroy()
    return

#label and entry root
namelabel=Label(roothead,font=('arial',15,'italic'),text="Name:",padx=3,pady=4,bg='light grey').grid(row=0,column=0,sticky=W)
nametxt=Entry(roothead,font=('arial',15,'italic'),textvariable=name,width=25,bg='ghost white')
nametxt.grid(row=0,column=1,sticky=W)

emaillabel=Label(roothead,font=('arial',15,'italic'),text="Email:",padx=3,pady=4,bg='light grey').grid(row=1,column=0,sticky=W)
emailtxt=Entry(roothead,font=('arial',15,'italic'),textvariable=email,width=25,bg='ghost white')
emailtxt.grid(row=1,column=1,sticky=W)

phone_numlabel=Label(roothead,font=('arial',15,'italic'),text="Mobile:",padx=3,pady=4,bg='light grey').grid(row=2,column=0,sticky=W)
phone_numtxt=Entry(roothead,font=('arial',15,'italic'),textvariable=mobile,width=25,bg='ghost white')
phone_numtxt.grid(row=2,column=1,sticky=W)

addresslabel=Label(roothead,font=('arial',15,'italic'),text="Address:",padx=3,pady=4,bg='light grey').grid(row=3,column=0,sticky=W)
addresstxt=Entry(roothead,font=('arial',15,'italic'),textvariable=address,width=25,bg='ghost white')
addresstxt.grid(row=3,column=1,sticky=W)

doblabel=Label(roothead,font=('arial',15,'italic'),text="DoB:",padx=3,pady=4,bg='light grey').grid(row=4,column=0,sticky=W)
dobtext=Entry(roothead,font=('arial',15,'italic'),textvariable=dob,width=25,bg='ghost white')
dobtext.grid(row=4,column=1,sticky=W)

genderlabel=Label(roothead,font=('arial',15,'italic'),text="Gender:",padx=3,pady=4,bg='light grey').grid(row=5,column=0,sticky=W)
colabel=Label(roothead,font=('arial',15,'italic'),text="Career Objective:",padx=3,pady=4,bg='light grey').grid(row=6,column=0,sticky=W)
cotext=Text(roothead,width=48,height=5,bd=3,bg="white",wrap=WORD,padx=3,pady=5,font=('arial',13,'italic'))
cotext.grid(row=7,column=0,columnspan=2,sticky=W)
#radiobutton
def select():
    select=choice.get()
male=Radiobutton(roothead,text="Male",font=('arial',10,'italic'),bg="light grey",fg="grey",variable=choice,value=1,command=select).grid(row=5,column=1,sticky=W)
female=Radiobutton(roothead,text="Female",font=('arial',10,'italic'),bg="light grey",fg="grey",variable=choice,value=2,command=select).grid(row=5,column=1,sticky=E)
#button
rootnextbtn=Button(roothead,text="Save&Continue",font=('arial',13),pady=5,height=1,width=49,bd=2,command=rootnext).grid(row=8,column=0,sticky=W,columnspan=2,pady=2)
rootexitbtn=Button(roothead,text="Exit",font=('arial',13),pady=5,height=1,width=49,bd=2,command=iexit).grid(row=9,column=0,sticky=W,columnspan=2,pady=2)
#rootaddtbtn=Button(roothead,text="add",font=('arial',13),padx=3,pady=5,height=1,width=40,bd=1,command=add).grid(row=9,column=0,columnspan=2)
