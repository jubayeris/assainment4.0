def calculate_salary(hours, rate):
  

  if hours <= 40:
    salary = hours * rate
  else:
    salary = 40 * rate + (hours - 40) * 1.5 * rate
  return salary


def main():


  try:
    hours = int(input("Enter the number of hours worked: "))
    rate = float(input("Enter the rate per hour: "))
  except ValueError:
    print("Invalid input. Please enter a number for both the hours worked and the rate per hour.")
    exit()

  salary = calculate_salary(hours, rate)
  print("The salary is ", salary)


if __name__ == "__main__":
  main()