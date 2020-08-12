import json

def error_response(error):
    response_error = error.details()
    response_error = response_error.replace("\'", "\"")
    response_error = json.loads(response_error)

    return response_error
