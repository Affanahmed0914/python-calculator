import math
# Empty dictionary, user can store username and strong password
users = {}

def get_int(message):
    while True:
        value = input(message).strip()
        # Only allow integers with optional negative sign
        if value.lstrip('-').isdigit():
            return int(value)
        else:
            print("Invalid!Please enter a valid integer")

def get_float(message):
    while True:
        value = input(message).strip()
        # Check if valid float (supports negative)
        try:
            return float(value)
        except ValueError:
            print("Invalid!Please enter a valid number")

#I used this function so that if students type letters or symbols, the calculator will not crash.It will show an error message and ask again


def sign_up():   #function define
    print("\tSign Up\t")     #\t for big space
    username =input("Create a username: ") #declaringn a variable username
    if username in users:
        print("This username is already used! Try another username.") #print is used to display
        return
    password =input("Create a password: ") #declaring a variable password
    users[username] =password
    print("successfully created an account")
    print("\n\"WELCOME!\"\n Dear",username )
def login():
    print("\tLogin\t")
    username =input("Enter username: ")
    password =input("Enter password: ")

    if username in users and users[username] == password:
        print("Login successful! ")
        calculator_menu()  # Go to calculator menu after login
    else:
        print("Invalid username or password!\n")


#General maths
def basic_mathematical_functions():
 while True:
    print("\n \tBasic Mathematics\t\n")
    print("1. Addition")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Remainder")
    print("6. Exponentiation")
    print("7. Go back")
    print("8. back to main menu")
    choice = input("Choose option (1-8): ").strip()
    if choice not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("Invalid choice! Please select 1-8 only.")
        return


    if choice == "8":
        print("going back to the main menu")
        calculator_menu()
    elif choice =="7":
        print("going back")
        basic_mathematical_functions()
        break

    x =get_float("Enter first number: ")
    y =get_float("Enter second number: ")
    if choice == "1":
        print("Result =",x+y)
    elif choice == "2":
        print("Result =", x-y)
    elif choice == "3":
        print("Result =", x*y)
    elif choice == "4":
        if y == 0:
            print("Invalid!") #Cannot divide by zero
        else:
            print("Result =", x/y)
    elif choice == "5":
        if y == 0:
            print("invalid!") #Cannot divide by zero
        else:
            print("Result =", x%y)
    elif choice == "6":
        print("Result =", x**y)
    else:
        print("Invalid choice!")


def sqrt():
    user_input = input("Enter a number: ").strip() #asks for a user input
    if user_input =="": # if the input is null will return to ask for input
        print("Invalid input!")
        return
    # defining square root function
    number = float(user_input) #takes the user input if not null

    if number < 0: #if the number is 0 or in negative the square root does not exist
        print("Number can not be negative!")
        return # returns to enter a positive number

    result = math.sqrt(number)  # calculates the square root of the input
    print("The result is: ", result) #prints result


# user has to enter number that is less than 50, and all multiples found will also be less than 50
def multiples_under_50():  # defining function for reusable block of code
    a = int(input("Enter a number less than 50:"))  # will ask user to input a single digit less than 50

    while a >= 50:  # if user enters a number greater than 50
        print("invalid. No multiples found.")  # will display an error to user
        a = int(input("Enter a number less than 50:"))  # asks user again

    else:  # if no error
        for i in range(100):  # prints first 100 multiples
            if i * a < 50:  # only print multiples less than 50
                print(i * a)  # output to user


def find_hcf(a, b):
    # function to calculate hcf of numbers using repeated substraction
    while a != b:  # keep looping until both numbers are equal
        if a > b:
            a = a - b  # subtract small from big
        else:
            b = b - a
    return a  # when both numbers are equal, return that number as HCF

def find_lcm(a, b):
    hcf = find_hcf(a, b)  # first find the HCF using our HCF function
    lcm = (a * b) // hcf  # LCM formula
    return lcm  # return the LCM

def hcf_lcm_menu():
    while True:
        try:
            num1 = int(input("Enter The First Number: "))  # asks user for the first number
            num2 = int(input("Enter The Second Number: "))  # second number
            break  # exits loop if inputs are correct
        except ValueError:
            print("Invalid input! Please input whole numbers only.")  # prints error message if input are incorrect

# check special case when both numbers are zero
    if num1 == 0 and num2 == 0:
        print("HCF and LCM are undefined for both being 0.")  # show message if both are zero
    else:
        hcf = find_hcf(num1, num2)  # find HCF
        lcm = find_lcm(num1, num2)  #find lcm
        print("The HCF =", hcf)  # print HCF
        print("The LCM =", lcm)  #print LCM

