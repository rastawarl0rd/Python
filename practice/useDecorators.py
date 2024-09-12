import math
from decorators import timer
from decorators import debug

@timer
def waste_some_time(num_times):
	for _ in range(num_times):
		sum([number**2 for number in range(10_000)])

waste_some_time(1)

waste_some_time(999)

print()
print("#################################")
print()

@debug
def make_greeting(name, age=None):
	if age is None:
		return f"Hello {name}"
	else:
		return f"You are the {name} at {age} already!"

make_greeting("rasta")
make_greeting("warl0rds", age=43)

print()
print("#################################")
print()

math.factorial = debug(math.factorial)

def approximate_e(terms=18):
	return sum(1 / math.factorial(n + 1) for n in range(terms))

approximate_e(10)
