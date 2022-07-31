import cerberus as cerberus
import pytest
import requests as requests


class TestJsonPlaceholderTypicode:

    def setup(self):
        self.url = 'https://jsonplaceholder.typicode.com/posts'

    @pytest.mark.parametrize("user_id", [1, 2, 3])
    def test_create_json_status_code(self, user_id):
        response = requests.post(self.url, json={
            'title': 'test',
            'body': 'test for hw',
            'userId': user_id})
        assert response.ok

    @pytest.mark.parametrize("id", [1, 2, 3])
    def test_get_json_schema(self, id):
        response = requests.get(f'{self.url}/{id}')
        schema = {
            "userId": {"type": "number"},
            "id": {"type": "number"},
            "title": {"type": "string"},
            "body": {"type": "string"}
        }
        v = cerberus.Validator()
        assert v.validate(response.json(), schema)

    def test_list_json(self):
        response = requests.get(f'{self.url}')
        assert response.ok

    def test_update_json_status_code(self):
        response = requests.post(self.url, json={
            'id': '1',
            'title': 'test',
            'body': 'test for hw',
            'userId': 5})
        assert response.ok

    def test_list_json(self):
        response = requests.delete(f'{self.url}/1')
        assert response.ok
