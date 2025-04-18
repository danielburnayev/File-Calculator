import math

def equationReader(fileWithEquation):
	equationFile = open(fileWithEquation)
	operation_dict = {"^": 3, "*": 2, "/": 2, "+": 1, "-": 1}
	answer = ""
	allProblemsList = equationFile.readlines()
	
	for line in range(len(allProblemsList)):
		problem = allProblemsList[line]
		problemInList = []
		prevOperatorLoc = 0
		for i in range(len(problem)):
			if i > 0 and problem[i] in operation_dict:
				problemInList.append(problem[prevOperatorLoc : i])
				problemInList.append(problem[i])
				prevOperatorLoc = i + 1
			if i == len(problem) - 1:
				problemInList.append(problem[prevOperatorLoc : i])
		
		while len(problemInList) >= 3:
			highestOperatorValue = 0
			pieceOfEquation = []
			operatorIndex = -1
			parenthesisAdder = 0
		
			for index in range(1, len(problemInList), 2):
				if operation_dict[problemInList[index]] > highestOperatorValue:
					highestOperatorValue = operation_dict[problemInList[index]]
					pieceOfEquation = [problemInList[index - 1], problemInList[index], problemInList[index + 1]]
					operatorIndex = index
					
			del problemInList[operatorIndex - 1]
			del problemInList[operatorIndex - 1]
			del problemInList[operatorIndex - 1]
			
			partAnswer = str(doOperation(pieceOfEquation))
			problemInList.insert(operatorIndex - 1, partAnswer)
		
		answer += problem[0 : len(problem) - 1] + "=" + problemInList[0] + "\n"
	
	answerFile = open(fileWithEquation[0 : len(fileWithEquation) - 4] + " answers.txt", "w")
	answerFile.write(answer)
	answerFile.close()
	
def doOperation(equation):
	if equation[0][-1] == "!":
		equation[0] = math.factorial(int(equation[0][0 : -1]))
	if equation[2][-1] == "!":
		equation[2] = math.factorial(int(equation[2][0 : -1]))
	
	if equation[1] == "^":
		return float(equation[0]) ** float(equation[2])
	elif equation[1] == "*":
		return float(equation[0]) * float(equation[2])
	elif equation[1] == "/":
		return float(equation[0]) / float(equation[2])
	elif equation[1] == "+":
		return float(equation[0]) + float(equation[2])
	elif equation[1] == "-":
		return float(equation[0]) - float(equation[2])

if __name__ == "__main__":
	import sys
	equationReader(sys.argv[1])
	
	
	
	