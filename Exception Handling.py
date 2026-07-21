# =======================================================
# TRY 
# ======================================================

# Q1.Take two numbers from the user and try to divide them.
try:
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))

    result=num1/num2
    print("Result:",result)

except:
    print("Something went wrong!")
    
# Q2.Take input from the user and convert it into an integer
try:
    num=int(input("Enter a number:"))
    print("Number is:",num)

except:
    print("Invalid Output!")

# Q3.Create a list 5 numbers and print the 7th element.
try:
    number=[10,20,30,40,50]

    print(number[7])

except:
    print("Index does not exist!")

# Q4. open a file named student.txt
try:
    file = open("student.txt","r")

    print(file.read())

except:
    print("File not found!")

# Q5.Convert the string "25.5" into a float.

try:
    number=float("25.5")
    print("Float Value:",number)

except:
    print("Conversion failed")

# ==============================================================
#   TRY + EXCEPT
# ==============================================================

# Q1. Handle the ZeroDivisionError when divinig two numbers.

try:
    num1=int(input("Enter First number:"))
    num2=int(input("Enter Second number:"))

    result=num1/num2
    print("Result is :",result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")


# Q2. Handle ValueError if the user enters text instead of a number.

try:
    age=int(input("Enter your age:"))
    print("Age:",age)

except ValueError:
    print("Error: Please enter numbers only.")


# Q3. Handle IndexError while accessing an invalid list index.

try:
    number=[10,20,30]
    print(number[5])

except IndexError:
    print("Error: Index is out of range.")
# Q4. Handle FileNotFound when opening a file

try:
    file=open("student.txt","r")
    print(file.read())

except FileNotFoundError:
    print("Error : File Not Found.")

# Q5. Handle typeError by trying to add an integer and a string.

try:
    num=10
    text="20"

    print(num+text)

except TypeError:
    print("Error : Cannot add integer and sting")


# =============================================================
# MULTIPLIE EXCEPT
# =============================================================

# Q1. Write a program that can raise both ZeroDivisionErro and ValueError.handle both separately.

try:
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number"))

    result=num1/num2
    print("Result:",result)

except ValueError:
    print("Error: Please eneter numbers only")
    
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

# Q2. Handle IndexError and TypeError in the same program.

try:
    number=[10,20,30]

    print(number[5])

    print(10+"20")

except IndexError:
    print("Error: Invalid index")
except TypeError:
    print("Error : Cannot and integer and string.")



# Q3. Take a filename from the user handle both FileNotFoundError and PermissionError.

try:
    file=open("student.txt","r")
    print(file.read())

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")


# Q4. Write a program that handle NameError and ValueError

try:
    age=int(input("Enter age:"))
    print(age)

except ValueError:
    print("Erro: Invalid age.")

except NameError:
    print("Error: variable not defined.")

# Q5. Write a program that handle KeyError and IndexError.

try: 
    student={
        "name":"Rahul",
        "age":21

    }

    print(student["marks"])

except KeyError:
    print("Error: Key not found")

except IndexError:
    print("Error: Invalid index.")


# =============================================================
# TRY + EXCEPT + ELSE
# =============================================================

# Q1. Divide two numbers if no error occurs , print "Division Successful"using else.
try:
    num1=int(input("Enter first num:"))
    num2=int(input("Enter second num:"))

    result=num1/num2

except ZeroDivisionError:
    print("Error : Cannot divide by zero")

except ValueError:
    print("Error: Enter numbers only.")

else:
    print("Division Successful!")
    print("Result:",result)
    
# Q2. Convert user input to an integers . if successful, print it square in else.
try:
    age=int(input("Enter your age:"))

except ValueError:
    print("Invalid input!")

else:
    print("Your age is :",age)


# Q3. Open a file if it opens successfully print "File Opened Successfully" in else.

try: 
    file=open("student.txt","r")

except FileNotFoundError:
    print("File not found")

else:
    print("File opened successfully.")
    print(file.read())
    file.close()
# Q4. Take the user's age if it entered correctly, print"Eligible" in else

try:
    age=int(input("Enter your age:"))

except ValueError:
    print("Please enter a valid number.")

else:
    if age>18:
        print("Eligible")
    else:
        print("Not Eligible")
# Q5. Access a list element if no error occurs , print "Element Found" in else.

try:
    number=[10,20,30,40,50]
    print(number[2])

except IndexError:
    print("Index out of range.")

else:
    print("Element Found")


# ==============================================================
# TRY + EXCEPT + FINALLY 
# ==============================================================

# Q1. Divide two numbers and print "Program Ended" in finally.
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Program Ended")


# Q2. Open a file and make sure it is closed using finally.
try:
    file = open("student.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found.")

finally:
    print("File operation completed.")
# Q3. Convert user input into an integer and print "Thank You" in finally.try:
try:
    age = int(input("Enter your age: "))
    print("Age:", age)

except ValueError:
    print("Invalid input.")

finally:
    print("Thank You!")

# Q4. Access a dictionary key. Whether the key exists or not, print "Execution Completed" in finally.
try:
    student = {
        "name": "Rahul",
        "age": 21
    }

    print(student["marks"])

except KeyError:
    print("Key not found.")

finally:
    print("Execution Completed")
# Q5. Create a program that handles an exception and always prints "Goodbye" in the finally block.
try:
    numbers = [10, 20, 30]

    print(numbers[1])

except IndexError:
    print("Invalid Index")

finally:
    print("Goodbye")
# ===============================================================
# CUSTOM EXCEPTIONS (RAISE)
# ===============================================================

# Q1. Raise an exception if the user's age is less than 18.
try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise ValueError("You are not eligible.")

    print("Welcome!")

except ValueError as e:
    print(e)
# Q2. Raise a ValueError if a number entered is negative.
try:
    num = int(input("Enter a number: "))

    if num < 0:
        raise ValueError("Negative numbers are not allowed.")

    print("Number:", num)

except ValueError as e:
    print(e)
# Q3. Raise an exception if the password is shorter than 8 characters.
try:
    password = input("Enter password: ")

    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters.")

    print("Password Accepted")

except ValueError as e:
    print(e)
# Q4. Raise an exception if the user enters a salary less than 10,000.
try:
    salary = int(input("Enter salary: "))

    if salary < 10000:
        raise ValueError("Salary must be at least ₹10,000.")

    print("Salary Accepted")

except ValueError as e:
    print(e)
# Q5. Raise an exception if the marks entered are greater than 100 or less than 0.
try:
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")

    print("Marks:", marks)

except ValueError as e:
    print(e)