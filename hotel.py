print ("-----------------------------")
print ("zeto")
print("------------------------------")
import mysql.connector as c
con=c.connect(host="localhost",user="root",password= "593427",database="zeto",auth_plugin="mysql_native_password")
cur=con.cursor()
#cur.execute("create database zeto")
#cur.execute("create table hotel_user(hotel_name char(45),hotel_user varchar(30),password varchar(20),phone int(12),address varchar(100))"
#cur.execute("create table hotels(hotel_name varchar(30),hotel_user varchar(20),hotel_id int(10))
#con.commit()
def login():
    global hotel_user
    hotel_user=input("user name")
    b=input("enter password")
    q="select hotel_user,password from hotel_user where hotel_user='{}'".format(hotel_user)
    cur.execute(q)
    d=cur.fetchall()
    if hotel_user in d[0] and b in d[0]:
        print("successfully loggined")
    else:
        print("wrong user name or password")
        login()
def signin():
    x=input("enter hotel name: ")
    a=input("user name      : ")
    b=input("password       : ")
    c=int(input("phone number   : "))
    d=input("address        : ")
    g=int(input("enter hotel code"))
    q="select hotel_user from hotel_user"
    cur.execute(q)
    s=cur.fetchall()
    if a not in s[0] or len(s)==0:
        f="insert into hotels values('{}','{}',{})".format(x,a,g)
        cur.execute(f)
        con.commit()
        y="insert into hotel_user values('{}','{}','{}',{},'{}')".format(x,a,b,c,d)
        cur.execute(y)
        con.commit()
        z="create table {}(hotel_name varchar(20),ITEM_NAME varchar(25),COST int(10),ITEM_CODE int(5))".format(a)
        cur.execute(z)
        con.commit()
        k="create table {}_order(user_name varchar(20),NAME char(40),ADDRESS varchar(50),ITEM_NAME varchar(25),COST int(10),ITEM_CODE int(5),ordre_code int(10),status varchar(20))".format(a)
        cur.execute(k)
        con.commit()
    else :
        print("user aldready exist on:",a)
def orders():
    b="select * from {}_order".format(hotel_user)
    cur.execute(b)
    c=cur.fetchall()
    print(c)
    z=input("enter user name")
    x=int(input("enter order code"))
    print("confirm------------1")
    print("cooking------------2")
    print("out of delevary----3")
    print("cancle-------------4")
    a=int(input("enter choise : "))
    if a==1:
        c="update {} set status='confirm' where order_code={}".format(z,x)
        cur.execute(c)
        con.commit()
    elif a==2:
        s="update {} set status='cooking' where order_code={}".format(z,x)
        cur.execute(s)
        con.commit()
    elif a==3:
        u="update {} set status='out of delevary' where order_code={}".format(z,x)
        cur.execute(u)
        con.commit()
    elif a==4:
        i="update {} set status='cancel' where order_code={}".format(z,x)
        cur.execute(i)
        con.commit()
    else:
        print("wrong input")
def menu():
    z="select * from {}".format(hotel_user)
    cur.execute(z)
    x=cur.fetchall()
    print(x)
    d=input("hotel name")
    a=input("enter item name")
    b=int(input("enter cost"))
    c=int(input("enter  item code"))
    q="insert into {} values('{}','{}',{},{})".format(hotel_user,d,a,b,c)
    cur.execute(q)
    con.commit()


while True:
    print("1------ hotel login")
    print("2-------hotel regestration")
    print("3-------exit")
    a=int(input("enter the choice"))
    if a==1:
        login()
        while True:
            print("1-----orderd")
            print("2-----menue add")
            print("3-----menue deleat")
            x=int(input("enter "))
            if  x==1:
                orders()
            elif x==2:
                menu()
            elif x==3:
                menu_del()
    elif a==2:
        signin()
    elif a==3:
        break
        
