num = int(input())

if (num % 2 == 1):
    print("Weird")
elif ( 2 <= num and num <= 5):
    print("Not Weird")
elif ( 6 <= num and num <= 20):
    print("Weird")
else:
    print("Not Weird")