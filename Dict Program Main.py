#---------------#
#Summative Unit 4 - Dictionaries Program
#keeping track of expenses program
#By Marb Pano
#April 14, 2023
#---------------#

import random
import time 


#----dictionaries---#

employee_salary = {
    }#name of employee and thier salary

operating_cost = {'Rent': 0,
                  'Accounting and Legal Fees': 0,
                  'Bank Charges': 0,
                  'Sales Fees': 0,
                  'Marketing Fees': 0,
                  'Officce Supplies': 0,
                  'Repairs': 0,
                  'Utilities': 0,
                  
                  
    }
#other expenses like banking fees,accouting fees, marketing, office supplies.etc

product_cost = {
    }#how much did it cost to buy the product(s)



#---list---#
inspirational_words = ['If your going through a rough patch, just know everything will be alright we all been there!',
                       'People love you and you know it.',
                       'You can do this!',
                       'You are important',
                       'NEVER GIVE UP!',
                       'Your Business is doing good',
                       'Sales up, share prices down, life is good',
                       'A Rescession is bad... but not for investors',
                       'Invest Wisely!',
                       'Invest in my Crypto Pump and Dump(totes not a scam)',
                       'If you were told to invest in a Crypto Pump and Dump, dont do it!',
                       
]#when working on your business it is important we have inspirational words to help you through the day
#------inspiration-------#
def random_inspirational_words():
    x = random.choice(inspirational_words)
    print(x)
    
#------Printing dicts and lists----#
def print_operating_cost():
    print("")
    
    for item, cost in list(operating_cost.items()):#for every item and cost in shopping_list print the {item} or key, {cost} or value. in dict
        print(f"{item}: ${cost}")
        
def print_employee_salary():
    print("")
    
    for item, cost in list(employee_salary.items()):
        print(f"{item}: ${cost}")
        
def print_product_cost():
     print("")
    
     for item, cost in list(product_cost.items()):
        print(f"{item}: ${cost}")

        
#------adding info-------#    
def adding_employee_salary():
    print(" ")
    
    while True:#the only problem with this is that if you have two employees with the same name, the more recent input employee
        #will overwrite the previous ones value
        try:
            for_question = int(input("How many Employees? "))
            
            for i in range(for_question):
                item = input("Emplyee Name: ")#the key in dictionary
                cost = float(input("Salary: "))#value in dictionary
                employee_salary[item] = cost#this is the only way I figured out how to add things to dictionary
            
            print("")   
            print("Contains")
            print_employee_salary()
            break
        
        except:
            print("ONLY USE NUMBERS(CONTINUE WHERE YOU LEFT OFF)") 
    
    
def adding_operating_cost():
    print("")
    
    while True:
        
        try:
            for item, cost in list(operating_cost.items()):
                
                x = float(input(f"Overall cost of {item} "))
                operating_cost[item] = x#i just wanted the value to change and not the set key
            
            print("")
            print("Contains")
            print_operating_cost()
            break# this is to exit out of the loop
            
        except:
            print("ONLY USE NUMBERS(CONTINUE WHERE YOU LEFT OFF") 
        
def adding_product_cost():
    print(" ")
    
    while True:
        try:
            for_question = int(input("How many Products? "))
            
            for i in range(for_question):
                item = input("Product Name: ")#the key in dictionary
                cost = float(input("Cost: "))#value in dictionary
                product_cost[item] = cost#this is the only way I figured out how to add things to dictionary
           
            print("")   
            print("Contains")
            print_product_cost()
            
            break
        
        except:
            print("ONlY USE NUMBERS(CONTINUE WHERE YOU LEFT OFF)") 
    
def adding_cost():#to add up all the expenses so that we can calculate net income
    
    
    x = sum(value for key, value in operating_cost.items())#didnt know u can do this to this day 
    y = sum(value for key, value in employee_salary.items())
    z = sum(value for key, value in product_cost.items())
        
    a = x + y + z
           
    print(f"Overall Cost of Expenses: ${a}")
    
    return a

#----removing things from lists----#

