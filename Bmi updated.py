print('Hello')
name = input('What is your name:\n').strip()
print(f'Hello {name}')
print('I am about to calculate your Body Mass Index (BMI)')
weight = float(input('What is your weight (kg): '))
height = float(input('What is your height (m): '))
BMI = weight / (height ** 2)
print(f'Your BMI is {BMI}')

if BMI < 18.5:
    print('Underweight.')
elif BMI >= 18.5 and BMI <= 25.5:
    print('Ideal BMI')
elif BMI >= 25.6 and BMI <= 30.5:
    print('Slightly obese')
elif BMI >= 30.6 and BMI <= 34.5:
    print('Obesity stage 1')
elif BMI >= 34.6 and BMI <= 39.5:
    print('Obesity stage 2')
else:
    print('Obesity stage 3')