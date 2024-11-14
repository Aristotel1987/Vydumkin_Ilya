
class Room:
    def __init__(self, room_number, max_guests, price, room_type = '', is_available=True):
        # Вводим базовый класс для комнаты с  номером, категорией, максимальным количеством гостей и ценой за ночь
        self.room_number = room_number
        self.room_type = room_type
        self.max_guests = max_guests
        self.price = price
        self.is_available = is_available#   Комната доступна для бронирования

    def book(self):
        # Метод для бронирования комнаты
        if self.is_available:
            self.is_available = False  # Устанавливаем комнату как недоступную
            print(f"Комната номер{self.room_number} забронирована")  # Сообщение о бронировании
        else:
            print(f"Комната {self.room_numver} не может быть забронирована.")  # Сообщение оневозможности бронирования

    def free(self):
        # Метод для освобождения комнаты
        self.is_available = True  # Устанавливаем комнату как доступную
        print(f"Комната {self.room_number} доступна для бронирования .")  # Сообщение об освобождении

class Lux(Room):
    def __init__(self, balcony, bar, *args, **kwargs):
        # ВВодим класс комнаты-люкс с дополнительными параметрами балкона и мини-бара
        super().__init__(*args, **kwargs)
        self.balcony = balcony   # Наличие балкона
        self.bar = bar  # Наличие мини-бара
        self.room_type = 'Люкс'
    def book(self):
        if self.is_available:
            self.is_available = False  # Устанавливаем комнату как недоступную
            print(f"Комната номер{self.room_number} забронирована. Внимание!! Люкс!! Спросить о дополнительных пожеланиях.")  # Сообщение о бронировании
        else:
            print(f"Комната {self.room_number} не может быть забронирована.")  # Сообщение оневозможности бронирования
class Standard(Room):
    def __init__(self, beds_count = 0, *args, **kwargs):
        # ВВодим класс стандарт с количеством кроватей
        super().__init__(*args, **kwargs)
        self.beds_count = beds_count  # Количество занятых кроватей в комнате
        self.room_type = 'Стандарт'
    def book(self):
        n=int(input('Введите число гостей: '))
        if n>self.max_guests:
            print('Бронирование невозможно, недостаточно мест.')
        else:
            self.beds_count+=n #Увеличиваем число занятых мест на размер бронированияn
            self.max_guests-=n # Уменьшаем число оставшихся мест на размер бронирования
            print(f'В комнате {self.room_number} забронировано {n} мест, осталось {self.max_guests} мест.')
            if self.max_guests==0:
                self.is_available=False
    def free(self):
        # Метод для освобождения комнаты
        exit=int(input('ВВедите число съезжающих гостей'))
        self.beds_count-=exit #Уменьшаем число занятых мест
        self.max_guests+=exit # Увеличиваем число доступных мест
        self.is_available = True  # Устанавливаем комнату как доступную

class Econom(Standard):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.room_type = 'Эконом'
class Guest:
    def __init__(self, full_name, phone_number, booking_id, room):
        # Инициализация гостя с полным именем, номером телефона и идентификатором бронирования
        self.__full_name = full_name # скрываем ФИО, как персональные данные
        self.__phone_number = phone_number
        self.booking_id = booking_id
        self.room= room
    def book_room(self, room):
        room.book()  # Бронирование указанной комнаты

class Hotel:
    def __init__(self):
        self.rooms = []  # Список для хранения комнат отеля
    def add_room(self, room):
        self.rooms.append(room)  # Добавление комнаты в список
        print(f"Комната {room.room_number} добавлена в отель.")  # Сообщение о добавлении комнаты

    def all_available_rooms(self):
        # Возвращает список всех доступных комнат
        return [Room.room_number for room in self.rooms if room.is_available]

    def find_rooms_for_guests(self, guest_count):
        # Возвращает список доступных комнат для заданного количества гостей
        free=[]
        for room in self.rooms:
            if room.is_available and room.max_guests >= guest_count:
                free.append(room.room_number)
        return free

hotel = Hotel()  # Создаем новый отель
while True:
        # Ввод данных о комнате
    room_type = input("Введите тип номера (Люкс/Стандарт/Эконом): ").strip().lower()
    room_number = input("Введите номер комнаты: ")
    room=room_number
    max_guests = int(input("Введите максимальное количество гостей: "))
    price = float(input("Введите цену за ночь: "))
    if room_type == "люкс":
        balcony = input("Есть ли балкон? (да/нет): ").strip().lower() == "да"
        bar = input("Есть ли мини-бар? (да/нет): ").strip().lower() == "да"
        room = Lux(room_number = room_number, max_guests = max_guests, price = price, balcony = balcony, bar = bar)
    elif room_type == "стандарт":
        beds_count = int(input("Введите количество кроватей: "))
        room = Standard(room_number = room_number, max_guests = max_guests, price = price, beds_count = beds_count)
    elif room_type == "эконом":
        beds_count = int(input("Введите количество кроватей: "))
        room = Econom(room_number = room_number, max_guests = max_guests, price = price, beds_count = beds_count)
    else:
        print("Неверный тип номера. Попробуйте снова.")
        continue
    hotel.add_room(room)  # Добавление комнаты в отель
    another = input("Хотите добавить еще одну комнату? (да/нет): ").strip().lower()
    if another != "да":
        break

while True:
        # Бронирование номера и добавлениегостя
    guest_name = input("Введите полное имя гостя: ")
    guest_phone = input("Введите номер телефона гостя: ")
    booking_id = input("Введите идентификатор бронирования: ")
    room=input(' Введите номер для бронирования.')
    for i in hotel.rooms:
        if i.room_number==room:
            room=i
    guest = Guest(guest_name, guest_phone, booking_id, room)  # Создание нового  гостя
    guest.book_room(room)
    another_booking = input("Хотите забронировать еще одну комнату? (да/нет): ").strip().lower()
    if another_booking != "да":
        break
# Поиск номера для n гостей
n=int(input('Введите число гостей для поиска подходящего номера'))
room_to_book = hotel.find_rooms_for_guests(guest_count=n)  # Поиск доступных комнат для n
print(f'В отеле доступны следущие номера для{n} гостей: \n {room_to_book}')