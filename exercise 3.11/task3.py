score = input("Enter your score: ")
score = float(score)

if score >= 0.9:
    print("Your grade is A")
elif score >= 0.8:
    print("Your grade is B")
elif score >= 0.7:
    print("Your grade is C")
elif score >= 0.6:
    print("Your grade is D")
else:
    print("You have failed, your grade is F")