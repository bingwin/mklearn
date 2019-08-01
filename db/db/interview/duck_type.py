class Duck:
	def quack(self):
		print("gua gua")


class Person:
	def quack(self):
		print("我是人类,但我也会 gua gua gua")


def in_the_forest(duck):
	duck.quack()


def game():
	donald = Duck()
	john = Person()
	in_the_forest(donald)
	in_the_forest(john)
	print(type(donald))
	print(type(john))

game()