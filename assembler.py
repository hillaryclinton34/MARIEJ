"""
The assembler passes through the instruction list created by fileread.py twice - the first pass collects label data
and associates a label with an address. The second pass actually encodes the instructions into the memory.
"""

from fileread import readFile, getLabel, getInst, toInt

# dictionary to give each opcode a value to be used during assembly
OPCODES = {
    'LOAD':     1,
    'STORE':    2,
    'ADD':      3,
    'SUBTRACT': 4,
    'INPUT':    5,
    'OUTPUT':   6,
    'HALT':     7
}

def pass1(lines):
    variable_table = {}
    LC = 0
    for line in lines:
        label, other = getLabel(line)
        # ties a label to a memory address using LC (location counter)
        if label:
            variable_table[label] = LC
        inst, value = getInst(other)
        if inst:
            LC += 1
    return variable_table

def pass2(lines, variable_table):
    memory = [0] * 4096
    LC = 0

    for line in lines:
        label, other = getLabel(line)
        inst, value = getInst(other)

        if not inst:
            # can happen if line is only a label name
            continue

        if inst == 'DEC':
            num = toInt(value)
            memory[LC] = num

        elif inst in OPCODES:
            opcode = OPCODES[inst]
            opval = variable_table.get(value)
            # uses multiples of 4096 to store the opcode (4 leftmost bits) in the address - binary structure without binary numbers
            memory[LC] = opcode * 4096 + opval

        else:
            raise ValueError(f"Unknown instruction: {inst}")

        LC += 1
        if LC >= 4096:
            raise MemoryError("Out of memory")

    return memory

def assemble(file)
    # perform assembly on a passed file
    lines = readFile(file)
    var_table = pass1(lines)
    mem = pass2(lines, var_table)
    return mem
