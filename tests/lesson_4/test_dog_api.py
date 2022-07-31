import requests as requests


import pytest

from lesson_4.data_for_dog_api import LIST_ALL_BREEDS


class TestDogApi:

    def test_list_all_breeds(self):
        url = 'https://dog.ceo/api/breeds/list/all'
        response = requests.get(url)

        self.check_status_code(response, 200)
        assert response.json() == LIST_ALL_BREEDS, "Данные в ответе не соответствуют ожидаемым \n" \
                                                   f"Ожидалось {LIST_ALL_BREEDS}\n" \
                                                   f"Вернулось {response.json()}"

    def check_status_code(self, response, status_code: int):
        assert response.status_code == status_code, f"Ожидался {status_code}, а вернулся {requests.status_codes}"

    def test_random_image(self):
        url = 'https://dog.ceo/api/breeds/image/random'
        link_image = None
        for i in range(5):
            response = requests.get(url)
            self.check_status_code(response, 200)
            if i > 0:
                assert link_image is not None and link_image != response.json().get("message"), \
                    "При повторном вызове вернулась предыдущая картинка"
            link_image = response.json().get("message")

    @pytest.mark.parametrize('image_count', [0, 3, 10, 50, 51])
    def test_multiple_random_image(self, image_count):
        url = f'https://dog.ceo/api/breeds/image/random/{image_count}'
        response = requests.get(url)

        self.check_status_code(response, 200)
        response_image_count = len(response.json().get('message'))
        assert response_image_count == image_count or (image_count > 50 and response_image_count == 50), \
            "Количество картинок не соответствует ожидаемому \n" \
            f"Ожидалось {image_count}\n" \
            f"Вернулось {response_image_count}"

    @pytest.mark.parametrize('breed_name', ['akita', 'borzoi', 'redbone', 'pug'])
    def test_breeds_list(self, breed_name):
        url = f'https://dog.ceo/api/breed/{breed_name}/images/random'
        response = requests.get(url)

        self.check_status_code(response, 200)
        assert f'https://images.dog.ceo/breeds/{breed_name}/' in response.json().get('message'), "Вернулась картинка для неверной породы собак"

    def test_single_random_image_sub_breed(self):
        url = 'https://dog.ceo/api/breed/hound/afghan/images/random'
        response = requests.get(url)

        self.check_status_code(response, 200)
        assert 'https://images.dog.ceo/breeds/hound-afghan/' in response.json().get('message'), "Вернулась картинка для неверной подпороды собак"
