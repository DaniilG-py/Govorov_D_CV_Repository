"""
Генераторы данных новых клиентов
- Код клиента
- Имя
- Телефонный номер
- Дата рождения
- Группа клиентов
"""

import datetime
from random import randint, shuffle, choice


class DataGenerator:

    '''
    Генерация кода клиента
    '''
    def generate_client_code_list(self):
        '''
        По ТЗ код у первого из клиентов - равен 1, у второго - 2,
        у последующих - сумме кодов двух предыдущих клиентов.
        '''

        client_code_list = [1, 2]
        while len(client_code_list) < 50:
            next_num = client_code_list[-1] + client_code_list[-2]
            client_code_list.append(next_num)

        return client_code_list


    '''
    Генератор имен клиента
    '''

    def generate_name_list(self):
        first_name_str = 'Авдей Авксентий Агафон Акакий Александр Алексей Альберт Альвиан Анатолий Андрей Аникита Антон Антонин Анфим Аристарх Аркадий Арсений Артемий Артур Архипп Афанасий Богдан Борис Вавила Вадим Валентин Валерий Валерьян Варлам Варсонофий Василий Венедикт Виссарион Виталий Владислав Владлен Влас Всеволод Вячеслав Гавриил Галактион Геласий Геннадий Георгий Герасим Герман Германн Глеб Гордей Григорий Данакт Демьян Денис Дмитрий Добрыня Донат Дорофей Евгений Евдоким Евсей Назар Нестор Никанор Никита Никифор Николай Никон Лада Лариса Лидия Лилия Любовь Людмила Валентина Валерия Варвара Василиса Вера Вероника Виктория'

        first_name_list = first_name_str.split(' ')
        shuffle(first_name_list)

        return first_name_list


    '''
    Генерация случайных телефонных номеров
    '''

    def generate_phone_endings(self):

        num_list = [1,2,3,4,5,6,7,8,9,0]
        phone_ends_list = []
        phone = ''

        while len(phone_ends_list) < 50:
            index = randint(0, len(num_list))
            shuffle(num_list)
            if len(phone) != 7:
                phone += str(num_list[index-1])
            else:
                phone_ends_list.append(phone)
                phone = ''

        return phone_ends_list


    def generate_phone_list(self):
        phone_start = '7911'
        phone_list = [phone_start + i for i in self.generate_phone_endings()]

        return phone_list


    '''
    Генератор дней рождения
    '''

    def generate_birth_date(self):
        '''
        - Так как по ТЗ период дней рождений указан от 01.01.1970 года по 31.12.2000 год,
        - то период, выраженный в секундах по Unix-времени, будет иметь начальное значение 0 секунд.
        '''
        start_date_in_sec = 0
        final_date_in_sec = datetime.datetime(2000, 12, 31, 0, 0, 0).timestamp()
        random_seconds = randint(start_date_in_sec, final_date_in_sec)
        birth_date = datetime.datetime.utcfromtimestamp(random_seconds).strftime('%d.%m.%Y')

        return birth_date


    def generate_birth_date_list(self):
        birth_date_list = []

        while len(birth_date_list) < 50:
            birth_date_list.append(self.generate_birth_date())

        return birth_date_list


    '''
    Генератор групп клиентов
    '''

    def generate_client_group(self):
        client_group_types = ('новые клиенты', 'постоянные клиенты')
        client_group = choice(client_group_types)

        return client_group


    def generate_client_group_list(self):
        client_group_list = []

        while len(client_group_list) < 50:
            client_group_list.append(self.generate_client_group())

        return client_group_list
