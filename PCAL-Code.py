from tkinter import *
import math
import random
root = Tk()
root.title("Calculator")
root.resizable(False,False)

#ค่าเริ่มต้น
data = ""
message = StringVar(value=" ")

#คำสั่ง
def btn(number):
    global data
    data = data+str(number)
    message.set(data)

def result():
    try:
        global data
        calculate = ("%.2f"%eval(data))
        message.set(calculate)
    except:
        message.set("Error")
    data = ""

def clear():
    global data
    data = ""
    message.set(data)

def Delete():
    global data
    global message
    a = ""
    lenght = len(data)-1
    for i in range(lenght):
        a += data[i]
    data = a
    message.set(data)



#ฟังก์ชั่น
def percent01():
    global data
    global message
    try:
        result = str(float(eval(data))/100)
        message.set(result)
    except:
        message.set("Error")
    data = ""

def Abusolub02():
    global data
    global message
    try:
        result = str(abs(float(eval(data))))
        message.set("|"+result+"|")
    except:
        message.set("Error")
    data = ""

def Pi03():
    global data
    global message
    try:
        result = str(float(eval(data))*3.14159)
        message.set(result)
    except:
        message.set("Error")
    data = ""

def Xdivide04():
    global data
    global message
    try:
        result = 1/float(eval(data))
        message.set(result)
    except:
        message.set("Error")
    data = ""

def log05():
    global data
    global message
    try:
        result = math.log(eval(data),10)
        message.set(result)
    except:
        message.set("Error")
    data = ""

def In06():
    global data
    global message
    try:
        result = math.log(eval(data),2.71828182845904)
        message.set(result)
    except:
        message.set("Error")
    data = ""

def e07():
    global data
    global message
    try:
        result = str(float(eval(data))*2.71828182845904)
        message.set(result)
    except:
        message.set("Error")
    data = ""

def Ex08():
    global data
    global message
    try:
        result = math.exp(eval(data))
        message.set(result)
    except:
        message.set("Error")
    data = ""

def sin09():
    global data
    global message
    try:
        if data=="90":
            result = ("%.0f"%math.sin(math.radians(eval(data))))
            message.set(result)
        else:
            result = ("%.3f"%math.sin(math.radians(eval(data))))
            message.set(result)
    except:
        message.set("Error")
    data = ""

def cos10():
    global data
    global message
    try:
        if data=="90":
            result = ("%.0f"%math.cos(math.radians(eval(data))))
            message.set(result)
        else:
            result = ("%.3f"%math.cos(math.radians(eval(data))))
            message.set(result)
    except:
        message.set("Error")
    data = ""

def tan11():
    global data
    global message
    try:
        result = math.tan(math.radians(eval(data)))
        message.set(result)
    except:
        message.set("Error")
    data = ""

def sinh12():
    global data
    global message
    try:
        result = math.sinh(eval(data))
        message.set(result)
    except:
        message.set("Error")
    data = ""

def cosh13():
    global data
    global message
    try:
        result = math.cosh(eval(data))
        message.set(result)
    except:
        message.set("Error")
    data = ""

def tanh14():
    global data
    global message
    try:
        result = math.tanh(eval(data))
        message.set(result)
    except:
        message.set("Error")
    data = ""

def arcsin15():
    global data
    global message
    try:
        result = math.asin(eval(data))
        message.set(result)
    except:
        message.set("Error")
    data = ""

def arccos16():
    global data
    global message
    try:
        result = math.acos(eval(data))
        message.set(result)
    except:
        message.set("Error")
    data = ""

def arctan17():
    global data
    global message
    try:
        result = math.atan(eval(data))
        message.set(result)
    except:
        message.set("Error")
    data = ""

def arcsinh18():
    global data
    global message
    try:
        result = math.asinh(eval(data))
        message.set(result)
    except:
        message.set("Error")
    data = ""

def arccosh19():
    global data
    global message
    try:
        result = math.acosh(eval(data))
        message.set(result)
    except:
        message.set("Error")
    data = ""

def arctanh20():
    global data
    global message
    try:
        result = math.atanh(eval(data))
        message.set(result)
    except:
        message.set("Error")

def rad21():
    global data
    global message
    try:
        result = math.radians(eval(data))
        message.set(result)
    except:
        message.set("Error")
    data = ""

def deg22():
    global data
    global message
    try:
        result = math.degrees(eval(data))
        message.set(result)
    except:
        message.set("Error")
    data = ""

