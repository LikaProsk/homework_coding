import pytest
import requests as requests

from lesson_4.data_for_open_brewery_db import LIST_OF_BREWERIES


class TestOpenBreweryDbOrg:

    @pytest.mark.parametrize('page_count', [0, 10, 20, 51])
    def test_breweries_per_page(self, page_count):
        url = f'https://api.openbrewerydb.org/breweries?per_page={page_count}'
        response = requests.get(url)

        self.check_status_code(response, 200)

        number_of_breweries = len(response.json())

        assert number_of_breweries == page_count, "Количество пивоварен не соответствует ожидаемому \n" \
                                                  f"Ожидалось {page_count}\n" \
                                                  f"Вернулось {number_of_breweries}"

    def check_status_code(self, response, status_code: int):
        assert response.status_code == status_code, f"Ожидался {status_code}, а вернулся {requests.status_codes}"

    def test_list_breweries(self):
        url = 'https://api.openbrewerydb.org/breweries'
        response = requests.get(url)

        self.check_status_code(response, 200)
        assert response.json() == LIST_OF_BREWERIES, "Данные в ответе не соответствуют ожидаемым \n" \
                                                     f"Ожидалось {LIST_OF_BREWERIES}\n" \
                                                     f"Вернулось {response.json()}"

    @pytest.mark.parametrize('city', ['fayetteville', 'chardon', 'boring'])
    def test_breweries_by_city(self, city):
        url = f'https://api.openbrewerydb.org/breweries?by_city={city}&per_page=3'
        response = requests.get(url)

        self.check_status_code(response, 200)

        for brewery in response.json():
            assert city.lower() == brewery.get('city').lower(), "Вернулись пивоварни для неверного города"

    @pytest.mark.parametrize('state', ['ohio', 'massachusetts'])
    def test_breweries_by_state(self, state):
        url = f'https://api.openbrewerydb.org/breweries?by_state={state}&per_page=3'
        response = requests.get(url)

        self.check_status_code(response, 200)

        for brewery in response.json():
            assert state.lower() == brewery.get('state').lower(), "Вернулись пивоварни для неверного штата"

    def test_breweries_by_type(self):
        type = 'bar'
        url = f'https://api.openbrewerydb.org/breweries?by_type={type}&per_page=3'
        response = requests.get(url)

        self.check_status_code(response, 200)
        for brewery in response.json():
            assert type.lower() == brewery.get('brewery_type').lower(), "Вернулись пивоварни неверного типа"
