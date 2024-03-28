from convert import convert_to_byte, byte_to_dec, byte_to_hex
import pdb


def main():

    get_input = True

    name_blocks = []
    size_blocks = []
    unit_blocks = []

    print("Insert memory characteristics:")
    memory_size = int(input("Memory size: "))
    memory_unit = input("Memory unit [B, KB, MB, GB]: ")

    print("Insert block memory characteristics:")
    while True:

        name = input("Insert name block memory:")
        if name is None:
            break

        size = int(input("Insert size block memory:"))
        if size is None:
            break

        unit = input("Insert unit block memory [B, KB, MB, GB]:")
        if unit is None:
            break

        name_blocks.append(name)
        size_blocks.append(size)
        unit_blocks.append(unit)

        get_input = input("Do you want to insert another block memory? (y/n)")
        if get_input == "n":
            break

    if len(name_blocks) == 0:
        print("No blocks memory inserted")
        return

    memory_size_byte = convert_to_byte(memory_size, memory_unit)
    blocks_size_byte = [convert_to_byte(size_blocks[ii], unit_blocks[ii]) for ii in range(len(name_blocks))]

    start_addr_byte = 0  # Start address

    for ii in range(len(name_blocks)):

        print("---------------------")
        print("Block memory: ", name_blocks[ii])
        print("Start address (dec): ", start_addr_byte)
        print("End address (dec): ", start_addr_byte + blocks_size_byte[ii] - 1)
        print("Start address (hex): ", byte_to_hex(start_addr_byte))
        print("End address (hex): ", byte_to_hex(start_addr_byte + blocks_size_byte[ii] - 1))

        start_addr_byte += blocks_size_byte[ii]

    if int(memory_size_byte) < int(start_addr_byte):
        print("Memory size is not enough")
        return
    
    print("---------------------")

    if int(memory_size_byte) > int(start_addr_byte):
        # Print the remaining memory
        print("Remaining memory")
        print("Start address (dec): ", start_addr_byte)
        print("End address (dec): ", int(memory_size_byte) - 1)
        print("Start address (hex): ", byte_to_hex(start_addr_byte))
        print("End address (hex): ", byte_to_hex(int(memory_size_byte) - 1))
        print("---------------------")


if __name__ == "__main__":
    main()
