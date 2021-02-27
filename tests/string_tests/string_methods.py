def evaluate(expr, answer):
    ans=input(expr).strip()
    s='aB-Ha-Op'
    try:
        if eval(ans)==eval(answer):
            print("Good job! Correct Answer!")
            print("*"*100)
            return 1
    except:
        pass
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
Write an expression to create a string which has the same letters as s but in lower-case.
""",
"""A string is stored in the variable s
The string is in the format dd-mm-yy
Write an expression to create a list that has the date, month and year part.
""",
"""
s="abcdef"
i = s.find('c')
What is the value stored in i?
"""
    ]
    answers = [
        "s.upper()",
        "s.lower()",
        "s.split('-')",
        "2"
    ]
    score=0
    for e,a in zip(expressions, answers):
        score += evaluate(e, a)
    print(f"You got {score}/{len(expressions)} answers correct.\n\n")
        

