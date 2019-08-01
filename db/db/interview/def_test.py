def clear_list(l):
	l = []

ll = [1, 2, 3]
clear_list(ll)
print(ll)


def flist(l=[1]):
	l.append(1)
	print(l)

flist()
flist()


def print_all(a, *args, **kwargs):
	print(a)
	if args:
		print(args)
	if kwargs:
		print(kwargs)


print_all(1, 2, b=1)
print_all(1, *[2,4,5,6], **dict(b=1, c=2))

