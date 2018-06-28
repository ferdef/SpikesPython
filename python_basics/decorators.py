import sys

def main():
	print prueba()
	print prueba2()
	print prueba3()

def to_upper(origin):
	def new_origin():
		try:
			return origin().upper()
		except:
			return origin()
	return new_origin

class to_lower(object):
	def __init__(self, origin):
		self.f = origin

	def __call__(self):
		try:
			return self.f().lower() 
		except:
			return self.f()

@to_upper
def prueba():
	t = "Text at the function"
	return t

@to_lower
def prueba2():
	t = "Text at the function"
	return t

@to_upper
def prueba3():
	t = 5
	return t

if __name__ == "__main__":
	main()
