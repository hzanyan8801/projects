# Creating our addition function 

def additional (a, b):
    return a+b 

# Main program 

def main():
    num1 = float(input("Enter the first no:\n"))
    num2 = float(input("Enter the second no:\n"))

    result = additional(num1, num2)

    print("The result is" , result)

main()