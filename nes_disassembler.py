import struct
from enum import Enum


def auto_number():
    n = 0

    def _auto_number():
        nonlocal n
        n += 1
        return n

    return _auto_number

auto_number = auto_number()


class TypeInstruction(Enum):
    ADC = auto_number()
    AND = auto_number()
    ASL = auto_number()
    BCC = auto_number()
    BCS = auto_number()
    BEQ = auto_number()
    BIT = auto_number()
    BMI = auto_number()
    BNE = auto_number()
    BPL = auto_number()
    BRK = auto_number()
    BVC = auto_number()
    BVS = auto_number()
    CLC = auto_number()
    CLD = auto_number()
    CLI = auto_number()
    CLV = auto_number()
    CMP = auto_number()
    CPX = auto_number()
    CPY = auto_number()
    DEC = auto_number()
    DEX = auto_number()
    DEY = auto_number()
    EOR = auto_number()
    INC = auto_number()
    INX = auto_number()
    INY = auto_number()
    JMP = auto_number()
    JSR = auto_number()
    LDA = auto_number()
    LDX = auto_number()
    LDY = auto_number()
    LSR = auto_number()
    NOP = auto_number()
    ORA = auto_number()
    PHA = auto_number()
    PHP = auto_number()
    PLA = auto_number()
    PLP = auto_number()
    ROL = auto_number()
    ROR = auto_number()
    RTI = auto_number()
    RTS = auto_number()
    SBC = auto_number()
    SEC = auto_number()
    SED = auto_number()
    SEI = auto_number()
    STA = auto_number()
    STY = auto_number()
    STX = auto_number()
    TAX = auto_number()
    TAY = auto_number()
    TSX = auto_number()
    TXA = auto_number()
    TXS = auto_number()
    TYA = auto_number()


class TypeMode(Enum):
    Implied = auto_number()
    Immediate = auto_number()
    Indirect = auto_number()
    Indexed_indirect = auto_number()
    Indirect_indexed = auto_number()
    Zero_page = auto_number()
    Zero_page_x = auto_number()
    Zero_page_y = auto_number()
    Absolute = auto_number()
    Absolute_x = auto_number()
    Absolute_y = auto_number()
    Accumulator = auto_number()
    Relative = auto_number()


