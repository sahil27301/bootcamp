def evaluate(expr, answer):
    ans=input(expr).strip()
    if ans==answer:
        print("Good job! Correct Answer!")
        print("*"*100)
        return 1
    print("Oops! Incorrect Answer!")
    print("*"*100)
    return 0

def testIndices():
    score=0
    print("Enter the expected values of these expressions")
    expressions = [
"""s = 'abcde'
c=s[1]
What is the value stored in c after this?
""",
"""s='abcde'
c=s[-1]
What is the value stored in c after this?
""",
"""s='abcde'
What is the forward index of 'c' in s?
""",
"""s='abcde'
What is the reverse indec of 'c' in s?
""",
    ]
    answers = [
        "b",
        "e",
        "2",
        "-3",
    ]
    score=0
    for e,a in zip(expressions, answers):
        score += evaluate(e, a)
    print(f"You got {score}/{len(expressions)} answers correct.\n\n")
        

