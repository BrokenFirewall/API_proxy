import unittest
from unittest.mock import MagicMock
import json
import requests

import sys

sys.path.append('../app')

import call
import logics


class TestMethods(unittest.TestCase):
    def test_check_name_success(self):
        name = "luca"
        logics.check_name(name)

    def test_check_name_exception(self):
        name = "luca_"

        with self.assertRaises(Exception) as exception_context:
            logics.check_name(name)
        self.assertEqual(
            str(exception_context.exception),
            "Input name is invalid"
        )

    def test_define_most_probable_success(self):
        list_county = [{"country_id": "SM", "probability": 0.3961400461054557},
                       {"country_id": "IT", "probability": 0.28632298770976455},
                       {"country_id": "CH", "probability": 0.05572267050106734}]
        most_probable_country_expected = {"country_id": "SM", "probability": 0.3961400461054557}
        most_probable_country_received = logics.define_most_probable(list_county)

        self.assertEqual(most_probable_country_expected, most_probable_country_received)

    def test_define_most_probable_exception(self):
        list_county = [{"country_id": "SM"}, {"country_id": "IT", "probability": 0.28632298770976455}]

        with self.assertRaises(Exception) as exception_context:
            logics.define_most_probable(list_county)
        self.assertTrue(
            str(exception_context.exception) is not None
        )

    def test_call_nationalize_success(self):
        most_probable_country_expected = {"name": "luca",
                                          "country": [{"country_id": "SM", "probability": 0.3961400461054557},
                                                      {"country_id": "IT", "probability": 0.28632298770976455},
                                                      {"country_id": "CH", "probability": 0.05572267050106734}]}
        most_probable_country_received = call.call_nationalize("luca")

        self.assertEqual(most_probable_country_expected, most_probable_country_received.json())

    def test_call_nationalize_exception(self):
        response = call.call_nationalize("")
        self.assertTrue(
            str(response.status_code) != 200
        )

    def test_call_restcountries_success(self):
        country_expected = "Italy"
        country_received = call.call_rest_countries("IT")

        self.assertEqual(country_expected, country_received.json()[0]['name']['common'])

    def test_call_restcountries_exception(self):
        response = call.call_rest_countries("")
        self.assertTrue(
            str(response.status_code) != 200
        )

    def test_name_probability_success(self):
        # mock external API
        call.call_nationalize = MagicMock(status_code=200, response=json.dumps({"name": "luca",
                                                                                "country": [{"country_id": "SM",
                                                                                             "probability": 0.3961400461054557},
                                                                                            {"country_id": "IT",
                                                                                             "probability": 0.28632298770976455},
                                                                                            {"country_id": "CH",
                                                                                             "probability": 0.05572267050106734}]}))

        call.call_rest_countries = MagicMock(status_code=200, response=json.dumps([{"name": {"common": "Italy"}}]))

        response = requests.get('http://127.0.0.1:5000/name-probability?name=luca')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'Luca may be from San Marino')

    def test_name_probability_500(self):
        # mock external API
        call.call_nationalize = MagicMock(status_code=500, response=json.dumps({}))

        call.call_rest_countries = MagicMock(status_code=500, response=json.dumps({}))

        response = requests.get('http://127.0.0.1:5000/name-probability?name=luca')
        self.assertEqual(response.status_code, 500)

if __name__ == '__main__':
    unittest.main()
