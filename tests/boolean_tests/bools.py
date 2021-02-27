def evaluate(expr, answer):
    ans=input(expr).strip()
    if ans==answer:
        print("Good job! Correct Answer!")
        print("*"*100)
        return 1
    print("Oops! Incorrect Answer!")
    print("*"*100)
    return 0

def testBools():
    score=0
    print("Answer True or False for the following questions.")
    expressions = [
"""
c = 1>2 or 1<2
What is the value stored in c after this?
""",
"""c = 1>2 and 1<2
What is the value stored in c after this?
""",
"""a = [1, 2, 3]
c = 2 in a
What is the value stored in c after this?
""",
"""a = [[1, 2, 3]]
c = 2 in a
What is the value stored in c after this?
""",
    ]
    answers = [
        "True",
        "False",
        "True",
        "False",
    ]
    score=0
    for e,a in zip(expressions, answers):
        score += evaluate(e, a)
    print(f"You got {score}/{len(expressions)} answers correct.\n\n")
        

