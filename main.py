i = 1
while i >= 1 and i <= 100:
    if i % 3 == 0 and i % 5 !=0:
        print("Fizz")
    else:
        if i % 5 == 0 and i % 3 !=0:
            print("Buzz")
        else:
            if i % 3 == 0 and i % 5 ==0:
                print("Fizz Buzz")
            else:
                print(i)
    i += 1