def simple_gen():
	yield 'hello'
	yield 'world'


gen = simple_gen()
# print(type(gen))
# print(next(gen))
# print(next(gen))


def coro():
	hello = yield 'hello'
	yield hello

c = coro()

# print(type(c))
# print(next(c))
# print(c.send('world'))


from functools import wraps


def coroutine(func):

	@wraps(func)
	def primer(a, *args, **kwargs):
		gen = func(a, *args, **kwargs)
		return gen
	next(gen)
	return primer


@coroutine
def coro(a):
	return a

a = (i for i in range(1,20))

f = coro(a=a)
for i in f:
	print(i)
