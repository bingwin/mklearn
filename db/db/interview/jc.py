import multiprocessing


def fib(n):
	if n <= 1:
		return 1
	return fib(n-1) + fib(n-2)

if __name__ == '__main__':
	jobs = []
	for i in range(10, 20):
		p = multiprocessing.Process(target=fib, args=(i,))
		jobs.append(p)
		p.start()