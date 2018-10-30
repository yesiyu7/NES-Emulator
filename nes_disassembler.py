from utils import log
from nes_type import TypeInstruction, TypeMode


def instruction_init(instruction, mode, length):
    ins = {
        'instruction': instruction,
        'mode': mode,
        'length': length,
    }

    return ins


def nes_disassembler(nes_code):
    instruction_list = {
        0x00: instruction_init(TypeInstruction.BRK, TypeMode.Implied, 1),
        0x01: instruction_init(TypeInstruction.ORA, TypeMode.Indexed_indirect, 2),
        0x05: instruction_init(TypeInstruction.ORA, TypeMode.Zero_page, 2),
        0x06: instruction_init(TypeInstruction.ASL, TypeMode.Zero_page, 2),
        0x08: instruction_init(TypeInstruction.PHP, TypeMode.Implied, 1),
        0x09: instruction_init(TypeInstruction.ORA, TypeMode.Immediate, 2),
        0x0a: instruction_init(TypeInstruction.ASL, TypeMode.Accumulator, 1),
        0x0d: instruction_init(TypeInstruction.ORA, TypeMode.Absolute, 3),
        0x0e: instruction_init(TypeInstruction.ASL, TypeMode.Absolute, 3),
        0x10: instruction_init(TypeInstruction.BPL, TypeMode.Relative, 2),
        0x11: instruction_init(TypeInstruction.ORA, TypeMode.Indirect_indexed, 2),
        0x15: instruction_init(TypeInstruction.ORA, TypeMode.Zero_page_x, 2),
        0x16: instruction_init(TypeInstruction.ASL, TypeMode.Zero_page_x, 2),
        0x18: instruction_init(TypeInstruction.CLC, TypeMode.Implied, 1),
        0x19: instruction_init(TypeInstruction.ORA, TypeMode.Absolute_y, 3),
        0x1d: instruction_init(TypeInstruction.ORA, TypeMode.Absolute_x, 3),
        0x1e: instruction_init(TypeInstruction.ASL, TypeMode.Absolute_x, 3),
        0x20: instruction_init(TypeInstruction.JSR, TypeMode.Absolute, 3),
        0x21: instruction_init(TypeInstruction.AND, TypeMode.Indexed_indirect, 2),
        0x24: instruction_init(TypeInstruction.BIT, TypeMode.Zero_page, 2),
        0x25: instruction_init(TypeInstruction.AND, TypeMode.Zero_page, 2),
        0x26: instruction_init(TypeInstruction.ROL, TypeMode.Zero_page, 2),
        0x28: instruction_init(TypeInstruction.PLP, TypeMode.Implied, 1),
        0x29: instruction_init(TypeInstruction.AND, TypeMode.Immediate, 2),
        0x2a: instruction_init(TypeInstruction.ROL, TypeMode.Accumulator, 1),
        0x2c: instruction_init(TypeInstruction.BIT, TypeMode.Absolute, 3),
        0x2d: instruction_init(TypeInstruction.AND, TypeMode.Absolute, 3),
        0x2e: instruction_init(TypeInstruction.ROL, TypeMode.Absolute, 3),
        0x30: instruction_init(TypeInstruction.BMI, TypeMode.Relative, 2),
        0x31: instruction_init(TypeInstruction.AND, TypeMode.Indirect_indexed, 2),
        0x35: instruction_init(TypeInstruction.AND, TypeMode.Zero_page_x, 2),
        0x36: instruction_init(TypeInstruction.ROL, TypeMode.Zero_page_x, 2),
        0x38: instruction_init(TypeInstruction.SEC, TypeMode.Implied, 1),
        0x39: instruction_init(TypeInstruction.AND, TypeMode.Absolute_y, 3),
        0x3d: instruction_init(TypeInstruction.AND, TypeMode.Absolute_x, 3),
        0x3e: instruction_init(TypeInstruction.ROL, TypeMode.Absolute_x, 3),
        0x40: instruction_init(TypeInstruction.RTI, TypeMode.Implied, 1),
        0x41: instruction_init(TypeInstruction.EOR, TypeMode.Indexed_indirect, 2),
        0x45: instruction_init(TypeInstruction.EOR, TypeMode.Zero_page, 2),
        0x46: instruction_init(TypeInstruction.LSR, TypeMode.Zero_page, 2),
        0x48: instruction_init(TypeInstruction.PHA, TypeMode.Implied, 1),
        0x49: instruction_init(TypeInstruction.EOR, TypeMode.Immediate, 2),
        0x4a: instruction_init(TypeInstruction.LSR, TypeMode.Accumulator, 1),
        0x4c: instruction_init(TypeInstruction.JMP, TypeMode.Absolute, 3),
        0x4d: instruction_init(TypeInstruction.EOR, TypeMode.Absolute, 3),
        0x4e: instruction_init(TypeInstruction.LSR, TypeMode.Absolute, 3),
        0x50: instruction_init(TypeInstruction.BVC, TypeMode.Relative, 2),
        0x51: instruction_init(TypeInstruction.EOR, TypeMode.Indirect_indexed, 2),
        0x55: instruction_init(TypeInstruction.EOR, TypeMode.Zero_page_x, 2),
        0x56: instruction_init(TypeInstruction.LSR, TypeMode.Zero_page_x, 2),
        0x58: instruction_init(TypeInstruction.CLI, TypeMode.Implied, 1),
        0x59: instruction_init(TypeInstruction.EOR, TypeMode.Absolute_y, 3),
        0x5d: instruction_init(TypeInstruction.EOR, TypeMode.Absolute_x, 3),
        0x5e: instruction_init(TypeInstruction.LSR, TypeMode.Absolute_x, 3),
        0x60: instruction_init(TypeInstruction.RTS, TypeMode.Implied, 1),
        0x61: instruction_init(TypeInstruction.ADC, TypeMode.Indexed_indirect, 1),
        0x65: instruction_init(TypeInstruction.ADC, TypeMode.Zero_page, 2),
        0x66: instruction_init(TypeInstruction.ROR, TypeMode.Zero_page, 2),
        0x68: instruction_init(TypeInstruction.PLA, TypeMode.Implied, 1),
        0x69: instruction_init(TypeInstruction.ADC, TypeMode.Immediate, 2),
        0x6a: instruction_init(TypeInstruction.ROR, TypeMode.Accumulator, 1),
        0x6c: instruction_init(TypeInstruction.JMP, TypeMode.Indirect, 3),
        0x6d: instruction_init(TypeInstruction.ADC, TypeMode.Absolute, 3),
        0x6e: instruction_init(TypeInstruction.ROR, TypeMode.Absolute_x, 3),
        0x70: instruction_init(TypeInstruction.BVS, TypeMode.Relative, 2),
        0x71: instruction_init(TypeInstruction.ADC, TypeMode.Indirect_indexed, 2),
        0x75: instruction_init(TypeInstruction.ADC, TypeMode.Zero_page_x, 2),
        0x76: instruction_init(TypeInstruction.ROR, TypeMode.Zero_page_x, 2),
        0x78: instruction_init(TypeInstruction.SEI, TypeMode.Implied, 1),
        0x79: instruction_init(TypeInstruction.ADC, TypeMode.Absolute_y, 3),
        0x7d: instruction_init(TypeInstruction.ADC, TypeMode.Absolute_x, 3),
        0x7e: instruction_init(TypeInstruction.ROR, TypeMode.Absolute, 3),
        0x81: instruction_init(TypeInstruction.STA, TypeMode.Indexed_indirect, 2),
        0x84: instruction_init(TypeInstruction.STY, TypeMode.Zero_page, 2),
        0x85: instruction_init(TypeInstruction.STA, TypeMode.Zero_page, 2),
        0x86: instruction_init(TypeInstruction.STX, TypeMode.Zero_page, 2),
        0x88: instruction_init(TypeInstruction.DEY, TypeMode.Implied, 1),
        0x8a: instruction_init(TypeInstruction.TXA, TypeMode.Implied, 1),
        0x8c: instruction_init(TypeInstruction.STY, TypeMode.Absolute, 3),
        0x8d: instruction_init(TypeInstruction.STA, TypeMode.Absolute, 3),
        0x8e: instruction_init(TypeInstruction.STX, TypeMode.Absolute, 3),
        0x90: instruction_init(TypeInstruction.BCC, TypeMode.Relative, 2),
        0x91: instruction_init(TypeInstruction.STA, TypeMode.Indirect_indexed, 2),
        0x94: instruction_init(TypeInstruction.STY, TypeMode.Zero_page_x, 2),
        0x95: instruction_init(TypeInstruction.STA, TypeMode.Zero_page_x, 2),
        0x96: instruction_init(TypeInstruction.STX, TypeMode.Zero_page_y, 2),
        0x98: instruction_init(TypeInstruction.TYA, TypeMode.Implied, 1),
        0x99: instruction_init(TypeInstruction.STA, TypeMode.Absolute_y, 3),
        0x9a: instruction_init(TypeInstruction.TXS, TypeMode.Implied, 1),
        0x9d: instruction_init(TypeInstruction.STA, TypeMode.Absolute_x, 3),
        0xa0: instruction_init(TypeInstruction.LDY, TypeMode.Immediate, 2),
        0xa1: instruction_init(TypeInstruction.LDA, TypeMode.Indexed_indirect, 2),
        0xa2: instruction_init(TypeInstruction.LDX, TypeMode.Immediate, 2),
        0xa4: instruction_init(TypeInstruction.LDY, TypeMode.Zero_page, 2),
        0xa5: instruction_init(TypeInstruction.LDA, TypeMode.Zero_page, 2),
        0xa6: instruction_init(TypeInstruction.LDX, TypeMode.Zero_page, 2),
        0xa8: instruction_init(TypeInstruction.TAY, TypeMode.Implied, 1),
        0xa9: instruction_init(TypeInstruction.LDA, TypeMode.Immediate, 2),
        0xaa: instruction_init(TypeInstruction.TAX, TypeMode.Implied, 1),
        0xac: instruction_init(TypeInstruction.LDY, TypeMode.Absolute, 3),
        0xad: instruction_init(TypeInstruction.LDA, TypeMode.Absolute, 3),
        0xae: instruction_init(TypeInstruction.LDX, TypeMode.Absolute, 3),
        0xb0: instruction_init(TypeInstruction.BCS, TypeMode.Relative, 2),
        0xb1: instruction_init(TypeInstruction.LDA, TypeMode.Indirect_indexed, 2),
        0xb4: instruction_init(TypeInstruction.LDY, TypeMode.Zero_page_x, 2),
        0xb5: instruction_init(TypeInstruction.LDA, TypeMode.Zero_page_x, 2),
        0xb6: instruction_init(TypeInstruction.LDX, TypeMode.Zero_page_y, 2),
        0xb8: instruction_init(TypeInstruction.CLV, TypeMode.Implied, 1),
        0xb9: instruction_init(TypeInstruction.LDA, TypeMode.Absolute_y, 3),
        0xba: instruction_init(TypeInstruction.TSX, TypeMode.Implied, 1),
        0xbc: instruction_init(TypeInstruction.LDY, TypeMode.Absolute_x, 3),
        0xbd: instruction_init(TypeInstruction.LDA, TypeMode.Absolute_x, 3),
        0xbe: instruction_init(TypeInstruction.LDX, TypeMode.Absolute_y, 3),
        0xc0: instruction_init(TypeInstruction.CPY, TypeMode.Immediate, 2),
        0xc1: instruction_init(TypeInstruction.CMP, TypeMode.Indexed_indirect, 2),
        0xc4: instruction_init(TypeInstruction.CPY, TypeMode.Zero_page, 2),
        0xc5: instruction_init(TypeInstruction.CMP, TypeMode.Zero_page, 2),
        0xc6: instruction_init(TypeInstruction.DEC, TypeMode.Zero_page, 2),
        0xc8: instruction_init(TypeInstruction.INY, TypeMode.Implied, 1),
        0xc9: instruction_init(TypeInstruction.CMP, TypeMode.Immediate, 2),
        0xca: instruction_init(TypeInstruction.DEX, TypeMode.Implied, 1),
        0xcc: instruction_init(TypeInstruction.CPY, TypeMode.Absolute, 3),
        0xcd: instruction_init(TypeInstruction.CMP, TypeMode.Absolute, 3),
        0xce: instruction_init(TypeInstruction.DEC, TypeMode.Absolute, 3),
        0xd0: instruction_init(TypeInstruction.BNE, TypeMode.Relative, 2),
        0xd1: instruction_init(TypeInstruction.CMP, TypeMode.Indirect_indexed, 2),
        0xd5: instruction_init(TypeInstruction.CMP, TypeMode.Zero_page_x, 2),
        0xd6: instruction_init(TypeInstruction.DEC, TypeMode.Zero_page_x, 2),
        0xd8: instruction_init(TypeInstruction.CLD, TypeMode.Implied, 1),
        0xd9: instruction_init(TypeInstruction.CMP, TypeMode.Absolute_y, 3),
        0xdd: instruction_init(TypeInstruction.CMP, TypeMode.Absolute_x, 3),
        0xde: instruction_init(TypeInstruction.DEC, TypeMode.Absolute_x, 3),
        0xe0: instruction_init(TypeInstruction.CPX, TypeMode.Immediate, 2),
        0xe1: instruction_init(TypeInstruction.SBC, TypeMode.Indexed_indirect, 2),
        0xe4: instruction_init(TypeInstruction.CPX, TypeMode.Zero_page, 2),
        0xe5: instruction_init(TypeInstruction.SBC, TypeMode.Zero_page, 2),
        0xe6: instruction_init(TypeInstruction.INC, TypeMode.Zero_page, 2),
        0xe8: instruction_init(TypeInstruction.INX, TypeMode.Implied, 1),
        0xe9: instruction_init(TypeInstruction.SBC, TypeMode.Immediate, 2),
        0xea: instruction_init(TypeInstruction.NOP, TypeMode.Implied, 1),
        0xec: instruction_init(TypeInstruction.CPX, TypeMode.Absolute, 3),
        0xed: instruction_init(TypeInstruction.SBC, TypeMode.Absolute, 3),
        0xee: instruction_init(TypeInstruction.INC, TypeMode.Absolute, 3),
        0xf0: instruction_init(TypeInstruction.BEQ, TypeMode.Relative, 2),
        0xf1: instruction_init(TypeInstruction.SBC, TypeMode.Indirect_indexed, 2),
        0xf5: instruction_init(TypeInstruction.SBC, TypeMode.Zero_page_x, 2),
        0xf6: instruction_init(TypeInstruction.INC, TypeMode.Zero_page_x, 2),
        0xf8: instruction_init(TypeInstruction.SED, TypeMode.Implied, 1),
        0xf9: instruction_init(TypeInstruction.SBC, TypeMode.Absolute_y, 3),
        0xfd: instruction_init(TypeInstruction.SBC, TypeMode.Absolute_x, 3),
        0xfe: instruction_init(TypeInstruction.INC, TypeMode.Absolute_x, 3),
    }

    assemblers_code = []
    pc = 0

    while pc < len(nes_code):
        op = nes_code[pc]
        ins = instruction_list[op]
        length = ins['length']

        assemblers_code.append(ins)
        for i in range(1, length):
            assemblers_code.append(nes_code[pc + i])

        pc += length
        log_assembler_code(pc, op, ins, length)

    return assemblers_code


def log_assembler_code(pc, op, instruction, n):
    ins_name = instruction['instruction'].name
    log("pc(0x{:0>4x}) op(0x{:0>2x}) {} {}".format(pc, op, ins_name, n))


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
