def evaluate(expr):
    ans=input(f"{expr} = ")
    if ans==str(eval(expr)):
        print("Good job! Correct Answer!")
        print("*"*50)
        return 1
    print("Oops! Incorrect Answer!")
    print("*"*50)
    return 0

def testPrecedence():
    score=0
    print("Enter the expected values of these expressions")
    expressions = [
        "100-3*2**2+1",
        "100-(3*2)**2+1",
        "100-3*2**(2+1)",
        "100-(3*2)**(2+1)",
        "100-16//3**2",
        "5*5/5*5",
    ]
    score=0
    for e in expressions:
        score += evaluate(e)
    print(f"You got {score}/{len(expressions)} answers correct.\n\n")
        