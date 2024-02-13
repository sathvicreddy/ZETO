print ("-----------------------------")
print ("zeto")
print("------------------------------")
import random
import mysql.connector as c
con=c.connect(host="localhost",user="root",password= "593427",database="zeto",auth_plugin="mysql_native_password")
cur=con.cursor()
#cur.execute("create database zeto")
#cur.execute("create table user(name char(45),user_name varchar(30),password varchar(20),phone int(12),address varchar(100))"
#cur.execute("create table orders(hotel_user varchar(20),Name varchar(20),cost int(12),order_code int(12))"
#con.commit()
global number
number=random.randint(1000,9999)
global hotel_user
def history():
    print("order history")
    x="select * from {}".format(user_name)
    cur.execute(x)
    c=cur.fetchall()
    print(c)
    
    
def profile():
    x="select * from user where user_name='{}'".format(user_name)
    cur.execute(x)
    b=cur.fetchall()
    print("name     : ",b[0][0])
    print("user name: ",b[0][1])
    print("password : ",b[0][2])
    print("phone    : ",b[0][3])
    print("address  : ",b[0][4])
    
def login():
    global user_name
    user_name=input("user name")
    b=input("enter password")
    q="select user_name,password from user where user_name='{}'".format(user_name)
    cur.execute(q)
    d=cur.fetchall()
    if user_name in d[0] and b in d[0]:
        print("successfully loggined")
    else:
        print("wront user name or password")
        login()
def signin():
    x=input("enter your name: ")
    a=input("user name      : ")
    b=input("password       : ")
    c=int(input("phone number   : "))
    d=input("address        : ")
    q="select user_name from user"
    cur.execute(q)
    s=cur.fetchall()
    if a in s[0]:
        print("user aldready exist on:",a)
    else:
        y="insert into user values('{}','{}','{}',{},'{}')".format(x,a,b,c,d)
        cur.execute(y)
        con.commit()
        z="create table {}(hotel_name varchar(20),item_name char(25),cost int(10),order_code int(10),status varchar(20) default 'pending')".format(a)
        cur.execute(z)
        con.commit()
    
def hotels():
    b="select * from hotels"
    cur.execute(b)
    c=cur.fetchall()
    for i in c:
        print(i)
def order():
    f="update orders set order_code={}".format(number)
    cur.execute(f)
    con.commit()
    print("your orders are")
    b="select * from orders"
    cur.execute(b)
    c=cur.fetchall()
    print(c)
    e="select sum(cost) from orders"
    cur.execute(e)
    d=cur.fetchall()
    print("total payment",d)
    y="insert into {}(hotel_name,item_name,cost,order_code) select hotel_user,Name,cost,order_code from orders".format(user_name)
    cur.execute(y)
    con.commit()
    x="delete from orders"
    cur.execute(x)
    con.commit()
    
    
def menu():
    hotel_user=input("entr hotel name use _ in place of space")
    b="select * from {}".format(hotel_user)
    cur.execute(b)
    c=cur.fetchall()
    print(c)
    a=int(input("enter the item code"))
    y="insert into orders(hotel_user,Name,cost) select hotel_name,ITEM_NAME,COST from {} where ITEM_CODE={}".format(hotel_user,a)
    cur.execute(y)
    con.commit()
    z="select name,address from user where user_name='{}'".format(user_name)
    cur.execute(z)
    s=cur.fetchall()
    d=s[0][0]
    q=s[0][1]
    v="select ITEM_NAME,COST,ITEM_CODE from {} where ITEM_CODE={}".format(hotel_user,a)
    cur.execute(v)
    f=cur.fetchall()
    h=f[0][0]
    i=f[0][1]
    j=f[0][2]
    o="pending"
    x="insert into {}_order values('{}','{}','{}','{}',{},{},{},'{}')".format(hotel_user,user_name,d,q,h,i,j,number,o)
    cur.execute(x)
    con.commit()
    print("item added to orders")
    print("-"*30)



while True :
    print ("1.......login")
    print("2........sign in ")
    print("3.........exit")
    a=int(input("selected value"))
    if a==1:
        login()
        while True:
            print("1.......order")
            print("2.......history")
            print("3.......profile")
            print("4.......login page")
            z=int(input("enter the selected number"))
            if z==1:
                hotels() 
                menu()
                while True:
                    print("1 hotels")
                    print("2 order other items")
                    print("3 payment")
                    print("4 login")
                    print("5 exit")
                    c=int(input("enter the choise"))
                    if c==1:
                        break
                    elif c==2:
                        menu()
                    elif c==3:
                        order()
                    elif c==4:
                        login()
                    elif c==5:
                        break
                    else:
                        print("invalid code")
            elif z==2:
                history()
            elif z==3:
                profile()
            elif z==4:
                login()
            else:
                print("invalid code")
    elif a==2:
        signin()
    elif a==3:
        break
    else:
        print("invalid code")
    
    
    
