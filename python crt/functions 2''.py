guest_list=[]
print("Welcome to party project")
while(True):
    print("***************Menu****************")
    print("1.enter 1 to add a guest")
    print("2.enter 2 to remove a guest who cancels")
    print("3.enter 3 to check if a friend is on the list or not")
    print("4.enter 4 to sort and print the final guest list")
    print("5.enter 5 to exit")
    choice=int(input("enter your choice:"))
    if(choice>=1 and choice<=5):
        if(choice==1):
            name=input("enter the guest name:")
            guest_list.append(name)
            print(f"{name} is added to the guest list")
        elif(choice==2):
            cancelled_name=input("enter the name of guest who cancelled:")
            if cancelled_name in guest_list:
                guest_list.remove(cancelled_name)
                print("f{cancelled_name} is removed from the guest list..!")
            else:
                print(f"{cancelled_name} is not present in guest list..!")
        elif(choice==3):
            check_guest=input("enter the guest name:")
            if check_guest in guest_lists:
                print(f"{check_guest} is attending the party..!")
            else:
                print(f"{check_guest}is not attending the party..!")
        elif(choice==4):
            guest_list.sort()
            print("Here's the finalised list of guestd who are attending the party..!")
            print(guest_list)
    else:
        print("enjoy the party..!")



