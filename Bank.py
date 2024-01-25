import mysql.connector
import datetime
con=mysql.connector.connect(host='localhost',user='root',password='',database='Bank')
cur=con.cursor()

print('Press 1 for Login into an Account')
print('Press 2 for Creating an account')
print('Press 3 for Document Verification')
print('Press 4 for Nomniees')
print('Press 5 for knowing the status of your loan')
print('Press 6 for Credit')
print('Press 7 for Deposite')
print('Press 8 for Transfer')
print('Press 9 for Balance Enquiry')
print('Press 10 for Password Change')
print('Press 11 for Account Summary')

n=int(input("What you want to do? "))
date=datetime.date.today()
print("***********************<////////////////////>***********************")

if n==1:
    print('WELCOME!! Enter your Email address and Password:')

elif n==2:
     A=input("Enter your New Password:")
     N=input("Enter your Full Name:")
     D=input("Enter your Address:")
     G=input("Enter your Gender:")
     M=input("Enter your Mobile:")
     E=input("Enter your Email:")
     C=input("Enter your Country:")
     S=input("Enter your State:")
     T=input("Enter your City:")
     P=input("Enter your Zipcode:")
     Z=int(input("Enter your Balance:"))

     AC="SBI"
     x=0
     W="select * from Account_Opening"
     cur.execute(W)
     for row in cur:
          x=x+1
     if x>0:
        x=x+1
        x=x+100
        AC=AC+str(x)
     else:
        AC="SBI101"
     s="insert into Account_Opening values('"+AC+"','"+A+"','"+N+"','"+D+"','"+G+"',"+str(M)+",'"+E+"','"+C+"','"+S+"','"+T+"',"+str(P)+","+str(Z)+")"
     cur.execute(s)
     con.commit()
     print("Sucessfull"," Thank you!")
     con.close()

elif n==3:
    a=input('Enter your High School Roll:')
    n=input('Enter your High School Marks:')
    d=input('Enter your High School Percent:')
    g=input('Enter your Secondary School Roll:')
    m=input('Enter your Secondarys School Marks:')
    e=input('Enter your Secondarys School Percent:')
    c=input('Enter your Aadhar Number:')
    s=input('Enter your Pan Number:')
    t=input('Enter your Father Aadhar Number:')
    z='select * from Document_Verification'
    x=0
    cur.execute(z)
    for row in cur:
        x=x+1
    s="insert into Document_Verification values('"+str(a)+"','"+n+"','"+d+"','"+g+"',"+str(m)+",'"+e+"','"+c+"','"+s+"','"+t+"')" 
    cur.execute(s)
    con.commit()
    print("Sucessfull"," Thank you!")
    con.close()

elif n==4:
    q=input("Enter Name:")
    w=input("Enter Age:")
    e=input("Enter Account Number:")
    t=input("Enter IFSC Code:")
    y=input("Enter Branch:")
    u=input("Enter Area:")
    i=input("Relation:")
    Q="select * from Nominee_Details"
    x=0
    cur.execute(Q)
    for row in cur:
        x=x+1
    l="insert into Nominee_Details(Name,Age,Account Number,IFSC Code,Branch,Area,Relation) values('"+q+"','"+w+"','"+e+"','"+t+"','"+y+"','"+u+"','"+i+"')"
    cur.execute(l)
    con.commit()
    print("Sucessfull"," Thank you!")
    con.close()

elif n==5:
    print("Your lone is approved, Please move forward to your amount:")

elif n==6:
     a=input("Enter Account Number:")
     p=input("Enter Pin:")
     s="select * from Account_Opening where account='"+a+"' and password='"+p+"'"
     camt=0
     x=0
     cur.execute(s)
     for d in cur:
          x=x+1
          camt=int(d[10])
     if x>0:
          wamt=int(input("Enter amount to Withdraw:"))
          if wamt<=camt:
               camt=camt-wamt
               s="update Account_Opening set balance="+str(camt)+" where account='"+a+"'"
               cur.execute(s)
               con.commit()
               s="insert into Account_Summary (Account,Transaction,Date,Action,Balance) values('"+a+"','"+str(wamt)+"','"+str(date)+"','Withdraw','"+str(camt)+"')"
               cur.execute(s)
               con.commit()
               print("After Withdraw ",wamt," your current balance is =",camt)
          else:
               print("Sorry!! You have enterd wrong value")
     else:
               print("Sorry!! You have incorrect ACCOUNT OR PIN")

