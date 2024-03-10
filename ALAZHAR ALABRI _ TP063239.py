#Alazhar_Alabri
#TP063239


# Requirements of the program
# Users of the program: Admin, register user, login user
# Admin:
# 1. Can login to access system.
# 2. Can upload Medicine detail in system. (Medicine name, exp date, price, 
# specification, etc...)
# 3. Can view all uploaded Medicines.
# 4. Can update/modify Medicine information if required.
# 5. Can delete Medicine information.
# 6. Can search specific Medicine detail.
# 7. Can view all orders of customers.
# 8. Can search order of specific customer.
# 9. Exit
# 
# New Customer:
# 1. Can view Medicine detail.
# 2. Can do registration by providing their detail like Name, Address, Email ID, Contact 
# Number, Gender, Date_Of_Birth, User ID, Password, Rewrite Password, etc…
# 3. Exit
# 
# Registered Customer:
# 1. Can login to the system.
# 2. View all Medicines detail.
# 3. Place order of medicines and do payment.
# 4. Can view own order.
# 5. Can view personal information.
# 6. Exit



#This is the main menu of the program
def mainpage():
    print("\t\n----------------(Welcome to our OPMS System)----------------")
    print("\t-------------- Enter choice number -------------- ")
    choose = input("\n----------------------\n1.To Login as Admin\n----------------------\n2.To Login as user\n----------------------\n3.To register a new user\n----------------------\n")
    print("----------------------")
    if choose == "1":
        login_admin()
    elif choose == "2":
        login_user()
    elif choose == "3":
        register_user()
    else:
        print("\t-------------- Enter choice number -------------- ")
        mainpage()
#This is page to login admin.
def login_admin():
 User_admin = str(input("Enter username:"))
 Password_admin = str(input("Enter password:"))
 case1 = False 
 file = open("admin account.txt","r")

 for line in file.readlines():
  line = line.split(",")
  user_admin = line[0]
  password_admin = line[1]
  if User_admin == user_admin and Password_admin == password_admin:
    case1 = True

 if case1 == True:
  print("You login sucssefuly ")  
  choice_admin()
 else:
  print("Username or password is incorrect")  
  mainpage()
 file.close() 
#This page to login user.
def login_user():
 global USername
 USername = (input("Enter username:"))
 Password_user = (input("Enter password:"))
 print("----------------------")

 case2 = False 
 file = open("users account.txt","r")
 count = 0
 for line in file.readlines():
  line = line.split(",")
  count +=1
  username = line[0]
  password_user = line[6]
  if USername == username and Password_user == password_user:
    case2 = True

 if case2 == True:
  print("You login sucssefuly ")  
  choices_user()
 else:
  print("username or password is incorrect")  
  mainpage()
 file.close()
#This page to regist in system as user.
def register_user():
 global USername   
 print("\t----------------- Welcome to regeister page --------------------")   
 print("\t----------------- Create your account to be able to wiew and order mediecnes----------------\n")
 print("1.regiest")
 print("2.Exit")
 choose = (input("choice number:"))
 if choose == "2":
    mainpage()
 elif choose == "1":
  USername = input("Enter your name: ")
  Address = input("Enter your address: ")
  email = input("Enter your email: ")
  contact_num = input("Enter contact number: ")
  Gender = input("Gender: M or F  ")
  Date_of_birth = input("Enter date of birth: ")
  password = input("Enter password: ")
  confirm_password = input("Confirm password: ")
  file = open("users account.txt" , "a")
  data = f"{USername},{Address},{email},{contact_num},{Gender},{Date_of_birth},{password},{confirm_password}, \n"
  file.write(data)
  file.close()
  print("\t-----------------------------------------------")
  print("\t----------(Registered successfully)------------")
  print("\t-----------------------------------------------")
  choices_user()

 else:
    print("\t-------------- Enter choice number -------------- ")
    mainpage()   
#This is page for choicses that available for users
def choices_user():
 print("\n----------------------\n1.View medicine:\n----------------------\n2.Search for medicine\n----------------------\n3.Order medicine\n----------------------\n4.View your orders\n----------------------\n5.View your personal profile\n----------------------\n6.Exit\n----------------------\n ")
 choose = input("Enter choice number :   ")
 if choose == "1": 
    medicine_view()
 elif choose == "2":
  search_medicine()
 elif choose == "3":
    order_page()
 elif choose == "4":
    view_order_user()
 elif choose == "5":
    profile_page()
 elif choose == "6":
     mainpage()  
 else:
    print("\t-------------- Enter choice number -------------- ")
    choices_user()
#This page to see menue of medicines that availabe in pharmacy.
def medicine_view():
   file = open("medcines.txt", "r")
   count = 0
   for line in file.readlines():   
      line = line.split(",")
      count+=1
      medicine_name = line[1]
      medicine_price = line[5]
      medicine_exp = line[2]
      medicine_number = line[3]
      medicine_details = line[4]
      print(f"1.medicine name: ", medicine_name, "\n------------\n2.Price: ", medicine_price,"RM" "\n------------\n3.Expire date: ", medicine_exp, "\n------------\n4.Number available of this medicine: ", medicine_number, "\n------------\n5.Details: ", medicine_details,"\n---------------------------------------\n")
   file.close()
   mainpage()
