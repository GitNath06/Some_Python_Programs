print("Press S to Stop!!! ")
while(True):
    user_input = input("Enter calculation: ")
    if user_input.upper() == 'S':
        break
    
    result = eval(user_input)
    print(f"{user_input} = {result}")

print("Thank you!!!")


'''


advance method

def safe_eval(expression):
    try:
        # Use eval with a restricted environment
        result = eval(expression, {"__builtins__": None}, {})
        return result
    except Exception as e:
        return f"Error: {e}"

print("Press S to Stop!!!")

while True:
    user_input = input("Enter calculation: ")
    if user_input.upper() == 'S':
        break
    
    result = safe_eval(user_input)
    print(f"{user_input} = {result}")

print("Thank you!!!")

'''