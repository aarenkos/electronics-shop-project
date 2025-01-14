import csv

class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = 'Файл items.csv поврежден'

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        super().__init__()


    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self,other):
        """
        Сложение эеземпляров классов phone и item по колличеству товара в магазине
        """
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        return ValueError

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self. quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            raise Exception('Длина наименования товара больше 10 символов')
        self.__name = name

    @classmethod
    def instantiate_from_csv(cls, path=r"../src/items.csv"):
        """
        Инициализирует экземпляры класса `Item` данными из файла _src/items.csv
        """

        try:
            with open(path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                cls.all.clear()
                try:
                    for row in reader:
                        item = (cls(row['name'], row['price'], row['quantity']))
                except KeyError:
                    raise InstantiateCSVError('Файл items.csv поврежден')
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл items.csv')


    @staticmethod
    def string_to_number(string: str):
        """
        Статический метод, возвращающий число из строки
        """
        return int(float(string))




