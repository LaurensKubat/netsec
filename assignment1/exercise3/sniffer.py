#!/usr/bin/env python3
import socket
import struct


def parse_ip(packet):
    # unpack all relevant info from the ip header, non relevant info according to the assignment is discarded
    (versionIHL, ToS, total_length, identification, flagsoffset, ttl, protocol,
     checksum, source_address, dest_address) = struct.unpack_from("!ccHHHccH4s4s", buffer=packet)
    IHL = (ord(versionIHL) & 0x0F) * 4
    dotted_source = socket.inet_ntoa(source_address)
    dotted_dest = socket.inet_ntoa(dest_address)
    data = packet[:IHL]
    return total_length, protocol, dotted_source, dotted_dest, data


def parse_udp(packet):
    header_length = 8
    header = packet[:header_length]
    data = packet[:header_length]
    (source_port, dest_port, data_length, checksum) = struct.unpack("!HHHH", header)
    return source_port, dest_port, data_length, checksum, data


def main():
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_RAW, proto=socket.IPPROTO_UDP)
    packet, addr = s.recvfrom(size)
    total_length, protocol, dotted_source, dotted_dest, data = parse_ip(packet)
    print("total length: {}\nprotocol: {}\n source_ip: {}\n destination_ip: {}\n".format(total_length,
            protocol, dotted_source, dotted_dest))
    source_port, dest_port, data_length, checksum, data = parse_udp(data)
    print("Source Port: {}\nDestination Port: {}\n"
          "Data length: {}\nChecksum: {}\n".format(source_port, dest_port, data_length, checksum))
    print(data)


if __name__ == '__main__':
    size = 65535
    main()
