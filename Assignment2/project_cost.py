
def calculate_project_cost():

    # inputs
    team_members = int(input("Enter number of team members: "))
    months = int(input("Enter number of months: "))
    monthly_salary = float(input("Enter monthly salary: "))
    cloud_cost = float(input("Enter total cloud cost: "))


    # Calculate costs
    salary_cost = team_members * months * monthly_salary
    subtotal = salary_cost + cloud_cost
    vat = subtotal * 0.14
    total = subtotal + vat

    # results
    print(f"Salary Cost: {salary_cost:,.2f}")
    print(f"Subtotal: {subtotal:,.2f}")
    print(f"VAT: {vat:,.2f}")
    print(f"Total Project Cost: {total:,.2f}")


calculate_project_cost()
