def evaluate(expr, answer):
    ans=input(expr)
    if ans==answer:
        print("Good job! Correct Answer!")
        print("*"*50)
        return 1
    print("Oops! Incorrect Answer!")
    print("*"*50)
    return 0

def testVariables():
    score=0
    print("Enter the expected values of these expressions")
    expressions = [
"""a=5
b=7
c=a+b-a*b//2
What is the value stored in c after this?
""",
"""a=5
b=7
a += 1
b -= 2
a //= 3
c=a+b-a*b//2
What is the value stored in c after this?
""",
"""b=5
b-=-5
What is the value stored in b after this?
""",
"""b=5
b%=3
What is the value stored in b after this?
""",
    ]
    answers = [
        "-5",
        "2",
        "10",
        "2",
    ]
    score=0
    for e,a in zip(expressions, answers):
        score += evaluate(e, a)
    print(f"You got {score}/{len(expressions)} answers correct.\n\n")
        
