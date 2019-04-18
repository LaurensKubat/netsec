#!/usr/bin/env python3
import socket
import struct

def parse_ethernet(packet):
    # an 802.1Q tag is present if the if is true
    (tagbuf,) = struct.unpack_from("!H", packet[13:15])
    if tagbuf & 0x8100 == 0x8100:
        hastag = True
        (eth_dest_addr, eth_dest, eth_src, eth_src_addr, tag, typecode) = struct.unpack_from("!LHHLLH", buffer=packet)
        data = packet[19:]
    else:
        (eth_dest_addr, eth_dest, eth_src, eth_src_addr, typecode) = struct.unpack_from("!LHHLH", buffer=packet)
        hastag = False
        tag = 0
        data = packet[15:]
    return eth_dest_addr, eth_dest, eth_src, eth_src_addr, hastag, tag, typecode, data

def parse_ip(packet):
    # unpack all relevant info from the ip header, non relevant info according to the assignment is discarded
    (versionIHL, ToS, total_length, identification, flags_offset, ttl, protocol,
     checksum, source_address, dest_address) = struct.unpack_from("!BBHHHBBH4s4s", buffer=packet)
    IHL = (packet[0] & 0xf) * 4 + 20  # the + 20 seems to be necessary to get the udp packets
    dotted_source = socket.inet_ntoa(source_address)
    dotted_dest = socket.inet_ntoa(dest_address)
    print("protocol: {}, IHL: {}".format(protocol, IHL))
    data = packet[IHL:]
    return total_length, protocol, dotted_source, dotted_dest, data


def parse_udp(packet):
    header_length = 8
    header = packet[:header_length + 1]
    data = packet[header_length:]
    (source_port, dest_port, data_length, checksum) = struct.unpack_from("!HHHH", header)
    return source_port, dest_port, data_length, checksum, data


def main():
    s = socket.socket(family=socket.AF_PACKET, type=socket.SOCK_RAW, proto=socket.ntohs(0x0003))
    for i in range(1000): # we parse a thousand packets
        packet, addr = s.recvfrom(size)
        print(addr)
        eth_dest_addr, eth_dest, eth_src, eth_src_addr, hastag, tag, typecode, rest_data = parse_ethernet(packet)
        print(eth_dest_addr)
        print(eth_src_addr)
        if typecode == 0x0800:
            total_length, protocol, dotted_source, dotted_dest, data = parse_ip(rest_data)
            #print("total length: {}\nprotocol: {}\n source_ip: {}\n destination_ip: {}\n".format(total_length,
             #   protocol, dotted_source, dotted_dest))
            if protocol == 17: # somehow protocol is never 17
                source_port, dest_port, data_length, checksum, data = parse_udp(data)
                print("Source Port: {}\nDestination Port: {}\n"
                        "Data length: {}\nChecksum: {}\n".format(source_port, dest_port, data_length, checksum))
                print(data)
            else:
                continue

if __name__ == '__main__':
    size = 65535
    main()
