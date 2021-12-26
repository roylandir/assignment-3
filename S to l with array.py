number = []
counter = int( input ('enter the counter :') )

for i in range(counter) :

    num = int (input ('Enter the number :')) 
    number.append(num)

for i in range (counter-1) :
    
    if number[i] < number[i+1] :
        continue
    
    else :
        print ('The condition has not been met')
        break