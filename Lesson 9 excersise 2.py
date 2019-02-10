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
  flag = True
  while (flag):
      name = input("Enter your name: ")
      if(len(name)<2):
          print("Please enter name with at least 2 letters!")
      else:
          flag = False
  #weight
  flag = True
  while (flag):
      W = float(input("Enter your weight in kilograms: ").replace(",","."))
      if(W<5):
          print("You cannot be that light. Please enter actual weight between 5kg and 250kg!")
      elif(W>250):
          print("Wow you are heavy! Please enter actual weight between 5kg and 250kg!")
      else:
          flag = False
  
  #height
  flag = True
  while(flag):
      H_cm = float(input("Enter your height in centimeters: ").replace(",","."))
      if(H_cm<50):
          print("Too short. Please enter actual height between 50cm and 250cm!")
      elif(H_cm>250):
          print("Too high. Please enter actual height between 50cm and 250cm!")
      else:
          flag = False
  H = cm_to_meters(H_cm)
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
  meter = cm / 100.0;
  return meter

user_data = get_user_data()
bmi = calc_BMI(user_data["weight"],user_data["height"] )
bmi_category = calc_BMI_category(bmi)
print_results(bmi_category)
