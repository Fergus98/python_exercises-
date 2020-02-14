def gradeCalc(number1, number2):
	answer = number1 + number2
	answer /= 75
	return answer

firstNumber = int(input("What is your Homework Grade?"))
secondNumber = int(input("What is your assessment grade?"))
gradeNumber = gradeCalc(firstNumber, secondNumber)

print(gradeNumber)
