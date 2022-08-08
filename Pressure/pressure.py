'''Pressure under crane mats '''

class CrawleCrane():

    def __init__(self, length, width, model):
        self.length = int(length)
        self.width = int(width)
        self.model = str(model)
    
    def __repr__(self) -> str:
        return f'Crane: {self.model} [{self.length} x {self.width}]'


class Mats():

    def __init__(self):
        self.legth = 5000
        self.width = 1000
        self.height = 200
        self.weight = 1.15
        self.pressure = self.weight / ((self.legth * self.width) * 0.000001)

def start()->tuple:
    '''Primitive of interface'''
    print("""
        1 — LIEBHERR LR1350/1
        2 — LIEBHERR LR1600
        3 — LIEBHERR LR1750
        4 — LIEBHERR LR11350
        5 — другое
        """)
    ModelOfCrane = input('Введите модель крана: ')
    if ModelOfCrane not in [str(x) for x in range(1,5)]:
        length, width = input('Введите длину и ширину опорной поверхности в мм:').split(' ')
        model = 'unnamed'
    else:
        length, width, model = _choose_cranes(ModelOfCrane)
    print(f'{model}')
    return tuple([length, width, model])

def _choose_cranes(ModelOfCrane:int)->list:
    BaseOfCranes = {"LIEBHERR LR1350/1" : (7400, 1040), 
        "LIEBHERR LR1600" : (8700, 1840),
        "LIEBHERR LR1750" : (9100, 1300),
        "LIEBHERR LR11350" : (11400, 1810)}
    list_cranes = tuple(BaseOfCranes.keys())
    model = list_cranes[int(ModelOfCrane) - 1]
    return list([*BaseOfCranes[model], str(model)])

def end():
    end_v = str(input("\nPress any key to escape or n = restart: ")).lower()
    if end_v != ("n"):
        return True
    return False


def calculation(crawle_length:int, crawle_width:int, pressure:float):
    new_load = []
    for numbers_mats in range(1, 6):
        crane_square = crawle_length * crawle_width
        new_legth = (crawle_length + 2 * Mats().height * numbers_mats)
        new_width = (crawle_width + 2 * Mats().height * numbers_mats)
        new_square = new_legth * new_width
        new_sqcoef = crane_square / new_square
        new_load.append(round(pressure * new_sqcoef + Mats().pressure * numbers_mats,2))
        print(f"[+] Колво слоев: {numbers_mats}")
        print(f"[+] Исх давление, т/м2: {pressure}")
        print(f"[+] Новая длина опорной поверхности, мм: {new_legth}")
        print(f"[+] Новая ширина опорной поверхности, мм: {new_width}")
        print(f"[+] Коеф увеличения опорной поверхности: {round(new_square / crane_square, 2)}\n")
    for i in range(5):
        print(f"[+] Новая нагрузка для слоя #{i + 1} в т/м2: {new_load[i]}")
    return new_load[0], new_load[1]


if __name__ == '__main__':
    end_v = False
    while end_v == False:
        parametrs_crane = start()
        CraneBase = CrawleCrane(*parametrs_crane)
        pressure = float(input("Введите давление в т/м2 "))
        # mat, mat_2 = calculation(CraneBase.length, CraneBase.width, pressure)
        print(type(calculation(CraneBase.length, CraneBase.width, pressure)))
        # print(calculation(CraneBase.length, CraneBase.width, pressure))
        # print(CraneBase)

        end_v = end()
