d = {}

while True :
    print("1. Add Records")
    print("2. Search Records")
    print("3. Update Records")
    print("4. Delete Records")
    print("5. Display Records")
    
    choice = int(input("Enter the choice : "))
    
    if choice == 1 :
        
        print("------------------------------------")
        records = int(input("How many records you want to enter : "))
        print("------------------------------------")
        
        for i in range(records) :
            print("------------------------------------")
            roll = int(input("Enter the Roll Number : "))
            d[roll] = {}
            name = input("Enter the Name : ")
            klass = input("Enter the Class : ")
            add   = input("Enter the Address : ")
            print("------------------------------------")
            d[roll]["Name"] = name
            d[roll]["Class"] = klass
            d[roll]["Address"] = add
    elif choice == 2 :
        s = int(input("Enter the Roll Number to be searched : "))
        for i in d :
            if i == s :
                print("------------------------------------")
                print("Roll    :  " , i)
                print("Name    :  " , d[i]["Name"])
                print("Class   :  " , d[i]["Class"])
                print("Address :  " , d[i]["Address"])
                print("------------------------------------")
    elif choice == 3 :
        s = int(input("Enter the Roll Number to be Updated : "))
        for i in d :
            if i == s :
                print("------------------------------------")
                print("Roll    :  " , i)
                print("Name    :  " , d[i]["Name"])
                print("Class   :  " , d[i]["Class"])
                print("Address :  " , d[i]["Address"])
                print("------------------------------------")
                print(" 1. Name \n 2. Class \n 3. Address")
                o = int(input("Enter the choice : "))
                
                if o == 1 :
                    Nname = input("Enter the New Name : ")
                    
                    d[i]["Name"] = Nname
                    print("Name Updated!")
                elif o == 2 :
                    Nklass = input("Enter the New Class : ")
                    
                    d[i]["Class"] = Nklass
                    print("Class Updated!")
                elif o == 3 :
                    Nadd = input("Enter the New Address : ")
                    d[i]["Address"] = Nadd
                    print("Address Updated!")
    elif choice == 4 :
        rno = int(input("Enter the Roll Number to be Deleted : "))
        del d[rno]
        print()
        print("Roll Number Deleted!")
        print()

    elif choice == 5 :
        t = int(input(" 1.All Records \n 2.Individual Records "))
        if t == 1 :
            for i in d :
                print("------------------------------------")
                print("Roll    :  " , i)
                print("Name    :  " , d[i]["Name"])
                print("Class   :  " , d[i]["Class"])
                print("Address :  " , d[i]["Address"])
                print("------------------------------------")
        elif t == 2 :
            s = int(input("Enter the Roll Number to be searched : "))
            for i in d :
             
             if i == s :
                    print("------------------------------------")
                    print("Roll    :  " , i)
                    print("Name    :  " , d[i]["Name"])
                    print("Class   :  " , d[i]["Class"])
                    print("Address :  " , d[i]["Address"])
                    print("------------------------------------")
    c = input("Do u want to cotinue the program : ")
    if c == 'y' :
        continue
    elif c == 'n' :
        break