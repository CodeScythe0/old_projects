
import patientnew
import doctor
import opd
import os



def menu():

 print("+=================================================================================+")
 print("|                            HOSPITAL MANAGEMENT SYSTEM                           |")
 print("+-------------------++-----------------++-----------++----------------++----------+")
 print("|       DOCTOR      ||      PATIENT    ||    OPD    ||    BILL PRINT  ||   EXIT   |")
 print("+-------------------++-----------------++-----------++----------------++----------+")


def mainmenu():
    while True:
        os.system("cls")
        menu()
        print("\n"*5)

        ch=input("\t\t\t\tChoice[D/P/O/B/X]::")
        if ch=="D" or ch=="d":
            os.system("cls")
            menu()
            doctor.getchoice()
        elif ch=="P" or ch=="p":
            os.system("cls")
            menu()
            patient.getchoice()
        elif ch=="O" or ch=="o":
            os.system("cls")
            #print("OPD")
            opd.newOpd()
        elif ch=="B" or ch=="b":
            os.system("cls")
            #print("OPD")
            opd.printBill()
        elif ch=="X" or ch=="x":
            print("THANKS")
            print("EXISTING...")
            break
        else:
            print("Invalid Choice")


mainmenu()            

###########################DOCTOR.PY######################### 


import pandas as pd
import os

##############################################
#                   DOCOR MENU               #
##############################################



def dmenu():
    #os.system("cls")
     print("+=======================+")
     print("|     DOCTOR SUB.MENU   |")
     print("+=======================+")
     print("|1.Register New Doctor  |")
     print("|2.Update Doctor        |")
     print("|3.Remove Doctor        |")
     print("|4.Search Doctor        |")            
     print("|5.All Doctor List      |")
     print("|6.Back to Main Menu    |")
     print("+=======================+")
     print()



#############################################
#       NEW DOCTOR REGISTRATION             #
#############################################

def drRegister():
    drdf=pd.read_csv("csvfile\\doctor.csv",index_col=0)
    rno=len(drdf)
    print(rno)
    while True:
        did=int(input("Doctor ID:"))
        if serDoctorbyID(did)>0:
            print("Duplicate Doctor Id,ENTER A VALID DR ID")
        else:
            break
    name=input(("DOCTOR NAQME"))
    dept=input("Department: ")
    drdf.to_csv("csvfile\\doctor,csv",mode="w")



################################################
#            UPDATE DOCTOR                     #
################################################
def drupdate():
    drdf=pd.read_csv("csvfile\\doctor.csv",index_col=0)
    did=int(input("entre Doctor ID to update:"))


    if serDoctorById(did)>0:
        print("Doctor Found")
        #print(drdf.loc[drdf["drdf']==did].index)
        name=input("Enter Update Doctor Name: ")
        dept=input("Department:")
        drdf.loc[drdf.loc[drdf['drdf']==did].index:]=[did,name,dept]
        drdf.to_csv("csvfile\\doctor.csv",mode="w")
        print("Update Succsfully")
        
    else:
        print("Invalid Doctor ID:")

####################################################
#                 REMOVE DOCTOR                    #
####################################################


def drRemove():
    drdf=pd.read_csv("csvfile\\doctor.csv",index_col=0)
    did=int(input("Enter Doctor Id to Delete:  "))
    drdf.drop(drdf.loc[drdf["drdf"]==did].index,inplace=True)
    #print(drdf)
    drdf.to_csv ("csvfile\\docotr.csv",mode="w")




###########################################
#         DISPLAY ALL DOCTOR              #
###########################################
def dispDoctor():
    drdf=pd.read_csv("csvfile\\doctor.csv",index_col=o)
    print(drdf)



#######################################################
#               SEARCH DOCTOR  BY ID                  #
#######################################################

def serDoctorById(did):
    drdf=pd.read_csv("csvfile\\doctor".csv,index_col=0)
    return len(drdf.loc[drdf["drdf"]==did])
    


##################################################
#             SEARCH  DOCTOR BY NAME              #
##################################################
def serDoctorbyName():
    global drdf
    drdf=pd.read_csv("csvfile\\doctor.csv",index_col=0)
    dname=input("Doctor Name:: ")
    print(drdf.loc[drdf['drname']==dname])


