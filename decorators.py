import sys

def main():
	print prueba()
	print prueba2()

def to_upper(origin):
	def new_origin():
		return origin().upper()
	return new_origin


def to_lower(origin):
	def new_origin():
		return origin().lower()
	return new_origin

@to_upper
def prueba():
	t = "Text at the function"
	return t

@to_lower
def prueba2():
	t = "Text at the function"
	return t

if __name__ == "__main__":
	main()
