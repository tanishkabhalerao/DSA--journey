numbers = [4, 7, 2, 7, 9, 4]


for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] == numbers[j]:
         
            print(numbers[i])