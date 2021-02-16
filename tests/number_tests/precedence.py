def evaluate(expr):
    ans=input(f"{expr} = ")
    if ans==str(eval(expr)):
        print("Good job! Correct Answer!")
        return 1
    print("Oops! Incorrect Answer!")
    return 0

def testPrecedence():
    score=0
    print("Enter the expected values of these expressions")
    expressions = [
        "100-3*2**2+1",
        "100-(3*2)**2+1",
        "100-3*2**(2+1)",
        "100-(3*2)**(2+1)",
    ]
    score=0
    for e in expressions:
        score += evaluate(e)
    print(f"You got {score}/{len(expressions)} answers correct.")
        