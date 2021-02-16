import sys
from tests.number_tests import precedence

# Dictionary of all the functions
functions_to_test = {
    "precedence":precedence.testPrecedence,
}

def displayOptions():
    print('*'*100)
    print("You can test the functions by running:")
    print("py[/python3/python] test.py function_name")
    print("If you want to test more than one function at a time, enter the function names space-separated.")
    print('*'*100)
    print("The functions available for testing are: ")
    for index, function in enumerate(functions_to_test):
        print(f"{index+1:02d}. {function}")

def testFunction(function):
    return functions_to_test[function]
  
def valid(function):
    return function in functions_to_test

def main(functions):
    if not functions:
        displayOptions()
        return
    for function in functions:
        if valid(function):
            testFunction(function)()
        else:
            print(f"Error: '{function}' is not a valid function.")
            print("Please check the spelling and the list of available functions and try again!")
            



if __name__=="__main__":
    main(sys.argv[1:])