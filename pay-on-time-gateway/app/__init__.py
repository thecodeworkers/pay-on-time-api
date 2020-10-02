from flask import jsonify, request
from grpc import RpcError, insecure_channel
from google.protobuf.json_format import MessageToDict
from marshmallow import ValidationError
from .protos import ExchangeStub, SendCryptoRequest
from .constants import HOST, PORT, DEBUG, PROVIDER_HOST
from .schemas import SendMoneyInput, PayrollInput
from .utils import error_response
from .bootstrap import app

@app.errorhandler(404)
def page_not_found(error):
    return { 'result': 'not_found' }, 404

@app.route('/send-money', methods=['POST'])
def send_money():
    try:
        schema = SendMoneyInput()
        data = schema.load(request.json)
        response = send(data['address'], data['amount'])

        return jsonify(response)

    except RpcError as error:
        response_error = error_response(error)
        return jsonify(response_error), 400

    except ValidationError as err:
        return jsonify(err.messages), 400

@app.route('/payroll', methods=['POST'])
def payroll():
    try:
        schema = PayrollInput()
        data = schema.load(request.json)

        total_amount = (data['amount'] * data['btc_total_amount']) / data['usd_total_amount']
        total_amount = round(total_amount, 8)

        response = send(data['address'], total_amount)
        return jsonify(response)

    except RpcError as error:
        response_error = error_response(error)
        return jsonify(response_error), 400

    except ValidationError as err:
        return jsonify(err.messages), 400


def send(address, amount):
    channel = insecure_channel(PROVIDER_HOST)
    stub = ExchangeStub(channel)

    request_grpc = SendCryptoRequest(address=address, amount=amount)
    response = stub.send_crypto(request_grpc)

    return MessageToDict(response)


def run_server():
    app.run(host=HOST, port=PORT, debug=DEBUG)
