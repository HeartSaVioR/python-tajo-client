# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tajo_protos.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tajo_protos.proto',
  package='',
  serialized_pb='\n\x11tajo_protos.proto\"\xa5\x01\n\x19WorkerConnectionInfoProto\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0c\n\x04host\x18\x02 \x02(\t\x12\x13\n\x0bpeerRpcPort\x18\x03 \x02(\x05\x12\x16\n\x0epullServerPort\x18\x04 \x02(\x05\x12\x17\n\x0fqueryMasterPort\x18\x05 \x01(\x05\x12\x12\n\nclientPort\x18\x06 \x02(\x05\x12\x14\n\x0chttpInfoPort\x18\x07 \x02(\x05*\xe7\x01\n\nQueryState\x12\x15\n\x11QUERY_MASTER_INIT\x10\x00\x12\x19\n\x15QUERY_MASTER_LAUNCHED\x10\x01\x12\r\n\tQUERY_NEW\x10\x02\x12\x0e\n\nQUERY_INIT\x10\x03\x12\x11\n\rQUERY_RUNNING\x10\x04\x12\x13\n\x0fQUERY_SUCCEEDED\x10\x05\x12\x10\n\x0cQUERY_FAILED\x10\x06\x12\x10\n\x0cQUERY_KILLED\x10\x07\x12\x13\n\x0fQUERY_KILL_WAIT\x10\x08\x12\x0f\n\x0bQUERY_ERROR\x10\t\x12\x16\n\x12QUERY_NOT_ASSIGNED\x10\n*\xa4\x01\n\x10TaskAttemptState\x12\n\n\x06TA_NEW\x10\x00\x12\x11\n\rTA_UNASSIGNED\x10\x01\x12\x0f\n\x0bTA_ASSIGNED\x10\x02\x12\x0e\n\nTA_PENDING\x10\x03\x12\x0e\n\nTA_RUNNING\x10\x04\x12\x10\n\x0cTA_SUCCEEDED\x10\x05\x12\r\n\tTA_FAILED\x10\x06\x12\x10\n\x0cTA_KILL_WAIT\x10\x07\x12\r\n\tTA_KILLED\x10\x08*X\n\x0c\x46\x65tcherState\x12\x0e\n\nFETCH_INIT\x10\x00\x12\x12\n\x0e\x46\x45TCH_FETCHING\x10\x01\x12\x12\n\x0e\x46\x45TCH_FINISHED\x10\x02\x12\x10\n\x0c\x46\x45TCH_FAILED\x10\x03\x42#\n\x0forg.apache.tajoB\nTajoProtos\x88\x01\x00\xa0\x01\x01')

_QUERYSTATE = _descriptor.EnumDescriptor(
  name='QueryState',
  full_name='QueryState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='QUERY_MASTER_INIT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUERY_MASTER_LAUNCHED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUERY_NEW', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUERY_INIT', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUERY_RUNNING', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUERY_SUCCEEDED', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUERY_FAILED', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUERY_KILLED', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUERY_KILL_WAIT', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUERY_ERROR', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUERY_NOT_ASSIGNED', index=10, number=10,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=190,
  serialized_end=421,
)

QueryState = enum_type_wrapper.EnumTypeWrapper(_QUERYSTATE)
_TASKATTEMPTSTATE = _descriptor.EnumDescriptor(
  name='TaskAttemptState',
  full_name='TaskAttemptState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TA_NEW', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TA_UNASSIGNED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TA_ASSIGNED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TA_PENDING', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TA_RUNNING', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TA_SUCCEEDED', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TA_FAILED', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TA_KILL_WAIT', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TA_KILLED', index=8, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=424,
  serialized_end=588,
)

TaskAttemptState = enum_type_wrapper.EnumTypeWrapper(_TASKATTEMPTSTATE)
_FETCHERSTATE = _descriptor.EnumDescriptor(
  name='FetcherState',
  full_name='FetcherState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FETCH_INIT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FETCH_FETCHING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FETCH_FINISHED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FETCH_FAILED', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=590,
  serialized_end=678,
)

FetcherState = enum_type_wrapper.EnumTypeWrapper(_FETCHERSTATE)
QUERY_MASTER_INIT = 0
QUERY_MASTER_LAUNCHED = 1
QUERY_NEW = 2
QUERY_INIT = 3
QUERY_RUNNING = 4
QUERY_SUCCEEDED = 5
QUERY_FAILED = 6
QUERY_KILLED = 7
QUERY_KILL_WAIT = 8
QUERY_ERROR = 9
QUERY_NOT_ASSIGNED = 10
TA_NEW = 0
TA_UNASSIGNED = 1
TA_ASSIGNED = 2
TA_PENDING = 3
TA_RUNNING = 4
TA_SUCCEEDED = 5
TA_FAILED = 6
TA_KILL_WAIT = 7
TA_KILLED = 8
FETCH_INIT = 0
FETCH_FETCHING = 1
FETCH_FINISHED = 2
FETCH_FAILED = 3



_WORKERCONNECTIONINFOPROTO = _descriptor.Descriptor(
  name='WorkerConnectionInfoProto',
  full_name='WorkerConnectionInfoProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='WorkerConnectionInfoProto.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='host', full_name='WorkerConnectionInfoProto.host', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='peerRpcPort', full_name='WorkerConnectionInfoProto.peerRpcPort', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pullServerPort', full_name='WorkerConnectionInfoProto.pullServerPort', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='queryMasterPort', full_name='WorkerConnectionInfoProto.queryMasterPort', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='clientPort', full_name='WorkerConnectionInfoProto.clientPort', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='httpInfoPort', full_name='WorkerConnectionInfoProto.httpInfoPort', index=6,
      number=7, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=22,
  serialized_end=187,
)

DESCRIPTOR.message_types_by_name['WorkerConnectionInfoProto'] = _WORKERCONNECTIONINFOPROTO

class WorkerConnectionInfoProto(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _WORKERCONNECTIONINFOPROTO

  # @@protoc_insertion_point(class_scope:WorkerConnectionInfoProto)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\017org.apache.tajoB\nTajoProtos\210\001\000\240\001\001')
# @@protoc_insertion_point(module_scope)