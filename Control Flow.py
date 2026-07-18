# ===========================================
# CONDITIONAL STATEMENTS
# ===========================================

# Q1.Take a number as input. Print "Positive" if it is greater than 0.
num=int(input())

if num >0:
    print("Positive")
else:
    print("Negative")

# Q2.Take a number as input.
# Print "Even" if it is divisible by 2.
# Otherwise print "Odd".
num=int(input())
if num % 2 ==0:
    print("Even")
else:
    print("Odd")

# Q3. Take a student's marks as input.
# Marks ≥ 40 → Print "Pass"
# Otherwise → Print "Fail"
marks=int(input())

if marks >= 40:
    print("Pass")
else:
    print("Fail")

# Q4. Take age as input.
# Age ≥ 18 → Print "Eligible to Vote"
# Otherwise → Print "Not Eligible"
age=int(input())

if age >=18:
    print("Eligible for vote")
else:
    print("Not Eligible")

# Q5.Take two numbers as input.
# Print the greater number.
# If both are equal, print "Both are Equal".

num=int(input("Enter num:"))
num2=int(input("Enter num2"))

if num == num2:
    print("Both are Equal")
else:
    print("Both are not Equal")

# ===========================================
# FOR LOOPS
# ===========================================

# Q1.Print numbers from 1 to 10 using a for loop.
num=0

for n in range(1,11):

    print(n)

# Q2.Print all even numbers from 1 to 20.
num=1

for n in range(1,21):
    if n%2==0:
        print(n)


# Q3.Take a number n as input and print numbers from 1 to n.
n=int(input())

for i in range(1,n+1):
    print(i)

# Q4.Take a number and print its multiplication table.
num=int(input())

for i in range(1,11):
    print(num*i)    

# Q5.Calculate the sum of numbers from 1 to 100 using a for loop.
total=0

for i in range(1,101):
    total+=1

print(total)

# ============================================
# WHILE LOOPS
# ============================================

# Q1.Print numbers from 1 to 10 using a while loop.
num=1

while num <=10:
    print(num)
    num+=1


# Q2.Print numbers from 10 to 1.

num=10

while num >=1:
    print(num)
    num-=1

# Q3.Take a number n as input and print 1 to n using while.

n=int(input())
num=1
while num <=n:
    print(num)
    num+=1

# Q4.Print all even numbers from 2 to 20 using while.

num=2

while num <=20:
    print(num)
    num+=2

# Q5.Take a number and print its multiplication table using while.
num=4

i=1
while i <=10:
    print(num*i)
    i+=1
    

# =============================================
# LOOP CONTROL
# =============================================

# Q1.(break)
# Print numbers from 1 to 10, but stop when the number becomes 6.

for i in range(1,11):
    if i ==6:
        break
    print(i)    

# Q2.(continue)
# Print numbers from 1 to 10, but skip 5.
for i in range(1,11):
    if i ==5:
        continue
    print(i)


# Q3.(continue)
# Print only odd numbers from 1 to 20.
for i in range(1,21):
    if i%2==0:
        continue
    print(i)

# Q4.(break)
# Keep asking the user to enter a number.
# Stop the loop if the user enters 0.

while True:
    num=int(input())
    if num==0:
        break

# Q5.(pass)

# Write an if statement that checks if a number is positive.
# If it is positive, use pass.
# Otherwise print "Negative".

num=int(input())

if num > 0:
    pass
else:
    print("Negative")