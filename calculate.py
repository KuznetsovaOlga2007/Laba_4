import circle
import square
import triangle


figs = ['circle', 'square','triangle']
funcs = ['perimeter', 'area']
sizes = {
		'circle-area': 1,
		'circle-perimeter': 1,
		'square-area': 1,
		'square-perimeter': 1,
		'triangle-area': 3,
		'triangle-perimeter': 3
}

def calc(fig, func, size):
	'''Функция принимает в себя первым аргументом имя фигуры, вторым аргусентом - то значение,
		которое функция должна получить у данной, третьим - размер, чтобы получить данное значение'''
	assert fig in figs
	assert func in funcs

	key = f'{fig}-{func}'
	args = sizes.get(key)
	assert args is not None
	assert len(size) == args

	assert all(s >= 0 for s in size)

	if fig == "triangle":
		a,b,c = size
		assert a + b > c and a + c > b and b + c > a

	result = eval(f'{fig}.{func}(*{size})')
	return result
if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		'''Необходимо ввести фигуру, с которой будут произуведены операции'''
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		'''Необходимо ввести функцию, которая будет применена к фигуре'''
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		'''Необходимо ввести размер нужной фигуры'''
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)



