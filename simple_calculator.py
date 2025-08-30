def to_add (first_number, second_number):
    return first_number + second_number

def to_subtract(first_number, second_number):
    return first_number - second_number

def to_multiply(first_number, second_number):
    return first_number * second_number

def to_devide(first_number, second_number):
    try:
        result = first_number / second_number
    except ZeroDivisionError as e:
        return f"Can't a divide a number by zero: {e}"
    else:
        return result

def exponent(first_number, second_number):
    return first_number ** second_number

def percent(first_number, second_number):
    try:
        result = (first_number / second_number) * 100
    except ZeroDivisionError as e:
        return f"Can't a divide a number by zero: {e}"
    else:
        return f"%{result}"



first_number = float(input("Enter first number: "))
operator = input("Enter Operator: ")
second_number = float(input("Enter second number: "))

match operator:
    case "+":
        print(to_add(first_number, second_number))
    case "-":
        print(to_subtract(first_number, second_number))
    case "*":
        print(to_multiply(first_number, second_number))
    case "/":
        print(to_devide(first_number, second_number))
    case "**":
        print(exponent(first_number, second_number))
    case "%":
        print(percent(first_number, second_number))
        