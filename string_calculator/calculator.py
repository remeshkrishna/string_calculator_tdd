class Calculator:
    def add(self,inputString:str):
        try:
            if inputString=="":
                return 0
            delimiter = ','
            if inputString.startswith("//"):
                parts = inputString.split('\n',1)
                delimiter = parts[0].replace('//','')
                inputString = parts[1]

            inputString = inputString.replace('\n',delimiter)

            int_numbers = list(map(int,inputString.split(delimiter)))
            negative_numbers = [num for num in int_numbers if num<0]
            if negative_numbers:
                raise Exception("negatives not allowed: "+','.join(map(str,negative_numbers)))

            res=sum(int_numbers)
            return res
        except ValueError:
            raise ValueError("Invalid string provided")