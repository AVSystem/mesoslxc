# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: containerizer.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

import mesos_pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name='containerizer.proto',
    package='mesoslxc.interface',
    serialized_pb=_b(
        '\n\x13\x63ontainerizer.proto\x12\x12mesoslxc.interface\x1a\x0bmesos.proto\"\xa0\x02\n\x06Launch\x12\x35\n\x0c\x63ontainer_id\x18\x01 \x02(\x0b\x32\x1f.mesoslxc.interface.ContainerID\x12/\n\ttask_info\x18\x02 \x01(\x0b\x32\x1c.mesoslxc.interface.TaskInfo\x12\x37\n\rexecutor_info\x18\x03 \x01(\x0b\x32 .mesoslxc.interface.ExecutorInfo\x12\x11\n\tdirectory\x18\x04 \x01(\t\x12\x0c\n\x04user\x18\x05 \x01(\t\x12-\n\x08slave_id\x18\x06 \x01(\x0b\x32\x1b.mesoslxc.interface.SlaveID\x12\x11\n\tslave_pid\x18\x07 \x01(\t\x12\x12\n\ncheckpoint\x18\x08 \x01(\x08\"p\n\x06Update\x12\x35\n\x0c\x63ontainer_id\x18\x01 \x02(\x0b\x32\x1f.mesoslxc.interface.ContainerID\x12/\n\tresources\x18\x02 \x03(\x0b\x32\x1c.mesoslxc.interface.Resource\"=\n\x04Wait\x12\x35\n\x0c\x63ontainer_id\x18\x01 \x02(\x0b\x32\x1f.mesoslxc.interface.ContainerID\"@\n\x07\x44\x65stroy\x12\x35\n\x0c\x63ontainer_id\x18\x01 \x02(\x0b\x32\x1f.mesoslxc.interface.ContainerID\">\n\x05Usage\x12\x35\n\x0c\x63ontainer_id\x18\x01 \x02(\x0b\x32\x1f.mesoslxc.interface.ContainerID\">\n\x0bTermination\x12\x0e\n\x06killed\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x02(\t\x12\x0e\n\x06status\x18\x03 \x01(\x05\"A\n\nContainers\x12\x33\n\ncontainers\x18\x01 \x03(\x0b\x32\x1f.mesoslxc.interface.ContainerIDB(\n\x1eorg.apache.mesos.containerizerB\x06Protos')
    ,
    dependencies=[mesos_pb2.DESCRIPTOR, ])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_LAUNCH = _descriptor.Descriptor(
    name='Launch',
    full_name='mesoslxc.interface.Launch',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='container_id', full_name='mesoslxc.interface.Launch.container_id', index=0,
            number=1, type=11, cpp_type=10, label=2,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='task_info', full_name='mesoslxc.interface.Launch.task_info', index=1,
            number=2, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='executor_info', full_name='mesoslxc.interface.Launch.executor_info', index=2,
            number=3, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='directory', full_name='mesoslxc.interface.Launch.directory', index=3,
            number=4, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='user', full_name='mesoslxc.interface.Launch.user', index=4,
            number=5, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='slave_id', full_name='mesoslxc.interface.Launch.slave_id', index=5,
            number=6, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='slave_pid', full_name='mesoslxc.interface.Launch.slave_pid', index=6,
            number=7, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='checkpoint', full_name='mesoslxc.interface.Launch.checkpoint', index=7,
            number=8, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
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
    oneofs=[
    ],
    serialized_start=57,
    serialized_end=345,
)

_UPDATE = _descriptor.Descriptor(
    name='Update',
    full_name='mesoslxc.interface.Update',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='container_id', full_name='mesoslxc.interface.Update.container_id', index=0,
            number=1, type=11, cpp_type=10, label=2,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='resources', full_name='mesoslxc.interface.Update.resources', index=1,
            number=2, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
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
    oneofs=[
    ],
    serialized_start=347,
    serialized_end=459,
)

_WAIT = _descriptor.Descriptor(
    name='Wait',
    full_name='mesoslxc.interface.Wait',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='container_id', full_name='mesoslxc.interface.Wait.container_id', index=0,
            number=1, type=11, cpp_type=10, label=2,
            has_default_value=False, default_value=None,
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
    oneofs=[
    ],
    serialized_start=461,
    serialized_end=522,
)

_DESTROY = _descriptor.Descriptor(
    name='Destroy',
    full_name='mesoslxc.interface.Destroy',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='container_id', full_name='mesoslxc.interface.Destroy.container_id', index=0,
            number=1, type=11, cpp_type=10, label=2,
            has_default_value=False, default_value=None,
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
    oneofs=[
    ],
    serialized_start=524,
    serialized_end=588,
)

_USAGE = _descriptor.Descriptor(
    name='Usage',
    full_name='mesoslxc.interface.Usage',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='container_id', full_name='mesoslxc.interface.Usage.container_id', index=0,
            number=1, type=11, cpp_type=10, label=2,
            has_default_value=False, default_value=None,
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
    oneofs=[
    ],
    serialized_start=590,
    serialized_end=652,
)