#Statistics part
def mode():
    user_input = input("Enter Separated Numbers: ").strip() # asking for user input
    if user_input == "": #if null returns to enter an input
        print("Invalid! No numbers entered" )
        return

    numbers = list(map(int, user_input.split()))

    freq = {num: numbers.count(num) for num in numbers} #counts the frequency of each number
    max_count = max(freq.values()) #finds the most frequent number
    if max_count == 1: # if all numbers occur once
        print("There is no mode all numbers occur once")
        return
    mode_value= max(numbers, key=numbers.count) # finds the most frequent number
    print("The mode =", mode_value) #prints value


# Calculate the mean of from the list of numbers entered
def mean():  # defining reusable block of code
    # input() allows user to enter numbers
    # split () changes entered string into a list of them at each space between them
    # map(float) will change every string in the list into a decimal number
    # nums is a map object and does not store all values yet, so list() turns it into a list that can store all values
    nums = list(map(float, input("Enter multiple numbers. Make sure they're separated with spaces:").split()))

    # len(nums) gives the amount of number in the list
    if len(nums) == 0:  # if there are no numbers found in the list
        print("No numbers found. Please enter a number.")  # display message to user
        return  # ends function since no number are found in the list
    # calculates the mean of the list of number given
    # sum(nums) adds the numbers in the list
    mean_value = sum(nums) / len(nums)  # mean is equals to the sum divided by the amount of number in the list
    print("The mean of the given numbers are:", mean_value)  # will display the mean of the given list of numbers

# function to find the median
def find_median(nums):
    nums.sort()  # sorts the numbers
    n = len(nums)  # total number of numbers
    mid = n // 2  # middle index
    if n % 2 != 0:  # if count is odd
        return nums[mid]  # median is the middle number
    else:
        return (nums[mid - 1] + nums[mid]) / 2  # if even, median is average of 2 numbers

def median_menu():
    numbers = []  # list to store user input
    print("Enter the numbers. Type 'done' when finished.")  # instructions
    while True:
        value = input("Enter a number: ")
        if value.lower() == "done":  # user finished entering number
            break
        try:
            numbers.append(float(value))  # add number to list (assumes valid input)
        except ValueError:
            print("Invalid input! Please enter a number or 'done' when finished.")

    if numbers:
        median = find_median(numbers)  # calls function to calculate median
        print("The Median is: ", median)  # show results
    else:  #check if the list is empty
        print("Error: No numbers entered")


#conversion of number
#convert decimal to binary including fractions
def d_b(n):
    try:
        n = float(n)  #convert input to float to handle decimals
    except(ValueError,TypeError):
        return "invalid input"  #error if not a number

    w = int(n)    #separate the whole number part
    f = n - w     #calculate the fractional part

    w_bin = bin(w)[2:]  #convert whole part to binary and remove 0b prefix

    f_bin = ''  #initialize string to store fractional binary part
    count = 0   #counter to prevent infinite loops
    while f != 0 and count < 10:  #repeat until fraction becomes 0 or limit reached
        f *= 2
        bit = int(f)
        f_bin += str(bit)
        f -= bit
        count += 1

    if f_bin:
        return w_bin + '.' + f_bin  #combine whole and fraction parts
    else:
        return w_bin               #return only whole part if no fraction


#convert decimal to octal including fractions
def d_o(n):
    try:
        n = float(n)  #convert input to float
    except(ValueError,TypeError):
        return "invalid input"

    w = int(n)
    f = n - w

    w_oct = oct(w)[2:]  #convert whole part to octal and remove 0o prefix

    f_oct = ''  #string to store fractional octal
    count = 0
    while f != 0 and count < 10:
        f *= 8
        digit = int(f)
        f_oct += str(digit)
        f -= digit
        count += 1

    if f_oct:
        return w_oct + '.' + f_oct  #combine whole and fraction parts
    else:
        return w_oct


#convert decimal to hexadecimal including fractions
def d_h(n):
    try:
        n = float(n)  #convert input to float
    except(ValueError,TypeError):
        return "invalid input"

    w = int(n)
    f = n - w

    w_hex = hex(w)[2:].upper()  #convert whole part to hex remove 0x and make uppercase

    f_hex = ''  #store fractional hex
    count = 0
    while f != 0 and count < 10:
        f *= 16
        digit = int(f)
        if digit < 10:
            f_hex += str(digit)
        else:
            f_hex += chr(ord('A') + digit - 10)
        f -= digit
        count += 1

    if f_hex:
        return w_hex + '.' + f_hex
    else:
        return w_hex


