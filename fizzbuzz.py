for i in range(1,21):
    if i % 3 != 0 and i % 5 != 0:
        print(i)
    else: 
        if i % 3 == 0:
            print("Fizz", end='')
        if i % 5 == 0:
            print("Buzz", end ='')
        print()

   