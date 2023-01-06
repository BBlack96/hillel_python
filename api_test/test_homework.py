import json

import requests
with open("post_body_booking.json", "r") as f:
    body = json.load(f)
    f.close()
class TestSuite:

    def test_opening(self):
        url = "https://restful-booker.herokuapp.com/booking"
        get_request = requests.get(url)
        assert 200 == get_request.status_code

    def test_post(self):
        url = "https://restful-booker.herokuapp.com/auth"
        post_request = requests.post(url, body)
        assert 200 == post_request.status_code

    def test_get(self):
        url = "https://api.chucknorris.io/"
        get_request = requests.get(url)
        assert 200 == get_request.status_code





