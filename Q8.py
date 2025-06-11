num = int(input("Enter a number: "))

temp = num
count = 0
while temp > 0:
    count = count + 1
    temp = temp // 10

temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    sum = sum + (digit ** count)
    temp = temp // 10

if sum == num:
    print("It is an Armstrong number.")
else:
    print("It is not an Armstrong number.")
