#initials
name = input("Enter name:\n")
name = name.split(' ')
for word in name:
	print(word[0]+'.',end=' ')
print()

#phone number translator
letter_dict = {"ABC":2,"DEF":3,"GHI":4,"JKL":5,"MNO":6,"PQRS":7,"TUV":8,"WXYZ":9}
number = input("Enter a phone number:\n")
for index, char in enumerate(number):
	for key in letter_dict:
		if char in key:
			number = number.replace(char,str(letter_dict[key]))

print("New number:",number)

#vowels and consonants
def count_vowels(string):
	count = 0
	vowels = "aeiou"
	for char in string:
		if char in vowels:
			count += 1
	return count
def count_consanants(string):
	vowels = "aeiou \n\t"
	count = 0
	for char in string:
		if char not in vowels:
			count += 1
	return count

user_string = input("Enter a string:\n")
print("Number of vowels: %d, number of consonants: %d"%(count_vowels(user_string),count_consanants(user_string)))

#pig latin
user_string = input("Enter a string for pig latin:\n")
def to_pig_latin(string):
	str_array = string.split(' ')
	new_array = []
	for word in str_array:
		first_letter = word[0]
		new_str = word[1:]+first_letter+"ay"
		new_array.append(new_str)
	return ' '.join(new_array)
print("Pig latin string:",to_pig_latin(user_string))
