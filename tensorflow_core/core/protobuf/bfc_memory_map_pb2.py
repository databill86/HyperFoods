# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/protobuf/bfc_memory_map.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/protobuf/bfc_memory_map.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n-tensorflow/core/protobuf/bfc_memory_map.proto\x12\ntensorflow\"\x92\x01\n\x11MemAllocatorStats\x12\x12\n\nnum_allocs\x18\x01 \x01(\x03\x12\x14\n\x0c\x62ytes_in_use\x18\x02 \x01(\x03\x12\x19\n\x11peak_bytes_in_use\x18\x03 \x01(\x03\x12\x1a\n\x12largest_alloc_size\x18\x04 \x01(\x03\x12\x1c\n\x14\x66ragmentation_metric\x18\x05 \x01(\x02\"\xae\x01\n\x08MemChunk\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x04\x12\x0c\n\x04size\x18\x02 \x01(\x03\x12\x16\n\x0erequested_size\x18\x03 \x01(\x03\x12\x0b\n\x03\x62in\x18\x04 \x01(\x05\x12\x0f\n\x07op_name\x18\x05 \x01(\t\x12\x16\n\x0e\x66reed_at_count\x18\x06 \x01(\x04\x12\x14\n\x0c\x61\x63tion_count\x18\x07 \x01(\x04\x12\x0e\n\x06in_use\x18\x08 \x01(\x08\x12\x0f\n\x07step_id\x18\t \x01(\x04\"\x8b\x01\n\nBinSummary\x12\x0b\n\x03\x62in\x18\x01 \x01(\x05\x12\x1a\n\x12total_bytes_in_use\x18\x02 \x01(\x03\x12\x1a\n\x12total_bytes_in_bin\x18\x03 \x01(\x03\x12\x1b\n\x13total_chunks_in_use\x18\x04 \x01(\x03\x12\x1b\n\x13total_chunks_in_bin\x18\x05 \x01(\x03\".\n\x08SnapShot\x12\x14\n\x0c\x61\x63tion_count\x18\x01 \x01(\x04\x12\x0c\n\x04size\x18\x02 \x01(\x03\"\xcd\x01\n\nMemoryDump\x12\x16\n\x0e\x61llocator_name\x18\x01 \x01(\t\x12+\n\x0b\x62in_summary\x18\x02 \x03(\x0b\x32\x16.tensorflow.BinSummary\x12#\n\x05\x63hunk\x18\x03 \x03(\x0b\x32\x14.tensorflow.MemChunk\x12\'\n\tsnap_shot\x18\x04 \x03(\x0b\x32\x14.tensorflow.SnapShot\x12,\n\x05stats\x18\x05 \x01(\x0b\x32\x1d.tensorflow.MemAllocatorStatsb\x06proto3')
)




_MEMALLOCATORSTATS = _descriptor.Descriptor(
  name='MemAllocatorStats',
  full_name='tensorflow.MemAllocatorStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_allocs', full_name='tensorflow.MemAllocatorStats.num_allocs', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytes_in_use', full_name='tensorflow.MemAllocatorStats.bytes_in_use', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='peak_bytes_in_use', full_name='tensorflow.MemAllocatorStats.peak_bytes_in_use', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='largest_alloc_size', full_name='tensorflow.MemAllocatorStats.largest_alloc_size', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fragmentation_metric', full_name='tensorflow.MemAllocatorStats.fragmentation_metric', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=62,
  serialized_end=208,
)


_MEMCHUNK = _descriptor.Descriptor(
  name='MemChunk',
  full_name='tensorflow.MemChunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='tensorflow.MemChunk.address', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='tensorflow.MemChunk.size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requested_size', full_name='tensorflow.MemChunk.requested_size', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bin', full_name='tensorflow.MemChunk.bin', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='op_name', full_name='tensorflow.MemChunk.op_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='freed_at_count', full_name='tensorflow.MemChunk.freed_at_count', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action_count', full_name='tensorflow.MemChunk.action_count', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='in_use', full_name='tensorflow.MemChunk.in_use', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='step_id', full_name='tensorflow.MemChunk.step_id', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=211,
  serialized_end=385,
)


