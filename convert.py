import argparse


def convert_to_byte(num, units):

    if units == "B":
        return num
    elif units == "KB":
        return num * 1024
    elif units == "MB":
        return num * 1024 * 1024
    elif units == "GB":
        return num * 1024 * 1024 * 1024
    else:
        raise ValueError("Invalid units")


def byte_to_dec(num):
    return num * 8


def byte_to_hex(num):
    return hex(byte_to_dec(num))


def main():

    parser = argparse.ArgumentParser(description="Convert units")
    parser.add_argument("num", type=int, help="Number to convert")
    parser.add_argument("units", type=str, help="Units to convert from")
    args = parser.parse_args()

    print(f"Input: {args.num} {args.units}")
    hex_num = byte_to_dec(convert_to_byte(args.num, args.units))
    print(f"Output: {hex_num}")


if __name__ == "__main__":
    main()
