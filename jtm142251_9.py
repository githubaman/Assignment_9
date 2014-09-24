#!/usr/bin/python
import re
dict={}
totalNoOfBehaviours=7
happy=0
sad=0
angry=0
sarcastic=0
surprised=0
crook=0
neutral=0

happyPercent=0
angryPercent=0
sadPercent=0
surprisedPercent=0
crookPercent=0
neutralPercent=0
sarcasticPercent=0

f = open('content.txt', 'rU')
for line in f:     	
		user=line[0]			## iterates over the lines of the file
		match= re.search(r':\)', line)
		if match:
			print match.group() 
			if user == 'A':
				dict['A']='happy' 
			elif user == 'B':
				dict['B']='happy' 
			elif user == 'C':
				dict['C']='happy' 
			elif user == 'D':
				dict['D']='happy' 
			elif user == 'E':
				dict['E']='happy' 
			elif user == 'F':
				dict['F']='happy' 
			elif user == 'G':
				dict['G']='happy' 
			elif user == 'H':
				dict['H']='happy' 
			elif user == 'I':
				dict['I']='happy' 
			elif user == 'J':
				dict['J']='happy' 
			elif user == 'K':
				dict['K']='happy' 
			elif user == 'L':
				dict['L']='happy' 
			elif user == 'M':
				dict['M']='happy' 
			elif user == 'N':
				dict['N']='happy' 
			elif user == 'O':
				dict['O']='happy' 
			elif user == 'P':
				dict['P']='happy' 
			elif user == 'Q':
				dict['Q']='happy' 
			elif user == 'R':
				dict['R']='happy'
			elif user == 'S':
				dict['S']='happy' 
			elif user == 'T':
				dict['T']='happy'
			elif user == 'U':
				dict['U']='happy'
			elif user == 'V':
				dict['V']='happy'
			elif user == 'W':
				dict['W']='happy'
			elif user == 'X':
				dict['X']='happy'
			elif user == 'Y':
				dict['Y']='happy'
			elif user == 'Z':
				dict['Z']='happy'
		match= re.search(r':D', line)
		if match:
			print match.group() 
			if user == 'A':
				dict['A']='happy' 
			elif user == 'B':
				dict['B']='happy' 
			elif user == 'C':
				dict['C']='happy' 
			elif user == 'D':
				dict['D']='happy' 
			elif user == 'E':
				dict['E']='happy' 
			elif user == 'F':
				dict['F']='happy' 
			elif user == 'G':
				dict['G']='happy' 
			elif user == 'H':
				dict['H']='happy' 
			elif user == 'I':
				dict['I']='happy' 
			elif user == 'J':
				dict['J']='happy' 
			elif user == 'K':
				dict['K']='happy' 
			elif user == 'L':
				dict['L']='happy' 
			elif user == 'M':
				dict['M']='happy' 
			elif user == 'N':
				dict['N']='happy' 
			elif user == 'O':
				dict['O']='happy' 
			elif user == 'P':
				dict['P']='happy' 
			elif user == 'Q':
				dict['Q']='happy' 
			elif user == 'R':
				dict['R']='happy'
			elif user == 'S':
				dict['S']='happy' 
			elif user == 'T':
				dict['T']='happy'
			elif user == 'U':
				dict['U']='happy'
			elif user == 'V':
				dict['V']='happy'
			elif user == 'W':
				dict['W']='happy'
			elif user == 'X':
				dict['X']='happy'
			elif user == 'Y':
				dict['Y']='happy'
			elif user == 'Z':
				dict['Z']='happy'
		match= re.search(r'X-\(', line)
		if match:
			print match.group() 
			if user == 'A':
				dict['A']='Angry' 
			elif user == 'B':
				dict['B']='Angry' 
			elif user == 'C':
				dict['C']='Angry' 
			elif user == 'D':
				dict['D']='Angry' 
			elif user == 'E':
				dict['E']='Angry' 
			elif user == 'F':
				dict['F']='Angry' 
			elif user == 'G':
				dict['G']='Angry' 
			elif user == 'H':
				dict['H']='Angry' 
			elif user == 'I':
				dict['I']='Angry' 
			elif user == 'J':
				dict['J']='Angry' 
			elif user == 'K':
				dict['K']='Angry' 
			elif user == 'L':
				dict['L']='Angry' 
			elif user == 'M':
				dict['M']='Angry' 
			elif user == 'N':
				dict['N']='Angry' 
			elif user == 'O':
				dict['O']='Angry' 
			elif user == 'P':
				dict['P']='Angry' 
			elif user == 'Q':
				dict['Q']='Angry' 
			elif user == 'R':
				dict['R']='Angry'
			elif user == 'S':
				dict['S']='Angry' 
			elif user == 'T':
				dict['T']='Angry'
			elif user == 'U':
				dict['U']='Angry'
			elif user == 'V':
				dict['V']='Angry'
			elif user == 'W':
				dict['W']='Angry'
			elif user == 'X':
				dict['X']='Angry'
			elif user == 'Y':
				dict['Y']='Angry'
			elif user == 'Z':
				dict['Z']='Angry'
		match= re.search(r'>_<', line)
		if match:
			print match.group() 
			if user == 'A':
				dict['A']='Angry' 
			elif user == 'B':
				dict['B']='Angry' 
			elif user == 'C':
				dict['C']='Angry' 
			elif user == 'D':
				dict['D']='Angry' 
			elif user == 'E':
				dict['E']='Angry' 
			elif user == 'F':
				dict['F']='Angry' 
			elif user == 'G':
				dict['G']='Angry' 
			elif user == 'H':
				dict['H']='Angry' 
			elif user == 'I':
				dict['I']='Angry' 
			elif user == 'J':
				dict['J']='Angry' 
			elif user == 'K':
				dict['K']='Angry' 
			elif user == 'L':
				dict['L']='Angry' 
			elif user == 'M':
				dict['M']='Angry' 
			elif user == 'N':
				dict['N']='Angry' 
			elif user == 'O':
				dict['O']='Angry' 
			elif user == 'P':
				dict['P']='Angry' 
			elif user == 'Q':
				dict['Q']='Angry' 
			elif user == 'R':
				dict['R']='Angry'
			elif user == 'S':
				dict['S']='Angry' 
			elif user == 'T':
				dict['T']='Angry'
			elif user == 'U':
				dict['U']='Angry'
			elif user == 'V':
				dict['V']='Angry'
			elif user == 'W':
				dict['W']='Angry'
			elif user == 'X':
				dict['X']='Angry'
			elif user == 'Y':
				dict['Y']='Angry'
			elif user == 'Z':
				dict['Z']='Angry'
		match= re.search(r':\(', line)
		if match:
			print match.group() 
			if user == 'A':
				dict['A']='Sad' 
			elif user == 'B':
				dict['B']='Sad' 
			elif user == 'C':
				dict['C']='Sad' 
			elif user == 'D':
				dict['D']='Sad' 
			elif user == 'E':
				dict['E']='Sad' 
			elif user == 'F':
				dict['F']='Sad' 
			elif user == 'G':
				dict['G']='Sad' 
			elif user == 'H':
				dict['H']='Sad' 
			elif user == 'I':
				dict['I']='Sad' 
			elif user == 'J':
				dict['J']='Sad' 
			elif user == 'K':
				dict['K']='Sad' 
			elif user == 'L':
				dict['L']='Sad' 
			elif user == 'M':
				dict['M']='Sad' 
			elif user == 'N':
				dict['N']='Sad' 
			elif user == 'O':
				dict['O']='Sad' 
			elif user == 'P':
				dict['P']='Sad' 
			elif user == 'Q':
				dict['Q']='Sad' 
			elif user == 'R':
				dict['R']='Sad'
			elif user == 'S':
				dict['S']='Sad' 
			elif user == 'T':
				dict['T']='Sad'
			elif user == 'U':
				dict['U']='Sad'
			elif user == 'V':
				dict['V']='Sad'
			elif user == 'W':
				dict['W']='Sad'
			elif user == 'X':
				dict['X']='Sad'
			elif user == 'Y':
				dict['Y']='Sad'
			elif user == 'Z':
				dict['Z']='Sad'
		match= re.search(r":\(", line)
		if match:
			print match.group() 
			if user == 'A':
				dict['A']='Sad' 
			elif user == 'B':
				dict['B']='Sad' 
			elif user == 'C':
				dict['C']='Sad' 
			elif user == 'D':
				dict['D']='Sad' 
			elif user == 'E':
				dict['E']='Sad' 
			elif user == 'F':
				dict['F']='Sad' 
			elif user == 'G':
				dict['G']='Sad' 
			elif user == 'H':
				dict['H']='Sad' 
			elif user == 'I':
				dict['I']='Sad' 
			elif user == 'J':
				dict['J']='Sad' 
			elif user == 'K':
				dict['K']='Sad' 
			elif user == 'L':
				dict['L']='Sad' 
			elif user == 'M':
				dict['M']='Sad' 
			elif user == 'N':
				dict['N']='Sad' 
			elif user == 'O':
				dict['O']='Sad' 
			elif user == 'P':
				dict['P']='Sad' 
			elif user == 'Q':
				dict['Q']='Sad' 
			elif user == 'R':
				dict['R']='Sad'
			elif user == 'S':
				dict['S']='Sad' 
			elif user == 'T':
				dict['T']='Sad'
			elif user == 'U':
				dict['U']='Sad'
			elif user == 'V':
				dict['V']='Sad'
			elif user == 'W':
				dict['W']='Sad'
			elif user == 'X':
				dict['X']='Sad'
			elif user == 'Y':
				dict['Y']='Sad'
			elif user == 'Z':
				dict['Z']='Sad'
		match= re.search(r":P", line)
		if match:
			print match.group() 
			if user == 'A':
				dict['A']='Sarcastic' 
			elif user == 'B':
				dict['B']='Sarcastic' 
			elif user == 'C':
				dict['C']='Sarcastic' 
			elif user == 'D':
				dict['D']='Sarcastic' 
			elif user == 'E':
				dict['E']='Sarcastic' 
			elif user == 'F':
				dict['F']='Sarcastic' 
			elif user == 'G':
				dict['G']='Sarcastic' 
			elif user == 'H':
				dict['H']='Sarcastic' 
			elif user == 'I':
				dict['I']='Sarcastic' 
			elif user == 'J':
				dict['J']='Sarcastic' 
			elif user == 'K':
				dict['K']='Sarcastic' 
			elif user == 'L':
				dict['L']='Sarcastic' 
			elif user == 'M':
				dict['M']='Sarcastic' 
			elif user == 'N':
				dict['N']='Sarcastic' 
			elif user == 'O':
				dict['O']='Sarcastic' 
			elif user == 'P':
				dict['P']='Sarcastic' 
			elif user == 'Q':
				dict['Q']='Sarcastic' 
			elif user == 'R':
				dict['R']='Sarcastic'
			elif user == 'S':
				dict['S']='Sarcastic' 
			elif user == 'T':
				dict['T']='Sarcastic'
			elif user == 'U':
				dict['U']='Sarcastic'
			elif user == 'V':
				dict['V']='Sarcastic'
			elif user == 'W':
				dict['W']='Sarcastic'
			elif user == 'X':
				dict['X']='Sarcastic'
			elif user == 'Y':
				dict['Y']='Sarcastic'
			elif user == 'Z':
				dict['Z']='Sarcastic'
		match= re.search(r";\)", line)
		if match:
			print match.group() 
			if user == 'A':
				dict['A']='Sarcastic' 
			elif user == 'B':
				dict['B']='Sarcastic' 
			elif user == 'C':
				dict['C']='Sarcastic' 
			elif user == 'D':
				dict['D']='Sarcastic' 
			elif user == 'E':
				dict['E']='Sarcastic' 
			elif user == 'F':
				dict['F']='Sarcastic' 
			elif user == 'G':
				dict['G']='Sarcastic' 
			elif user == 'H':
				dict['H']='Sarcastic' 
			elif user == 'I':
				dict['I']='Sarcastic' 
			elif user == 'J':
				dict['J']='Sarcastic' 
			elif user == 'K':
				dict['K']='Sarcastic' 
			elif user == 'L':
				dict['L']='Sarcastic' 
			elif user == 'M':
				dict['M']='Sarcastic' 
			elif user == 'N':
				dict['N']='Sarcastic' 
			elif user == 'O':
				dict['O']='Sarcastic' 
			elif user == 'P':
				dict['P']='Sarcastic' 
			elif user == 'Q':
				dict['Q']='Sarcastic' 
			elif user == 'R':
				dict['R']='Sarcastic'
			elif user == 'S':
				dict['S']='Sarcastic' 
			elif user == 'T':
				dict['T']='Sarcastic'
			elif user == 'U':
				dict['U']='Sarcastic'
			elif user == 'V':
				dict['V']='Sarcastic'
			elif user == 'W':
				dict['W']='Sarcastic'
			elif user == 'X':
				dict['X']='Sarcastic'
			elif user == 'Y':
				dict['Y']='Sarcastic'
			elif user == 'Z':
				dict['Z']='Sarcastic'
		match= re.search(r"O_O", line)
		if match:
			print match.group() 
			if user == 'A':
				dict['A']='Surprised' 
			elif user == 'B':
				dict['B']='Surprised' 
			elif user == 'C':
				dict['C']='Surprised' 
			elif user == 'D':
				dict['D']='Surprised' 
			elif user == 'E':
				dict['E']='Surprised' 
			elif user == 'F':
				dict['F']='Surprised' 
			elif user == 'G':
				dict['G']='Surprised' 
			elif user == 'H':
				dict['H']='Surprised' 
			elif user == 'I':
				dict['I']='Surprised' 
			elif user == 'J':
				dict['J']='Surprised' 
			elif user == 'K':
				dict['K']='Surprised' 
			elif user == 'L':
				dict['L']='Surprised' 
			elif user == 'M':
				dict['M']='Surprised' 
			elif user == 'N':
				dict['N']='Surprised' 
			elif user == 'O':
				dict['O']='Surprised' 
			elif user == 'P':
				dict['P']='Surprised' 
			elif user == 'Q':
				dict['Q']='Surprised' 
			elif user == 'R':
				dict['R']='Surprised'
			elif user == 'S':
				dict['S']='Surprised' 
			elif user == 'T':
				dict['T']='Surprised'
			elif user == 'U':
				dict['U']='Surprised'
			elif user == 'V':
				dict['V']='Surprised'
			elif user == 'W':
				dict['W']='Surprised'
			elif user == 'X':
				dict['X']='Surprised'
			elif user == 'Y':
				dict['Y']='Surprised'
			elif user == 'Z':
				dict['Z']='Surprised'
		match= re.search(r":-o", line)
		if match:
			print match.group() 
			if user == 'A':
				dict['A']='Surprised' 
			elif user == 'B':
				dict['B']='Surprised' 
			elif user == 'C':
				dict['C']='Surprised' 
			elif user == 'D':
				dict['D']='Surprised' 
			elif user == 'E':
				dict['E']='Surprised' 
			elif user == 'F':
				dict['F']='Surprised' 
			elif user == 'G':
				dict['G']='Surprised' 
			elif user == 'H':
				dict['H']='Surprised' 
			elif user == 'I':
				dict['I']='Surprised' 
			elif user == 'J':
				dict['J']='Surprised' 
			elif user == 'K':
				dict['K']='Surprised' 
			elif user == 'L':
				dict['L']='Surprised' 
			elif user == 'M':
				dict['M']='Surprised' 
			elif user == 'N':
				dict['N']='Surprised' 
			elif user == 'O':
				dict['O']='Surprised' 
			elif user == 'P':
				dict['P']='Surprised' 
			elif user == 'Q':
				dict['Q']='Surprised' 
			elif user == 'R':
				dict['R']='Surprised'
			elif user == 'S':
				dict['S']='Surprised' 
			elif user == 'T':
				dict['T']='Surprised'
			elif user == 'U':
				dict['U']='Surprised'
			elif user == 'V':
				dict['V']='Surprised'
			elif user == 'W':
				dict['W']='Surprised'
			elif user == 'X':
				dict['X']='Surprised'
			elif user == 'Y':
				dict['Y']='Surprised'
			elif user == 'Z':
				dict['Z']='Surprised'
		match= re.search(r"B-\)", line)
		if match:
			print match.group() 
			if user == 'A':
				dict['A']='Crook' 
			elif user == 'B':
				dict['B']='Crook' 
			elif user == 'C':
				dict['C']='Crook' 
			elif user == 'D':
				dict['D']='Crook' 
			elif user == 'E':
				dict['E']='Crook' 
			elif user == 'F':
				dict['F']='Crook' 
			elif user == 'G':
				dict['G']='Crook' 
			elif user == 'H':
				dict['H']='Crook' 
			elif user == 'I':
				dict['I']='Crook' 
			elif user == 'J':
				dict['J']='Crook' 
			elif user == 'K':
				dict['K']='Crook' 
			elif user == 'L':
				dict['L']='Crook' 
			elif user == 'M':
				dict['M']='Crook' 
			elif user == 'N':
				dict['N']='Crook' 
			elif user == 'O':
				dict['O']='Crook' 
			elif user == 'P':
				dict['P']='Crook' 
			elif user == 'Q':
				dict['Q']='Crook' 
			elif user == 'R':
				dict['R']='Crook'
			elif user == 'S':
				dict['S']='Crook' 
			elif user == 'T':
				dict['T']='Crook'
			elif user == 'U':
				dict['U']='Crook'
			elif user == 'V':
				dict['V']='Crook'
			elif user == 'W':
				dict['W']='Crook'
			elif user == 'X':
				dict['X']='Crook'
			elif user == 'Y':
				dict['Y']='Crook'
			elif user == 'Z':
				dict['Z']='Crook'
		match= re.search(r";\)", line)
		if match:
			print match.group() 
			if user == 'A':
				dict['A']='Crook' 
			elif user == 'B':
				dict['B']='Crook' 
			elif user == 'C':
				dict['C']='Crook' 
			elif user == 'D':
				dict['D']='Crook' 
			elif user == 'E':
				dict['E']='Crook' 
			elif user == 'F':
				dict['F']='Crook' 
			elif user == 'G':
				dict['G']='Crook' 
			elif user == 'H':
				dict['H']='Crook' 
			elif user == 'I':
				dict['I']='Crook' 
			elif user == 'J':
				dict['J']='Crook' 
			elif user == 'K':
				dict['K']='Crook' 
			elif user == 'L':
				dict['L']='Crook' 
			elif user == 'M':
				dict['M']='Crook' 
			elif user == 'N':
				dict['N']='Crook' 
			elif user == 'O':
				dict['O']='Crook' 
			elif user == 'P':
				dict['P']='Crook' 
			elif user == 'Q':
				dict['Q']='Crook' 
			elif user == 'R':
				dict['R']='Crook'
			elif user == 'S':
				dict['S']='Crook' 
			elif user == 'T':
				dict['T']='Crook'
			elif user == 'U':
				dict['U']='Crook'
			elif user == 'V':
				dict['V']='Crook'
			elif user == 'W':
				dict['W']='Crook'
			elif user == 'X':
				dict['X']='Crook'
			elif user == 'Y':
				dict['Y']='Crook'
			elif user == 'Z':
				dict['Z']='Crook'
		match= re.search(r":-/", line)
		if match:
			print match.group() 
			if user == 'A':
				dict['A']='Neutral' 
			elif user == 'B':
				dict['B']='Neutral' 
			elif user == 'C':
				dict['C']='Neutral' 
			elif user == 'D':
				dict['D']='Neutral' 
			elif user == 'E':
				dict['E']='Neutral' 
			elif user == 'F':
				dict['F']='Neutral' 
			elif user == 'G':
				dict['G']='Neutral' 
			elif user == 'H':
				dict['H']='Neutral' 
			elif user == 'I':
				dict['I']='Neutral' 
			elif user == 'J':
				dict['J']='Neutral' 
			elif user == 'K':
				dict['K']='Neutral' 
			elif user == 'L':
				dict['L']='Neutral' 
			elif user == 'M':
				dict['M']='Neutral' 
			elif user == 'N':
				dict['N']='Neutral' 
			elif user == 'O':
				dict['O']='Neutral' 
			elif user == 'P':
				dict['P']='Neutral' 
			elif user == 'Q':
				dict['Q']='Neutral' 
			elif user == 'R':
				dict['R']='Neutral'
			elif user == 'S':
				dict['S']='Neutral' 
			elif user == 'T':
				dict['T']='Neutral'
			elif user == 'U':
				dict['U']='Neutral'
			elif user == 'V':
				dict['V']='Neutral'
			elif user == 'W':
				dict['W']='Neutral'
			elif user == 'X':
				dict['X']='Neutral'
			elif user == 'Y':
				dict['Y']='Neutral'
			elif user == 'Z':
				dict['Z']='Neutral'
		match= re.search(r"=_=", line)
		if match:
			print match.group() 
			if user == 'A':
				dict['A']='Neutral' 
			elif user == 'B':
				dict['B']='Neutral' 
			elif user == 'C':
				dict['C']='Neutral' 
			elif user == 'D':
				dict['D']='Neutral' 
			elif user == 'E':
				dict['E']='Neutral' 
			elif user == 'F':
				dict['F']='Neutral' 
			elif user == 'G':
				dict['G']='Neutral' 
			elif user == 'H':
				dict['H']='Neutral' 
			elif user == 'I':
				dict['I']='Neutral' 
			elif user == 'J':
				dict['J']='Neutral' 
			elif user == 'K':
				dict['K']='Neutral' 
			elif user == 'L':
				dict['L']='Neutral' 
			elif user == 'M':
				dict['M']='Neutral' 
			elif user == 'N':
				dict['N']='Neutral' 
			elif user == 'O':
				dict['O']='Neutral' 
			elif user == 'P':
				dict['P']='Neutral' 
			elif user == 'Q':
				dict['Q']='Neutral' 
			elif user == 'R':
				dict['R']='Neutral'
			elif user == 'S':
				dict['S']='Neutral' 
			elif user == 'T':
				dict['T']='Neutral'
			elif user == 'U':
				dict['U']='Neutral'
			elif user == 'V':
				dict['V']='Neutral'
			elif user == 'W':
				dict['W']='Neutral'
			elif user == 'X':
				dict['X']='Neutral'
			elif user == 'Y':
				dict['Y']='Neutral'
			elif user == 'Z':
				dict['Z']='Neutral'
	
		