def remove_operating_cost():#this is where I touched new lands 
    print("")#i WANTED only the value to be "removed" and not the key
    
    while True:
        
        print_operating_cost()
        
        expense = str(input('What Expense do you want removed?(Type "done" to exit) '))
        
        if expense == "done":#prety self explanatory
            break
        
        else:
            if expense in operating_cost: 
                operating_cost[expense] = 0#essentially not removing the value and making it "None" but change value to 0
                #this allows for math to be done, important for calc the net income
                
            else:
                print(f"{expense} is not in the Operating Cost") 
        
        print("") 
        
        print_operating_cost()#print often to show what is in list and what happen
        print("")
        
def remove_employee_salary():
    print("")
    
    while True:
        print_employee_salary()
        
        employee = input('What Employee/Salary do you want removed?(Type "done" to exit) ')
        if employee == 'done':
            break
        
        else:
            if employee in employee_salary:
                del employee_salary[employee]
                print_employee_salary()
                
            else:
                print(f"{employee} is not in the Employee List")
                
def remove_product_cost():#this function is created the same way basically as the remove_employee_salary() function 
    print("")
    
    while True:
        print_product_cost()
        
        product = input('What Product do you want removed?(Type "done" to exit) ')#asking for specific key in dic
        
        if product == 'done':#i used your model so that whenever done is typed, it goes out of the loop 
            break
        
        else:
            if product in employee_salary:
                del product_cost[product]#dont wanna make it too hard, so its better to just remove the key
                print_product_cost()#i like to print the dict often to show user whats there and what was removed
                
            else:
                print(f"{product} is not in the Product Cost") 
        
while 1:
    print("") 
    random_inspirational_words()
    
#asking a question #I used "str" to solve constant error for when you put random things in the input
    question = str(input("""
Options:
1. Print Current List's 
2. Add Items to lists's 
3. Remove Items from List's
4. Pre-Tax Net Income
5. Exit
"""))
    
    if question == "1":#simply printing 
        
        print("Operating Cost")
        print_operating_cost()
        print("")
        
        print("Employee's Salaries") 
        print_employee_salary()
        print("")
        
        print("Product Cost's")
        print_product_cost()
        print("")
        
        e = adding_cost()
        
        
    elif question == "2":#adding items from lists
        
        while True:
            add_question = str(input("""
What list do you want to Add To?

1. Operating Cost
2. Employee's Salaries
3. Product Cost's
4. Exit
"""))#since we are working with many lists
            
            if add_question == "1":
                adding_operating_cost()
               
                
            elif add_question == "2":
                adding_employee_salary()
                
                
            elif add_question == "3":
                adding_product_cost()
                
                
            elif add_question == "4":
                break
            
            else:
                print("ONLY USE NUMBERS ABOVE")#This is for when the anwser is given a integer but not 1,2,3,4
                
          
                    
        
    
    elif question == "3":#removing items from lists
        
        while True:
            remove_question = str(input("""
What list do you want to Remove From?

1. Operating Cost
2. Employee's Salaries
3. Product Cost's
4. Exit
"""))#since we are working with many lists
            
            if remove_question == "1":
                remove_operating_cost()
               
                
            elif remove_question == "2":
                remove_employee_salary()
                
                
            elif remove_question == "3":
                remove_product_cost()
                
                
            elif remove_question == "4":
                break
            
            else:
                print("ONLY USE NUMBERS ABOVE")#This is for when the anwser is given a integer but not 1,2,3,4
            
            
        
    
    elif question == "4":#net income 
        
        while True: 
        
            try:
            
                d = float(input("What was the business Total Revenue?(Only numbers) "))
                e = adding_cost()
                        
                net_income = d - e
                
                print(f"Net Income is ${net_income}")
                break
                
            except:
                print("ONLY NUMBERS")
                continue 
                
            
                       
    
    elif question == "5":
        time.sleep(3)
        break
    
    else:
        print("ONLY USE NUMBERS: 1,2,3,4,5")
        continue
    
      
    
        


        
        
        

        
    