class Calculator:
    def add(self,inputString):
        try:
            if inputString=="":
                return 0
            
            if len(inputString)==1:
                return int(inputString)
        except ValueError:
            raise ValueError("Invalid string provided")