def nes_disassembler(code):
    opcode = {
        0x00: {
            'instruction': TypeInstruction.BRK,
            'mode': TypeMode.Implied,
        },
        0x01: {
            'instruction': TypeInstruction.ORA,
            'mode': TypeMode.Indexed_indirect,
        },
        0x05: {
            'instruction': TypeInstruction.ORA,
            'mode': TypeMode.Zero_page,
        },
        0x06: {
            'instruction': TypeInstruction.ASL,
            'mode': TypeMode.Zero_page,
        },
        0x08: {
            'instruction': TypeInstruction.PHP,
            'mode': TypeMode.Implied,
        },
        0x09: {
            'instruction': TypeInstruction.ORA,
            'mode': TypeMode.Immediate,
        },
        0x0a: {
            'instruction': TypeInstruction.ASL,
            'mode': TypeMode.Accumulator,
        },
        0x0d: {
            'instruction': TypeInstruction.ORA,
            'mode': TypeMode.Absolute,
        },
        0x0e: {
            'instruction': TypeInstruction.ASL,
            'mode': TypeMode.Absolute,
        },
        0x10: {
            'instruction': TypeInstruction.BPL,
            'mode': TypeMode.Relative,
        },
        0x11: {
            'instruction': TypeInstruction.ORA,
            'mode': TypeMode.Indirect_indexed,
        },
        0x15: {
            'instruction': TypeInstruction.ORA,
            'mode': TypeMode.Zero_page_x,
        },
        0x16: {
            'instruction': TypeInstruction.ASL,
            'mode': TypeMode.Zero_page_x,
        },
        0x18: {
            'instruction': TypeInstruction.CLC,
            'mode': TypeMode.Implied,
        },
        0x19: {
            'instruction': TypeInstruction.ORA,
            'mode': TypeMode.Absolute_y,
        },
        0x1d: {
            'instruction': TypeInstruction.ORA,
            'mode': TypeMode.Absolute_x,
        },
        0x1e: {
            'instruction': TypeInstruction.ASL,
            'mode': TypeMode.Absolute_x,
        },
        0x20: {
            'instruction': TypeInstruction.JSR,
            'mode': TypeMode.Absolute,
        },
        0x21: {
            'instruction': TypeInstruction.AND,
            'mode': TypeMode.Indexed_indirect,
        },
        0x24: {
            'instruction': TypeInstruction.BIT,
            'mode': TypeMode.Zero_page,
        },
        0x25: {
            'instruction': TypeInstruction.AND,
            'mode': TypeMode.Zero_page,
        },
        0x26: {
            'instruction': TypeInstruction.ROL,
            'mode': TypeMode.Zero_page,
        },
        0x28: {
            'instruction': TypeInstruction.PLP,
            'mode': TypeMode.Implied,
        },
        0x29: {
            'instruction': TypeInstruction.AND,
            'mode': TypeMode.Immediate,
        },
        0x2a: {
            'instruction': TypeInstruction.ROL,
            'mode': TypeMode.Accumulator,
        },
        0x2c: {
            'instruction': TypeInstruction.BIT,
            'mode': TypeMode.Absolute,
        },
        0x2d: {
            'instruction': TypeInstruction.AND,
            'mode': TypeMode.Absolute,
        },
        0x2e: {
            'instruction': TypeInstruction.ROL,
            'mode': TypeMode.Absolute,
        },
        0x30: {
            'instruction': TypeInstruction.BMI,
            'mode': TypeMode.Relative,
        },
        0x31: {
            'instruction': TypeInstruction.AND,
            'mode': TypeMode.Indirect_indexed,
        },
        0x35: {
            'instruction': TypeInstruction.AND,
            'mode': TypeMode.Zero_page_x,
        },
        0x36: {
            'instruction': TypeInstruction.ROL,
            'mode': TypeMode.Zero_page_x,
        },
        0x38: {
            'instruction': TypeInstruction.SEC,
            'mode': TypeMode.Implied,
        },
        0x39: {
            'instruction': TypeInstruction.AND,
            'mode': TypeMode.Absolute_y,
        },
        0x3d: {
            'instruction': TypeInstruction.AND,
            'mode': TypeMode.Absolute_x,
        },
        0x3e: {
            'instruction': TypeInstruction.ROL,
            'mode': TypeMode.Absolute_x,
        },
        0x40: {
            'instruction': TypeInstruction.RTI,
            'mode': TypeMode.Implied,
        },
        0x41: {
            'instruction': TypeInstruction.EOR,
            'mode': TypeMode.Indexed_indirect,
        },
        0x45: {
            'instruction': TypeInstruction.EOR,
            'mode': TypeMode.Zero_page,
        },
        0x46: {
            'instruction': TypeInstruction.LSR,
            'mode': TypeMode.Zero_page,
        },
        0x48: {
            'instruction': TypeInstruction.PHA,
            'mode': TypeMode.Implied,
        },
        0x49: {
            'instruction': TypeInstruction.EOR,
            'mode': TypeMode.Immediate,
        },
        0x4a: {
            'instruction': TypeInstruction.LSR,
            'mode': TypeMode.Accumulator,
        },
        0x4c: {
            'instruction': TypeInstruction.JMP,
            'mode': TypeMode.Absolute,
        },
        0x4d: {
            'instruction': TypeInstruction.EOR,
            'mode': TypeMode.Absolute,
        },
        0x4e: {
            'instruction': TypeInstruction.LSR,
            'mode': TypeMode.Absolute,
        },
        0x50: {
            'instruction': TypeInstruction.BVC,
            'mode': TypeMode.Relative,
        },
        0x51: {
            'instruction': TypeInstruction.EOR,
            'mode': TypeMode.Indirect_indexed,
        },
        0x55: {
            'instruction': TypeInstruction.EOR,
            'mode': TypeMode.Zero_page_x,
        },
        0x56: {
            'instruction': TypeInstruction.LSR,
            'mode': TypeMode.Zero_page_x,
        },
        0x58: {
            'instruction': TypeInstruction.CLI,
            'mode': TypeMode.Implied,
        },
        0x59: {
            'instruction': TypeInstruction.EOR,
            'mode': TypeMode.Absolute_y,
        },
        0x5d: {
            'instruction': TypeInstruction.EOR,
            'mode': TypeMode.Absolute_x,
        },
        0x5e: {
            'instruction': TypeInstruction.LSR,
            'mode': TypeMode.Absolute_x,
        },
        0x60: {
            'instruction': TypeInstruction.RTS,
            'mode': TypeMode.Implied,
        },
        0x61: {
            'instruction': TypeInstruction.ADC,
            'mode': TypeMode.Indexed_indirect,
        },
        0x65: {
            'instruction': TypeInstruction.ADC,
            'mode': TypeMode.Zero_page,
        },
        0x66: {
            'instruction': TypeInstruction.ROR,
            'mode': TypeMode.Zero_page,
        },
        0x68: {
            'instruction': TypeInstruction.PLA,
            'mode': TypeMode.Implied,
        },
        0x69: {
            'instruction': TypeInstruction.ADC,
            'mode': TypeMode.Immediate,
        },
        0x6a: {
            'instruction': TypeInstruction.ROR,
            'mode': TypeMode.Accumulator,
        },
        0x6c: {
            'instruction': TypeInstruction.JMP,
            'mode': TypeMode.Indirect,
        },
        0x6d: {
            'instruction': TypeInstruction.ADC,
            'mode': TypeMode.Absolute,
        },
        0x6e: {
            'instruction': TypeInstruction.ROR,
            'mode': TypeMode.Absolute_x,
        },
        0x70: {
            'instruction': TypeInstruction.BVS,
            'mode': TypeMode.Relative,
        },
        0x71: {
            'instruction': TypeInstruction.ADC,
            'mode': TypeMode.Indirect_indexed,
        },
        0x75: {
            'instruction': TypeInstruction.ADC,
            'mode': TypeMode.Zero_page_x,
        },
        0x76: {
            'instruction': TypeInstruction.ROR,
            'mode': TypeMode.Zero_page_x,
        },
        0x78: {
            'instruction': TypeInstruction.SEI,
            'mode': TypeMode.Implied,
        },
        0x79: {
            'instruction': TypeInstruction.ADC,
            'mode': TypeMode.Absolute_y,
        },
        0x7d: {
            'instruction': TypeInstruction.ADC,
            'mode': TypeMode.Absolute_x,
        },
        0x7e: {
            'instruction': TypeInstruction.ROR,
            'mode': TypeMode.Absolute,
        },
        0x81: {
            'instruction': TypeInstruction.STA,
            'mode': TypeMode.Indexed_indirect,
        },
        0x84: {
            'instruction': TypeInstruction.STY,
            'mode': TypeMode.Zero_page,
        },
        0x85: {
            'instruction': TypeInstruction.STA,
            'mode': TypeMode.Zero_page,
        },
        0x86: {
            'instruction': TypeInstruction.STX,
            'mode': TypeMode.Zero_page,
        },
        0x88: {
            'instruction': TypeInstruction.DEY,
            'mode': TypeMode.Implied,
        },
        0x8a: {
            'instruction': TypeInstruction.TXA,
            'mode': TypeMode.Implied,
        },
        0x8c: {
            'instruction': TypeInstruction.STY,
            'mode': TypeMode.Absolute,
        },
        0x8d: {
            'instruction': TypeInstruction.STA,
            'mode': TypeMode.Absolute,
        },
        0x8e: {
            'instruction': TypeInstruction.STX,
            'mode': TypeMode.Absolute,
        },
        0x90: {
            'instruction': TypeInstruction.BCC,
            'mode': TypeMode.Relative,
        },
        0x91: {
            'instruction': TypeInstruction.STA,
            'mode': TypeMode.Indirect_indexed,
        },
        0x94: {
            'instruction': TypeInstruction.STY,
            'mode': TypeMode.Zero_page_x,
        },
        0x95: {
            'instruction': TypeInstruction.STA,
            'mode': TypeMode.Zero_page_x,
        },
        0x96: {
            'instruction': TypeInstruction.STX,
            'mode': TypeMode.Zero_page_y,
        },
        0x98: {
            'instruction': TypeInstruction.TYA,
            'mode': TypeMode.Implied,
        },
        0x99: {
            'instruction': TypeInstruction.STA,
            'mode': TypeMode.Absolute_y,
        },
        0x9a: {
            'instruction': TypeInstruction.TXS,
            'mode': TypeMode.Implied,
        },
        0x9d: {
            'instruction': TypeInstruction.STA,
            'mode': TypeMode.Absolute_x,
        },
        0xa0: {
            'instruction': TypeInstruction.LDY,
            'mode': TypeMode.Immediate,
        },
        0xa1: {
            'instruction': TypeInstruction.LDA,
            'mode': TypeMode.Indexed_indirect,
        },
        0xa2: {
            'instruction': TypeInstruction.LDX,
            'mode': TypeMode.Immediate,
        },
        0xa4: {
            'instruction': TypeInstruction.LDY,
            'mode': TypeMode.Zero_page,
        },
        0xa5: {
            'instruction': TypeInstruction.LDA,
            'mode': TypeMode.Zero_page,
        },
        0xa6: {
            'instruction': TypeInstruction.LDX,
            'mode': TypeMode.Zero_page,
        },
        0xa8: {
            'instruction': TypeInstruction.TAY,
            'mode': TypeMode.Implied,
        },
        0xa9: {
            'instruction': TypeInstruction.LDA,
            'mode': TypeMode.Immediate,
        },
        0xaa: {
            'instruction': TypeInstruction.TAX,
            'mode': TypeMode.Implied,
        },
        0xac: {
            'instruction': TypeInstruction.LDY,
            'mode': TypeMode.Absolute,
        },
        0xad: {
            'instruction': TypeInstruction.LDA,
            'mode': TypeMode.Absolute,
        },
        0xae: {
            'instruction': TypeInstruction.LDX,
            'mode': TypeMode.Absolute,
        },
        0xb0: {
            'instruction': TypeInstruction.BCS,
            'mode': TypeMode.Relative,
        },
        0xb1: {
            'instruction': TypeInstruction.LDA,
            'mode': TypeMode.Indirect_indexed,
        },
        0xb4: {
            'instruction': TypeInstruction.LDY,
            'mode': TypeMode.Zero_page_x,
        },
        0xb5: {
            'instruction': TypeInstruction.LDA,
            'mode': TypeMode.Zero_page_x,
        },
        0xb6: {
            'instruction': TypeInstruction.LDX,
            'mode': TypeMode.Zero_page_y,
        },
        0xb8: {
            'instruction': TypeInstruction.CLV,
            'mode': TypeMode.Implied,
        },
        0xb9: {
            'instruction': TypeInstruction.LDA,
            'mode': TypeMode.Absolute_y,
        },
        0xba: {
            'instruction': TypeInstruction.TSX,
            'mode': TypeMode.Implied,
        },
        0xbc: {
            'instruction': TypeInstruction.LDY,
            'mode': TypeMode.Absolute_x,
        },
        0xbd: {
            'instruction': TypeInstruction.LDA,
            'mode': TypeMode.Absolute_x,
        },
        0xbe: {
            'instruction': TypeInstruction.LDX,
            'mode': TypeMode.Absolute_y,
        },
        0xc0: {
            'instruction': TypeInstruction.CPY,
            'mode': TypeMode.Immediate,
        },
        0xc1: {
            'instruction': TypeInstruction.CMP,
            'mode': TypeMode.Indexed_indirect,
        },
        0xc4: {
            'instruction': TypeInstruction.CPY,
            'mode': TypeMode.Zero_page,
        },
        0xc5: {
            'instruction': TypeInstruction.CMP,
            'mode': TypeMode.Zero_page,
        },
        0xc6: {
            'instruction': TypeInstruction.DEC,
            'mode': TypeMode.Zero_page,
        },
        0xc8: {
            'instruction': TypeInstruction.INY,
            'mode': TypeMode.Implied,
        },
        0xc9: {
            'instruction': TypeInstruction.CMP,
            'mode': TypeMode.Immediate,
        },
        0xca: {
            'instruction': TypeInstruction.DEX,
            'mode': TypeMode.Implied,
        },
        0xcc: {
            'instruction': TypeInstruction.CPY,
            'mode': TypeMode.Absolute,
        },
        0xcd: {
            'instruction': TypeInstruction.CMP,
            'mode': TypeMode.Absolute,
        },
        0xce: {
            'instruction': TypeInstruction.DEC,
            'mode': TypeMode.Absolute,
        },
        0xd0: {
            'instruction': TypeInstruction.BNE,
            'mode': TypeMode.Relative,
        },
        0xd1: {
            'instruction': TypeInstruction.CMP,
            'mode': TypeMode.Indirect_indexed,
        },
        0xd5: {
            'instruction': TypeInstruction.CMP,
            'mode': TypeMode.Zero_page_x,
        },
        0xd6: {
            'instruction': TypeInstruction.DEC,
            'mode': TypeMode.Zero_page_x,
        },
        0xd8: {
            'instruction': TypeInstruction.CLD,
            'mode': TypeMode.Implied,
        },
        0xd9: {
            'instruction': TypeInstruction.CMP,
            'mode': TypeMode.Absolute_y,
        },
        0xdd: {
            'instruction': TypeInstruction.CMP,
            'mode': TypeMode.Absolute_x,
        },
        0xde: {
            'instruction': TypeInstruction.DEC,
            'mode': TypeMode.Absolute_x,
        },
        0xe0: {
            'instruction': TypeInstruction.CPX,
            'mode': TypeMode.Immediate,
        },
        0xe1: {
            'instruction': TypeInstruction.SBC,
            'mode': TypeMode.Indexed_indirect,
        },
        0xe4: {
            'instruction': TypeInstruction.CPX,
            'mode': TypeMode.Zero_page,
        },
        0xe5: {
            'instruction': TypeInstruction.SBC,
            'mode': TypeMode.Zero_page,
        },
        0xe6: {
            'instruction': TypeInstruction.INC,
            'mode': TypeMode.Zero_page,
        },
        0xe8: {
            'instruction': TypeInstruction.INX,
            'mode': TypeMode.Implied,
        },
        0xe9: {
            'instruction': TypeInstruction.SBC,
            'mode': TypeMode.Immediate,
        },
        0xea: {
            'instruction': TypeInstruction.NOP,
            'mode': TypeMode.Implied,
        },
        0xec: {
            'instruction': TypeInstruction.CPX,
            'mode': TypeMode.Absolute,
        },
        0xed: {
            'instruction': TypeInstruction.SBC,
            'mode': TypeMode.Absolute,
        },
        0xee: {
            'instruction': TypeInstruction.INC,
            'mode': TypeMode.Absolute,
        },
        0xf0: {
            'instruction': TypeInstruction.BEQ,
            'mode': TypeMode.Relative,
        },
        0xf1: {
            'instruction': TypeInstruction.SBC,
            'mode': TypeMode.Indirect_indexed,
        },
        0xf5: {
            'instruction': TypeInstruction.SBC,
            'mode': TypeMode.Zero_page_x,
        },
        0xf6: {
            'instruction': TypeInstruction.INC,
            'mode': TypeMode.Zero_page_x,
        },
        0xf8: {
            'instruction': TypeInstruction.SED,
            'mode': TypeMode.Implied,
        },
        0xf9: {
            'instruction': TypeInstruction.SBC,
            'mode': TypeMode.Absolute_y,
        },
        0xfd: {
            'instruction': TypeInstruction.SBC,
            'mode': TypeMode.Absolute_x,
        },
        0xfe: {
            'instruction': TypeInstruction.INC,
            'mode': TypeMode.Absolute_x,
        },
    }

    print(opcode[0])
    print(auto_number())


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
    print(nes_code)

    nes_disassembler(nes_code)


if __name__ == '__main__':
    main()
