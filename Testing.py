class Test:

    def __init__(self, first, second):
        self.first = first
        self.second = second
    def new_function(self):
        result = self.first + self.second
        return result
    def old_function(self, vb1):
        new_vb = vb1**2
        return new_vb


My_Test = Test(5,7)
print(My_Test.old_function(3))