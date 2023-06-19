def main():
    workhours = int(input('Enter your work hours: '))
    reg_hours = 40
    reg_rate = 18.25
    ov_rate = 27.78

   ##################################################
   # Code your program here
   ##################################################
    # overtime = workhours - reg_hours
    # overtime_wage = overtime * ov_rate
    # regular_wage = reg_hours * reg_rate
    # total_wage = regular_wage + overtime_wage
    overtime = workhours - reg_hours
    overtime_wage = ov_rate * overtime
    regular_wage = reg_rate * reg_hours
    total_wage = regular_wage + overtime_wage

    print("")
    print(f"Regular Charge: ${regular_wage}")
    print(f"Overtime Charge: ${overtime_wage:.2f}")
    print(f"Total wage : ${total_wage:.2f}")
    print("")

   ##################################################
   # Do not delete the return statement
   ##################################################
    return regular_wage, overtime_wage, total_wage


if __name__ == '__main__':
    main()
