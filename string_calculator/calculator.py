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

            res=sum(map(int,inputString.split(delimiter)))
            return res
        except ValueError:
            raise ValueError("Invalid string provided")