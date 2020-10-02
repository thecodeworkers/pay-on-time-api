# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/services/exchange/exchange.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='app/services/exchange/exchange.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n$app/services/exchange/exchange.proto\"K\n\x11SendCryptoRequest\x12\x15\n\x08\x63urrency\x18\x01 \x01(\t:\x03\x42TC\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x02(\t\x12\x0e\n\x06\x61mount\x18\x03 \x02(\x01\"$\n\x12SendCryptoResponse\x12\x0e\n\x06result\x18\x01 \x02(\t2B\n\x08\x45xchange\x12\x36\n\x0bsend_crypto\x12\x12.SendCryptoRequest\x1a\x13.SendCryptoResponse'
)




_SENDCRYPTOREQUEST = _descriptor.Descriptor(
  name='SendCryptoRequest',
  full_name='SendCryptoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='currency', full_name='SendCryptoRequest.currency', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=b"BTC".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='SendCryptoRequest.address', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='SendCryptoRequest.amount', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=115,
)


_SENDCRYPTORESPONSE = _descriptor.Descriptor(
  name='SendCryptoResponse',
  full_name='SendCryptoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='SendCryptoResponse.result', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=153,
)

DESCRIPTOR.message_types_by_name['SendCryptoRequest'] = _SENDCRYPTOREQUEST
DESCRIPTOR.message_types_by_name['SendCryptoResponse'] = _SENDCRYPTORESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SendCryptoRequest = _reflection.GeneratedProtocolMessageType('SendCryptoRequest', (_message.Message,), {
  'DESCRIPTOR' : _SENDCRYPTOREQUEST,
  '__module__' : 'app.services.exchange.exchange_pb2'
  # @@protoc_insertion_point(class_scope:SendCryptoRequest)
  })
_sym_db.RegisterMessage(SendCryptoRequest)

SendCryptoResponse = _reflection.GeneratedProtocolMessageType('SendCryptoResponse', (_message.Message,), {
  'DESCRIPTOR' : _SENDCRYPTORESPONSE,
  '__module__' : 'app.services.exchange.exchange_pb2'
  # @@protoc_insertion_point(class_scope:SendCryptoResponse)
  })
_sym_db.RegisterMessage(SendCryptoResponse)



_EXCHANGE = _descriptor.ServiceDescriptor(
  name='Exchange',
  full_name='Exchange',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=155,
  serialized_end=221,
  methods=[
  _descriptor.MethodDescriptor(
    name='send_crypto',
    full_name='Exchange.send_crypto',
    index=0,
    containing_service=None,
    input_type=_SENDCRYPTOREQUEST,
    output_type=_SENDCRYPTORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EXCHANGE)

DESCRIPTOR.services_by_name['Exchange'] = _EXCHANGE

# @@protoc_insertion_point(module_scope)
