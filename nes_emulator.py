from utils import log
from nes_instruction import instruction_list


MEMORY_SIZE = 1 << 16
HEADER_SIZE = 1 << 4
PRG_ROM_SIZE = 1 << 14
CHR_ROM_SIZE = 1 << 13


def load_nes_code(file_path):
    nes_code = []
    with open(file_path, 'rb') as f:
        data = f.read()
        for i in data:
            nes_code.append(i)

    return nes_code


def load_prg_rom(memory, prg_rom):
    for i in range(PRG_ROM_SIZE):
        memory[0x8000 + i] = prg_rom[i]
        memory[0xc000 + i] = prg_rom[i]


def emulator_init(nes_code):
    memory = [0 for i in range(MEMORY_SIZE)]

    header = nes_code[:HEADER_SIZE]
    prg_rom = nes_code[HEADER_SIZE:HEADER_SIZE + PRG_ROM_SIZE]
    chr_rom = nes_code[HEADER_SIZE + PRG_ROM_SIZE:]

    load_prg_rom(memory, prg_rom)

    return memory


def emulator_run(memory):
    cpu = {
        'A': 0,
        'X': 0,
        'Y': 0,
        'PC': 0xfffc,
        'S': 0x00fd,
        'P': {
            'C': 0,
            'Z': 1,
            'I': 0,
            'D': 0,
            'V': 0,
            'N': 0,
        },
    }
    pc = cpu['PC']


def log_instruction(pc, op, instruction, length):
    ins_name = instruction['instruction'].name
    log("pc(0x{:0>4x}) op(0x{:0>2x}) {} {}".format(pc, op, ins_name, length))


def main():
    file_path = "test.nes"
    nes_code = load_nes_code(file_path)
    memory = emulator_init(nes_code)
    emulator_run(memory)


if __name__ == '__main__':
    main()
