def evaluate(expr, answer, n):
    ans=input(expr).lower().strip()
    try:
        if eval(ans)==answer:
            print("Good job! Correct Answer!")
            print("*"*100)
            return 1
        else:
            print("Oops! Incorrect Answer!")
            print("*"*100)
            return 0
    except:
        print("Except")
        print("Oops! Incorrect Answer!")
        print("*"*100)
        return 0

def testFormatting():
    score=0
    print("You can use f-strings or string formatting for the following questions.")
    print("The answer is NOT case sensitive.")
    expressions = [
"""An integer is stored in a variable n
Write an expression to create a string which is of the format:
The answer is <n>
Where <n> is the value stored in n
""",
"""A float is stored in a variable n
Write an expression to create a string which is of the format:
The answer is <n>
Where <n> is the value stored in n, UPTO 3 DECIMAL PLACES.
""",
    ]
    answers = [
        "the answer is 1",
        "the answer is 1.333",
    ]
    ns=[1,4/3]
    score=0
    for e,a,n in zip(expressions, answers, ns):
        score += evaluate(e, a, n)
    print(f"You got {score}/{len(expressions)} answers correct.\n\n")
        

