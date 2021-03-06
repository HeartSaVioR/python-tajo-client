import socket
import io
import py.RpcProtos_pb2 as rpc_pb2
from channel import RpcChannel
from proto_util import ProtoUtils

class TajoRpcChannel(RpcChannel):
    def prepareRequest(self, method, request):
        rpc_request = rpc_pb2.RpcRequest()
        rpc_request.id = 1
        rpc_request.method_name = method.name
        rpc_request.request_message = request.SerializeToString()
        return rpc_request

    def sendRequest(self, rpc_request):
        data = rpc_request.SerializeToString()
        lenbytes = ProtoUtils.EncodeVarint(len(data))
        return [lenbytes, data]

    def recevieResponse(self, handle):
        try:
            byte_stream = self.readMoreN(handle, 4)
            v, l = ProtoUtils.DecodeVarint(byte_stream)
            byte_stream = byte_stream[l:]
            size = len(byte_stream)
            if size < (v-l):
                byte_stream += self.readMoreN(handle, v-l)

            rpc_response = rpc_pb2.RpcResponse()
            rpc_response.ParseFromString(byte_stream)
            return rpc_response

        except socket.error:
            self.closeSocket(sock)
            raise Exception("Error reading data from server")

    def parseResponse(self, rpc_response, response_class):
        response = response_class()

        byte_stream = rpc_response.response_message
        try:
            response.ParseFromString(byte_stream)
        except Exception, e:
            raise Exception("Invalid response (decodeError): " + str(e))

        return response

