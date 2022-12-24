#Natasha Sanchez
#11/23/22
#Sanchez-HealthCalculator.py
#This program will allow you to calculate a person's Body Mass Index (BMI). 
#It will inform you if the person is underweight, normal, overweight, or obese.
#In addition, this program will calculate the person's heart rate at varying levels of exercise intensity.


print ('Please enter the following values for the user . . .')

def determine_BMI (height, weight):
    height = float(height)
    weight = float(weight)

    weight_kilograms = (weight * .453592)
    height_meters = (height * .0254) * (height * .0254)
    bmi = weight_kilograms / height_meters
    return bmi

def karvonen_formula(age, resting_hr, intensity):
    karvonen = (((220 - age) - resting_hr) * intensity) + resting_hr
    return karvonen

height = float(input('Height in inches: '))
weight = float(input('Weight in pounds: '))
age = int(input('Current age: '))
resting_hr = int(input('Resting Heart rate: '))
print ('\nResults . . .')

weight_kilograms = (weight * .453592)
height_meters = (height * .0254) * (height * .0254)
bmi = weight_kilograms / height_meters
if bmi < 18.5:
        print ('Your BMI is {}'.format(round(bmi,2)), '-- Uderweight')
elif bmi < 25:
        print ('Your BMI is {}'.format(round(bmi,2)),'-- Normal Weight')
elif bmi < 30:
        print ('Your BMI is {}'.format(round(bmi,2)), '-- Overweight')
else: print ('Obese')

print ('\nExercise Intensity Heart Rates: ')
print ('Intensity\tMax Heart Rate\n')

intensity = .50
for i in range(10):
    karvonen = karvonen_formula(age, resting_hr, intensity)
    print('{:.2f}\t\t{}'.format(intensity,int(karvonen)))
    intensity +=.05
