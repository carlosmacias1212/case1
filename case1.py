import csv
from sys import argv
from cs50 import SQL



#Feature Set
def total_credit_limit(months_since_inquiry):
    return credit_limit

def avg_interest_rate(state):
    return interest

def annual_income(job_title):
    return income

def avg_loan(ownership_type):
    return amount

def avg_loan_amount(purpose):
    return amount


#Interest Rate Model
db = SQL("sqlite:///LoanData.db")

if len(argv) != 2:
    print("ERROR")
    exit(1)

with open(argv[1], 'r') as loan_data:

    # Use DictReader
    reader = csv.DictReader(loan_data, delimiter=",")

    # Our two algorithms will use loan_amount with verified income / loan_amount with emp_length
    for row in reader:
        db.execute("INSERT INTO LoanData (verified_income, loan_amount, emp_length) VALUES (?, ?, ?)", row["verified_income"], row["loan_amount"], row["emp_length"])





## Data Cleansing- 
    #   CSV File contains some rows with NA in emp_length, this should either be updated or excluded
    #   No issues seen with verified_income and loan_amount, however should still be analysed as proper values


# interest_rate model
def predict_interest_rate(loan_amount, verification, emp_length):
    
    total_interest = 0
    income_interest = interest_from_verification(loan_amount, verification)
    emp_interest = interest_from_employment(loan_amount, emp_length)
    
    total_interest = income_interest + emp_interest
    
    return total_interest
    
    
#First Algorithm
    
def interest_from_verification(amount, status):
    if status == "Source Verified":
        
        if amount < 1500:
            return .015
            
        elif amount < 5000:
            return .02
            
        else:
            return .025
            
    elif status == "Verified":
        
        if amount < 1500:
            return .02
            
        elif amount < 5000:
            return .025
            
        else:
            return .03
    
    elif status == "Not Verified":
        
        if amount < 1500:
            return .025
            
        elif amount < 5000:
            return .03
            
        else:
            return .035
        
    
# Second Algorithm

def interest_from_employment(amount, length):
    base_interest = .035
    
    updated_interest = .035 - (.003 * length)
    
    if updated_interest < 0:
        return 0
    else: 
        return updated_interest
        
    
    

