
try:
	file = open("randomfile.pdf", "r")
	data = file.read()
	print(data)
except Exception as e:
	print(f"An error occurred: {e}")