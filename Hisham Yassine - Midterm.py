def Sort_by_ID(sub_list):
  new_list= sorted(sub_list, key = lambda x: x[0])
  return new_list
  #Source [after customization to suite the problem]: https://www.geeksforgeeks.org/python-sort-list-according-second-element-sublist/

def Sort_by_Date(sub_list):
  new_list= sorted(sub_list, key = lambda x: x[2], reverse=True)
  return new_list

emp_unsorted=[]
sorted_id=[]
sorted_date=[]


def load_data():
  with open('Employee Database.txt') as f:
    database = f.readlines()
  f.close()
  #Source [after customization to suite the problem]:https://www.pythontutorial.net/python-basics/python-read-text-file/
  
  for i in database:
    datalines= i.splitlines()
    emp_data=datalines[0].split(',')
    emp_unsorted.append(emp_data)
    
  return emp_unsorted

  
def booting():
  start=input("Hello! Do you want to access the Employees Database System? [Yes/No]  ")
  if start == "Yes":
    welcome()


def display():
  male_count=0
  female_count=0

  for i in emp_unsorted:
    if i[3]=="male":
      male_count+=1
    elif i[3]=="female":
      female_count+=1
  
  print("We have ",male_count," males and ",female_count," females in the company")
  print("You will be re-directed to the main menu again")
  admin()
  pass

def add():
  from datetime import date
  today = date.today()
  joining_date=str(today).replace("-","")
  #Source [after customization to suite the problem]: https://www.geeksforgeeks.org/get-current-date-using-python/


  last_emp_id=sorted_id[-1][0]
  last_id=int(last_emp_id[-3:])
  new_id=str(last_id+1)
  length=len(new_id)

  if length==1:
    new_emp_id="emp00"+new_id
  elif length==2:
    new_emp_id=="emp0"+new_id
  elif length==3:
    new_emp_id=="emp"+new_id

  

  new_user=input("Please enter the username of the new employee ")
  new_sex=input("Please specify his/her sex  ")
  new_salary=input("What is his/her salary?  ")

  new_employee=[new_emp_id,new_user,joining_date,new_sex,new_salary]

  emp_unsorted.append(new_employee)
  print("\n\nThe new Employee has been added successfuly!")
  print("\nYou will be re-directed to the main menu again")
  admin()
  pass
  


def all():
  print("Here is the list of all employees (from newest to oldest in company):\n")
  for i in sorted_date:
    print("Employee ID: ",i[0]," Employee username: ",i[1]," Date of Joining [YYYYMMDD]: ",i[2]," Employee Sex: ",i[3]," Employee's Salary: ",i[4])
  
  print("\nYou will be re-directed to the main menu again")
  admin()
  pass

def change():
  emp=input("\nPlease enter the ID of the employee that you want to change his/her salary:  ")
  user_found=False
  for i in emp_unsorted:
    if emp==i[0]:
      new_sal=input("Please enter the new salary:  ")
      i[4]=new_sal
      user_found=True
      print("\nSalary changed successfuly!")
      break
  
  if user_found==False:
    print("No Employee has this ID\n")

  print("\nYou will be re-directed to the main menu again")
  admin()
  pass

def remove():
  print("Let's remove some employees from the database")
  emp_id=input("Please enter the ID of the employee you want to remove:  ")

  user_found==False

  for i in emp_unsorted:
    if emp_id==i[0]:
      emp_unsorted.remove(i)
      user_found=True
      print("Employee Removed Successfully!")

  if user_found==False:
    print("No Employee has this ID\n")
  
  print("\nYou will be re-directed to the main menu again")
  admin()

  pass

def raising():
  print("Yes! It's time to have some raises")
  emp_id=input("Please enter the ID of the employee you want to raise their salary:  ")
  

  user_found=False

  for i in emp_unsorted:
    if emp_id==i[0]:
      percentage=input("What is the percentage of the raise?  ")    
      user_found=True
      original_salary=int(i[4])
      new_salary=original_salary*percentage
      i[4]=str(new_salary)
      print("The Salary is raised Successfully!")

  if user_found==False:
    print("No Employee has this ID\n")
  
  print("\nYou will be re-directed to the main menu again")
  admin()

  pass

def exit():
  with open('Employee Database.txt', 'w') as file:
    for item in emp_unsorted:
            file.write(",".join(map(str,item)))
            file.write("\n")
#Source [after customization to suite the problem]:https://www.jquery-az.com/3-ways-convert-python-list-string-join-map-str/
  pass

  

def admin():
  admin_option = int(input("\n\nPlease choose the required operation:\n1. Display Statistics\n2. Add an Employee\n3. Display all Employees\n4. Change Employee's Salary\n5. Remove Employee\n6. Raise Employee's Salary\n7. Exit\n\n"))
  
  if admin_option ==1:
    display()
  elif admin_option==2:
    add()
  elif admin_option==3:
    all()
  elif admin_option==4:
    change()
  elif admin_option==5:
    remove()
  elif admin_option==6:
    raising()
  elif admin_option==7:
    exit()
  else:
    print("Invalid Entry\n")
    admin()

def user_access(employee):
  user_option = int(input("\n\nPlease choose the required operation:\n1. Check My Salary\n2. Exit\n\n"))

  if user_option==1:
    for i in emp_unsorted:
      if i[1]==employee:
        print("Your Salary is: ", i[4])
        print("Have a Good Day :) \n\n") 
  else:
    booting()


def welcome():
  
  print("Welcome to the Employees Database System!\n\nPlease login to continue")
  user=input("Enter Your Username:  ")
  if user=="admin":
    password= input("Enter Your Password:  ")
    if password=="admin123123":
      admin()
    else:
      print("Your username/password is incorrect\nPlease enter a valid authentication")

  else:     
      user_found=False
      for i in emp_unsorted:  
          if i[1]==user:
             user_found=True
             user_access(user)
             break
      if user_found==False:
        print("This username is not available. Please enter a valid username")
        
    
 
       




while 1:
  emp_unsorted=load_data()
  sorted_id=Sort_by_ID(emp_unsorted)
  sorted_date=Sort_by_Date(emp_unsorted)
  booting()
    

  
