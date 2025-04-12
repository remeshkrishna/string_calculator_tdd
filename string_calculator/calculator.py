class Calculator:
    def add(self,inputString):
        if inputString=="":
            return 0
        
        if len(inputString)==1:
            return int(inputString)