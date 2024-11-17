from art import logo


def add(num1, num2):
    return num1 + num2
  
def sub(num1, num2):
    return num1 - num2
    
def mul(num1, num2):
    return num1 * num2
    
def div(num1, num2):
    return num1 / num2




Operations = {"+" : add, "-" : sub, "*" : mul, "/" : div}

def Calculator():
  print(logo)

  is_true = True
  n1 = float(input("What's the first number: "))
  
  while is_true == True:
    
    n2 = float(input("What's the Second number: "))
    
    for op in Operations:
      print(op)
  
    operation_sym = input("Pick an operation form the above line : ")
    
    if operation_sym == "+" or operation_sym == "-" or operation_sym == "*" or operation_sym == "/":
        
      Calculation_function = Operations[operation_sym]
      
      answer = Calculation_function(num1 = n1, num2 = n2)
  
      print(f"{n1} {operation_sym} {n2} = {round(answer, 2)}" )
  
    
      is_continue = input("do you want to continue then type Yes and No to exit or 'Restart' for new calculation : ").title()
    
      if is_continue == "Yes":
        n1 = answer
        is_true = True
    
      elif is_continue == "No":
        is_true = False

      elif is_continue == "Restart":
        Calculator()
    
      else:
        print("Invalid Input !")
  
    else:
      print("invalid symbol !")

Calculator()
    
