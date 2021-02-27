import sys
from tests.number_tests import precedence, binary
from tests.variable_tests import variables
from tests.string_tests import indexing, slicing, string_methods,string_formatting
from tests.list_tests import list_methods
from tests.sets_dicts_test import sets_and_dicts
from tests.boolean_tests import bools
from tests.functions_and_control_flow import function_tests

# Dictionary of all the functions
functions_to_test = {
    "precedence":precedence.testPrecedence,
    "binary":binary.testBinary,
    "variable":variables.testVariables,
    "indexing":indexing.testIndices,
    "slicing":slicing.testSlices,
    "string_methods":string_methods.testMethods,
    "formatting":string_formatting.testFormatting,
    "lists":list_methods.testLists,
    "dictionaries_sets":sets_and_dicts.testSets,
    "booleans":bools.testBools,
    "check_odd_even":function_tests.check_odd_even,
    "check_divisibility":function_tests.check_divisibility,
    "check_grade":function_tests.check_grade,
    "check_prime":function_tests.check_prime,
    "find_primes":function_tests.find_primes,
    "highest_multiple_of_3":function_tests.highest_multiple_of_3,
}

def displayOptions():
    print('*'*100)
    print("You can test the functions by running:")
    print("py[/python/python3 test.py function_name")
    print("If you want to test more than one function at a time, enter the function names space-separated.")
    print('*'*100)
    print("The functions available for testing are: ")
    for index, function in enumerate(functions_to_test):
        print(f"{index+1:02d}. {function}")
    print("To test all functions, enter:")
    print("py[/python/python3 test.py all")

def testFunction(function):
    return functions_to_test[function]
  
def valid(function):
    return function in functions_to_test

def main(functions):
    if "all" in functions:
        functions=[i for i in functions_to_test]
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