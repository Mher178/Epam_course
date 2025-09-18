class Test:

    def __init__(self, first, second):
        self.first = first
        self.second = second
    def new_function(self):
        result = self.first + self.second
        return result


My_Test = Test(5,7)
print(My_Test.new_function())