from marshmallow import Schema, fields, ValidationError, validate

class SendMoneyInput(Schema):
    address = fields.Str(required=True)
    amount = fields.Float(required=True)

class PayrollInput(SendMoneyInput):
    btc_total_amount = fields.Float(required=True)
    usd_total_amount = fields.Float(required=True, validate=validate.Range(min=1))
