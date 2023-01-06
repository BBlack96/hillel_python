import json

import requests

with open("post_body_request.json", "r") as f:
    body = json.load(f)
    f.close()
with open("put_body_request.json", "r") as f:
    put_body = json.load(f)
    f.close()

class TestSuite:

    def test_get(self):
        baseURL = "https://rahulshettyacademy.com"
        resource = "/maps/api/place/get/json"
        key = "?key =qaclick123"
        get_url = baseURL + resource + key
        request = requests.get(get_url)
        assert 200 == request.status_code

    def test_post(self):
        baseURL = "https://rahulshettyacademy.com"
        resouruce = "/maps/api/place/add/json"
        key = "?key =qaclick123"
        post_url = baseURL + resouruce + key
        request_post = requests.post(post_url, body )
        assert 200 == request_post.status_code

    def test_put(self):
        baseURL = "https://rahulshettyacademy.com"
        resource = "/maps/api/place/update/json"
        key = "?key =qaclick123"
        put_url = baseURL + resource + key
        request_put = requests.put(put_url, put_body)
        assert 200 == request_put.status_code
