# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: image_detection_3.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import image_1_pb2 as image__1__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='image_detection_3.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17image_detection_3.proto\x1a\rimage_1.proto\"j\n\x0b\x42oundingBox\x12\x0b\n\x03top\x18\x01 \x01(\x05\x12\x0c\n\x04left\x18\x02 \x01(\x05\x12\x0e\n\x06\x62ottom\x18\x03 \x01(\x05\x12\r\n\x05right\x18\x04 \x01(\x05\x12\r\n\x05label\x18\x05 \x01(\t\x12\x12\n\nconfidence\x18\x06 \x01(\x02\"\x83\x01\n\x14ImageDetectionResult\x12\x15\n\x05image\x18\x01 \x01(\x0b\x32\x06.Image\x12#\n\rboundingBoxes\x18\x02 \x03(\x0b\x32\x0c.BoundingBox\x12\x1f\n\x0f\x64\x65tectedObjects\x18\x03 \x03(\x0b\x32\x06.Image\x12\x0e\n\x06sentAt\x18\x04 \x01(\x02\"]\n\x15ImageDetectionResults\x12\x34\n\x15imageDetectionResults\x18\x01 \x03(\x0b\x32\x15.ImageDetectionResult\x12\x0e\n\x06sentAt\x18\x02 \x01(\x02\x32\x35\n\x05\x42rick\x12,\n\x07process\x12\x07.Images\x1a\x16.ImageDetectionResults\"\x00\x62\x06proto3'
  ,
  dependencies=[image__1__pb2.DESCRIPTOR,])




_BOUNDINGBOX = _descriptor.Descriptor(
  name='BoundingBox',
  full_name='BoundingBox',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='top', full_name='BoundingBox.top', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='left', full_name='BoundingBox.left', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bottom', full_name='BoundingBox.bottom', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='right', full_name='BoundingBox.right', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='BoundingBox.label', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='BoundingBox.confidence', index=5,
      number=6, type=2, cpp_type=6, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=42,
  serialized_end=148,
)


_IMAGEDETECTIONRESULT = _descriptor.Descriptor(
  name='ImageDetectionResult',
  full_name='ImageDetectionResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='ImageDetectionResult.image', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='boundingBoxes', full_name='ImageDetectionResult.boundingBoxes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='detectedObjects', full_name='ImageDetectionResult.detectedObjects', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sentAt', full_name='ImageDetectionResult.sentAt', index=3,
      number=4, type=2, cpp_type=6, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=151,
  serialized_end=282,
)


_IMAGEDETECTIONRESULTS = _descriptor.Descriptor(
  name='ImageDetectionResults',
  full_name='ImageDetectionResults',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='imageDetectionResults', full_name='ImageDetectionResults.imageDetectionResults', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sentAt', full_name='ImageDetectionResults.sentAt', index=1,
      number=2, type=2, cpp_type=6, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=284,
  serialized_end=377,
)

_IMAGEDETECTIONRESULT.fields_by_name['image'].message_type = image__1__pb2._IMAGE
_IMAGEDETECTIONRESULT.fields_by_name['boundingBoxes'].message_type = _BOUNDINGBOX
_IMAGEDETECTIONRESULT.fields_by_name['detectedObjects'].message_type = image__1__pb2._IMAGE
_IMAGEDETECTIONRESULTS.fields_by_name['imageDetectionResults'].message_type = _IMAGEDETECTIONRESULT
DESCRIPTOR.message_types_by_name['BoundingBox'] = _BOUNDINGBOX
DESCRIPTOR.message_types_by_name['ImageDetectionResult'] = _IMAGEDETECTIONRESULT
DESCRIPTOR.message_types_by_name['ImageDetectionResults'] = _IMAGEDETECTIONRESULTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BoundingBox = _reflection.GeneratedProtocolMessageType('BoundingBox', (_message.Message,), {
  'DESCRIPTOR' : _BOUNDINGBOX,
  '__module__' : 'image_detection_3_pb2'
  # @@protoc_insertion_point(class_scope:BoundingBox)
  })
_sym_db.RegisterMessage(BoundingBox)

ImageDetectionResult = _reflection.GeneratedProtocolMessageType('ImageDetectionResult', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEDETECTIONRESULT,
  '__module__' : 'image_detection_3_pb2'
  # @@protoc_insertion_point(class_scope:ImageDetectionResult)
  })
_sym_db.RegisterMessage(ImageDetectionResult)

ImageDetectionResults = _reflection.GeneratedProtocolMessageType('ImageDetectionResults', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEDETECTIONRESULTS,
  '__module__' : 'image_detection_3_pb2'
  # @@protoc_insertion_point(class_scope:ImageDetectionResults)
  })
_sym_db.RegisterMessage(ImageDetectionResults)



_BRICK = _descriptor.ServiceDescriptor(
  name='Brick',
  full_name='Brick',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=379,
  serialized_end=432,
  methods=[
  _descriptor.MethodDescriptor(
    name='process',
    full_name='Brick.process',
    index=0,
    containing_service=None,
    input_type=image__1__pb2._IMAGES,
    output_type=_IMAGEDETECTIONRESULTS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BRICK)

DESCRIPTOR.services_by_name['Brick'] = _BRICK

# @@protoc_insertion_point(module_scope)
