from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Calculator")

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)

tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Standard')

tab_control.add(tab2, text='Scientific')
#Standard calc:

op=""
ans=0
e=0
def eq():
    global e
    res1=txt1.get()
    if res1=="":
        res1=0
    else:
        res1=float(res1)
    res2=txt2.get()
    if res2=="":
        res2=0
    else:
        res2=float(res2)
    if op=="+":
        ans=res1+res2
    elif op=="-":
        ans=res1-res2
    elif op=="*":
        ans=res1*res2
    elif op=="/":
        ans=res1/res2
    else:
        ans=res1
    e=0
    lbl1.configure(text=ans)

def add():
    global op
    global e
    op="+"
    e=1
def sub():
    global op
    global e
    op="-"
    e=1
def mul():
    global op
    global e
    op="*"
    e=1
def div():
    global op
    global e
    op="/"
    e=1
def cli1():
    if e==0:
        txt1.insert(END,"1")
    elif e==1:
        txt2.insert(END,"1")
    else:
        None
def cli2():
    if e==0:
        txt1.insert(END,"2")
    elif e==1:
        txt2.insert(END,"2")
    else:
        None
def cli3():
    if e==0:
        txt1.insert(END,"3")
    elif e==1:
        txt2.insert(END,"3")
    else:
        None
def cli4():
    if e==0:
        txt1.insert(END,"4")
    elif e==1:
        txt2.insert(END,"4")
    else:
        None
def cli5():
    if e==0:
        txt1.insert(END,"5")
    elif e==1:
        txt2.insert(END,"5")
    else:
        None
def cli6():
    if e==0:
        txt1.insert(END,"6")
    elif e==1:
        txt2.insert(END,"6")
    else:
        None
def cli7():
    if e==0:
        txt1.insert(END,"7")
    elif e==1:
        txt2.insert(END,"7")
    else:
        None
def cli8():
    if e==0:
        txt1.insert(END,"8")
    elif e==1:
        txt2.insert(END,"8")
    else:
        None
def cli9():
    if e==0:
        txt1.insert(END,"9")
    elif e==1:
        txt2.insert(END,"9")
    else:
        None
def cli0():
    if e==0:
        txt1.insert(END,"0")
    elif e==1:
        txt2.insert(END,"0")
    else:
        None
def cli():
    if e==0:
        txt1.insert(END,".")
    elif e==1:
        txt2.insert(END,".")
    else:
        None
def de():
    if e==0:
        res=txt1.get()
        res=res[:-1]
        txt1.delete(0,END)
        txt1.insert(END,res)
    elif e==1:
        res=txt2.get()
        res=res[:-1]
        txt2.delete(0,END)
        txt2.insert(END,res)
    else:
        None
def ac():
    txt1.delete(0,END)
    txt2.delete(0,END)
    lbl1.configure(text="Answer")

txt1=Entry(tab1,width=10)
txt1.grid(row=0,column=0)
txt2=Entry(tab1,width=10)
txt2.grid(row=1,column=0)
lbl1=Label(tab1,text="Answer")
lbl1.grid(row=2,column=0)

Button(tab1,text="1",command=cli1).grid(row=5,column=1)
Button(tab1,text="2",command=cli2).grid(row=5,column=2)
Button(tab1,text="3",command=cli3).grid(row=5,column=3)
Button(tab1,text="4",command=cli4).grid(row=4,column=1)
Button(tab1,text="5",command=cli5).grid(row=4,column=2)
Button(tab1,text="6",command=cli6).grid(row=4,column=3)
Button(tab1,text="7",command=cli7).grid(row=3,column=1)
Button(tab1,text="8",command=cli8).grid(row=3,column=2)
Button(tab1,text="9",command=cli9).grid(row=3,column=3)
Button(tab1,text="0",command=cli0).grid(row=6,column=2)
Button(tab1,text=".",command=cli).grid(row=6,column=1)

