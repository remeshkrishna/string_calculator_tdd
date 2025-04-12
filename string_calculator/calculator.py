class Calculator:
    def add(self,inputString:str):
        try:
            if inputString=="":
                return 0
            delimiter = ','
            delimiters_list = []

            if inputString.startswith("//"):
                [delimiter_part,inputString] = inputString.split('\n',1)
                if delimiter_part.startswith("//["):
                    delimiter = delimiter_part[3:len(delimiter_part)-1]
                    delimiters_list = delimiter.split('][')
                    if len(delimiters_list)>1:
                        delimiter=delimiters_list[0]
                else:
                    delimiter = delimiter_part[2:]
                    if(len(delimiter)>1):
                        raise ValueError
                
            for d in delimiters_list:
                inputString = inputString.replace(d,delimiter)

            inputString = inputString.replace('\n',delimiter)

            int_numbers = list(map(int,inputString.split(delimiter)))
            negative_numbers = [num for num in int_numbers if num<0]
            if negative_numbers:
                raise Exception("negatives not allowed: "+','.join(map(str,negative_numbers)))

            res=sum(int_numbers)
            return res
        except ValueError:
            raise ValueError("Invalid string provided")