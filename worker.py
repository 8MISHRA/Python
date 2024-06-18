class Worker(object):
    """
    Class to represent a worker at a company
    """
    def __init__(self, n, s, b):      
        self.lname = n
        self.ssn = s
        self.boss = b
    def __repr__(self):
        return str(self.__class__) +  '('+str(self.lname) + ',' + str(self.ssn) + ',' +str(self.boss) + ')'
        # return str(self.__class__) + str(self)
        

# # w = Worker("university", 123, None)
# p = Worker('divyansh', 'male', 'available')
# print(Worker.lname)