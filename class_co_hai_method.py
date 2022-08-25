class InputOutString(object):
    def __init__(self):
        self.a = ""

    def get_string(self):
        self.a = input("Chuỗi:")

    def print_string(self):
        print(self.a.upper())


strObj = InputOutString()
strObj.get_string()
strObj.print_string()
