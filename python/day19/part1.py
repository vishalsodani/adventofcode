registers = [0, 0, 0, 0, 0, 0]
instructions = []

def execute(opcode, register_val):
    
    if opcode[0] == 'gtrr':
        if registers[opcode[1]] > registers[opcode[2]]:
            val = 1
        else:
            val = 0
    if opcode[0] == 'gtri':
        if registers[opcode[1]] > opcode[2]:
            val = 1
        else:
            val = 0
    if opcode[0] == 'gtir':
        if opcode[1] > registers[opcode[2]]:
            val = 1
        else:
            val = 0

    if opcode[0] == 'seti':
        val = opcode[1]
    if opcode[0] == 'addr':
        val = registers[opcode[1]] + registers[opcode[2]]
    if opcode[0] == 'setr':
        val = registers[opcode[1]]
    if opcode[0] == 'addi':
        val = registers[opcode[1]] + opcode[2]

    if opcode[0] == 'mulr':
        val = registers[opcode[1]] * registers[opcode[2]]

    if opcode[0] == 'muli':
        val = registers[opcode[1]] * opcode[2]

    if opcode[0] == 'eqrr':
        if registers[opcode[1]] == registers[opcode[2]]:
            val = 1
        else:
            val = 0
    if opcode[0] == 'eqri':
        if registers[opcode[1]] == opcode[2]:
            val = 1
        else:
            val = 0
    if opcode[0] == 'eqir':
        if opcode[1] == registers[opcode[2]]:
            val = 1
        else:
            val = 0

    registers[opcode[3]] = val

    register_val = registers[3]
    register_val += 1

    return register_val

with open('input.txt') as fp:
    for input in fp:
        data = input.strip().split(' ')
        instructions.append([data[0], int(data[1]), int(data[2]), int(data[3])])

register_val = 0

while register_val < 37:
    registers[3] = register_val
    register_val = execute(instructions[register_val], register_val)


print(registers)