def x2_23():
    global data
    global message
    try:
        result = (eval(data))**2
        message.set(result)
    except:
        message.set("Error")
    data = ""

def root2_24():
    global data
    global message
    try:
        result = (eval(data))**(1/2)
        message.set(result)
    except:
        message.set("Error")
    data = ""

def x3_25():
    global data
    global message
    try:
        result = (eval(data))**3
        message.set(result)
    except:
        message.set("Error")
    data = ""

def root3_26():
    global data
    global message
    try:
        result = (eval(data))**(1/3)
        message.set(result)
    except:
        message.set("Error")
    data = ""

def facx27():
    global data
    global message
    try:
        result = math.factorial(eval(data))
        message.set(result)
    except:
        message.set("Error")
    data = ""

def gemmax28():
    global data
    global message
    try:
        result = math.factorial(eval(data)-1)
        message.set(result)
    except:
        message.set("Error")
    data = ""

def rand29():
    global data
    global message
    try:
        result = random.randint(1,eval(data))
        message.set(result)
    except:
        message.set("Error")

def log30():
    global data
    global message
    try:
        result = math.log(eval(data),2)
        message.set(result)
    except:
        message.set("Error")
    data = ""

def Pi2_31():
    global data
    global message
    try:
        result = (eval(data)*(2*3.14159))
        message.set(result)
    except:
        message.set("Error")
    data = ""

#หน้าจอคำนวนเรขาคณิต
def geometrix():
    rootgeo = Tk()
    rootgeo.title("Geometrix calculator")
    rootgeo.resizable(False,False)
    head = Label(rootgeo,text="Input Value                                  Select Result",fg="orange",font=20).grid(columnspan=4)
    Label(rootgeo,fg="orange",text=" Radius:",font=30).grid(row=1)
    radius = IntVar(rootgeo)
    pic1 = Entry(rootgeo,width=15,textvariable=radius,font=30)
    pic1.grid(row=1,column=1)
 
    Label(rootgeo,fg="orange",text="Width:",font=30).grid(row=2)
    width = IntVar(rootgeo)
    pic2 = Entry(rootgeo,width=15,textvariable=width,font=30)
    pic2.grid(row=2,column=1)

    Label(rootgeo,fg="orange",text=" Long:",font=30).grid(row=3)
    long = IntVar(rootgeo)
    pic3 = Entry(rootgeo,width=15,textvariable=long,font=30)
    pic3.grid(row=3,column=1)

    Label(rootgeo,fg="orange",text="Height:",font=30).grid(row=4)
    height = IntVar(rootgeo)
    pic4 = Entry(rootgeo,width=15,textvariable=height,font=30)
    pic4.grid(row=4,column=1)

    Label(rootgeo,fg="orange",text="Base:",font=30).grid(row=5)
    base = IntVar(rootgeo)
    pic6 = Entry(rootgeo,width=15,textvariable=base,font=30)
    pic6.grid(row=5,column=1)

    #ฟังก์ชั่นเรขาคณิต
    def circle_area32():
        global data
        global message
        try:
            r = radius.get()
            data = (22/7)*r**2
            message.set(data)
        except:
            message.set("Missing Value")
        data = ""
    def circumference33():
        global data
        global message
        try:
            r = radius.get()
            data = 2*(22/7)*r
            message.set(data)
        except:
            message.set("Missing Value")
        data = ""
    def square_area34():
        global data
        global message
        try:
            w = width.get()
            l = long.get()
            data = w*l
            message.set(data)
        except:
            message.set("Missing Value")
        data = ""
    def triangle_area35():
        global data
        global message
        try:
            b = base.get()
            h = height.get()
            data = b*h*(1/2)
            message.set(data)
        except:
            message.set("Missing Value")
        data = ""
    def sphere_volume36():
        global data
        global message
        try:
            r = radius.get()
            data = (4/3)*(22/7)*(r**3)
            message.set(data)
        except:
            message.set("Missing Value")
        data = ""
    def sphere_surface37():
        global data
        global message
        try:
            r = radius.get()
            data = 4*(22/7)*(r**2)
            message.set(data)
        except:
            message.set("Missing Value")
        data = ""
    def cylinder_volume38():
        global data
        global message
        try:
            r = radius.get()
            h = height.get()
            data = (22/7)*(r**2)*h
            message.set(data)
        except:
            message.set("Missing Value")
        data = ""
    def conical_volume39():
        global data
        global message
        try:
            r = radius.get()
            h = height.get()
            data = (1/3)*(22/7)*(r**2)*h
            message.set(data)
        except:
            message.set("Missing Value")
        data = ""
    def pyramid_volume40():
        global data
        global message
        try:
            a = base.get()
            h = height.get()
            data = (1/3)*a*h
            message.set(data)
        except:
            message.set("Missing Value")
        data = ""
    def prism_volume41():
        global data
        global message
        try:
            a = base.get()
            h = height.get()
            data = a*h
            message.set(data)
        except:
            message.set("Missing Value")
        data = ""

    btn1 = Button(rootgeo,fg="white",bg="gray",font=('arial',15,'bold'),text="Circle area",width=15,height=1,border=5,command=circle_area32).grid(row=1,column=2)
    btn2 = Button(rootgeo,fg="white",bg="gray",font=('arial',15,'bold'),text="Circumference",width=15,height=1,border=5,command=circumference33).grid(row=1,column=3)
    btn3 = Button(rootgeo,fg="white",bg="gray",font=('arial',15,'bold'),text="Square area",width=15,height=1,border=5,command=square_area34).grid(row=2,column=2)
    btn4 = Button(rootgeo,fg="white",bg="gray",font=('arial',15,'bold'),text="Triangle area",width=15,height=1,border=5,command=triangle_area35).grid(row=2,column=3)
    btn5 = Button(rootgeo,fg="white",bg="gray",font=('arial',15,'bold'),text="Sphere volume",width=15,height=1,border=5,command=sphere_volume36).grid(row=3,column=2)
    btn6 = Button(rootgeo,fg="white",bg="gray",font=('arial',15,'bold'),text="Sphere surface",width=15,height=1,border=5,command=sphere_surface37).grid(row=3,column=3)
    btn7 = Button(rootgeo,fg="white",bg="gray",font=('arial',15,'bold'),text="Cylinder volume",width=15,height=1,border=5,command=cylinder_volume38).grid(row=4,column=2)
    btn8 = Button(rootgeo,fg="white",bg="gray",font=('arial',15,'bold'),text="Conical volume",width=15,height=1,border=5,command=conical_volume39).grid(row=4,column=3)
    btn9 = Button(rootgeo,fg="white",bg="gray",font=('arial',15,'bold'),text="Pyramid volume",width=15,height=1,border=5,command=pyramid_volume40).grid(row=5,column=2)
    btn10 = Button(rootgeo,fg="white",bg="gray",font=('arial',15,'bold'),text="Prism volume",width=15,height=1,border=5,command=prism_volume41).grid(row=5,column=3)

