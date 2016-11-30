#!/usr/bin/env python

#Function returnNGrams 
#If speed becomes issue then can try sets or bisecting. to bisect will need to modify to be a sorted list

def datafileGenerator(name, sep='\t'):
	"Read key,value pairs from file."
	for line in file(name):
		yield line.split(sep)

def datafileIterator(name, sep='\t'):
	"Read key,value pairs from file."
	return [line.split(sep) for line in file(name)]

#returns dictionary of words as keys with frequency rankings as values
def returnNGrams(wordList):
	wordList = [word.lower() for word in wordList]
	position = 1
	returnDict = {}
	frequencyList = []

	for item in datafileGenerator('ngrams/count_1w.txt'):
		frequencyList.append(item[0])

	for frequencyItem in frequencyList:
		for word in wordList:
			if frequencyItem == word:
				returnDict[word] = position
				wordList.remove(word)
		position+=1
	return returnDict

def findInPersonalWordList(wordList, mustHaveEtymology=True):
	import json
	match =[]
	wordList = [word.lower() for word in wordList]
	with open('wordList3.json') as personalWordListFile:
		personalWordListJson = json.load(personalWordListFile)
		match = [personalWordItem for personalWordItem in personalWordListJson 
			if ((personalWordItem['Word'] in wordList) and 
				(not mustHaveEtymology or personalWordItem['Etymology']))]
		# for personalWord in personalWordListJson:
		# 	print personalWord['Word']
		return match


#If called directly, run the function with the sys.argv as the arguments
if __name__ == "__main__":
    import sys
    import pprint
    pprint.pprint(returnNGrams(sys.argv[1:]))

