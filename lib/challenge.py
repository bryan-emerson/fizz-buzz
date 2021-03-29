for num in range(0,100):
    if num % 5 == 0 and num % 3 == 0:
        print('fizzbuzz')
    if num % 3 == 0:
        print('fizz')
    if num % 5 == 0:
        print('buzz')
    print(num)