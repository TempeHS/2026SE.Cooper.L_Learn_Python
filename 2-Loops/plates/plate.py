def main():
	plate = input("Plate: ")
	if is_valid(plate):
		print("Valid")
	else:
		print("Invalid")


def is_valid(s):
	if 2 > len(s) > 6:
		return False
	if not s[0].isalpha() or not s[1].isalpha():
		return False
	for char in s:
		if not (char.isalpha() or char.isdigit()):
			return False
	number_found = False
	for char in s:
		if char.isdigit():
			number_found = True
		if number_found and char.isalpha():
			return False
	first_number = 0
	for char in s:
		if char.isdigit() and char != "0":
			first_number += 1
		if char == "0" and first_number == 0:
			return False
	return True
main()