from utils import log
from nes_instruction import instruction_list


def nes_disassembler(nes_code):
    assemblers_code = []
    pc = 0

    while pc < len(nes_code):
        op = nes_code[pc]
        ins = instruction_list[op]
        length = ins['length']

        assemblers_code.append(ins)
        for i in range(1, length):
            assemblers_code.append(nes_code[pc + i])

        log_instruction(pc, op, ins, length)
        pc += length

    return assemblers_code


def log_instruction(pc, op, instruction, length):
    ins_name = instruction['instruction'].name
    log("pc(0x{:0>4x}) op(0x{:0>2x}) {} {}".format(pc, op, ins_name, length))


def load_nes_code(file_path):
    nes_code = []
    with open(file_path, 'rb') as f:
        # 抛弃前 16 个字节
        data = f.readline(16)
        # 读取真正的数据
        data = f.read()
        for i in data:
            nes_code.append(i)

    return nes_code


def main():
    file_path = "test.nes"
    nes_code = load_nes_code(file_path)
    log(nes_code)

    nes_disassembler(nes_code)


if __name__ == '__main__':
    main()