Button(tab1,text="+",command=add).grid(row=3,column=0)
Button(tab1,text="*",command=mul).grid(row=4,column=0)
Button(tab1,text="-",command=sub).grid(row=5,column=0)
Button(tab1,text="/",command=div).grid(row=6,column=0)
Button(tab1,text="=",command=eq).grid(row=6,column=3)

Button(tab1,text="del",command=de).grid(row=0,column=2)
Button(tab1,text="AC",command=ac).grid(row=1,column=2)

#Scientific

import math
op=""
ans=0
e=0
cnt=0
cnt1=0
mp=1
mp1=1
a1=0
a2=0
opt=""
def eq():
    global e
    global ans
    if opt=="si":
        res3=a1
        res4=a2
    else:
        res3=txt3.get()
        resu=res3
        if res3=="" or res3 in "+-*/":
            res3=0
        else:
            if mp==1:
                res3=res3[:-1]
                res3=float(res3)
            elif mp==-1:
                res3=res3[1:-1]
                res3=float(res3)
                res3=-res3
            else:
                None
        res4=txt4.get()
        if res4=="" or res4=="-":
            res4=0
        else:
            if mp1==1:
                res4=float(res4)
            elif mp1==-1:
                res4=res4[1:]
                res4=float(res4)
                res4=-res4
            else:
                None
    if op=="+":
        ans=res3+res4
    elif op=="-":
        ans=res3-res4
    elif op=="*":
        ans=res3*res4
    elif op=="/":
        ans=res3/res4
    elif op=="^":
        ans=res3**res4
    elif op=="!":
        if res3%1==0 and res3>=0:
            ans=math.factorial(res3)
        else:
            ans="Invalid"
    elif op=="%":
        if res4==0:
            ans=(res3/100)
        else:
            ans=(res3/(res4*100))
    elif opt=="si":
        ans=res3
    else:
        ans=resu
    e=0
    lbl.configure(text=ans)

def add():
    global op
    global e
    op="+"
    e=1
    txt3.insert(END,"+")
def sub():
    global op
    global e
    op="-"
    e=1
    txt3.insert(END,"-")
def mul():
    global op
    global e
    op="*"
    e=1
    txt3.insert(END,"*")
def div():
    global op
    global e
    op="/"
    e=1
    txt3.insert(END,"/")
def po():
    global op
    global e
    op="^"
    e=1
    txt3.insert(END,"^")
def fac():
    global op
    global e
    op="!"
    e=1
    txt3.insert(END,"!")
def cliper():
    global op
    global e
    op="%"
    e=1
    txt3.insert(END,"%")

def cli1():
    global cnt
    global cnt1
    if e==0:
        txt3.insert(INSERT,"1")
        cnt+=1
    elif e==1:
        txt4.insert(INSERT,"1")
        cnt1+=1
    else:
        None
def cli2():
    global cnt
    global cnt1
    if e==0:
        txt3.insert(INSERT,"2")
        cnt+=1
    elif e==1:
        txt4.insert(INSERT,"2")
        cnt1+=1
    else:
        None
def cli3():
    global cnt
    global cnt1
    if e==0:
        txt3.insert(INSERT,"3")
        cnt+=1
    elif e==1:
        txt4.insert(INSERT,"3")
        cnt1+=1
    else:
        None
def cli4():
    global cnt
    global cnt1
    if e==0:
        txt3.insert(INSERT,"4")
        cnt+=1
    elif e==1:
        txt4.insert(INSERT,"4")
        cnt1+=1
    else:
        None
def cli5():
    global cnt
    global cnt1
    if e==0:
        txt3.insert(INSERT,"5")
    elif e==1:
        txt4.insert(INSERT,"5")
    else:
        None
def cli6():
    global cnt
    global cnt1
    if e==0:
        txt3.insert(INSERT,"6")
        cnt+=1
    elif e==1:
        txt4.insert(INSERT,"6")
        cnt1+=1
    else:
        None
def cli7():
    global cnt
    global cnt1
    if e==0:
        txt3.insert(INSERT,"7")
        cnt+=1
    elif e==1:
        txt4.insert(INSERT,"7")
        cnt1+=1
    else:
        None
