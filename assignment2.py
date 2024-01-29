import socket
from typing import Any


class Assignment2:

    # part 1

    def __init__(self, year):
        self.year = year
    
    def tellAge(self, currentYear):
        age = currentYear - self.year 

        print("Your age is", age)

    def listAnniversaries(self):
        currentYear = 2022
        l = []
        
        num = 1

        while self.year + num * 10 < currentYear:
            l.append(num*10)
            num +=1


        return l

    def modifyYear(self, n):
       
       part1 = str(self.year)
       part1 = part1[:2]*n
       converted_year = str(self.year * n)
       
       
       char = []
       for i in range(0, len(converted_year),2):
           char.append(converted_year[i])
           result = "".join(char)
    
       l = [part1,result]
       result = "".join(l)
       return result


    @staticmethod
    def checkGoodString(string):

        if len(string) < 9:
            return False
        
        l = []
        for char in string:
            l.append(char)

        counter = 0
        while l:
            k = l.pop()
            
            if k.isdigit():
                counter +=1
            if len(l) == 1:
                lastCheck = l.pop()
                if lastCheck.isdigit() or lastCheck.isupper():
                    return False
            


            

        if counter > 1 or counter != 1:
            return False


        return True

    @staticmethod
    def connectTcp(host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            s.connect((host, port))
            return True
        
        except (socket.error, OSError):
            return False
    




a = Assignment2(2000)

#part2 = a.tellAge(2024)

# part3 = a.listAnniversaries()

#part4 = a.modifyYear(5)

#part5 = a.checkGoodString("f1obar0more")


#part 6 
"""retval = Assignment2.connectTcp("www.google.com", 80)

if retval:
    print("Connection established correctly")
else:
    print("Some error")"""

# test


print("""Insert part to test here""")