#This page to search for specific medicine.
def search_medicine():
    print("\t--------------(Search for medicine)----------------")
    search_med = input("Medicne name: ")
    file = open("medcines.txt", "r")
    count = 0
    for line in file.readlines():   
     line = line.split(",")
     count+=1
     medicine_name = line[1]
     medicine_price = line[5]
     medicine_exp = line[2]
     medicine_number = line[3]
     medicine_details = line[4]
     if search_med == medicine_name:
       print(f"\n1.medicine name: ", medicine_name, "\n------------\nPrice: ", medicine_price,"RM" "\n------------\nExpire date: ", medicine_exp, "\n------------\nNumber available of this medicine: ", medicine_number, "\n------------\nDetails: ", medicine_details,"\n---------------------------------------\n")
       mainpage()

     else:
        print("Medicine not found")

    mainpage()
    file.close()
#This page is to order medicine from Pharmacy.
def order_page():
    print("\t----------------(Order Page)----------------------")
    choose = str(input("Enter medicine name:  "))
    choose1 = int(input("quantity:  "))


    
    with open("medcines.txt", "r", encoding='utf-8') as file:
        newline = file.readlines()   


    file1 = open("medcines.txt", "r+")
    for line in file1.readlines():   
        line = line.split(",")
        id = line[0]
        medicine_name = line[1]
        medicine_price = line[5]
        medicine_exp = line[2]
        medicine_number = line[3]
        medicine_details = line[4]
        if choose == medicine_name:
           print("The medicine is available")
           (total) = int(choose1)*float(medicine_price)
          
           print("Total price: ",total,"RM")
           new_number = int(medicine_number) - int(choose1)
           print("----------(Payment Page)------------")
           card_number = input("Enter card number:")
           CVV = input("Enter CVV:")
           order = print("\t-----------(your order has been processed successfully)------------")
           newline[int(id)-1] = (f"{id},{medicine_name},{medicine_exp},{new_number},{medicine_details},{medicine_price}, \n")
           with open('medcines.txt', 'w', encoding='utf-8') as file:
                file.writelines(newline)
           file2 = open("orders list.txt", "a")
           make_oder = f"{USername},{medicine_name},{choose1},{total}, \n"
           file2 = file2.write(make_oder)
           file3 = open("payment details.txt", "a")
           data = f"{USername},{card_number},{CVV}, \n"
           file3 = file3.write(data) 
           print("................................\t\n..............Bill..................\n................................")
           print("Medicine name :" + str(choose))
           print("..................................................")
           print("Quantity :"+str(choose1))
           print("..................................................")
           print("Total price :"+str(total),"RM")
           print("..................................................")
           choices_user()
        else:
         print("Medicine is not available or not enough quantity")
    choices_user()
#By this page, user can see his order.          
def view_order_user():  
 file = open("orders list.txt", "r")
 for line in file.readlines():
    line = line.split(",")
    username = line[0]
    medecine_name = line[1]
    quanteity = line[2]
    total = line[3]
    if USername == username:   
       print(f"\n1.Email: ",username, "\n------------\n2.Medicine name: ",medecine_name, "\n------------\n3.Quantity: ", quanteity, "\n------------\n4.Total prcie: ", total,"RM","\n---------------------------------------\n")
   
    else:
        print("There is no order found")
 choices_user()   
#This page show profile page of user.     
def profile_page():
  print("\t--------------(view personal profile)----------------")
  file = open("users account.txt", "r")
  case1 = False
  count = 0
  for line in file.readlines():   
     line = line.split(",")
     count+=1
     username1 = line[0]
     Email = line[2]
     location = line[1]
     gender1 = line[4]
     phone_number = line[3]
     birhtday = line[5]
     if USername == username1:
       print(f"\n1.Username: ", username1, "\n------------\nEmail: ", Email, "\n------------\nAdress: ", location, "\n------------\nPhone number: ", phone_number, "\n------------\nGender: ", gender1,"\n------------\nBirthday: ", birhtday,"\n---------------------------------------\n")
       choices_user()
     else:
      print("User not found")
  choices_user()
#This page show options that are availabe for Admin.
def choice_admin():
     print("\t---------------(Admin Page)------------------")
     print("1.Add new medicine\n---------------\n2.Edit midecine details\n---------------\n3.Delet medicine\n---------------\n4.View medicines\n---------------\n5.Search medicien\n---------------\n6.View all orders\n---------------\n7.Search order\n---------------\n8.Payment Details\n---------------\n9.Exit\n---------------\n")
     choose = input("Enter choice number: ")
     if choose == "1":
        add_med()
     elif choose == "2":
        edit_med()
     elif choose == "3":
        delete_med()
     elif choose == "4":
        medicine_view()
     elif choose == "5":
        search_medicine()
     elif choose == "6":
        view_orders_Admin()
     elif choose == "7":
        search_order() 
     elif choose == "8":
         payment_detils()  
     elif choose == "9":
        mainpage()
     else:
        print("choose option number")
        choice_admin()               
