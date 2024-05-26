# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import torchbearer_pb2 as torchbearer__pb2

GRPC_GENERATED_VERSION = '1.64.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in torchbearer_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class TorchBearerGRPCAgentStub(object):
    """Interface exported by the server.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.initialize = channel.unary_unary(
                '/torchdeeprl.TorchBearerGRPCAgent/initialize',
                request_serializer=torchbearer__pb2.Config.SerializeToString,
                response_deserializer=torchbearer__pb2.Confirmation.FromString,
                _registered_method=True)
        self.step = channel.unary_unary(
                '/torchdeeprl.TorchBearerGRPCAgent/step',
                request_serializer=torchbearer__pb2.Percept.SerializeToString,
                response_deserializer=torchbearer__pb2.Matrix.FromString,
                _registered_method=True)


class TorchBearerGRPCAgentServicer(object):
    """Interface exported by the server.
    """

    def initialize(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def step(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TorchBearerGRPCAgentServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'initialize': grpc.unary_unary_rpc_method_handler(
                    servicer.initialize,
                    request_deserializer=torchbearer__pb2.Config.FromString,
                    response_serializer=torchbearer__pb2.Confirmation.SerializeToString,
            ),
            'step': grpc.unary_unary_rpc_method_handler(
                    servicer.step,
                    request_deserializer=torchbearer__pb2.Percept.FromString,
                    response_serializer=torchbearer__pb2.Matrix.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'torchdeeprl.TorchBearerGRPCAgent', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('torchdeeprl.TorchBearerGRPCAgent', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TorchBearerGRPCAgent(object):
    """Interface exported by the server.
    """

    @staticmethod
    def initialize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/torchdeeprl.TorchBearerGRPCAgent/initialize',
            torchbearer__pb2.Config.SerializeToString,
            torchbearer__pb2.Confirmation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def step(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/torchdeeprl.TorchBearerGRPCAgent/step',
            torchbearer__pb2.Percept.SerializeToString,
            torchbearer__pb2.Matrix.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)