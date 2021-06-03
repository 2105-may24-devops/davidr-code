import unittest
import re
# write a function that convernts a word into different casings
# assume no spacing
# snake_case example fire_truck OR Fire_Truck  (capitalization does not matter)
# camelCase example fireTruck
# PascalCase example FireTruck
# kebab-case example fire-truck

# this is an edit
# casing('registeredUser','camelCase','kebab-case') -> registered-user
def casing(word, initial, target):
    words = []
    newCase = ""

    # WORD SEPARATION SEGMENT
    # Find all caps if a word is in camelCase or PascalCase 
    if (initial == "camelCase" or initial == "PascalCase"):
        res = re.findall('([A-Z])', word)
        cutoff = 0

        # Iterate through every capital letter we found and split word into substrings
        # For each iteration, remove the current wordSegment from word
        for cap in res:
            cutoff = word.find(cap)
            wordSegment = word[:cutoff]
            if (wordSegment != ""): words.append(wordSegment)
            word = word[cutoff:]

        # Don't forget the last word
        words.append(word)
    elif (initial == "kebab-case"):
        words = word.split("-")
    elif (initial == "snake_case"):
        words = word.split("_")
    else:
        print("Invalid initial case")

    # WORD RECASING SEGMENT
    # For camelCase make the first word lowercase and each subsequent word start with a capital
    if (target == "camelCase"):
        for i, word in enumerate(words):
            if (i == 0): newCase += word.lower()
            else: newCase += word.capitalize()
    # For PascalCase make each word start with a capital
    elif (target == "PascalCase"):
        for word in words:
            newCase += word.capitalize()
    elif (target == "kebab-case"):
        newCase = '-'.join([word.lower() for word in words])
    elif (target == "snake_case"):
        newCase = '_'.join(words)
    else:
        print("Invalid target case")

    return newCase


########################### TESTS ##############################################################
class TestMethods(unittest.TestCase):

    def test_camel_to_Pascal(self):
        result = casing(word='redSphere',initial='camelCase',target='PascalCase')
        self.assertEqual(result,'RedSphere')

    def test_camel_to_kebab(self):
        result = casing('redSphere','camelCase','kebab-case')
        self.assertEqual(result,'red-sphere')

    def test_camel_to_snake(self):
        result = casing('redSphere','camelCase','snake_case')
        self.assertEqual(result,'red_Sphere')


    def test_Pascal_to_snake(self):
        result = casing('GreenApple','PascalCase','snake_case')
        self.assertEqual(result,'Green_Apple')

    def test_Pascal_to_kebab(self):
        result = casing('GreenApple','PascalCase','kebab-case')
        self.assertEqual(result,'green-apple')

    def test_Pascal_to_camel(self):
        result = casing('GreenApple','PascalCase','camelCase')
        self.assertEqual(result,'greenApple')
    

    def test_kebab_to_camel(self):
        result = casing('green-apple','kebab-case','camelCase')
        self.assertEqual(result,'greenApple')

    def test_kebab_to_Pascal(self):
        result = casing('green-apple','kebab-case','PascalCase')
        self.assertEqual(result,'GreenApple')   

    def test_kebab_to_snake(self):
        result = casing('green-apple','kebab-case','snake_case')
        self.assertEqual(result,'green_apple') 
    

    def test_snake_to_camel(self):
        result = casing('green_apple','snake_case','camelCase')
        self.assertEqual(result,'greenApple') 
    
    def test_snake_to_Pascal(self):
        result = casing('green_apple','snake_case','PascalCase')
        self.assertEqual(result,'GreenApple') 
    
    def test_snake_to_kebab(self):
        result = casing('green_apple','snake_case','kebab-case')
        self.assertEqual(result,'green-apple') 

if __name__ == '__main__':
    print(casing("a-really-long-kebab-yummy", "kebab-case", "PascalCase"))
    unittest.main()

    