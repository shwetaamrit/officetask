num=int(input("A number given by u:"))
if num>1:
    for i in range (1,num+1):
        if (i%3==0 and i%5==0):
            print(i,"--This no is divisible by 3 n 5. fizzbuzz")
        elif i%3==0:
              print(i,"--This no is divisible by 3. fizz")
        elif i%5==0:
              print(i,"--This no is divisible by 5. buzz")
        else:
            print(end=" ")