###############################################
#              GET DOCTOR DF BY ID            #
###############################################


def getDoctor(did):
    drdf=pd.read_csv("csvfile\\doctor.csv",index_col=0)
    if drdf.empty:
        return "Invalid Dr.ID"
    else:
        return drdf.loc[drdf['drdf']==did]
    
##################################################
#              GET CHOICE                        #
##################################################


def getchoice():
    #while True:
    dmenu()
    ch=input("\t\t\t\t Your Choice ::")
    if ch=="1":
        print("DOCTOR REGISTRATION")
    
        drRegister()
    elif ch=='2':
                   drUpdate()
    elif ch=='3':
                 drRemoval()
    elif ch=='4':
                 print("SEARCH DOCTOR")
                 serDoctorbyName()
    elif ch=='5':
                 print("List Of Doctor")
                 dispDoctor()
    elif ch=='6':
                 pass
                #break

    else:
                 print('Invalid Choice')
input("Press any key to continue.....")





import pandas as pd
import os

################################################
#        PATIENT MANAGEMENT MENU               #
################################################

def pmenu():
    #os.system("cls")
    print("\t\t\t +--------------------------+")
    print("\t\t\t |     PATIENT MAIN MENU    |")
    print("\t\t\t +--------------------------+")
    print("\t\t\t |1. New Patiet Registration|")
    print("\t\t\t |2. Update Patient Details |")
    print("\t\t\t |3. Remove Patient         |")
    print("\t\t\t |4. Search Patient by PNo  |")
    print("\t\t\t |5. All Patient List       |")
    print("\t\t\t |6. EXIT                   |")
    print("\t\t\t +--------------------------+")
    print()


################################################
#          NEW PATIENT REGISTRATION            #
################################################
def patRegister():
    patdf = pd.read_csv("csvfile\\patientnew.csv", index_col = 0)
    rno = len(patdf)
    #print(rno)
    while True:
        print("Please Enter Patient Details")
        pid = int(input("Patient Id : "))
        if serPatientbyId(pid)> 0 :
            print("Duplicate Patient Id, ENTER A VALID PATIENT ID")        
        else:
            break
    
    name = input("Name : ")
    age = input("Age : ")
    weight = input("Weight : ")
    gender = input("Gender : ")
    address = input("Address : ")
    phoneno = input("Phone Number : ")
    disease = input("Disease : ")
    patdf.loc[pid,:] = [pid,name,age,weight,gender,address,phoneno,disease]
    #print(patdf)
    patdf.to_csv("csvfile\\patientnew.csv", mode='w')

################################################
#              UPDATE PATIE                   #
################################################

def patUpdate():
    patdf = pd.read_csv("csvfile\\patientnew.csv", index_col = 0)
    pid = int(input("Enter Patient Id to Update: "))

    if serPatientbyId(pid)> 0 :
        print("Patient Found")
        print("Enter details to update patient")
        name = input("Name : ")
        age = input("Age : ")
        weight = input("Weight : ")
        gender = input("Gender : ")
        address = input("Address : ")
        phoneno = input("Phone Number : ")
        disease = input("Disease : ")
        patdf.loc[patdf.loc[patdf['pid'] == pid].index,:] = [pid,name,age,weight,gender,address,phoneno,disease]
        
        patdf.to_csv("csvfile\\patientnew.csv", mode='w')
        print("Updated Successfully")
    else:
        print("Invaid Patient ID")

################################################
#                    REMOVE PATIENT            #
################################################
          
def patRemove():
    patdf = pd.read_csv("csvfile\\patientnew.csv", index_col = 0)
    pid = int(input("Enter Patient Id to Delete: "))
    patdf.drop(patdf.loc[patdf['pid']==pid].index, inplace=True) #Remove
    
    patdf.to_csv("csvfile\\patientnew.csv", mode='w')    
    
################################################
#              DISPLAY ALL PATIENT             #
################################################

def dispPatient():
    patdf = pd.read_csv("csvfile\\patientnew.csv", index_col= 0)
    print(patdf)

