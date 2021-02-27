def evaluate(expr, answer):
    ans=input(expr).strip()
    if ans==answer:
        print("Good job! Correct Answer!")
        print("*"*100)
        return 1
    print("Oops! Incorrect Answer!")
    print("*"*100)
    return 0

def testSets():
    score=0
    print("Enter the expected values of these expressions")
    expressions = [
"""
s=dict()
s[1]=[1, 2, 3]
s[2]=4
s[1]=5
c=len(s)
What is the value stored in c after this?
""",
"""s = {1, 2, 3, 2, 3, 3, 1, 4, 2}
c=len(s)
What is the value stored in c after this?
""",
"""s1={1, 2, 3}
s2={3, 4, 5}
c=len(s1.union(s2))
What is the value stored in c after this?
""",
"""s1={1, 2, 3}
s2={3, 4, 5}
c=len(s1.intersection(s2))
What is the value stored in c after this?
""",
"""s1={1, 2, 3}
s2={3, 4, 5}
c=len(s1.symmetric_difference(s2))
What is the value stored in c after this?
""",
    ]
    answers = [
        "2",
        "4",
        "5",
        "1",
        "4",
    ]
    score=0
    for e,a in zip(expressions, answers):
        score += evaluate(e, a)
    print(f"You got {score}/{len(expressions)} answers correct.\n\n")
        

