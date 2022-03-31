print("enter weight")
weight = int(input( ))
print("enter height")
height = float(input( ))
bmi = weight / (height**2)
print(bmi)
while bmi:
  if bmi < 18.5:
    print('underweight')
    break
  elif bmi >=18.5 and bmi < 25:
    print("normal")
    break
  elif bmi >=25 and bmi < 30:
    print("overweight")
    break
  else:
    print('obesity')
    break