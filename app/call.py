from urllib.error import HTTPError

import requests


def call_nationalize(name):
    try:
        response = requests.get("https://api.nationalize.io/?name=" + name)
        return response
    except HTTPError as http_err:
        raise HTTPError(http_err.url, http_err.code, "HTTPError", http_err.hdrs, http_err.fp)
    except Exception as e:
        raise Exception(e)


def call_rest_countries(code):
    try:
        response = requests.get("https://restcountries.com/v3.1/alpha/" + code)
        return response
    except HTTPError as http_err:
        raise HTTPError(http_err.url, http_err.code, "HTTPError", http_err.hdrs, http_err.fp)
    except Exception as e:
        raise Exception(e)