if 'A' in dict:     	 							## Avoid KeyError
	print 'Person A Behaviour is: ' + dict.get('A')  
	if dict.get('A') == 'happy':	
		happy = happy +1
	elif dict.get('A') == 'Angry':	
		angry = angry +1
	elif dict.get('A') == 'Sad':	
		sad = sad +1
	elif dict.get('A') == 'Sarcastic':	
		sarcastic = sarcastic +1
	elif dict.get('A') == 'Crook':	
		crook = crook +1
	elif dict.get('A') == 'Neutral':	
		neutral = neutral +1
	elif dict.get('A') == 'Surprised':	
		surprised = surprised +1	
if 'B' in dict:     	 							## Avoid KeyError
	print 'Person B Behaviour is: ' + dict.get('B')  
	if dict.get('B') == 'happy':	
		happy = happy +1
	elif dict.get('B') == 'Angry':	
		angry = angry +1
	elif dict.get('B') == 'Sad':	
		sad = sad +1
	elif dict.get('B') == 'Sarcastic':	
		sarcastic = sarcastic +1
	elif dict.get('B') == 'Crook':	
		crook = crook +1
	elif dict.get('B') == 'Neutral':	
		neutral = neutral +1
	elif dict.get('B') == 'Surprised':	
		surprised = surprised +1	
