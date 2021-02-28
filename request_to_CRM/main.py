from time import sleep

import urllib3

from data_generator import DataGenerator


# Authentication credentials must be set here.
_ACCOUNT_ID = ''
_USER_ID = ''
_ACCESS_TOKEN = ''
_URL = ''

HEADERS = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }


def get_data_for_request():
    data_generator = DataGenerator()

    phone_list = data_generator.generate_phone_list()
    name_list = data_generator.generate_name_list()
    birth_date_list = data_generator.generate_birth_date_list()
    client_code_list = data_generator.generate_client_code_list()
    client_group = data_generator.generate_client_group_list()

    client_data_pack = zip(phone_list, name_list, birth_date_list, client_code_list, client_group)

    return client_data_pack


def send_data_to_api():
    http = urllib3.PoolManager()
    url = f'{_URL}{_ACCOUNT_ID}/u/{_USER_ID}/t/{_ACCESS_TOKEN}/m/Clients/'
    data_pack = get_data_for_request()

    for client in data_pack:
        print(client)
        fields = {
                'phone': client[0],
                'first_name': client[1],
                'birth_date': client[2],
                'number': client[3],
                'client_groups': client[4],
            }

        request_to_api = http.request(
                'POST',
                url,
                fields=fields,
            )

        print(f'STATUS = {request_to_api.status}')
        sleep(1.1)


if __name__=='__main__':
    send_data_to_api()
    print('DONE')