def cli8():
    global cnt
    global cnt1
    if e==0:
        txt3.insert(INSERT,"8")
        cnt+=1
    elif e==1:
        txt4.insert(INSERT,"8")
        cnt1+=1
    else:
        None
def cli9():
    global cnt
    global cnt1
    if e==0:
        txt3.insert(INSERT,"9")
        cnt+=1
    elif e==1:
        txt4.insert(INSERT,"9")
        cnt1+=1
    else:
        None
def cli0():
    global cnt
    global cnt1
    if e==0:
        txt3.insert(INSERT,"0")
        cnt+=1
    elif e==1:
        txt4.insert(INSERT,"0")
        cnt1+=1
    else:
        None
def cli():
    global cnt
    global cnt1
    if e==0:
        txt3.insert(INSERT,".")
        cnt+=1
    elif e==1:
        txt4.insert(INSERT,".")
        cnt+=1
    else:
        None
def clipi():
    p=math.pi
    if e==0:
        txt3.insert(END,p)
    elif e==1:
        txt4.insert(END,p)
    else:
        None
def clie():
    ex=math.e
    if e==0:
        txt3.insert(END,ex)
    elif e==1:
        txt4.insert(END,ex)
    else:
        None
def de():
    global cnt
    global cnt1
    global mp
    global mp1
    if e==0:
        res=txt3.get()
        i=txt3.index(INSERT)
        txt3.delete(i-1,INSERT)
        cnt-=1
        if mp==-1 and len(res)==1:
            mp=1
    elif e==1:
        res=txt4.get()
        i=txt4.index(INSERT)
        txt4.delete(i-1,INSERT)
        cnt1-=1
        if mp1==-1 and len(res)==1:
            mp1=1
    else:
        None
def ac():
    global cnt
    global cnt1
    global mp
    global mp1
    global e
    global res3
    global res4
    global op
    global opt
    global a1
    global a2
    global resu
    a1=0
    a2=0
    resu=0
    opt=""
    op=""
    mp=1
    mp1=1
    cnt=0
    cnt1=0
    e=0
    res3=0
    res4=0
    txt3.delete(0,END)
    txt4.delete(0,END)
    lbl.configure(text="Answer")
def answ():
    if e==0:
        txt3.delete(0,INSERT)
        txt3.insert(INSERT,ans)
        ans1=str(ans)
        cnt=len(ans1)
    elif e==1:
        txt4.delete(0,INSERT)
        txt4.insert(INSERT,ans)
        ans2=str(ans)
        cnt1=len(ans2)
def clisin():
    global ans
    global a1
    global a2
    global opt
    dr=sel.get()
    if e==0:
        res3=txt3.get()
        if res3=="" or res3=="-":
            res3=0
        else:
            if mp==1:
                res3=float(res3)
            elif mp==-1:
                res3=res3[1:]
                res3=float(res3)
                res3=-res3
        txt3.insert(0,"sin(")
        txt3.insert(END,")")
        if dr==2:
            res3=math.radians(res3)
        a1=math.sin(res3)
    elif e==1:
        res4=txt4.get()
        if res4=="" or res4=="-":
            res4=0
        else:
            if mp1==1:
                res4=float(res4)
            elif mp1==-1:
                res4=res4[1:]
                res4=float(res4)
                res4=-res4
        txt4.insert(0,"sin(")
        txt4.insert(END,")")
        if dr==2:
            res4=math.radians(res4)
        a2=math.sin(res4)
    opt="si"        
def clicos():
    global ans
    global a1
    global a2
    global opt
    dr=sel.get()
    if e==0:
        res3=txt3.get()
        if res3=="" or res3=="-":
            res3=0
        else:
            if mp==1:
                res3=float(res3)
            elif mp==-1:
                res3=res3[1:]
                res3=float(res3)
                res3=-res3
        txt3.insert(0,"cos(")
        txt3.insert(END,")")
        if dr==2:
            res3=math.radians(res3)
        a1=math.cos(res3)
    elif e==1:
        res4=txt4.get()
        if res4=="" or res4=="-":
            res4=0
        else:
            if mp1==1:
                res4=float(res4)
            elif mp1==-1:
                res4=res4[1:]
                res4=float(res4)
                res4=-res4
        txt4.insert(0,"cos(")
        txt4.insert(END,")")
        if dr==2:
            res4=math.radians(res4)
        a2=math.cos(res4)
    opt="si"
