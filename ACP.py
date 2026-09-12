print(" Welcome Swimming Pool Checker ")
print(" Answer 3 questions to check if you can swim in specific swimming pools ")

age = int(input(" What is your age? "))
can_swim = input(" Can you swim 25 meters? (Y/N) ")
adult_here = input(" Is an adult with you? (Y/N) ")

print()
print(" Entry Discision ")
print("-" * 32)

if age < 4:
    print("You are a toddler, use the toddler pool with an adult")

elif age < 12:
    print("You are a child, use the main pool with an adult")

elif age < 18:
    print("You are a teenager, you can use the main pool alone if you can swim")

else:
    print("You are an adult, you can use all pools")

if can_swim != "Y" and can_swim != "N":
    print("Input error")
    swim_known = False
else:
    swim_known = True
    
if adult_here != "Y" and adult_here != "N":
    print("Input error")
    adult_known = False
else:
    adult_known = True


if can_swim == "Y" and adult_here == "Y":
    print("Deep pool allowed")


if age < 12 or can_swim == "N":
    print("Warning: Use the shallow end")


if adult_known == True and adult_here == "N":
    print("Lifeguard reminder: There is no adult with you")


if swim_known == False or adult_known == False:
    print("Cannot decide")
elif age < 4:
    print("Toddler pool only")
elif age < 12:
    print("Child: Adult required")
elif age < 18:
    if can_swim == "Y":
        print("Teen: Main pool allowed")
    else:
        print("Teen: Swimming not allowed")
else:
    print("Adult: All pools open")