_TERMINATION = _descriptor.Descriptor(
    name='Termination',
    full_name='mesoslxc.interface.Termination',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='killed', full_name='mesoslxc.interface.Termination.killed', index=0,
            number=1, type=8, cpp_type=7, label=2,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='message', full_name='mesoslxc.interface.Termination.message', index=1,
            number=2, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='status', full_name='mesoslxc.interface.Termination.status', index=2,
            number=3, type=5, cpp_type=1, label=1,
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
    oneofs=[
    ],
    serialized_start=654,
    serialized_end=716,
)

_CONTAINERS = _descriptor.Descriptor(
    name='Containers',
    full_name='mesoslxc.interface.Containers',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='containers', full_name='mesoslxc.interface.Containers.containers', index=0,
            number=1, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
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
    oneofs=[
    ],
    serialized_start=718,
    serialized_end=783,
)

_LAUNCH.fields_by_name['container_id'].message_type = mesos_pb2._CONTAINERID
_LAUNCH.fields_by_name['task_info'].message_type = mesos_pb2._TASKINFO
_LAUNCH.fields_by_name['executor_info'].message_type = mesos_pb2._EXECUTORINFO
_LAUNCH.fields_by_name['slave_id'].message_type = mesos_pb2._SLAVEID
_UPDATE.fields_by_name['container_id'].message_type = mesos_pb2._CONTAINERID
_UPDATE.fields_by_name['resources'].message_type = mesos_pb2._RESOURCE
_WAIT.fields_by_name['container_id'].message_type = mesos_pb2._CONTAINERID
_DESTROY.fields_by_name['container_id'].message_type = mesos_pb2._CONTAINERID
_USAGE.fields_by_name['container_id'].message_type = mesos_pb2._CONTAINERID
_CONTAINERS.fields_by_name['containers'].message_type = mesos_pb2._CONTAINERID
DESCRIPTOR.message_types_by_name['Launch'] = _LAUNCH
DESCRIPTOR.message_types_by_name['Update'] = _UPDATE
DESCRIPTOR.message_types_by_name['Wait'] = _WAIT
DESCRIPTOR.message_types_by_name['Destroy'] = _DESTROY
DESCRIPTOR.message_types_by_name['Usage'] = _USAGE
DESCRIPTOR.message_types_by_name['Termination'] = _TERMINATION
DESCRIPTOR.message_types_by_name['Containers'] = _CONTAINERS

Launch = _reflection.GeneratedProtocolMessageType('Launch', (_message.Message,), dict(
    DESCRIPTOR=_LAUNCH,
    __module__='containerizer_pb2'
    # @@protoc_insertion_point(class_scope:mesoslxc.interface.Launch)
))
_sym_db.RegisterMessage(Launch)

Update = _reflection.GeneratedProtocolMessageType('Update', (_message.Message,), dict(
    DESCRIPTOR=_UPDATE,
    __module__='containerizer_pb2'
    # @@protoc_insertion_point(class_scope:mesoslxc.interface.Update)
))
_sym_db.RegisterMessage(Update)

Wait = _reflection.GeneratedProtocolMessageType('Wait', (_message.Message,), dict(
    DESCRIPTOR=_WAIT,
    __module__='containerizer_pb2'
    # @@protoc_insertion_point(class_scope:mesoslxc.interface.Wait)
))
_sym_db.RegisterMessage(Wait)

Destroy = _reflection.GeneratedProtocolMessageType('Destroy', (_message.Message,), dict(
    DESCRIPTOR=_DESTROY,
    __module__='containerizer_pb2'
    # @@protoc_insertion_point(class_scope:mesoslxc.interface.Destroy)
))
_sym_db.RegisterMessage(Destroy)

Usage = _reflection.GeneratedProtocolMessageType('Usage', (_message.Message,), dict(
    DESCRIPTOR=_USAGE,
    __module__='containerizer_pb2'
    # @@protoc_insertion_point(class_scope:mesoslxc.interface.Usage)
))
_sym_db.RegisterMessage(Usage)

Termination = _reflection.GeneratedProtocolMessageType('Termination', (_message.Message,), dict(
    DESCRIPTOR=_TERMINATION,
    __module__='containerizer_pb2'
    # @@protoc_insertion_point(class_scope:mesoslxc.interface.Termination)
))
_sym_db.RegisterMessage(Termination)

Containers = _reflection.GeneratedProtocolMessageType('Containers', (_message.Message,), dict(
    DESCRIPTOR=_CONTAINERS,
    __module__='containerizer_pb2'
    # @@protoc_insertion_point(class_scope:mesoslxc.interface.Containers)
))
_sym_db.RegisterMessage(Containers)

DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(),
                                                _b('\n\036org.apache.mesos.containerizerB\006Protos'))
# @@protoc_insertion_point(module_scope)