elif n==7:
     a=input("Enter Account Number:")
     p=input("Enter Pin:")
     s="select * from Account_Opening where account='"+a+"' and password='"+p+"'"
     creadit=0
     x=0
     cur.execute(s)
     for d in cur:
          x=x+1
          credit=int(d[10])
     if x>0:
          damt=int(input("Enter amount to Deposite:"))
          if damt<60000:
               credit=credit+damt
               s="update Account_Opening set balance="+str(credit)+" where account='"+a+"'"
               cur.execute(s)
               con.commit()
               s="insert into Account_Summary (Account,Transaction,Date,Action,Balance) values('"+a+"','"+str(damt)+"','"+str(date)+"','Deposite','"+str(credit)+"')"
               cur.execute(s)
               con.commit()
               print("After Deposite ",damt," your current balance is =",credit)
          else:
               print("Sorry!! You have enterd wrong details")
     else:
               print("Sorry!! You have entered incorrect details")

elif n==8:
     a=input("Enter Account Number:")
     p=input("Enter Pin:")
     s="select * from Account_Opening where account='"+a+"' and password='"+p+"'"
     camt=0
     x=0
     cur.execute(s)
     for d in cur:
          x=x+1
          camt=int(d[10])
     if x>0:
          fund=int(input("Enter amount to transfer:"))
          if fund<=camt and fund>0:
               camt=camt-fund
               
          else:
               print("Sorry!! You have entered incorect details")
     else:
                print("Sorry!! You have incorrect ACCOUNT OR PIN")

     ac1=input("Enter Account Number where you transfer:")
     b="select * from Account_Opening where account='"+ac1+"'"
     cur.execute(b)
     camt1=0
     x1=0
     for row in cur:
          x1=x1+1
          camt1=int(row[10])
     if x1>0 and x>0:
          camt1=camt1+fund
          d="update Account_Opening set balance='"+str(camt1)+"'where account='"+ac1+"'"
          cur.execute(d)
          con.commit()
          w="update Account_Opening set balance='"+str(camt1)+"'where account='"+ac1+"'"
          cur.execute(w)
          con.commit()
          s="insert into Account_Summary (Account,Transaction,Date,Action,Balance) values ('"+a+"','"+str(fund)+"','"+str(date)+"','transfer','"+str(camt)+"')"
          cur.execute(s)
          con.commit() 
          print("Your amount is transfered")
     else:
          print("OOPS!! Insufficent Balance")

elif n==9:
     a=input("Enter Account Number:")
     p=input("Enter Pin:")
     s="select * from Account_Opening where account='"+a+"' and password='"+p+"'"
     camt=0
     x=0
     cur.execute(s)
     for d in cur:
          x=x+1
          camt=int(d[10])
     if x>0:
         print("Your Deposit balance is:=",camt)
              
     else:
          print("OOPS!! You have entered large amount")

elif n==10:
     a=input("Enter Account Number:")
     p=input("Enter Pin:")
     s="select * from Account_Opening where account='"+a+"' and password='"+p+"'"
     camt=0
     x=0
     cur.execute(s)
     for d in cur:
          x=x+1
     if x>0:
          v=input("Enter New Password:")
          s="update Account_Opening set password='"+v+"'where password='"+p+"'"
          cur.execute(s)
          con.commit()
          print("Password updated successfully")
     else:
          print("Enter wrong password")

elif n==11:
     a=input("Enter Account Number:")
     p=input("Enter Pin:")
     s="select * from Account_Opening where account='"+a+"' and password='"+p+"'"
     camt=0
     x=0
     cur.execute(s)
     for d in cur:
          x=x+1
     if x>0:
          s="select * from Account_Summary where account='"+a+"'"
          cur.execute(s)
          print("Account\t","Transaction\t","Date\t","Action\t","Balance")
          for d in cur:
               print(d[0],"\t",d[1],"\t",d[2],"\t",d[3],"\t",d[4],)
          
     else:
          print("OOPS!! You have entered wrong ACCOUNT or PASSWORD")
     
          