#กล่องหน้าจอแสดงผล
Input = Entry(font=('arial',30,'bold'),fg="black",bg="orange",width=30,textvariable=message,justify="right")
Input.grid(columnspan=8)

#เปลี่ยนปุ่ม
def mode1():
    btn01=Button(fg="orange",bg="gray",font=('arial',30,'bold'),text="🔁",width=3,height=1,border=5,command=mode2).grid(row=1,column=0)
    btn02=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="\u03c0",width=4,height=1,border=5,command=Pi03).grid(row=1,column=1)
    btn03=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="(",width=4,height=1,border=5,command=lambda:btn("(")).grid(row=1,column=2)
    btn04=Button(fg="white",bg="gray",font=('arial',30,'bold'),text=")",width=4,height=1,border=5,command=lambda:btn(")")).grid(row=1,column=3)
    btn05=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="Rad",width=3,height=1,border=5,command=rad21).grid(row=2,column=0)
    btn06=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="x!",width=4,height=1,border=5,command=facx27).grid(row=2,column=1)
    btn07=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="x\u00b2",width=4,height=1,border=5,command=x2_23).grid(row=2,column=2)
    btn08=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="\u00b2\u221Ax",width=4,height=1,border=5,command=root2_24).grid(row=2,column=3)
    btn09=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="Deg",width=3,height=1,border=5,command=deg22).grid(row=3,column=0)
    btn10=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="sin",width=4,height=1,border=5,command=sin09).grid(row=3,column=1)
    btn11=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="cos",width=4,height=1,border=5,command=cos10).grid(row=3,column=2)
    btn12=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="tan",width=4,height=1,border=5,command=tan11).grid(row=3,column=3)
    btn13=Button(fg="orange",bg="gray",font=('arial',30,'bold'),text="💠",width=3,height=1,border=5,command=geometrix).grid(row=4,column=0)
    btn14=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="sinh",width=4,height=1,border=5,command=sinh12).grid(row=4,column=1)
    btn15=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="cosh",width=4,height=1,border=5,command=cosh13).grid(row=4,column=2)
    btn16=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="tanh",width=4,height=1,border=5,command=tanh14).grid(row=4,column=3)
    btn17=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="1/x",width=3,height=1,border=5,command=Xdivide04).grid(row=5,column=0)
    btn18=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="log10",width=4,height=1,border=5,command=log05).grid(row=5,column=1)
    btn19=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="In",width=4,height=1,border=5,command=In06).grid(row=5,column=2)
    btn20=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="e",width=4,height=1,border=5,command=e07).grid(row=5,column=3)