def clitan():
    global ans
    global a1
    global a2
    global opt
    dr=sel.get()
    if e==0:
        res3=txt3.get()
        if res3=="" or res3=="-":
            res3=0
        else:
            if mp==1:
                res3=float(res3)
            elif mp==-1:
                res3=res3[1:]
                res3=float(res3)
                res3=-res3
        txt3.insert(0,"tan(")
        txt3.insert(END,")")
        if dr==2:
            res3=math.radians(res3)
        a1=math.tan(res3)
    elif e==1:
        res4=txt4.get()
        if res4=="" or res4=="-":
            res4=0
        else:
            if mp1==1:
                res4=float(res4)
            elif mp1==-1:
                res4=res4[1:]
                res4=float(res4)
                res4=-res4
        txt4.insert(0,"tan(")
        txt4.insert(END,")")
        if dr==2:
            res4=math.radians(res4)
        a2=math.tan(res4)
    opt="si"
def clilog():
    global ans
    global a1
    global a2
    global opt
    if e==0:
        res3=txt3.get()
        if res3=="" or res3=="-":
            res3=0
        else:
            if mp==1:
                res3=float(res3)
                a1=math.log10(res3)
            else:
                a1="Invalid"
        txt3.insert(0,"log(")
        txt3.insert(END,")")
    elif e==1:
        res4=txt4.get()
        if res4=="" or res4=="-":
            res4=0
        else:
            if mp1==1:
                res4=float(res4)
                a2=math.log10(res4)
            else:
                a2="Invalid"
        txt4.insert(0,"log(")
        txt4.insert(END,")")
    opt="si"
def cliln():
    global ans
    global a1
    global a2
    global opt
    if e==0:
        res3=txt3.get()
        if res3=="" or res3=="-":
            res3=0
        else:
            if mp==1:
                res3=float(res3)
                a1=math.log(res3)
            else:
                a1="Invalid"
        txt3.insert(0,"ln(")
        txt3.insert(END,")")
    elif e==1:
        res4=txt4.get()
        if res4=="" or res4=="-":
            res4=0
        else:
            if mp1==1:
                res4=float(res4)
                a2=math.log(res4)
            else:
                a2="Invalid"
        txt4.insert(0,"ln(")
        txt4.insert(END,")")
    opt="si"
def cliin():
    global ans
    if e==0:
        if mp==1:
            res3=txt3.get()
            res3=float(res3)
            if res3==0:
                ans="Infinity"
            else:
                ans=1/res3
        elif mp==-1:
            res3=txt3.get()
            res3=res3[1:]
            res3=float(res3)
            if res3==0:
                ans="Infinity"
            else:
                ans=-(1/res3)
        else:
            None
    elif e==1:
        if mp1==1:
            res4=txt4.get()
            res4=float(res4)
            if res4==0:
                ans="Infinity"
            else:
                ans=1/res4
        elif mp1==-1:
            res4=txt4.get()
            res4=res4[1:]
            res4=float(res4)
            if res4==0:
                ans="Infinity"
            else:
                ans=-(1/res4)
        else:
            None
    lbl.configure(text=ans)
def climin():
    global mp
    global mp1
    if e==0:
        if mp==1:
            txt3.insert(0,"-")
        elif mp==-1:
            txt3.delete(0,1)
        else:
            None
        mp*=-1
    elif e==1:
        if mp1==1:
            txt4.insert(0,"-")
        elif mp1==-1:
            txt4.delete(0,1)
        else:
            None
        mp1*=-1
    else:
        None
def clileft():
    global cnt
    global cnt1
    if e==0:
        cnt-=1
        txt3.icursor(cnt+1)
    elif e==1:
        cnt1-=1
        txt4.icursor(cnt1+1)
    else:
        None
