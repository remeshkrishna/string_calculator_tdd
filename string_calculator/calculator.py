class Calculator:
    def add(self,inputString):
        try:
            if inputString=="":
                return 0
            res=sum(map(int,inputString.split(',')))
            return res
        except ValueError:
            raise ValueError("Invalid string provided")