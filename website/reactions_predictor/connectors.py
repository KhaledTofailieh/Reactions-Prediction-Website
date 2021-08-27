import requests

mailer_api_url = "http://127.0.0.1:9000/"
reactions_api_url = "http://127.0.0.1:7000/"
BadList = [403, 404, 500]


def request_from_api(body, url, method="GET"):
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        global BadList
        response = requests.request(method, url, headers=headers, json=body)
        if response.status_code in BadList:
            print(response)
            raise Exception()
        response_data = response.json()
    except Exception as ex:
        print('Exception in Connector:', ex)
        response_data = {}
    return response_data


def get_reactions(parameters, path=''):
    global mailer_api_url
    url = reactions_api_url + path
    try:
        response_data = request_from_api(parameters, url, "GET")
    except Exception as ex:
        print('Exception in Mail-Sender:', ex)
        response_data = {}
    return response_data


def send_email_to_user(email):
    global mailer_api_url
    url = mailer_api_url + 'sendMail'
    try:
        response_data = request_from_api(email, url, "POST")
    except Exception as ex:
        print('Exception in Mail-Sender:', ex)
        response_data = {}
    return response_data
