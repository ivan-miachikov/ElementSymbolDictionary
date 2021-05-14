import sys
import enchant
d = enchant.Dict("en_UK")

maxSearchLength = 11 #22 letters is the longest word likely to be encountered in general reading
output = open("element_symbol_words.txt", "w")

##check the combination of atomic numbers against the dictionary
##if found, output the word and atomic number combination
def checkCombo(combo, elementSymbols, dictionary):
	
	symCombo = []

	for i in range(len(combo)):
		symCombo.append(elementSymbols[combo[i]])

	testWord = "".join(symCombo)

	if dictionary.check(testWord):
		outputString = testWord + "," + str(combo) + "\n"
		print(outputString)
		return output.write(outputString)

	return 0


##extract elemental symbols and atomic numbers from txt and put into dictionary
input_file = open("elemental_symbols.txt", "r")

elementSymbols = {}

for line in input_file:
	
	line = line.replace("\n", "")
	valuePair = line.split(",")

	elementSymbols[int(valuePair[0])] = valuePair[1]


##main combination creation code
for comboLen in range(1, maxSearchLength + 1) :
	
	combo =[None] * comboLen
	sym = 1

	for i in range(comboLen):
		combo[i] = sym
	
	while combo[0] != 119:
		checkCombo(combo, elementSymbols, d)

		combo[-1] += 1

		combo = combo[::-1]

		for x in range(len(combo)):
			if combo[-1] == 119:
				break
			
			elif combo[x] == 119:
				combo[x] = 1
				combo[x+1] += 1
		
		combo = combo[::-1]

output.close()