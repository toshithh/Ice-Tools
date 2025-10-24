import struct

def sid_hex_to_str(hex_string: str) -> str:
    sid_bytes = bytes.fromhex(hex_string)

    # unpack revision and subauthority count
    revision, sub_count = struct.unpack('BB', sid_bytes[:2])

    # identifier authority (6 bytes, big endian)
    id_auth = int.from_bytes(sid_bytes[2:8], 'big')

    # subauthorities (each 4 bytes, little endian)
    subs = struct.unpack('<' + 'I' * sub_count, sid_bytes[8:8 + 4 * sub_count])

    # format SID string
    return f"S-{revision}-{id_auth}-" + "-".join(str(s) for s in subs)


# Example usage with your hex string
hex_sid = input('Binary SID: ')
print(sid_hex_to_str(hex_sid))
