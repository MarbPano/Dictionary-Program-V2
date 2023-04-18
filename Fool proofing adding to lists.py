#fool proofing my adding to lists
product_cost = {}

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
            
            
            break
            
        except:
            print("ONLY USE NUMBERS")#the problem i hate with this is that, if you dont put in what python likes, it will restart back to the
            #original question 
            continue
    
adding_product_cost()

operating_cost = {'Rent': 300,
                  'Accounting and Legal Fees': 0,
                  'Bank Charges': 0,
                  'Sales Fees': 0,
                  'Marketing Fees': 0,
                  'Officce Supplies': 0,
                  'Repairs': 0,
                  'Utilities': 0,
}                 
def print_operating_cost():
    print("")
    
    for item, cost in list(operating_cost.items()):#for every item and cost in shopping_list print the {item} or key, {cost} or value. in dict
        print(f"{item}: ${cost}")
        
def remove_operating_cost():
    print("")
    
    while True:
        
        print_operating_cost()
        
        print("") 
        expense = str(input('What Expense do you want removed?(Type "done" to exit) '))
        if expense == "done":
            break
        
        else:
            if expense in operating_cost: 
                operating_cost[expense] = 0#essentially not removing the value and making it "None" but change value to 0
                #this allows for math to be done, important for calc the net income
                
            else:
                print(f"{expense} is not in the Operating Cost's") 
        
        print("") 
        print('CURRENT EXPENSES:')
        print_operating_cost()
        
     

remove_operating_cost()