first = -1
second = -1
quantityOfNumbersToFind = int(input("Enter a quatity of numbers to calc: ")) 

for i in range(1,quantityOfNumbersToFind,1):

    if second == -1 :
        print(1)
        if first>0:
            second = 1
        else:
            first = 1

        continue    
    else:
        sum = second + first
        print(sum)
        second = first
        first = sum
