import art

def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multilpy(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
def exponent(n1,n2):
    return n1**n2

calc={
    "+":add,
    "-":subtract,
    "*":multilpy,
    "/":divide,
    "**":exponent,
}

def calculator():
    print(art.logo)
    int_float=True
    while int_float:
        try:
            num1=float(input("What's the first number? "))
            int_float=False
        except:
            print("Wrong input! Please enter a valid number.")
            int_float=True
    
    for operation in calc:
        print(operation)
        
    valid_sym=True
    while valid_sym:
        symbol1=input("Pick an operation from the lines above: ")
        if symbol1!="+" and symbol1!="-" and symbol1!="*" and symbol1!="/" and symbol1!="**":
            print("Wrong input! Please select a valid operation")
            valid_sym=True
        else:
            valid_sym=False        
    
    int_float=True
    while int_float:
        try:
            num2=float(input("What's the second number? "))
            int_float=False
        except:
            print("Wrong input! Please enter a valid number.")
            int_float=True
    
    answer1=calc[symbol1](num1,num2)
    
    print(f"{num1}{symbol1}{num2} = {answer1}")
    
    repeat=True
    while repeat:
        run_again=input(f"Type 'yes' to continue calculating with {answer1}, or 'no' to begin a new calculation: \n").lower()[0]
        if run_again=="y":
            valid_sym=True
            while valid_sym:
                symbol2=input("Pick another operation: ")
                if symbol2!="+" and symbol2!="-" and symbol2!="*" and symbol2!="/" and symbol2!="**":
                    print("Wrong input! Please select a valid operation")
                    valid_sym=True
                else:
                    valid_sym=False  
                
            int_float=True
            while int_float:
                try:
                    num3=float(input("What's the other number? "))
                    int_float=False
                except:
                    print("Wrong input! Please enter a valid number.")
                    int_float=True
            answer2=calc[symbol2](answer1,num3)
            print(f"{answer1}{symbol2}{num3} = {answer2}")
            answer1=answer2
            repeat=True
        elif run_again=="n":
            calculator()
        else:
            print("Wrong command! Please reply with 'y' or 'n'")
            repeat=True
calculator()