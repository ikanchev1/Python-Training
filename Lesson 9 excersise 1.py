def get_user_data():
  """retrieves user data from the command line

  Returns:
    [dictionary] of the form:
      {
        "name" : "user_name",
        "height": "user heigth in meters",
        "weight": "user weight in kilograms"
      }
  """
  #name
  name = input("Enter your name: ")
  #weight
  W = float(input("Enter your weight in kilograms: ").replace(",","."))
  #height
  H = float(input("Enter your height in meters: ").replace(",","."))
  user_info = {
      'Name': name,
      'height': H,
      'weight': W,
  }
  return user_info

def calc_BMI(w,h):
  """calculates the BMI

  Arguments:
    w {[float]} -- [weight]
    h {[float]} -- [height]

  Returns:
    [float] -- [calculated BMI = w / (h*h)]
  """
  BMI = w/(h*h)
  return BMI

def calc_BMI_category(bmi):
  """Calculates the BMI category

  Arguments:
    bmi {[float]} -- [the bmi number index]

  Returns:
    [string] -- [bmi category]
  """
  if bmi <= 18.5:
    return "Underweight"
  elif bmi > 18.5 and bmi <= 24.9:
    return "Normal"
  elif bmi >= 25 and bmi <= 29.9:
    return "Overweight"
  elif bmi >= 30:
    return "Obesity"

def print_results(bmi_category):
  """[Prints the BMI category to the user ]

  Arguments:
    bmi_category {[string]} -- []
  """
  print(bmi_category)

def cm_to_meters(cm):
  """converts centimetres to meters

  Arguments:
    cm {[int]}

  Returns:
    [float]
  """
  pass

user_data = get_user_data()
bmi = calc_BMI(user_data["weight"],user_data["height"] )
bmi_category = calc_BMI_category(bmi)
print_results(bmi_category)
