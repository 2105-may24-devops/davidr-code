import unittest

# write a method that takes in a a phone_number as a string
# if the string contains letters it is invalid
# if a strig does not have 10 digits it is invalid
# any other chracter should be ignored

def isphone_number(phone_number: str):
    isValid = True
    justDigits = ""

    # If the string is alphanumeric then it is invalid
    if (phone_number.isalnum()): isValid = False
    else:
        # Make a new string just from the numeric chars in the phone number
        justDigits = justDigits.join(char for char in phone_number if char.isnumeric())
        
        if (len(justDigits) != 10): isValid = False

    return isValid


########################### TESTS ##############################################################
class TestMethods(unittest.TestCase):

    def test_phone_1(self):
        valid_number = isphone_number('555-555-5555')
        self.assertEquals(valid_number,True)
        
    def test_phone_2(self):
        valid_number = isphone_number('555!555 5555')
        self.assertEquals(valid_number,True)
    
    def test_phone_3(self):
        valid_number = isphone_number('5b5-5a5-5555')
        self.assertEquals(valid_number,False)
    
    def test_phone_4(self):
        valid_number = isphone_number('555-5a5-5555')
        self.assertEquals(valid_number,False)
    
    def test_phone_5(self):
        valid_number = isphone_number('555-555-555')
        self.assertEquals(valid_number,False)

    def test_phone_6(self):
        valid_number = isphone_number('5555-5555-5555')
        self.assertEquals(valid_number,False)

    

if __name__ == '__main__':
    unittest.main()