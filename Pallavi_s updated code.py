import mysql.connector
import datetime
from tabulate import tabulate
import matplotlib.pyplot as plt

db = input("Enter name of your database:")
mydb=mysql.connector.connect(host='localhost', user='root', passwd='2611@vishal')
mycursor= mydb.cursor()

sql ="CREATE DATABASE if not exists %s" % (db,)
mycursor.execute(sql)
print("Database created Successfully..")
mycursor=mydb.cursor()
mycursor.execute("Use "+db)
TableName=input("Name of Table to be created:")
query="Create table if not exists "+TableName+"\
(empno int primary key,\
name varchar (15) not null,\
job varchar(15),\
BasicSalary int, \
DA float, \
HRA float,\
GrossSalary float, \
Tax float, \
NetSalary float)"
print("Table "+TableName+" created successfully....")
mycursor.execute(query)

while True:
    print("\n\n\n")
    print("*"*95)
    print('\t\t\t\t\tMAIN MENU')
    print("*"*95)
    print("\t\t\t\t1. Adding Employee records")
    print("\t\t\t\t2. For Displaying Record of All the Employees")
    print("\t\t\t\t3. For displaying Record of a particular Employee")
    print("\t\t\t\t4. For deleting Records of all the Employees")
    print("\t\t\t\t5. For Deleting a Record of a particular employee")
    print("\t\t\t\tó. For Modification in a record")
    print("\t\t\t\t7. For displaying payroll")
    print("\t\t\t\t8. For displaying Salary Slip for all the Employees")
    print("\t\t\t\t9. For displaying Salary Slip for a particular Employee")
    print('\t\t\t\t10.For generating graph salary and job (A-simple / B-bar graph)')
    print('\t\t\t\t11.For Exit')
    print("Enter Choice...", end=' ')
    choice=input()
    if choice=='1':
        try:
            print("Enter employee information.....")
            mempno=int (input('Enter employee no:'))
            mname=input("Enter employee name: ")
            mjob=input('Enter employee job:')
            mbasic=float(input('Enter basic salary:'))
            if mjob.upper()=='OFFICER':
                mda=mbasic*0.5
                mhra=mbasic*0.35
                mtax=mbasic*0.2
            elif mjob.upper()=='MANAGER':
                mda=mbasic+0.45
                mhra=mbasic*0.38
                mtax=mbasic*0.15
            else:
                mda=mbasic*0.48
                mhra=mbasic*0.25
                mtax=mbasic*0.1
            mgross=mbasic+mda+mhra
            mnet=mgross-mtax
            rec=(mempno, mname, mjob, mbasic,mda, mhra, mgross,mtax,mnet)
            query="insert into "+TableName+" values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            mycursor.execute(query, rec)

            mydb.commit()
            print('Record added successfully....')
        except Exception as e:
            print('Something went wrong',e)
    elif choice=='2':
        try:
            query='select * from '+TableName
            mycursor.execute(query)
            #print(query)
            print(tabulate(mycursor, headers=["EmpNo","Name","Job","Basic Salary","DA","HRA","Gross Salary","Tax","Net Salary"],tablefmt="fancy_grid"))
            '''myrecords=mycursor.fetchall()
            for rec in myrecords:
                print(rec)'''

        except Exception as e:
            print("Something went wrong",e)

    elif choice=='3':
        try:
            en=input("Enter employee no. of the record to be displayed...")
            query="select * from "+TableName+" where empno="+en
            mycursor.execute(query)
            myrecord=mycursor.fetchone()
            print("\n\nRecord of Employee No.:"+en)
            print(myrecord)
            c=mycursor.rowcount
            if c==-1:
                print('Nothing to display')
        except:
            print("Something went wrong")
    elif choice=='4':
        try:
            ch=input('Do you want to delete all the records (y/n)')
            if ch.upper()=='Y':
                mycursor.execute('delete from '+TableName)
                mydb.commit()
                print('All the records are deleted...')
        except:
            print("Something went wrong")
    elif choice=='5':
        try:
            en=input('Enter employee no. of the record to be deleted...')
            query='delete from '+TableName+' where empno='+en
            mycursor.execute(query)
            mydb.commit()
            c=mycursor.rowcount
            if c>0:
                print('Deletion done')
            else:
                print('Employee no',en, 'not found')
        except:
             print('Something went wrong')
    elif choice=='6':
        try:
            en=input('Enter employee no. of the record to be modified...')
            query='select * from '+TableName+' where empno='+en
            mycursor.execute(query)
            myrecord=mycursor.fetchone()
            c=mycursor.rowcount
            if c==-1:
                print('Empno '+en+' does not exist')
            else:
                mname=myrecord[1]
                mjob=myrecord[2]
                mbasic=myrecord[3]
                print('empno :',myrecord[0])
                print('name  :',myrecord[1])
                print('job   :',myrecord[2])
                print('basic :',myrecord[3])
                print('da    :',myrecord[4])
                print('hra   :',myrecord[5])
                print('gross :',myrecord[6])
                print('tax   :',myrecord[7])
                print('net   :',myrecord[8])
                print('--------------------')
                print('Type Value to modify below or just press Enter for no change')
                x=input('Enter name ')
                if len(x)>0:
                    mname=x
                x=input('Enter job ')
                if len(x)>0:
                    mjob = x
                x=input('Enter basic salary')
                if len(x)>0:
                    mbasic=float(x)
                query='update '+TableName+' set name='+"'"+(mname)+"'"+','+'job='+"'"+(mjob)+"'"+','+'basicsalary='+str(mbasic)+' where empno='+en
                print(query)
                mycursor.execute(query)
                mydb.commit() 
                print('Record modified')
        except Exception as e:
            print('Something went wrong',e)
    elif choice=='7':
        try:
            query='select * from '+TableName
            mycursor.execute(query)
            myrecords=mycursor.fetchall()
            print("\n\n\n")
            print (95*'*')
            print('Employee Payroll'.center (90))
            print (95*'*')
            now = datetime.datetime.now()
            print("Current Date and Time: ", end=' ')
            print (now.strftime("%Y-%m-%d %H:%M:%S"))
            print()
            print (95*'-')
            print ('%-5s %-15s %-10s %-8s %-8s %-8s %-9s %-8s %-9s'\
                   %('Empno', 'Name','job','Basic','DA', 'HRA','Gross', 'Tax','Net'))
            print (95*'-')
            for rec in myrecords:
                print('%4d %-15s %-10s %8.2f %8.2f %8.2f %9.2f %8.2f %9.2f' %rec)
                print (95*'-')
        except Exception as e:
            print('Something went wrong',e)
    elif choice=='8':
        try:
            query='select * from '+TableName
            mycursor.execute(query)
            now = datetime.datetime.now()
            print("\n\n\n")
            print("-"*95)
            print("\t\t\t\tSalary Slip")
            print("-"*95)
            print("Current Date and Time:",end=' ')
            print(now.strftime("%Y-%m-%d %H:%M:%S"))
            myrecords=mycursor.fetchall()
            for rec in myrecords:
                print('%4d %-15s %-10s %8.2f %8.2f %8.2f %9.2f %8.2f %9.2f'%rec)
        except Exception as e:
            print('Something went wrong',e)
    elif choice=='9':
        try:
            en=input("Enter employee number whose pay slip you want to retreive:")
            query='select * from '+TableName+' where empno='+en
            mycursor.execute(query)
            now = datetime.datetime.now()
            print("\n\n\n\t\t\t\tSALARY SLIP ")
            print("Current Date and Time:",end=' ')
            print (now.strftime ("%Y-%m-%d %H:%M:%S"))
            #print (query)
            print(tabulate (mycursor, headers=["EmpNo","Name","Job","Basic Salary","DA","HRA","Gross Salary","Tax","Net Salary"]))
        except Exception as e:
            print('Something went wrong',e)
    elif choice=='10a' or choice=='10A':
        query='select sum(BasicSalary),job from '+TableName+' group by job'
        mycursor.execute(query)
        result = mycursor.fetchall
        salary = []
        jobs = []
        for i in mycursor:
            salary.append(i[0])
            jobs.append(i[1])
        print("Jobs :", jobs)
        print("Salary:",salary)
        plt.plot(jobs,salary)
        plt.xlabel('Job')
        plt.ylabel('Salary')
        plt.title('Job v/s salary')
        plt.show()
        
    elif choice=='10b' or choice=='10B':
        query='select sum(BasicSalary),job from '+TableName+' group by job'
        mycursor.execute(query)
        result = mycursor.fetchall
        salary = []
        jobs = []
        for i in mycursor:
            salary.append(i[0])
            jobs.append(i[1])
        print("Jobs :", jobs)
        print("Salary:",salary)
        plt.bar(jobs,salary)
        plt.xlabel('Job')
        plt.ylabel('Salary')
        plt.title('Job v/s salary')
        plt.show()

    elif choice=='11':
        print('Exit the program...')

        break
    else:
        print('wrong  choice...')