def cliup():
    global e
    e=0
def clidown():
    global e
    e=1
def cliright():
    global cnt
    global cnt1
    if e==0:
        cnt+=1
        txt3.icursor(cnt+1)
    elif e==1:
        cnt1+=1
        txt4.icursor(cnt1+1)
    else:
        None

txt3=Entry(tab2,width=25)
txt3.grid(row=0,column=3)
txt4=Entry(tab2,width=25)
txt4.grid(row=1,column=3)
lbl=Label(tab2,text="Answer")
lbl.grid(row=2,column=3)

sel=IntVar()
rad1=ttk.Radiobutton(tab2,text="Radians",value=1,variable=sel)
rad2=ttk.Radiobutton(tab2,text="Degrees",value=2,variable=sel)
rad1.grid(row=4,column=3)
rad2.grid(row=3,column=3)

Button(tab2,text=" 1 ",command=cli1).grid(row=5,column=0)
Button(tab2,text=" 2 ",command=cli2).grid(row=5,column=1)
Button(tab2,text=" 3 ",command=cli3).grid(row=5,column=2)
Button(tab2,text=" 4 ",command=cli4).grid(row=4,column=0)
Button(tab2,text=" 5 ",command=cli5).grid(row=4,column=1)
Button(tab2,text=" 6 ",command=cli6).grid(row=4,column=2)
Button(tab2,text=" 7 ",command=cli7).grid(row=3,column=0)
Button(tab2,text=" 8 ",command=cli8).grid(row=3,column=1)
Button(tab2,text=" 9 ",command=cli9).grid(row=3,column=2)
Button(tab2,text=" 0 ",command=cli0).grid(row=6,column=1)
Button(tab2,text=" . ",command=cli).grid(row=6,column=0)
Button(tab2,text="PI ",command=clipi).grid(row=3,column=5)
Button(tab2,text=" e ",command=clie).grid(row=3,column=6)

Button(tab2,text=" + ",command=add).grid(row=5,column=5)
Button(tab2,text=" * ",command=mul).grid(row=4,column=5)
Button(tab2,text=" - ",command=sub).grid(row=5,column=6)
Button(tab2,text=" / ",command=div).grid(row=4,column=6)
Button(tab2,text=" = ",command=eq).grid(row=6,column=6)
Button(tab2,text=" ^ ",command=po).grid(row=4,column=4)
Button(tab2,text="  !  ",command=fac,bg="black",fg="white").grid(row=0,column=4)
Button(tab2,text="sin",command=clisin,bg="black",fg="white").grid(row=1,column=4)
Button(tab2,text="cos",command=clicos,bg="black",fg="white").grid(row=1,column=5)
Button(tab2,text="tan",command=clitan,bg="black",fg="white").grid(row=1,column=6)
Button(tab2,text="log",command=clilog,bg="black",fg="white").grid(row=0,column=5)
Button(tab2,text="ln ",command=cliln,bg="black",fg="white").grid(row=0,column=6)
Button(tab2,text=" % ",command=cliper).grid(row=5,column=4)
Button(tab2,text="1/x",command=cliin).grid(row=3,column=4)
Button(tab2,text="+/-",command=climin).grid(row=2,column=1)

Button(tab2,text="del",command=de,bg="orange").grid(row=6,column=5)
Button(tab2,text="AC",command=ac,bg="orange").grid(row=6,column=4)
Button(tab2,text="Ans",command=answ).grid(row=6,column=2)

Button(tab2,text=" < ",command=clileft,bg="darkblue",fg="white").grid(row=1,column=0)
Button(tab2,text=" > ",command=cliright,bg="darkblue",fg="white").grid(row=1,column=2)
Button(tab2,text=" V  ",command=clidown,bg="darkblue",fg="white").grid(row=1,column=1)
Button(tab2,text=" /\ ",command=cliup,bg="darkblue",fg="white").grid(row=0,column=1)

#end

tab_control.pack(expand=1, fill='both')

window.mainloop()
