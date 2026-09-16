age = int(input("What is your age? "))

if age > 60:
	is_member = input("Are you a member? (yes/no) ").strip().lower()

	if is_member == "yes":
		password = input("What is the password? ")

		if password == "Ninety Lemon":
			print("You are allowed to go")
		else:
			print("not eligible")
	else:
		print("not eligible")
else:
	print("not eligible")
    