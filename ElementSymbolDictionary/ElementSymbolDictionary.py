import enchant

d = enchant.Dict("en_UK")


##check the combination of atomic numbers against the dictionary
##if found, output the word and atomic number combination
def checkCombo(combo, elementSymbols, dictionary):
	
	symCombo = []

	for i in range(len(combo)):
		symCombo.append(elementSymbols[combo[i]])

	testWord = "".join(symCombo)

	if dictionary.check(testWord):
		return print(testWord + ",", combo)

	return 0


def addToCombo(combo):
	
	for i in range(len(combo)):
		if i == None:
			combo[i] = addedSymbol
	
	return combo


##extract elemental symbols and atomic numbers from txt and put into dictionary
input_file = open("elemental_symbols.txt", "r")

elementSymbols = {}

for line in input_file:
	
	line = line.replace("\n", "")
	valuePair = line.split(",")

	elementSymbols[int(valuePair[0])] = valuePair[1]

maxSearchLength = 2

##for i in range(1, maxSearchLength):
for j in range(1, (len(elementSymbols) + 1)):	
	combo = [0, 0]
	combo[0] = j
	
	for k in range(1, (len(elementSymbols) + 1)):					
		combo[1] = k

		checkCombo(combo, elementSymbols, d)