def evaluate(expr, answer):
    ans=input(expr).strip(" \"'")
    if ans==answer:
        print("Good job! Correct Answer!")
        print("*"*100)
        return 1
    print("Oops! Incorrect Answer!")
    print("*"*100)
    return 0

def evaluate2(e, a):
    ans=input(e).strip(" \"'")
    s = [1, 4.5, "a string", [7, 8, 9]]
    try:
        if 's' in ans and eval(ans)==a:
            print("Good job! Correct Answer!")
            print("*"*100)
            return 1
    except:
        pass
    print("Oops! Incorrect Answer!")
    print("*"*100)
    return 0
    

def testLists():
    score=0

    expressions = [
"""s = [1, 4.5, "a string", [7, 8, 9]]
Write an expression in the form of s[...] to extract 8 from s.
""",
"""s = [1, 4.5, "a string", [7, 8, 9]]
c=s[3][-3]
What is the value stored in c after this?
""",
"""s = [1, 4.5, "a string", [7, 8, 9]]
c=s[-2][2]
What is the value stored in c after this?
""",
"""s=['b', 'abc', 'abcde']
s.sort()
c=len(s[1])
What is the value stored in c after this?
""",
    ]
    answers = [
        8,
        "7",
        "s",
        "5",
    ]
    score=0
    score += evaluate2(expressions[0], answers[0])
    for e,a in zip(expressions[1:], answers[1:]):
        score += evaluate(e, a)
    print(f"You got {score}/{len(expressions)} answers correct.\n\n")
        

