import circle
import square


figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
     '''
        Вычисляет площадь или периметр выбранной фигуры по заданным сторонам
        Параметры:
                fig (str) - название выбранной фигуры
                func (str) - название функции (area или perimetr)
                size (list) - задаваемые стороны
        Возвращаемое значение:
                (float) - Периметр или площадь выбранной фигуры, в зависимости от того, какую функцию указал пользователь
        Пример вызова:
                print (calc('square', 'area', [10]))
                100
        '''
	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)



