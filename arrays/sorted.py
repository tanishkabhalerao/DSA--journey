numbers = [2, 4, 6, 8, 10]
                      
sorted_array = True

for i in range(len(numbers)-1):
    if numbers[i]>numbers[i+1]:
        sorted_array=False
        break

if sorted_array:
    print("sorted")
else:
    print("not sorted")
