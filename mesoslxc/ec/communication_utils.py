import struct
import sys


class ComminicationUtils():
    @staticmethod
    # Read a data chunk prefixed by its total size from stdin.
    def receive(log):
        # Read size (uint32 => 4 bytes).
        size = struct.unpack('I', sys.stdin.read(4))
        if size[0] <= 0:
            log.error("Expected protobuf size over stdin. Received 0 bytes.")
            sys.exit(1)
        # Read payload.
        data = sys.stdin.read(size[0])
        if len(data) != size[0]:
            log.error("Expected %d bytes protobuf over stdin. Received %d bytes." % (size[0], len(data)))
            sys.exit(1)

        return data

    # Write a protobuf message prefixed by its total size (aka recordio)
    # to stdout.
    @staticmethod
    def send(data):
        # Write size (uint32 => 4 bytes).
        sys.stdout.write(struct.pack('I', len(data)))

        # Write payload.
        sys.stdout.write(data)