################################################
#              SEARCH PATIENT BY ID            #
################################################

def serPatientbyId(pid):
    patdf = pd.read_csv("csvfile\\patientnew.csv", index_col = 0)
    if patdf.empty:
        return 0
    else:
        return len(patdf.loc[patdf['pid'] == pid])

################################################
#           GET PATIENT  DF BY ID              #
################################################
def getPatient(pid):
    patdf = pd.read_csv("csvfile\\patientnew.csv", index_col = 0)
    if patdf.empty:
        return "Invalid ID"
    else:
        return patdf.loc[patdf['pid'] == pid]

################################################
#           GET PATIENT  NAME BY ID            #
################################################

def getPatientName(pid):
    patdf = pd.read_csv("csvfile\\patientnew.csv", index_col = 0)
    if patdf.empty:
        return "Invalid ID"
    else:
        return patdf.iat[0,1]


################################################
#              SEARCH PATIENT BY NAME          #
################################################
def serPatientbyName():
    global patdf
    patdf = pd.read_csv("csvfile\\patientnew.csv", index_col = 0)
    pname  = input("Patient Name :: ")
    print(patdf.loc[patdf['name'] == pname])

def serPatientbyIDPrint():
    global patdf
    patdf = pd.read_csv("csvfile\\patientnew.csv", index_col = 0)
    tid  = int(input("Patient ID :: "))
    print(patdf.loc[patdf['pid'] == tid])

################################################
#              GET CHOICE                      #
################################################
def getchoice():
    while True:
        pmenu()
        ch = input("\t\t\t Enter Your Choice :: ")
        if ch == '1':
            print("PATIENT REGISTRATION")
            patRegister()
        elif ch=='2':
            print("PATIENT UPDATION")
            patUpdate()
        elif ch=='3':
            print("PATIENT DELETION")
            patRemove()
        elif ch=='4':
            print("PATIENT SEARCHING")
            print("1. By ID")
            print("2. By Name")
            ch = input("Enter your search criteria :: ")
            if ch == '1':
                serPatientbyIDPrint()
                print()
                print()
            elif ch == '2':
                serPatientbyName()
                print()
                print()
        elif ch=='5':
            print("\t\tLIST OF PATIENTS")
            print("----------------------------------------")
            dispPatient()
        elif ch == '6':
            break
        else:
            print("INVALID CHOICE")

        input("Press ENTER KEY to continue.....")

#main

getchoice()

from datetime import date
import patient
import doctor
import pandas as pd
import sys

def newOpd():
    try:
        opddate=date.today().strftime("%d-%m-%Y")
        opddf=pd.read_csv("csvfile\\opd.csv",index_col=0)
        rno=len(opddf)
        opdno=rno+1
        print("+=================++=================++===============++==================+")
        print("|                    HOSPITAL MANAGEMENT SYSTEM(OPD)                      |")
        print("+=================++=================++===============++==================+")
        print("|Note: Press CTRL+C to terminate                                          |")
        print("+=========================================================================+")
        print("|OPD NUMBER  ::",opdno,end="                                              |")
        print("|\t\t\t\t\t\tDATE ::",opddate,"                                           |")
        print("+=========================================================================+")
        #print("Opd Number::",opdno,end=")

        while True:
            pid=int(input("\n\t\tPatient Id     ::"))
            if patient.serPatientbyId(pid)>0:
                break
            else:
                print("Error:NOT A VALID PATIENT ID")
        while True:
            drid=int(input("\n\t\tDoctor Id     ::"))
            if doctor.serDoctorbyId(drid)>0:
                break
            else:
                print("Error::NOT A VALID DOCTOR ID")

        disease=input("\n\t\tDisease             ::")

        drfee=float(input("\n\t\tDoctor Fee   (Rs)::"))
        medchrg=float(input("\n\t\tMedicine Charge   (Rs)::"))
        labchrg=float(input("\n\t\tLaboratory Charge (Rs)::"))
        otherchrg=float(input("\n\t\tOther Charge    (Rs)::"))

        totamt=drfee+medchrg+labchrg+otherchrg

        print("\n\n\t\t\tPlease pay Rs.",totamt,"to bill counter...")
        
        opddf.loc[rno,:]=[opdno,opddate,pid,drid,disease,drfee,medchrg,labchrg,otherchrg,totamt]

        opddf.to_csv("csvfile\\opd.csv",mode='w')

    except EOFError:
        print("Oops! EOF exception,please enter something and run me again")
        return
    except KeyboardInterrupt:
        print("Oops!You have pressed ctrl-c button.")
        return
    except Exception as e:
        print("Oops!",e.__class__,"occurred.")
        print()
        return
    else:
        print("Error::")
        return
