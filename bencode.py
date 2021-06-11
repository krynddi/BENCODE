

class DecodeBencode:

    def __init__(self, data: str):
        
        self.data = "l" + data + "e"
        self.position = 0
        self.lenght = len(data)
        

    def start(self):
        result = self.decode_list()
        return result

    def inc_pos(self):

        self.position += 1


    def decode_str(self):

        count_symb = ""
        while self.data[self.position] != ":":

            count_symb += self.data[self.position]
            self.inc_pos()

        self.inc_pos()
        try:
            count_symb = int(count_symb)

        except ValueError:
            print("Ошибка в декоде строки, позиция - ", self.position)
            return None

        substr = ""
        for c in range(count_symb):
            substr += self.data[self.position] 
            self.inc_pos()

        return substr


    def decode_int(self):

        number = ""
        self.inc_pos()
        while self.data[self.position] != "e":

            number += self.data[self.position]
            self.inc_pos()

        self.inc_pos()
        try:
            number = int(number)

        except ValueError:

            print("Ошибка декода целого, позиция - ", self.position)
            return None

        return number


    def decode_list(self):

        result_list = []
        self.inc_pos()
        while self.data[self.position] != "e":

            if self.data[self.position].isdigit():
                result = self.decode_str()

            elif self.data[self.position] == "i":
                result = self.decode_int()

            elif self.data[self.position] == "l":
                result = self.decode_list()

            elif self.data[self.position] == "d":
                result = self.decode_dict()

            else:
                print("Ошибка декода листа, позиция - ", self.position)
                return None

            result_list.append(result)

        self.inc_pos()
        return result_list


    def decode_dict(self):

        result_dict = dict()
        isKey = True
        self.inc_pos()

        while self.data[self.position] != "e":

            if self.data[self.position].isdigit():
                result = self.decode_str()

            elif self.data[self.position] == "i":
                result = self.decode_int()

            elif self.data[self.position] == "l":
                result = self.decode_list()

            elif self.data[self.position] == "d":
                result = self.decode_dict()

            else:
                print("Ошибка декода словаря, позиция - ", self.position)
                return -1
           
            if isKey:
                if type(result) == str:
                    key = result
                    result_dict[key] = None

                else:
                    print("Ошибка ключа")
                    return None
            else:

                result_dict[key] = result

            isKey = not isKey

        self.inc_pos()
        return result_dict


class EncodeBencode:

    def __init__(self, data: list):

        self.result = ""
        self.data = data


    def start(self):

        return self.main_loop(self.data)


    def main_loop(self, data):

        bencode_str = ""
        for el in data:

            if type(el) == int:
                result = self.encode_int(el)

            elif type(el) == str:
                result = self.encode_str(el)

            elif type(el) == list:
                result = self.encode_list(el)

            elif type(el) == dict:
                result = self.encode_dict(el)

            else:
                print("Ошибка типа - ", el, type(el))
                return None

            bencode_str += result

        return bencode_str


    def encode_int(self, el):

        return f"i{el}e"


    def encode_str(self, el):

        return f"{len(el)}:{el}"


    def encode_list(self, el):

        return f"l{self.main_loop(el)}e"


    def encode_dict(self, el):

        keys = list(el.keys())
        try:
            keys.sort()
        except TypeError:
            print("Ошибка типа")
            return ""

        result = ""

        for key in keys:

            if type(key) == str:
                result += self.encode_str(key)

            else:
                print("Ошибка типа ключа", key)

            value = el[key]
            if type(value) == int:
                result += self.encode_int(value)

            elif type(value) == str:
                result += self.encode_str(value)

            elif type(value) == list:
                result += self.encode_list(value)

            elif type(value) == dict:
                result += self.encode_dict(value)

            else:
                print("Ошибка типа - ", value, type(value))
                return None

        return f"d{result}e"
