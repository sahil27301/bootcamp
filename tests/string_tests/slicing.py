def evaluate(expr, answer):
    ans=input(expr).strip()
    if ans==answer:
        print("Good job! Correct Answer!")
        print("*"*50)
        return 1
    print("Oops! Incorrect Answer!")
    print("*"*50)
    return 0

def evaluateSlice(e, a):
    s='abcde'
    ans=input(e).strip()
    try:
        if 's' in ans and eval(ans)==a:
            print("Good job! Correct Answer!")
            print("*"*50)
            return 1
        else:
            print("Oops! Incorrect Answer!")
            print("*"*50)
            return 0
    except:
        print("Oops! Incorrect Answer!")
        print("*"*50)
        return 0


def testSlices():
    score=0
    print("Enter the expected values of these expressions")
    expressions = [
"""s = 'abcde'
c=s[2:4]
What is the value stored in c after this?
""",
"""s = 'abcde'
c=s[2:]
What is the value stored in c after this?
""",
"""s = 'abcde'
c=s[-2:]
What is the value stored in c after this?
""",
"""s = 'abcde'
c=s[:-2]
What is the value stored in c after this?
""",
"""s = 'abcde'
c=s[1:4:2]
What is the value stored in c after this?
""",
    ]
    answers = [
        "cd",
        "cde",
        "de",
        "abc",
        "bd",
    ]
    score=0
    for e,a in zip(expressions, answers):
        score += evaluate(e, a)
    expressions2 = [
"""
s = 'abcde'
Write an expression in the form of s[x:y:z],
such that it yields 'ace'
""",
"""
s = 'abcde'
Write an expression in the form of s[x:y:z],
such that it yields 'edcba'
""",
"""
s = 'abcde'
Write an expression in the form of s[x:y:z],
such that it yields 'ad'
""",
    ]
    answers2=[
        "ace",
        "edcba",
        "ad",
    ]
    for e,a in zip(expressions2, answers2):
        score += evaluateSlice(e, a)
    print(f"You got {score}/{len(expressions)+len(expressions2)} answers correct.\n\n")
        


