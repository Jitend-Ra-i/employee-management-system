# import pywhatkit
# pywhatkit.sendwhatmsg('+919399751354','opencode',19,14)

from dns.rdataclass import NONE
import mysql.connector
from mysql.connector import cursor
con = mysql.connector.connect(
    host="localhost", user="jittu1", password="<Jittu>12",database="employee")
c=con.cursor()

# c.execute("CREATE TABLE IF NOT EXISTS employee_details (ID int NOT NULL AUTO_INCREMENT,Name varchar(255) NOT NULL,Age int NOT NULL,Post varchar(255) NOT NULL,Salary BIGINT NOT NULL,PRIMARY KEY (ID));")
# c.execute("ALTER r=c.fetchall("select * from employee_details;")
# for i in r:
#     print(i)TABLE employee_details AUTO_INCREMENT=1001;")
# c.execute("INSERT INTO employee_details(Name,Age,Post,Salary) VALUES('Jitendra',22,'Manager',150000);")
# c.execute("INSERT INTO employee_details(Name,Age,Post,Salary) VALUES('Ajay',21,'Chief_executive',170000);")
# con.commit()
# r=c.fetchall("select * from employee_details;")
# for i in r:
#     print(i)

# c.execute('select * from employee_details;')
# for i in c:
#     print(i)



def add_employee(Name,Age,Post,Salary):
    cmd=f"INSERT INTO employee_details(Name,Age,Post,Salary)VALUES('{Name}',{Age},'{Post}',{Salary});"
    c=con.cursor()
    c.execute(cmd)
    con.commit()
    print('employee added successfully******************')
    main()

def check_employee(ID):
    cmd=f"select * from employee_details where ID={ID}"
    c=con.cursor(buffered=True)
    c.execute(cmd)
    r=c.rowcount
    if r==1:
        return True
    return False

def remove_employee(ID):
    if check_employee(ID)==True:
        cmd=f"delete from employee_details where ID={ID}"
        c=con.cursor()
        c.execute(cmd)
        con.commit()
        print("Employee removed successfully***********")
    else:
        print("Employee does not exist, please enter valid ID")
    main()

def display_employee(ID):
    if ID==0:
        cmd="select * from employee_details"
        c=con.cursor()
        c.execute(cmd)
        for i in c:
            print(i)
    else:
        if check_employee(ID)==True:
            cmd=f"select * from employee_details where ID={ID}"
            c=con.cursor()
            c.execute(cmd)
            for i in c:
                print(i)
        else:
            print("Employee does not exist, please enter valid ID")
    main()

def main():
    print("Welcome to Employee Management Record")
    print("press")
    print("1 to add employee")
    print("2 to delete employee")
    print("3 to display details")
    n=int(input("Enter your choice"))
    if n==1:
        Name=input("Enter Employee Name")
        Age=input("Enter Employee Age")
        Post=input("Enter Employee Post")
        Salary=input("Enter Employee Salary")
        add_employee(Name,Age,Post,Salary)
    elif n==2:
        ID=int(input("Enter Employee ID"))
        remove_employee(ID)
    elif n==3:
        print("press 0 to display all details or Enter Employee ID")
        ID=int(input("Enter your choice"))
        display_employee(ID)
    else:
        print("Invalid choice")
        main()

main()




        

