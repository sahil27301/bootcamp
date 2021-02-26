def evaluate(expr, answer):
    ans=input(expr).strip()
    s='aB-Ha-Op'
    try:
        if eval(ans)==eval(answer):
            print("Good job! Correct Answer!")
            print("*"*100)
            return 1
        else:
            print("Oops! Incorrect Answer!")
            print("*"*100)
            return 0
    except:
        print("Oops! Incorrect Answer!")
        print("*"*100)
        return 0

def testMethods():
    score=0
    expressions = [
"""A string is stored in the variable s
Write an expression to create a string which has the same letters as s but in upper-case.
""",
"""A string is stored in the variable s
Write an expression to create a string which has the same letters as s but in upper-case.
""",
"""A string is stored in the variable s
The string is in the format dd-mm-yy
Write an expression to create a list that has the date, month and year part.
""",
    ]
    answers = [
        "s.upper()",
        "s.lower()",
        "s.split('-')",
    ]
    score=0
    for e,a in zip(expressions, answers):
        score += evaluate(e, a)
    print(f"You got {score}/{len(expressions)} answers correct.\n\n")
        