if 'E' in dict:     	 							## Avoid KeyError
	print 'Person E Behaviour is: ' + dict.get('E')  
	if dict.get('E') == 'happy':	
		happy = happy +1
	elif dict.get('E') == 'Angry':	
		angry = angry +1
	elif dict.get('E') == 'Sad':	
		sad = sad +1
	elif dict.get('E') == 'Sarcastic':	
		sarcastic = sarcastic +1
	elif dict.get('E') == 'Crook':	
		crook = crook +1
	elif dict.get('E') == 'Neutral':	
		neutral = neutral +1
	elif dict.get('E') == 'Surprised':	
		surprised = surprised +1
if 'C' in dict:     	 							## Avoid KeyError
	print 'Person C Behaviour is: ' + dict.get('C')  
	if dict.get('C') == 'happy':	
		happy = happy +1
	elif dict.get('C') == 'Angry':	
		angry = angry +1
	elif dict.get('C') == 'Sad':	
		sad = sad +1
	elif dict.get('C') == 'Sarcastic':	
		sarcastic = sarcastic +1
	elif dict.get('C') == 'Crook':	
		crook = crook +1
	elif dict.get('C') == 'Neutral':	
		neutral = neutral +1
	elif dict.get('C') == 'Surprised':	
		surprised = surprised +1