def mode2():
    btn01=Button(fg="orange",bg="gray",font=('arial',30,'bold'),text="🔁",width=3,height=1,border=5,command=mode1).grid(row=1,column=0)
    btn02=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="\u03c0",width=4,height=1,border=5,command=Pi03).grid(row=1,column=1)
    btn03=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="(",width=4,height=1,border=5,command=lambda:btn("(")).grid(row=1,column=2)
    btn04=Button(fg="white",bg="gray",font=('arial',30,'bold'),text=")",width=4,height=1,border=5,command=lambda:btn(")")).grid(row=1,column=3)
    btn05=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="Rad",width=3,height=1,border=5,command=rad21).grid(row=2,column=0)
    btn06=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="Γ(x)",width=4,height=1,border=5,command=gemmax28).grid(row=2,column=1)
    btn07=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="x\u00b3",width=4,height=1,border=5,command=x3_25).grid(row=2,column=2)
    btn08=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="\u00b3\u221Ax",width=4,height=1,border=5,command=root3_26).grid(row=2,column=3)
    btn09=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="Deg",width=3,height=1,border=5,command=deg22).grid(row=3,column=0)
    btn10=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="sin\u207B\u00B9",width=4,height=1,border=5,command=arcsin15).grid(row=3,column=1)
    btn11=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="cos\u207B\u00B9",width=4,height=1,border=5,command=arccos16).grid(row=3,column=2)
    btn12=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="tan\u207B\u00B9",width=4,height=1,border=5,command=arctan17).grid(row=3,column=3)
    btn13=Button(fg="orange",bg="gray",font=('arial',30,'bold'),text="💠",width=3,height=1,border=5,command=geometrix).grid(row=4,column=0)
    btn14=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="sinh\u207B",width=4,height=1,border=5,command=arcsinh18).grid(row=4,column=1)
    btn15=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="cosh\u207B",width=4,height=1,border=5,command=arccosh19).grid(row=4,column=2)
    btn16=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="tanh\u207B",width=4,height=1,border=5,command=arctanh20).grid(row=4,column=3)
    btn17=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="Ran",width=3,height=1,border=5,command=rand29).grid(row=5,column=0)
    btn18=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="log2",width=4,height=1,border=5,command=log30).grid(row=5,column=1)
    btn19=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="2\u03c0",width=4,height=1,border=5,command=Pi2_31).grid(row=5,column=2)
    btn20=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="e\u02E3",width=4,height=1,border=5,command=Ex08).grid(row=5,column=3)

