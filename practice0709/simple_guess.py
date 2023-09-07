
number = int(input('ввести число -->  '))

##d = 0

def guess(number):
    if number == 1:
        return number
    else:
        for i in range(number):
            if i * i == number:
                y = i
##                d += 1
                return y
##            elif d == number :
##                print("такого корня нет")
##            else:
##                y: str = 'такого корня нет'
##                return y

                    
                                          
w = guess(number)
print(w)
                
            