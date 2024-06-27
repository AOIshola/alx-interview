#!/usr/bin/env python3
"""Validate utf-8"""


def validUTF8(data):
    def get_byte_type(byte):
        """ Determine the type of byte based
        on the number of leading 1s """
        if byte & 0x80 == 0x00:  # 0xxxxxxx
            return 1
        elif byte & 0xE0 == 0xC0:  # 110xxxxx
            return 2
        elif byte & 0xF0 == 0xE0:  # 1110xxxx
            return 3
        elif byte & 0xF8 == 0xF0:  # 11110xxx
            return 4
        else:
            return -1

    def is_continuation_byte(byte):
        """ Check if the byte is a valid
        continuation byte (10xxxxxx) """
        return byte & 0xC0 == 0x80

    i = 0
    while i < len(data):
        byte_type = get_byte_type(data[i])
        if byte_type == -1:
            return False
        if byte_type == 1:
            i += 1
        else:
            if i + byte_type > len(data):
                return False
            for j in range(1, byte_type):
                if not is_continuation_byte(data[i + j]):
                    return False
            i += byte_type
    return True
