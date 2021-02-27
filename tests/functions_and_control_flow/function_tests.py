from tests.functions_and_control_flow import CODE_HERE
def check_odd_even():
    e=[20, 31, 122128, 74632689]
    a=["even", "odd", "even", "odd"]
    score=0
    for i in range(len(e)):
        score += CODE_HERE.check_odd_even(e[i])==a[i]
    print(f"You passed {score} out of {len(e)} test cases!")
    print("*"*100)

def check_divisibility():
    e=[[20, 10], [20, 15], [122128, 8], [111111,1111]]
    a=[True, False, True, False]
    score=0
    for i in range(len(e)):
        score += CODE_HERE.check_divisibility(e[i][0], e[i][1])==a[i]
    print(f"You passed {score} out of {len(e)} test cases!")
    print("*"*100)

def highest_multiple_of_3():
    e=[[3, 6, 9], [3, 6, 9, 100, 99], [100, 200, 400]]
    a=[9, 99, -1]
    score=0
    for i in range(len(e)):
        score += CODE_HERE.highest_multiple_of_3(e[i])==a[i]
    print(f"You passed {score} out of {len(e)} test cases!")
    print("*"*100)

def check_grade():
    e=[99, 90, 89, 85, 65, 79, 42, 40, 39, 0, 100]
    a=list("AABBCCDDEEA")
    score=0
    for i in range(len(e)):
        score += CODE_HERE.check_grade(e[i])==a[i]
    print(f"You passed {score} out of {len(e)} test cases!")
    print("*"*100)

def check_prime():
    e=[63, 72899, 99999999, 104717 , 7607]
    a=[False, False, False, True, True]
    score=0
    for i in range(len(e)):
        score += CODE_HERE.check_prime(e[i])==a[i]
        # print(e[i],a[i], CODE_HERE.check_prime(e[i])==a[i])
    print(f"You passed {score} out of {len(e)} test cases!")
    print("*"*100)

def find_primes():
    e=[[271, 72899, 2, 17, 104729], [6, 4, 1024, 823543]]
    a=[[271, 2, 17, 104729], []]
    score=0
    for i in range(len(e)):
        score += CODE_HERE.find_primes(e[i])==a[i]
        print(CODE_HERE.find_primes(e[i]), a[i])
    print(f"You passed {score} out of {len(e)} test cases!")
    print("*"*100)