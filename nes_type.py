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
