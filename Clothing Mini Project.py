from tkinter import *
from tkinter import messagebox
import re
from PIL import ImageTk,Image
import pymysql

db=pymysql.Connect(host="localhost",user="root",password="10114nov",database="signup")
cur=db.cursor()

#cur.execute("create database signup")
#cur.execute("use signup")
#cur.execute("create table signup_info(Name varchar(20),Age varchar(10),Contact varchar(10),Address varchar(150),Mail varchar(20),Pw varchar(10))")


s=Tk()
s.title("Sign Up page")
s.geometry("1440x900")

c = Canvas(s, width=1440, height=900, bg='white')
c.pack()

img = ImageTk.PhotoImage(Image.open("img14.jpg"))
c.create_image(0, 0, anchor=NW, image=img)

global v1,v2

l1=Label(s,text="AHR Garments",fg="blue",font="cambria 35 italic").place(x=720,y=50)
l2=Label(s,text="SIGN UP",fg="black",font="cambria 25 bold").place(x=780,y=140)
l3=Label(s,text="Name ",fg="red",font="cambria 20 bold").place(x=620,y=210)
l4=Label(s,text="Age ",fg="red",font="cambria 20 bold").place(x=620,y=270)
l5=Label(s,text="Gender ",fg="red",font="cambria 20 bold").place(x=620,y=330)
l6=Label(s,text="Mobile no ",fg="red",font="cambria 20 bold").place(x=620,y=390)
l7=Label(s,text="Address ",fg="red",font="cambria 20 bold").place(x=620,y=450)  
l8=Label(s,text="Email ID ",fg="red",font="cambria 20 bold").place(x=620,y=510)
l9=Label(s,text="Password ",fg="red",font="cambria 20 bold").place(x=620,y=570)
l10=Label(s,text="R-Password ",fg="red",font="cambria 20 bold").place(x=620,y=640)
l11=Label(s,text="Password should be minimum 8 character(suggested atleast alphanumeric & one upper case and special character for strong password)",fg="yellow",bg="black",font="cambria 7").place(x=870,y=595)
def signup():
    global name,age,mob,addr,mail,pwd,rpwd

    name=e3.get()
    age=e4.get()
    mob=e6.get()
    addr=e7.get()
    mail=e8.get()
    pwd=e9.get()
    rpwd=e10.get()
    

    query="insert into signup_info values(%s,%s,%s,%s,%s,%s)"
    val=[name,age,mob,addr,mail,pwd]
    cur.execute(query,val)
    db.commit()
    
    if name.isalpha():
        if age.isnumeric():
            mob=re.findall("[0-9]",mob)
            if len(mob)==10:
                if "@" and (".com" or ".in") in mail:
                    if len(pwd)>=8:
                        if pwd==rpwd:
                            global s,s1,s2,s3
                            s1=Toplevel(s)
                            s1.geometry("1440x900")
                            load=Image.open("img11.jpg")
                            photo=ImageTk.PhotoImage(load)
                            label=Label(s1,image=photo)
                            label.image=photo
                            label.place(x=0,y=0)

                            s1.title("Login page")
                            l16=Label(s1,text="Login Page",font="cambria 35 italic",fg="blue").place(x=620,y=200)
                            l17=Label(s1,text="Email ID/\nMobile No.",font="cambria 20 bold",fg='red').place(x=420,y=350)
                            l18=Label(s1,text="Password",font="cambria 20 bold",fg='red').place(x=420,y=450)

                            e11=Entry(s1,width=40,bg="sky blue")
                            e11.place(x=620,y=360)
                            e12=Entry(s1,width=40,show="*",bg="sky blue")
                            e12.place(x=620,y=455)
                            def login():
                                email=e11.get()
                                pwsd=e12.get()
                                cur.execute("select * from signup_info")
                                for i in cur:
                                    if (email==i[4] or mob==i[2]) and pwsd==i[5]:
                                        l20=Label(s1,text="Login Successful",fg='red',font="cambria 20").place(x=620,y=720)         
                                        s2=Toplevel(s1)
                                        s2.title("Order page")
                                        s2.geometry("1440x900")
                                        load=Image.open("img34.webp")
                                        photo=ImageTk.PhotoImage(load)
                                        label=Label(s2,image=photo)
                                        label.image=photo
                                        label.place(x=0,y=0)
                                        
                                        l=Label(s2,text="Welcome to AHR Garments",fg="blue",font="cambria 35 italic").pack()
                                        l1=Label(s2,text="Mens: ",fg="red",font="Arial 25 bold").place(x=200,y=150)
                                        l2=Label(s2,text="Womens: ",fg="red",font="Arial 25 bold").place(x=600,y=150)
                                        l3=Label(s2,text="Kids: ",fg="red",font="Arial 25 bold").place(x=1000,y=150)
                                        l=Label(s2,text="Welcome "+name,fg="blue",font="Arial 15 bold").place(x=1200,y=50)

                                        
                                        l4=Label(s2,text="____________________________________________________________________________________________________").place(x=200,y=420)
                                        l5=Label(s2,text="Invoice",font="Arial 10 bold").place(x=400,y=440)
                                        l4=Label(s2,text="____________________________________________________________________________________________________").place(x=200,y=457)
                                        l5=Label(s2,text="Items",fg="red",font="Arial 12 bold").place(x=200,y=475)
                                        l6=Label(s2,text="Qty",fg="red",font="Arial 12 bold").place(x=400,y=475)
                                        l7=Label(s2,text="Price",fg="red",font="Arial 12 bold").place(x=620,y=475)
                                        l4=Label(s2,text="____________________________________________________________________________________________________").place(x=200,y=495)

                                        
                                        order=[]
                                        def f1():
                                            global a,b,c,d,e,f,g,h,i,j,k,l,m,n,o
                                            a=sp1.get()
                                            order.append(int(a)*350)
                                            l=Label(s2,text="Formal Pant"+(str(a)).center(60)+(str(int(a)*350)).center(50),fg="blue",font="cambria 12").place(x=200,y=515)

                                        l= Label(s2,text="Formal Pant_Rs.350",fg="teal",font="cambria 18").place(x=200,y=200)
                                        sp1=Spinbox(s2,from_=0,to=20,width=5,bg="sky blue")
                                        sp1.place(x=425,y=205)
                                        b=Button(s2,text="ok",width=5,height=1,fg="purple",activebackground="blue",font="cambria 10",command=f1).place(x=490,y=200)
                                        def f2():
                                            b=sp2.get()
                                            order.append(int(b)*150)
                                            l=Label(s2,text="T-shirt"+(str(b)).center(80)+"             "+str(int(b)*150),fg="blue",font="cambria 12").place(x=200,y=535)


                                        l= Label(s2,text="T-shirt-Rs.150",fg="teal",font="cambria 18").place(x=200,y=250)
                                        sp2=Spinbox(s2,from_=0,to=20,width=5,bg="sky blue")
                                        sp2.place(x=425,y=255)
                                        b=Button(s2,text="ok",width=5,height=1,fg="purple",activebackground="blue",font="cambria 10",command=f2).place(x=490,y=250)
                                        def f3():
                                            c=sp3.get()
                                            order.append(int(c)*750)
                                            l=Label(s2,text="Jeans"+(str(c)).center(81)+""+"               "+str(int(c)*750),fg="blue",font="cambria 12").place(x=200,y=555)


                                        l= Label(s2,text="Jeans-Rs.750",fg="teal",font="cambria 18").place(x=200,y=300)
                                        sp3=Spinbox(s2,from_=0,to=20,width=5,bg="sky blue")
                                        sp3.place(x=425,y=305)
                                        b=Button(s2,text="ok",width=5,height=1,fg="purple",activebackground="blue",font="cambria 10",command=f3).place(x=490,y=300)
                                        def f4():
                                            d=sp4.get()
                                            order.append(int(d)*1050)
                                            l=Label(s2,text="Casual Shirt"+(str(d)).center(60)+(str(int(d)*1050)).center(50),fg="blue",font="cambria 12").place(x=200,y=575)


                                        l= Label(s2,text="Casual Shirt-Rs.1050",fg="teal",font="cambria 18").place(x=200,y=350)
                                        sp4=Spinbox(s2,from_=0,to=20,width=5,bg="sky blue")
                                        sp4.place(x=425,y=355)
                                        b=Button(s2,text="ok",width=5,height=1,fg="purple",activebackground="blue",font="cambria 10",command=f4).place(x=490,y=350)
                                        def f5():
                                            e=sp5.get()
                                            order.append(int(e)*950)
                                            l=Label(s2,text="Formal Shirt"+(str(e)).center(60)+(str(int(e)*950)).center(50),fg="blue",font="cambria 12").place(x=200,y=595)
                                            
                                        l= Label(s2,text="Formal Shirt-Rs.950",fg="teal",font="cambria 18").place(x=200,y=400)
                                        sp5=Spinbox(s2,from_=0,to=20,width=5,bg="sky blue")
                                        sp5.place(x=425,y=405)
                                        b=Button(s2,text="ok",width=5,height=1,fg="purple",activebackground="blue",font="cambria 10",command=f5).place(x=490,y=400)

                                        def f6():
                                            f=sp6.get()
                                            order.append(int(f)*950)
                                            l=Label(s2,text="Cotton Saree"+(str(f)).center(60)+(str(int(f)*950)).center(50),fg="blue",font="cambria 12").place(x=200,y=615)
                                            
                                        l= Label(s2,text="Cotton Saree-Rs.950",fg="indigo",font="cambria 18").place(x=600,y=195)
                                        sp6=Spinbox(s2,from_=0,to=20,width=5,bg="sky blue")
                                        sp6.place(x=835,y=205)
                                        b=Button(s2,text="ok",width=5,height=1,fg="purple",activebackground="blue",font="cambria 10",command=f6).place(x=890,y=200)
                                        def f7():
                                            g=sp7.get()
                                            order.append(int(g)*750)
                                            l=Label(s2,text="Slik Saree"+(str(g)).center(65)+(str(int(g)*750)).center(50),fg="blue",font="cambria 12").place(x=200,y=635)
                                            
                                        l= Label(s2,text="Slik Saree-Rs.750",fg="indigo",font="cambria 18").place(x=600,y=245)
                                        sp7=Spinbox(s2,from_=0,to=20,width=5,bg="sky blue")
                                        sp7.place(x=835,y=255)
                                        b=Button(s2,text="ok",width=5,height=1,fg="purple",activebackground="blue",font="cambria 10",command=f7).place(x=890,y=250)
                                        def f8():
                                            h=sp8.get()
                                            order.append(int(h)*1250)
                                            l=Label(s2,text="Kurthi"+(str(h)).center(78)+""+"               "+str(int(h)*1250),fg="blue",font="cambria 12").place(x=200,y=655)
                                            
                                        l= Label(s2,text="Kurthi-Rs.1250",fg="indigo",font="cambria 18").place(x=600,y=295)
                                        sp8=Spinbox(s2,from_=0,to=20,width=5,bg="sky blue")
                                        sp8.place(x=835,y=305)
                                        b=Button(s2,text="ok",width=5,height=1,fg="purple",activebackground="blue",font="cambria 10",command=f8).place(x=890,y=300)
                                        def f9():
                                            i=sp9.get()
                                            order.append(int(i)*250)              
                                            l=Label(s2,text="Full Skirt"+(str(i)).center(65)+(str(int(i)*250)).center(50),fg="blue",font="cambria 12").place(x=200,y=675)
                                            
                                        l= Label(s2,text="Full Skirt-Rs.250",fg="indigo",font="cambria 18").place(x=600,y=345)
                                        sp9=Spinbox(s2,from_=0,to=20,width=5,bg="sky blue")
                                        sp9.place(x=835,y=355)
                                        b=Button(s2,text="ok",width=5,height=1,fg="purple",activebackground="blue",font="cambria 10",command=f9).place(x=890,y=350)
                                        def f10():
                                            j=sp10.get()
                                            order.append(int(j)*150)
                                            l=Label(s2,text="Makna"+(str(j)).center(77)+""+"               "+str(int(j)*150),fg="blue",font="cambria 12").place(x=200,y=695)
                                            
                                        l= Label(s2,text="Makna-Rs.150",fg="indigo",font="cambria 18").place(x=600,y=395)
                                        sp10=Spinbox(s2,from_=0,to=20,width=5,bg="sky blue")
                                        sp10.place(x=835,y=405)
                                        b=Button(s2,text="ok",width=5,height=1,fg="purple",activebackground="blue",font="cambria 10",command=f10).place(x=890,y=400)
                                        def f11():
                                            k=sp11.get()
                                            order.append(int(k)*200)
                                            l=Label(s2,text="Trousers"+(str(k)).center(65)+(str(int(k)*200)).center(50),fg="blue",font="cambria 12").place(x=200,y=715)
                                
                                        l= Label(s2,text="Trousers-Rs.200",fg="fuchsia",font="cambria 18").place(x=1000,y=190)
                                        sp11=Spinbox(s2,from_=0,to=20,width=5,bg="sky blue")
                                        sp11.place(x=1235,y=200)
                                        b=Button(s2,text="ok",width=5,height=1,fg="purple",activebackground="blue",font="cambria 10",command=f11).place(x=1300,y=195)
                                        def f12():
                                            l=sp12.get()
                                            order.append(int(l)*450)
                                            l=Label(s2,text="Kids Jeans"+(str(l)).center(63)+(str(int(l)*450)).center(50),fg="blue",font="cambria 12").place(x=200,y=735)
                                             
                                        l= Label(s2,text="Kid Jeans-Rs.450",fg="fuchsia",font="cambria 18").place(x=1000,y=240)
                                        sp12=Spinbox(s2,from_=0,to=20,width=5,bg="sky blue")
                                        sp12.place(x=1235,y=250)
                                        b=Button(s2,text="ok",width=5,height=1,fg="purple",activebackground="blue",font="cambria 10",command=f12).place(x=1300,y=245)
                                        def f13():
                                            m=sp13.get()
                                            order.append(int(m)*90)
                                            l=Label(s2,text="Woolen Socks"+(str(m)).center(56)+(str(int(m)*90)).center(50),fg="blue",font="cambria 12").place(x=200,y=755)
                                            
                                        l= Label(s2,text="Woolen Socks-Rs.90",fg="fuchsia",font="cambria 18").place(x=1000,y=290)
                                        sp13=Spinbox(s2,from_=0,to=20,width=5,bg="sky blue")
                                        sp13.place(x=1235,y=300)
                                        b=Button(s2,text="ok",width=5,height=1,fg="purple",activebackground="blue",font="cambria 10",command=f13).place(x=1300,y=295)
                                        def f14():
                                            n=sp14.get()
                                            order.append(int(n)*110)
                                            l=Label(s2,text="Caps "+(str(n)).center(81)+""+"               "+str(int(n)*110),fg="blue",font="cambria 12").place(x=200,y=775)
                                            
                                        l= Label(s2,text="Caps-Rs.110",fg="fuchsia",font="cambria 18").place(x=1000,y=340)
                                        sp14=Spinbox(s2,from_=0,to=20,width=5,bg="sky blue")
                                        sp14.place(x=1235,y=350)
                                        b=Button(s2,text="ok",width=5,height=1,fg="purple",activebackground="blue",font="cambria 10",command=f14).place(x=1300,y=345)
                                        def f15():
                                            o=sp15.get()
                                            order.append(int(o)*50)
                                            l=Label(s2,text="Mufler"+(str(o)).center(77)+""+"               "+str(int(o)*50),fg="blue",font="cambria 12").place(x=200,y=795)
                                            
                                        l= Label(s2,text="Mufler-Rs.50",fg="fuchsia",font="cambria 18").place(x=1000,y=390)
                                        sp15=Spinbox(s2,from_=0,to=20,width=5,bg="sky blue")
                                        sp15.place(x=1235,y=400)
                                        b=Button(s2,text="ok",width=5,height=1,fg="purple",activebackground="blue",font="cambria 10",command=f15).place(x=1300,y=395)
                                        def total():
                                            global addi
                                            add=0
                                            for i in order:
                                                add+=i
                                                addi="".join(str(add))
                                                l=Label(s2,text=name+" your Total bill amount is Rs."+str(add),fg="purple",font="cambria 20").place(x=780,y=550)
                                                l=Label(s2,text="Confirm Address:-",fg="red",font="camcbria 20").place(x=780,y=600)
                                                l=Label(s2,text=addr,fg="teal",font="camcbria 15").place(x=900,y=635)
                            

                                        b5=Button(s2,text="Order",width=5,height=2,activebackground="blue",fg="purple",font="Arial 10 italic",command=total).place(x=1150,y=450)                
                                        b8=Button(s2,text="Logout",width=7,height=2,activebackground="blue",fg="purple",font="Arial 10 italic",command=s2.destroy).place(x=1300,y=75)
                                        def pay():
                                            global upiid,upin
                                            upiid="9952990372@ybl.com"
                                            upin="121"
                                            s3=Toplevel(s2)
                                            s3.title("Payment Page")
                                            s3.geometry("1440x900")
                                            load=Image.open("img35.jpg")
                                            photo=ImageTk.PhotoImage(load)
                                            label=Label(s3,image=photo)
                                            label.image=photo
                                            label.place(x=0,y=0)

                                            l=Label(s3,text="Payment Options",fg="blue",font="cambria 35 italic").pack()
                                            l=Label(s3,text="Paytm/Gpay/Phonepae ",fg="red",font="cambria 25 bold").place(x=100,y=100)
                                            l=Label(s3,text="UPI ID/Mobile Number ",fg="blue",font="cambria 20 bold").place(x=175,y=150)
                                            e21=Entry(s3,width=40,bg="sky blue")
                                            e21.place(x=530,y=165)
                                            l=Label(s3,text="Amount ",fg="blue",font="cambria 20 bold").place(x=175,y=200)
                                            e22=Entry(s3,width=40,bg="sky blue")
                                            e22.place(x=530,y=215)
                                            l=Label(s3,text="UPI PIN ",fg="blue",font="cambria 20 bold").place(x=175,y=250)
                                            e23=Entry(s3,width=40,bg="sky blue")
                                            e23.place(x=530,y=265)
                                            l=Label(s3,text="Credit/Debit card ",fg="red",font="cambria 25 bold").place(x=100,y=350)
                                            l=Label(s3,text="Card Number ",fg="blue",font="cambria 20 bold").place(x=175,y=400)
                                            e24=Entry(s3,width=40,bg="sky blue")
                                            e24.place(x=400,y=415)
                                            l=Label(s3,text="Exp Date ",fg="blue",font="cambria 20 bold").place(x=175,y=450)
                                            e25=Entry(s3,width=10,bg="sky blue")
                                            e25.place(x=400,y=460)
                                            l=Label(s3,text="CVV ",fg="blue",font="cambria 20 bold").place(x=475,y=450)
                                            e26=Entry(s3,width=10,bg="sky blue")
                                            e26.place(x=550,y=460)
                                            l=Label(s3,text="Amount ",fg="blue",font="cambria 20 bold").place(x=175,y=500)
                                            e27=Entry(s3,width=20,bg="sky blue")
                                            e27.place(x=400,y=510)
                                            l=Label(s3,text="OTP ",fg="blue",font="cambria 20 bold").place(x=175,y=550)
                                            e28=Entry(s3,width=20,bg="sky blue")
                                            e28.place(x=400,y=560)
                                            def pay1():
                                                uid=e21.get()
                                                am=e22.get()
                                                up=e23.get()
                                                if uid==upiid or mob:
                                                    if addi==am:
                                                        if upin==up:
                                                            w=Tk()
                                                            w.eval("tk::PlaceWindow %s center"% w.winfo_toplevel())
                                                            w.withdraw()
                                                            messagebox.showinfo("Order & Payment Status","Payment Successful\nOrder Placed\nyour order will be deliverd in 3 working days\nThank You for shopping")
                                                            w.deiconify()
                                                            w.destroy()
                                                            w.quit()
                                                        else:
                                                            l=Label(s3,text="UPI PIN Incorrect",fg="red",font="cambria 10").place(x=530,y=290)
                                                    else:
                                                        l=Label(s3,text="",fg="red",font="cambria 10").place(x=530,y=240)
                                                else:
                                                    l=Label(s3,text="Invalid UPI-ID or Mobile Number",fg="red",font="cambria 10").place(x=530,y=190)
                                            def pay2():
                                                crno="1234 5678 9012"
                                                exp="08/23"
                                                cvv="212"
                                                otp="111"
                                                cr=e24.get()
                                                ep=e25.get()
                                                cv=e26.get()
                                                ap=e27.get()
                                                ot=e28.get()
                                                if crno==cr and exp==ep and cvv==cv:
                                                    if ap==addi:
                                                        if otp==ot:
                                                             w=Tk()
                                                             w.eval("tk::PlaceWindow %s center"% w.winfo_toplevel())
                                                             w.withdraw()
                                                             messagebox.showinfo("Order & Payment Status","Payment Successful\nOrder Placed\nyour order will be deliverd in 3 working days\nThank You for shopping")
                                                             w.deiconify()
                                                             w.destroy()
                                                             w.quit()
                                                        else:
                                                            l=Label(s3,text="Incorrect OTP",fg="red",font="cambria 10 bold").place(x=400,y=585)
                                                    else:
                                                        l=Label(s3,text="Invalid Amount",fg="red",font="cambria 10 bold").place(x=400,y=535)
                                                else:
                                                    l=Label(s3,text="Invalid card details ",fg="red",font="cambria 10 bold").place(x=400,y=485)
                                            def pay3():
                                                w=Tk()
                                                w.eval("tk::PlaceWindow %s center"% w.winfo_toplevel())
                                                w.withdraw()
                                                messagebox.showinfo("Order status","Order Placed\nyour order will be deliverd in 3 working days\nThank You for shopping")
                                                w.deiconify()
                                                w.destroy()
                                                w.quit()
                                                  
                                            b=Button(s3,text="Pay",fg="purple",width=7,height=2,activebackground="blue",font="Arial 10 bold",command=pay1).place(x=710,y=300)
                                            b=Button(s3,text="Pay",fg="purple",width=7,height=2,activebackground="blue",font="Arial 10 bold",command=pay2).place(x=710,y=580)
                                            c1=Checkbutton(s3,text="COD (cash on Delivery)",fg="red",font="cambria 20 bold",command=pay3).place(x=100,y=620)
                                        b7=Button(s2,text="Confirm",width=7,height=2,activebackground="blue",fg="purple",font="Arial 15 italic",command=pay).place(x=1130,y=700)
                                        b6=Button(s2,text="Cancel",width=7,height=2,activebackground="blue",fg="purple",font="Arial 15 italic",command=s2.destroy).place(x=780,y=700)
                                        s2.mainloop()
        
                                    else:
                                        l19=Label(s1,text="Account Notfound/Incorrect password",fg='red',font="cambria 20").place(x=620,y=480)
                                '''else:
                                    l20=Label(s1,text="Invalid mailId/Mobile Number",fg='red',font="cambria 20").place(x=620,y=380)'''
                                            
                            b3=Button(s1,text="Login",width=10,height=2,activebackground="blue",fg="purple",command=login,font="cambria 15 bold").place(x=800,y=560)
                            b=Button(s1,text="signup",width=5,height=1,activebackground="blue",fg="purple",command=s1.destroy,font="cambria 15 bold").place(x=850,y=660)
                            l=Label(s1,text="Create Account? ",fg="yellow",bg="black",font="cambria 15").place(x=680,y=665)
                            b4=Button(s1,text="Cancel",width=10,height=2,activebackground="blue",fg="purple",command=s1.destroy,font="cambria 15 bold").place(x=600,y=560)

                        else:
                             l12=Label(s,text="Password Mismatch",fg="red",font="cambria 10").place(x=870,y=670)
                    else:
                        l13=Label(s,text="Password not strong",fg="red",font="cambria 10").place(x=870,y=620)
                else:
                    l14=Label(s,text="Invalid Email ID",fg="red",font="cambria 10").place(x=870,y=540)
            else:
                l15=Label(s,text="Invalid Mobile Number",fg="red",font="cambria 10").place(x=870,y=420)
        else:
            l15=Label(s,text="Invalid Entry",fg="red",font="cambria 10").place(x=870,y=300)
    else:
        l15=Label(s,text="Invalid Name",fg="red",font="cambria 10").place(x=870,y=240)
    

e3=Entry(s,width=40,bg="sky blue")
e3.place(x=870,y=210)

e4=Entry(s,width=40,bg="sky blue")
e4.place(x=870,y=270)

e6=Entry(s,width=40,bg="sky blue")
e6.place(x=870,y=390)

e7=Entry(s,width=40,bg="sky blue")
e7.place(x=870,y=450)

e8=Entry(s,width=40,bg="sky blue")
e8.place(x=870,y=510)

e9=Entry(s,width=40,bg="sky blue",show="*")
e9.place(x=870,y=570)

e10=Entry(s,width=40,bg="sky blue",show="*")
e10.place(x=870,y=640)

b1=Button(s,text="Signup",width=10,height=2,command=signup,activebackground="blue",fg="purple",font="cambria 15 bold").place(x=1000,y=720)
b2=Button(s,text="Cancel",width=10,height=2,command=s.destroy,activebackground="blue",fg="purple",font="cambria 15 bold").place(x=800,y=720)

c1=Checkbutton(s,text="Male",bg='sky blue').place(x=870,y=325)
c2=Checkbutton(s,text="Female",bg='sky blue').place(x=870,y=355)






