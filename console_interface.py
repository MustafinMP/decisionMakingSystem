class ConsoleInterface:
    """Консольный вариант интерфейса"""
    def __init__(self):
        self.data: dict = dict()

    def read(self) -> dict:
        """Чтение всех необходимых данных"""
        print('Введите количество сравниваемых объектов: ')
        objects_count: int = self._read_count()
        self.data['objects_count'] = objects_count

        print('Введите сравниваемые объекты')
        objects: list = list()
        for i in range(objects_count):
            new_object: str = input(f'{i + 1}: ')
            while new_object in objects:
                print('Такой объект уже существует. Введите новый объект.')
                new_object: str = input(f'{i + 1}: ')
            objects.append(new_object)
        self.data['objects'] = objects

        print('Введите количество критериев сравнения: ')
        criterion_count: int = self._read_count()
        self.data['criterion_count'] = criterion_count

        print('Введите критерии сравнения')
        criterion: list = list()
        for i in range(criterion_count):
            new_criterion: str = input(f'{i + 1}: ')
            while new_criterion in criterion:
                print('Такой критерий уже существует. Введите новый критерий.')
                new_criterion: str = input(f'{i + 1}: ')
            criterion.append(new_criterion)
        print('Далее будут предложены пары для сравнения. Для их оценки укажите букву L для левого или R для правого,'
              'а также целое число баллов (через пробел), насколько выбранный объект лучше второго. Например: L 3')
        print(f'Оцените важность критериев')
        global_priority: list[list[int, int, int]] = self._compare_block(criterion_count, criterion)
        self.data['global_priority'] = global_priority

        self.data['crit_prior']: dict[int] = dict()
        for i in range(criterion_count):
            print(f'Сравните обьекты по криетрию "{criterion[i]}"')
            priority: list[list[int, int, int]] = self._compare_block(objects_count, objects)
            self.data['crit_prior'][criterion[i]] = priority

        return self.data

    def _read_count(self) -> int:
        """Чтение количества сравниваемых объектов"""
        try:
            count: int = int(input())
            if count <= 0:
                print('Количество не может быть меньше единицы.')
                return self._read_count()
            return count
        except ValueError:
            return self._read_count()

    def _compare_block(self, count: int, objects: list[str]) -> list[list[int, int, int]]:
        """Чтение группы пар сравнений по одному конкретному признаку"""
        block: list[list[int, int, int]] = list()
        for left_index in range(count - 1):
            for right_index in range(left_index + 1, count):
                left: str = objects[left_index]
                right: str = objects[right_index]
                print(f'{left} или {right}?')
                points: int = self._compare_two()
                block.append([left_index, right_index, points])
        return block

    @staticmethod
    def _compare_two() -> int:
        """Чтение пары сравнения"""
        inp: str = input()
        if inp == '0':
            return 0
        inp: [str, str] = inp.split()
        return {'L': 1, 'R': -1}[inp[0]] * int(inp[1])

    @staticmethod
    def print_result(result: list[list[str, float]]):
        """Форматированный вывод результата"""
        max_len = max([len(line[0]) for line in result])
        for line in result:
            print(f'{line[0]:<{max_len}} | {round(line[1], 4):0<6} | {"*" * int(line[1] * 20)}')
