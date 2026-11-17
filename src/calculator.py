def calculator(operation, num1, num2):
	"""Apply addition or subtraction to two numbers."""
	if operation == "add":
		return num1 + num2
	if operation == "subtract":
		return num1 - num2
	raise ValueError(f"Unsupported operation: {operation}")