_BINSUMMARY = _descriptor.Descriptor(
  name='BinSummary',
  full_name='tensorflow.BinSummary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bin', full_name='tensorflow.BinSummary.bin', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_bytes_in_use', full_name='tensorflow.BinSummary.total_bytes_in_use', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_bytes_in_bin', full_name='tensorflow.BinSummary.total_bytes_in_bin', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_chunks_in_use', full_name='tensorflow.BinSummary.total_chunks_in_use', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_chunks_in_bin', full_name='tensorflow.BinSummary.total_chunks_in_bin', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=388,
  serialized_end=527,
)


_SNAPSHOT = _descriptor.Descriptor(
  name='SnapShot',
  full_name='tensorflow.SnapShot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action_count', full_name='tensorflow.SnapShot.action_count', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='tensorflow.SnapShot.size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=529,
  serialized_end=575,
)


_MEMORYDUMP = _descriptor.Descriptor(
  name='MemoryDump',
  full_name='tensorflow.MemoryDump',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='allocator_name', full_name='tensorflow.MemoryDump.allocator_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bin_summary', full_name='tensorflow.MemoryDump.bin_summary', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chunk', full_name='tensorflow.MemoryDump.chunk', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='snap_shot', full_name='tensorflow.MemoryDump.snap_shot', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stats', full_name='tensorflow.MemoryDump.stats', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=578,
  serialized_end=783,
)

_MEMORYDUMP.fields_by_name['bin_summary'].message_type = _BINSUMMARY
_MEMORYDUMP.fields_by_name['chunk'].message_type = _MEMCHUNK
_MEMORYDUMP.fields_by_name['snap_shot'].message_type = _SNAPSHOT
_MEMORYDUMP.fields_by_name['stats'].message_type = _MEMALLOCATORSTATS
DESCRIPTOR.message_types_by_name['MemAllocatorStats'] = _MEMALLOCATORSTATS
DESCRIPTOR.message_types_by_name['MemChunk'] = _MEMCHUNK
DESCRIPTOR.message_types_by_name['BinSummary'] = _BINSUMMARY
DESCRIPTOR.message_types_by_name['SnapShot'] = _SNAPSHOT
DESCRIPTOR.message_types_by_name['MemoryDump'] = _MEMORYDUMP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MemAllocatorStats = _reflection.GeneratedProtocolMessageType('MemAllocatorStats', (_message.Message,), {
  'DESCRIPTOR' : _MEMALLOCATORSTATS,
  '__module__' : 'tensorflow.core.protobuf.bfc_memory_map_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.MemAllocatorStats)
  })
_sym_db.RegisterMessage(MemAllocatorStats)

MemChunk = _reflection.GeneratedProtocolMessageType('MemChunk', (_message.Message,), {
  'DESCRIPTOR' : _MEMCHUNK,
  '__module__' : 'tensorflow.core.protobuf.bfc_memory_map_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.MemChunk)
  })
_sym_db.RegisterMessage(MemChunk)

BinSummary = _reflection.GeneratedProtocolMessageType('BinSummary', (_message.Message,), {
  'DESCRIPTOR' : _BINSUMMARY,
  '__module__' : 'tensorflow.core.protobuf.bfc_memory_map_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.BinSummary)
  })
_sym_db.RegisterMessage(BinSummary)

SnapShot = _reflection.GeneratedProtocolMessageType('SnapShot', (_message.Message,), {
  'DESCRIPTOR' : _SNAPSHOT,
  '__module__' : 'tensorflow.core.protobuf.bfc_memory_map_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.SnapShot)
  })
_sym_db.RegisterMessage(SnapShot)

MemoryDump = _reflection.GeneratedProtocolMessageType('MemoryDump', (_message.Message,), {
  'DESCRIPTOR' : _MEMORYDUMP,
  '__module__' : 'tensorflow.core.protobuf.bfc_memory_map_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.MemoryDump)
  })
_sym_db.RegisterMessage(MemoryDump)


# @@protoc_insertion_point(module_scope)
