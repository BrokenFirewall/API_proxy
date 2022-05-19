from urllib.error import HTTPError

from flask import Flask
from flask import request

import log
import call
import logics

app = Flask(__name__)


@app.route('/')
def base():
    dict_api = {
        "API": [
            {
                "path": "/name-probability",
                "params": [
                    {"name": "name", "type": "string"}
                ]
            }
        ]
    }
    return dict_api


@app.route('/name-probability')
def name_probability():
    name = request.args.get('name')
    try:
        log.log_info("check name")
        logics.check_name(name)

        log.log_info("call external API to retrieve probabilities")
        res_nationalize = call.call_nationalize(name)
        res_nationalize = res_nationalize.json()

        log.log_info("determines the country with most probability")
        most_probable_country = logics.define_most_probable(res_nationalize['country'])

        log.log_info("call external API for retrieve country details")
        res_rest_countries = call.call_rest_countries(most_probable_country['country_id'])
        res_rest_countries = res_rest_countries.json()
        log.log_info("get the country name from the json received from the response")
        country_name = res_rest_countries[0]['name']['common']

        log.log_info("define the message from probability")
        message = logics.define_out_message(most_probable_country['probability'], name, country_name)

        return message
    except HTTPError as e:
        log.log_error("HTTPError: " + str(e))
        return {
            'name': name,
            'HTTP_code_error': e.response.status_code,
            'ErrorMessage': str(e)
        }
    except Exception as e:
        log.log_error("Exception: " + str(e))
        return {
            'name': name,
            'ErrorMessage': str(e)
        }


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
