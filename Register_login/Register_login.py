import array

usr=[]
pas=[]
spin =array.array("i",[])

while 1:
    ch=int(input("1.Register\n2.Login\n3.Password Change\n4.Recover Password\n5.Remove Account\n6.Exit\nEnter Your Choice :"))
    if ch==1:
        print("Register")
        usr.append(input("Enter Username :"))
        pas.append(input("Enter Password :"))
        spin.append(int(input("Enter Pin No :")))
        print("Registered")
    elif ch==2:
        stat=0
        uid=input("Username : ")
        pwd=input("Password : ")
        for x in range(len(usr)):
            if uid==usr[x] and pwd==pas[x]:
                stat=1
                print("Login Success")
                break
        if stat==0:
            print("Login Failed")
    elif ch==3:
        stat = 0
        uid = input("Username : ")
        pwd = input("Enter Old Password : ")
        for x in range(len(usr)):
            if uid == usr[x] and pwd == pas[x]:
                stat = 1
                while 1:
                    npas=input("Enter New Password   : ")
                    cpas=input("Confirm New Password : ")
                    if npas==cpas:
                        pas[x]=npas
                        print("Password Changed")
                        break
                    else:
                        print("Details Doesn't Match")
        if stat == 0:
            print("Invalid Credentials")

    elif ch==4:
        stat = 0
        uid = input("Username     : ")
        pin = int(input("Security Pin : "))
        for x in range(len(usr)):
            if uid == usr[x] and pin == spin[x]:
                stat = 1
                print(f"Password is {pas[x]}")
                break
        if stat == 0:
            print("Invalid Credentials")
    elif ch==5:
        stat = 0
        uid = input("Username : ")
        pwd = input("Password : ")
        for x in range(len(usr)):
            if uid == usr[x] and pwd == pas[x]:
                stat = 1
                usr.pop(x)
                pas.pop(x)
                spin.pop(x)
                print("Account Removed")
                break
        if stat == 0:
            print("Invalid Credentials")

    elif ch==6:
        exit(0)
    else:
        print("Wrong Choice...")

















