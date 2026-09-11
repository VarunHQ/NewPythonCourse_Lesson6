# Smart School day planner

print("Welcome to the Best School Day Planner! \n")
print("Answer 3 quick questions to get your complete school day schedule! \n")

day = input("What day of the week is it for you? ( Monday to Sunday ): ").strip().capitalize()
weather = input("What kind of weather is it like today? ( Sunny / Rainy / Cloudy ) ").strip().lower()
homework = input("Is your homework done? ( Yes / No ): ").strip().lower()

print()
print(f" === Your plan for {day} === ")
print(" - " * 35)
