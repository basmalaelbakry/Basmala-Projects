customers = [
    "Ahmed", "Sara", "Omar", "Mona",
    "Ali", "Nour", "Youssef", "Hana",
    "Khaled", "Mariam", "Hassan", "Laila"
]

scores = [
    91, 45, 78, 66, 88, 30,
    72, 95, 51, 60, 84, 39
]

risk_levels = []

for name, score in zip(customers, scores):

    if score >= 85:
        risk = "High"

    elif score >= 60:
        risk = "Medium"

    else:
        risk = "Low"

    risk_levels.append(risk)

high_count = 0
medium_count = 0
low_count = 0

total_score = 0

for score, risk in zip(scores, risk_levels):

    total_score += score

    if risk == "High":
        high_count += 1

    elif risk == "Medium":
        medium_count += 1

    else:
        low_count += 1

average_score = total_score / len(scores)

best_index = 0
worst_index = 0

for i in range(1, len(scores)):

    if scores[i] < scores[best_index]:
        best_index = i

    if scores[i] > scores[worst_index]:
        worst_index = i



def report():


    print("\n========== CUSTOMER RISK REPORT ==========")

    print("Name", end="    ")
    print("Score", end="    ")
    print("Risk")

    print("------------------------------------------")

    for name, score, risk in zip(customers, scores, risk_levels):
        print(name, end="    ")
        print(score, end="    ")
        print(risk)

    print("\n=============== SUMMARY ================")

    print("High Risk:", high_count)
    print("Medium Risk:", medium_count)
    print("Low Risk:", low_count)

    print("Average Score:", format(average_score, ".2f"))

    print("Best Customer:", customers[best_index], end=" ")
    print("(", scores[best_index], ")")

    print("Worst Customer:", customers[worst_index], end=" ")
    print("(", scores[worst_index], ")")


while True:

    print("\n========== MENU ==========")
    print("1. Show All Customers")
    print("2. Search for a Customer")
    print("0. Exit")
    print("==========================")

    choice = input("Enter your choice: ")

    if choice == "1":
        report()

    elif choice == "2":

        search_name = input("Enter customer name: ")

        found = False

        for name, score, risk in zip(customers, scores, risk_levels):

            if name.lower() == search_name.lower():

                print("Name:", name)
                print("Score:", score)
                print("Risk:", risk)

                found = True
                break

        if found == False:
            print("Customer not found!")

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")