def searchOpd(ono):
    tempdf=pd.read_csv("csvfile\\opd.csv",indeex_col=0)
    if tempdf.empty:
        return False
    else:
        return len(tempdf.loc[tempdf['opdno']==ono])
def printBill():
    try:
        prndate=date.today().strftime("%d-%m-%Y")
        print(prndate)
        opddf=pd_read_csv("csvfile\\opd.csv",index_col=0)
        opdno=int(input("Enter opdno to print(press'ctrl+c'to exit::"))
        if searchOpd(opdno)==False:
            print("Invalid OPD NO")
            return
        else:
            df=opddf.loc[opddf['opdno']==opdno]
            print("+=============++===============++===============++==================+")
            print("|                    HOSPITAL MANAGEMENT SYSTEM                     |")
            print("+=============++===============++===============++==================+")
            print("|                     ---BILL RECEIPT---                            |")
            print("|OPD NUMBER   ::",df.iat[0,0],end="                                 |")
            print("\t\t\t\t\t\tOPD DATE    ::",df.iat[0,1],"                           |")
            print("+===================================================================+")
            #pid name age weight gender address phoneno disease
            print("Patient ID       ::",df.iat[0,2],"\t|",end='')
            temp_patdf=patient.getPatient(df.iat[0,2])
                                          #temp patient df
            print("Patient Name     ::",temp_patdf.iat[0,1])
            print("Patient Age      ::",temp_patdf.iat[0,2],"\t|",end='')
            print("Patient Weight    ::",temp_patdf.iat[0,3])
            print("Patient Gender     ::",temp_patdf.iat[0,4],"\t|",end='')
            print("Patient Address    ::",temp_patdf.iat[0,5])
            print("Patient Phone Number    ::",temp_patdf.iat[0,6],"\t|",end='')
            print("Disease(as told by patient)::",temp_patdf.iat[0,7])
            print("|===================================================================|")                                          
            print("Doctor ID       ::",df.iat[0,3],"\t|",end='')
            temp_doctdf=doctor.getDoctor(df.iat[0,3])
            
            print("Doctor Name     ::",temp_doctdf.iat[0,1])
            print("Doctor Dept     ::",temp_doctdf.iat[0,2])
            print("|===================================================================|")
            print("Disease(as by Doctor) ::",df.iat[0,4])
            print("|===================================================================|")
            print("Charges=====>")
            print("\t\tDoctor Consulation Fee :: Rs.",df.iat[0,5])
            print("\t\tMedicine Charges :: Rs.",df.iat[0,6])
            print("\t\tLab Charges :: Rs.",df.iat[0,7])
            print("\t\tOther Charges :: Rs.",df.iat[0,8])
            print("\t\t============================================")
            print("\t\tTotal Amount :: Rs.",df.iat[0,9])
            totamt=df.iat[0,9]
            cgst=totamt*0.18
            sgst=totamt*0.18
            amtpay=totamt+cgst+sgst
            print("TAX====>")
            print("\t\tCGST@18%              :: Rs.".cgst)
            print("\t\tSGST@18%              :: Rs.".sgst)
            print("\t==============================================")
            print("\t\tAmount to pay         :: Rs.".round(amtpay,2))
            print("+===================================================================+")
            print("|Cashier:                               Checked By:                 |")                             
            print("+===================================================================+")
            print("|              ----THANKS FOR VISIT|GET WELL SOON----               |")
            print("+===================================================================+")
    except EOFError:
        print("Oops!EOF exception, please enter something and run me again")
        return
    except KeyboardInterrupt:
        print("Oops!You have pressed ctrl-c button.")
        return
