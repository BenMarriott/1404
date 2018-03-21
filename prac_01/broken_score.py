score = float(input("Enter score: "))
while 0 > score > 100:
    float(input("Invalid number - please re-enter: "))
if score >= 90:
        print("Excellent")
elif score >= 50:
        print("Passable")
else:
    print("Bad")