#This page to add new medicines by admin.
def add_med(): 
  print("-----------------------------------")
  name = int(input("Enter number of medicine in the menue:  ")) 
  print("-----------------------------------") 
  medicine_name = input("Enter medicine name : ")
  print("-----------------------------------")
  exp_date = input("Enter expire date of medicine  : ")
  print("-----------------------------------")
  medicine_number = int(input("Enter number of the available medicine: "))
  print("-----------------------------------")
  details = input("Enter details about medicine: ")
  print("-----------------------------------")
  price = float(input("Enter medicine price "))
  print("-----------------------------------")
  file = open("medcines.txt" , "a")
  info = f"{name},{medicine_name},{exp_date},{medicine_number},{details},{price}, \n"
  file.write(info)
  file.close()
  print("------------(The medicine is added successfully)--------------")
  choice_admin()
#This page to change details medicines that are availabe in pharmacy.
def edit_med():
    print("\t--------------(Edit Medicines Detials)----------------")
    name = input("Enter medicine name    :") 
    with open("medcines.txt", "r", encoding='utf-8') as file:
        newline = file.readlines()  
    file1 = open("medcines.txt","r+")
    count = 0
    for line in file1.readlines():   
     line = line.split(",")
     count+=1
     id = line[0]
     medicine_name = line[1]
     if medicine_name == name:
         print("-----------------------------------")
         print("The medicine is found")
         print("-----------------------------------")
         name1 = input("Enter new medicine name:  ")
         print("-----------------------------------")
         name2 = input("Enter expire date of this medicine: ")
         print("-----------------------------------")
         name3 = int(input("Enter quantity of this medicine:  "))
         print("-----------------------------------")
         name4 = input("Enter details about this medicine:  ")
         print("-----------------------------------")
         name5 = float(input("Enter price this medicine:  "))
         print("-----------------------------------")
         newline[int(id)-1] = (f"{id},{name1},{name2},{name3},{name4},{name5}, \n")
         with open('medcines.txt', 'w', encoding='utf-8') as file:
          file.writelines(newline)
         print("\n-----------------------------------\nEditing details this medicine has been done\n-----------------------------------")  
         choice_admin()             
     else:
        print("\n-----------------------------------\nMedicine is not found\n-----------------------------------")
    choice_admin()
    file1.close() 
 #This page to delet mediciens from pharmacy menue.     
def delete_med():
     print("\t--------------(Delete Medicine Page)----------------")
     name = input("Enter medicine name   :") 
     with open("medcines.txt", "r", encoding='utf-8') as file:
        newline = file.readlines()   
     file1 = open("medcines.txt","r+")
     count = 0
     for line in file1.readlines():   
      line = line.split(",")
      count+=1
      id = line[0]
      medicine_name = line[1]
      if medicine_name == name:
         print(medicine_name)
         newline[int(id)-1] = (f"")
         with open('medcines.txt', 'w', encoding='utf-8') as file:
             file.writelines(newline)
         print("\n-----------------------------------\nThis medicine has been deleted successfully\n-----------------------------------")  
         choice_admin() 
      else:          
        print("medicine is not found")
     choice_admin()   
     file1.close() 
 #This page to see all orders from users by admin.       
def view_orders_Admin():
    file = open("orders list.txt", "r")
    count = 0
    for line in file.readlines():   
     line = line.split(",")
     count+=1
     Email = line[0]
     medicine_name = line[1]
     medicine_number = line[2]
     total_price = line[3]
     print(f"\n------------\n1.Username :  ", Email, "\n------------\n2.Medicine name : ", medicine_name, "\n------------\n3.Quantity : ", medicine_number, "\n------------\n4.Total price : ", total_price,"RM","\n------------\n")

    choice_admin()
    file.close()     
#This page to find speccfic user's order.
def search_order():
    search_order = input("Username of user: ")
    file = open("orders list.txt", "r")
    count = 0
    for line in file.readlines():   
     line = line.split(",")
     count+=1
     username1 = line[0]
     medicine_name = line[1]
     medicine_number = line[2]
     total_price = line[3]
     if search_order == username1:
        print(f"\n------------\n1.Username:  ", username1, "\n------------\n2.Medicine name: ", medicine_name, "\n------------\n3.Number of this medicine: ", medicine_number, "\n------------\n4.Total price: ", total_price,"RM","\n------------\n")
     else:
        print("Order is not found")
    choice_admin()   
    file.close()
#This is page show for admin all data of payment details.
def payment_detils():
   print("\t--------------(Payment Details Page)----------------")
   file = open("payment details.txt", "r")
   for line in file.readlines():   
    line = line.split(",")
    username1 = line[0]
    Card_number = line[1]
    CVV = line[2]
    print(f"\n------------\n1.Username:  ", username1, "\n------------\n2.Card Number: ", Card_number, "\n------------\n3.CVV: ", CVV, "\n------------\n")
  
   choice_admin()
   file.close()
   
mainpage()