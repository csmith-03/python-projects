# Name : Channing Smith
# working_time.py
#
# Problem: In this function, the user will input the number of teams,
# number of employees, and working time. Then, the output will be the
# total hours/ minutes worked, and total hours/ minutes worked for
# all teams combined.
#
# The inputs will be the number of teams, number of employees,
# and amount of hours and minutes worked.
#
# The outputs will be the amount of hours and minutes worked by
# each employee, along with the total team time, and finally,
# the total time for all teams.
#
# The step-by-step list of what the program will do is listed
# below throughout the code.
#
# Certification of Authenticity:
#   I certify that this assignment is entirely my own work, but I
#   received help from the Tutoring Center and Anthony.
def working_time():
    print("This program will calculate the total days, hours, and "
          "minutes worked for each team and individual employee.")
    # user inputs number of teams
    number_teams = eval(input("Enter the number of teams:"))
    # starts grand hours/minutes at zero
    grand_total_hours = 0
    grand_total_minutes = 0
    # this loop is the outer loop for looping the team number and asking
    # for number of employees
    for j in range(number_teams):
        number_employees = eval(input("Enter the number of employees "
                                      "for team " + str(j + 1 ) + ":" ))
        # starts total hours/minutes at zero for inner loop
        total_hours = 0
        total_minutes = 0
        # inner loop for employees and asking for working time
        for i in range(number_employees):
            number_hours = int(input("Enter total hours worked for "
                                     "employee " + str(i + 1) + ":"))
            minutes_worked = int(input("Enter minutes worked for "
                                       "employee " + str(i + 1) + ":"))
            number_hours= number_hours + (minutes_worked // 60)
            minutes_worked = (minutes_worked % 60)
            print("Employee" , i + 1 , ":" , number_hours , "hours" ,
                  minutes_worked , "minutes ")
            total_hours += number_hours
            total_minutes += minutes_worked
        # calculates total hours/minutes for each team
        total_hours = total_hours + (total_minutes // 60)
        total_minutes = total_minutes % 60
        #calculates grand total hours/minutes for teams combined
        grand_total_hours += total_hours
        grand_total_minutes += total_minutes
        print("-" * 30)
        # prints team total time after each teams employee is complete
        print("Team" , j + 1 , "total time:" , total_hours , "hours" ,
              total_minutes , "minutes")
        print("-" * 30)
    # calculates grand total hours for days, hours, and minutes
    grand_total_hours = grand_total_hours + (grand_total_minutes // 60)
    grand_total_minutes = grand_total_minutes % 60
    grand_total_days = (grand_total_hours // 24)
    grand_total_hours = grand_total_hours % 24
    # prints total time for all teams combined
    print("The total of time for all teams is:" ,
          grand_total_days , "days",  grand_total_hours ,
          "hours" , grand_total_minutes , "minutes" )
    print("-" * 30)

def main():
    working_time()
main()