#convert binary to decimal including fractions
def b_d(b):
    try:
        if '.' in b:  #if input has a decimal point
            w, f = b.split('.')
            dec = int(w, 2)      #convert whole part from binary to decimal
            for i, digit in enumerate(f, start=1):
                if digit not in '01':  #check for invalid binary digit
                    return "invalid input"
                dec += int(digit) * (2 ** -i)
            return dec
        else:
            return int(b, 2)
    except(ValueError,TypeError):
        return "invalid input"


#convert octal to decimal including fractions
def o_d(o):
    try:
        if '.' in o:
            w, f = o.split('.')
            dec = int(w, 8)
            for i, digit in enumerate(f, start=1):
                if digit not in '01234567':
                    return "invalid input"
                dec += int(digit) * (8 ** -i)
            return dec
        else:
            return int(o, 8)
    except(ValueError,TypeError):
        return "invalid input"


#convert hexadecimal to decimal including fractions
def h_d(h):
    try:
        h = h.upper()  #make uppercase
        if '.' in h:
            w, f = h.split('.')
            dec = int(w, 16)
            for i, digit in enumerate(f, start=1):
                if digit.isdigit():
                    dec += int(digit) * (16 ** -i)
                elif digit in 'ABCDEF':
                    dec += (ord(digit) - ord('A') + 10) * (16 ** -i)
                else:
                    return "invalid input"
            return dec
        else:
            return int(h, 16)
    except(ValueError,TypeError):
        return "invalid input"


#program menu for conversions
def conversion_of_number():
    while True:  #infinite loop until user chooses to exit
        print("number conversion menu")
        print("1. decimal to binary")
        print("2. decimal to octal")
        print("3. decimal to hexadecimal")
        print("4. binary to decimal")
        print("5. octal to decimal")
        print("6. hexadecimal to decimal")
        print("7. back to main menu")

        choice = input("enter your choice 1-7: ")  #user selects option

        if choice == "1":
            num = input("enter a decimal number: ")
            print("binary:", d_b(num))

        elif choice == "2":
            num = input("enter a decimal number: ")
            print("octal:", d_o(num))

        elif choice == "3":
            num = input("enter a decimal number: ")
            print("hexadecimal:", d_h(num))

        elif choice == "4":
            num = input("enter a binary number: ")
            print("decimal:", b_d(num))

        elif choice == "5":
            num = input("enter an octal number: ")
            print("decimal:", o_d(num))

        elif choice == "6":
            num = input("enter a hexadecimal number: ")
            print("decimal:", h_d(num))

        elif choice == "7":
            break  #exit the menu

        else:
            print("invalid choice")  #input not 1-7


def calculator_menu(): #define menu list
    while True:    #while True is used for creating a loop
        print("\n\tCALCULATOR MENU\t\n")
        print("1. Basic Mathematics")
        print("2. Square Root")
        print("3. Find Multiples less 50")
        print("4. HCF and LCM")
        print("5. Mode")
        print("6. Median")
        print("7. Mean")
        print("8. Conversion of Number")
        print("9. Back to menu")
        print("10. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":        #declaring 1st condition
            basic_mathematical_functions()
        elif choice == "2":      #declaring 2nd condition
            sqrt()
        elif choice == "3":      #declaring 3rd condition
            multiples_under_50()
        elif choice == "4":      #declaring 4th condition
            hcf_lcm_menu()
        elif choice == "5":      #declaring 5th condition
            mode()
        elif choice == "6":      #declaring 6th condition
            median_menu()
        elif choice == "7":      #declaring 7th condition
            mean()
        elif choice == "8":      #declaring 8th condition
            conversion_of_number()
        elif choice == "9":     #declaring 9th condition
            print("back!")
            calculator_menu()
        elif choice == "10":     #declaring 10th condition
            print("Log out from calculator")
            print("Thank you for using our calculator!")
            main()
            break  # declaring break for stop the loop
        else:  # else used for if none of the above are true , do this
            print("Invalid choice! Try again.")


def main():
    while True:
        print("\t Welcome to \"INFORMATICS SCHOOL\" Calculator\t\n")
        print("1. Sign Up")
        print("2. Login")
        print("3. Exit")
        option = input("Enter your choice: ")
        if option == "1":
            sign_up()
        elif option == "2":
            login()
        elif option == "3":
            exit()


        else:
            print("Invalid option! Please try again.")


main() 