#button
#แถว1
btn01=Button(fg="orange",bg="gray",font=('arial',30,'bold'),text="🔁",width=3,height=1,border=5,command=mode2).grid(row=1,column=0)
btn02=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="\u03c0",width=4,height=1,border=5,command=Pi03).grid(row=1,column=1)
btn03=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="(",width=4,height=1,border=5,command=lambda:btn("(")).grid(row=1,column=2)
btn04=Button(fg="white",bg="gray",font=('arial',30,'bold'),text=")",width=4,height=1,border=5,command=lambda:btn(")")).grid(row=1,column=3)
btnC=Button(fg="orange",font=('arial',30,'bold'),text="C",width=3,height=1,border=5,command=clear).grid(row=1,column=4)
btnDel=Button(fg="black",font=('arial',30,'bold'),text="Del",width=3,height=1,border=5,command=Delete).grid(row=1,column=5)
btnpercent=Button(fg="black",font=('arial',30,'bold'),text="%",width=3,height=1,border=5,command=percent01).grid(row=1,column=6)
btndivision=Button(fg="orange",font=('arial',30,'bold'),text="÷",width=3,height=1,border=5,command=lambda:btn("/")).grid(row=1,column=7)
#แถว2
btn05=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="Rad",width=3,height=1,border=5,command=rad21).grid(row=2,column=0)
btn06=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="x!",width=4,height=1,border=5,command=facx27).grid(row=2,column=1)
btn07=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="x\u00b2",width=4,height=1,border=5,command=x2_23).grid(row=2,column=2)
btn08=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="\u00b2\u221Ax",width=4,height=1,border=5,command=root2_24).grid(row=2,column=3)
btn7=Button(fg="black",font=('arial',30,'bold'),text="7",width=3,height=1,border=5,command=lambda:btn(7)).grid(row=2,column=4)
btn8=Button(fg="black",font=('arial',30,'bold'),text="8",width=3,height=1,border=5,command=lambda:btn(8)).grid(row=2,column=5)
btn9=Button(fg="black",font=('arial',30,'bold'),text="9",width=3,height=1,border=5,command=lambda:btn(9)).grid(row=2,column=6)
btnmultiply=Button(fg="orange",font=('arial',30,'bold'),text="x",width=3,height=1,border=5,command=lambda:btn("*")).grid(row=2,column=7)
#แถว3
btn09=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="Deg",width=3,height=1,border=5,command=deg22).grid(row=3,column=0)
btn10=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="sin",width=4,height=1,border=5,command=sin09).grid(row=3,column=1)
btn11=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="cos",width=4,height=1,border=5,command=cos10).grid(row=3,column=2)
btn12=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="tan",width=4,height=1,border=5,command=tan11).grid(row=3,column=3)
btn4=Button(fg="black",font=('arial',30,'bold'),text="4",width=3,height=1,border=5,command=lambda:btn(4)).grid(row=3,column=4)
btn5=Button(fg="black",font=('arial',30,'bold'),text="5",width=3,height=1,border=5,command=lambda:btn(5)).grid(row=3,column=5)
btn6=Button(fg="black",font=('arial',30,'bold'),text="6",width=3,height=1,border=5,command=lambda:btn(6)).grid(row=3,column=6)
btnminus=Button(fg="orange",font=('arial',30,'bold'),text="-",width=3,height=1,border=5,command=lambda:btn("-")).grid(row=3,column=7)
#แถว4
btn13=Button(fg="orange",bg="gray",font=('arial',30,'bold'),text="💠",width=3,height=1,border=5,command=geometrix).grid(row=4,column=0)
btn14=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="sinh",width=4,height=1,border=5,command=sinh12).grid(row=4,column=1)
btn15=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="cosh",width=4,height=1,border=5,command=cosh13).grid(row=4,column=2)
btn16=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="tanh",width=4,height=1,border=5,command=tanh14).grid(row=4,column=3)
btn1=Button(fg="black",font=('arial',30,'bold'),text="1",width=3,height=1,border=5,command=lambda:btn(1)).grid(row=4,column=4)
btn2=Button(fg="black",font=('arial',30,'bold'),text="2",width=3,height=1,border=5,command=lambda:btn(2)).grid(row=4,column=5)
btn3=Button(fg="black",font=('arial',30,'bold'),text="3",width=3,height=1,border=5,command=lambda:btn(3)).grid(row=4,column=6)
btnplus=Button(fg="orange",font=('arial',30,'bold'),text="+",width=3,height=1,border=5,command=lambda:btn("+")).grid(row=4,column=7)
#แถว5
btn17=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="1/x",width=3,height=1,border=5,command=Xdivide04).grid(row=5,column=0)
btn18=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="log10",width=4,height=1,border=5,command=log05).grid(row=5,column=1)
btn19=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="In",width=4,height=1,border=5,command=In06).grid(row=5,column=2)
btn20=Button(fg="white",bg="gray",font=('arial',30,'bold'),text="e",width=4,height=1,border=5,command=e07).grid(row=5,column=3)
btn21=Button(fg="black",font=('arial',30,'bold'),text="|x|",width=3,height=1,border=5,command=Abusolub02).grid(row=5,column=4)
btn0=Button(fg="black",font=('arial',30,'bold'),text="0",width=3,height=1,border=5,command=lambda:btn(0)).grid(row=5,column=5)
btndot=Button(fg="black",font=('arial',30,'bold'),text=".",width=3,height=1,border=5,command=lambda:btn(".")).grid(row=5,column=6)
btnequal=Button(fg="black",bg="orange",font=('arial',30,'bold'),text="=",width=3,height=1,border=5,command=result).grid(row=5,column=7)

root.mainloop()