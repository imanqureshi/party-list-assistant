#20 lines of comment
#40 lines of code
#problem is described at the top 

#Assignment: invent ur own problem and solve it

#implement decisions using if statements
#statements using boolean primitive data types
#compare strings and/or characters
#wrtie loops using while or for 
#write functions

#Computer Organization 1 Binary Calculator 
#Decimal to Binary 
def dec_to_bin(num):
    binaryNum = []
    while num > 0.5: #while the number is still divisble by 2 (integer division)
        digit = num%2 
        binaryNum.append(digit) #add the 
        num = num//2 
    binaryNum = binaryNum[::-1]
    return binaryNum

def oct_to_bin(num):
    octalNum = []
    while num > 0 :
        digit = num%8
        octalNum.append(digit)
        num = num//8
    octalNum = octalNum[::-1]
    result = dec_to_bin(int(octalNum))
    return result

def hex_to_bin(num):
    octalNum = []
    while num//8 > 0:
        digit = num%8
        octalNum.append(digit)
        num = num//8
    octalNum = octalNum[::-1]
    result = dec_to_bin(int(octalNum))
    return result

def onesComp():
    pass

def twosComp():
    pass

if __name__ == '__main__':
    choice = int(input('Please enter your choice of Conversion:\n1. Base Conversion \n2. Complements\nEnter your choice: '))
    while choice != 1 and choice != 2:     #continues to ask user for input until valid option is given
        choice = int(input('Please enter a valid choice: '))
    if choice == 1:
        num = int(input('Please enter an integer: '))
        print(dec_to_bin(num))