if 'G' in dict:     	 							## Avoid KeyError
	print 'Person G Behaviour is: ' + dict.get('G')  
	if dict.get('G') == 'happy':	
		happy = happy +1
	elif dict.get('G') == 'Angry':	
		angry = angry +1
	elif dict.get('G') == 'Sad':	
		sad = sad +1
	elif dict.get('G') == 'Sarcastic':	
		sarcastic = sarcastic +1
	elif dict.get('G') == 'Grook':	
		crook = crook +1
	elif dict.get('G') == 'Neutral':	
		neutral = neutral +1
	elif dict.get('G') == 'Surprised':	
		surprised = surprised +1				

hash={}


happyPercent=((happy*100)/totalNoOfBehaviours)
hash[':) or :D']=happyPercent
#print 'Happy Behaviour Percentage: ' + str(happyPercent) + '%'

sadPercent=((sad*100)/totalNoOfBehaviours)
hash[":( or :'("]=sadPercent
#print 'Sad Behaviour Percentage: ' + str(sadPercent) + '%'
								
sarcasticPercent=((sarcastic*100)/totalNoOfBehaviours)
hash[':P or ;)']=sarcasticPercent
#print 'Sarcastic Behaviour Percentage: ' + str(sarcasticPercent) + '%'
								
surprisedPercent=((surprised*100)/totalNoOfBehaviours)
hash[':-o or O_O']=surprisedPercent
#print 'Surprised Behaviour Percentage: ' + str(surprisedPercent) + '%'
								
crookPercent=((crook*100)/totalNoOfBehaviours)
hash['B-) or ;)']=crookPercent
#print 'Crook Behaviour Percentage: ' + str(crookPercent) + '%'
								
neutralPercent=((neutral*100)/totalNoOfBehaviours)
hash[':-/ or =_=']=neutralPercent
#print 'Neutral Behaviour Percentage: ' + str(neutralPercent) + '%'
								
angryPercent=((angry*100)/totalNoOfBehaviours)
hash['X-( or >_<']=angryPercent
#print 'Angry Behaviour Percentage: ' + str(angryPercent) + '%'

fo = open('Outputfile.txt','w')

fo.write(str(hash)) 								# python will convert \n to os.linesep
fo.close()								
                  							 ## since 'line' already includes the end-of line.
f.close()
