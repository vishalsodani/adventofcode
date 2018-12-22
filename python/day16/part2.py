register = [0, 0, 0, 0]

def performOperation(opcode):
    if opcode[0] == 0:
        val = register[opcode[1]] & register[opcode[2]]
    if opcode[0] == 1:
        val = register[opcode[1]] + register[opcode[2]]
    if opcode[0] == 2:
        if register[opcode[1]] == opcode[2]:
            val = 1
        else:
            val = 0
    if opcode[0] == 3:
        val = register[opcode[1]]
    if opcode[0] == 4:
        if register[opcode[1]] > register[opcode[2]]:
            val = 1
        else:
            val = 0
    if opcode[0] == 5:
        val = register[opcode[1]] | opcode[2]
    if opcode[0] == 6:
        if opcode[1] > register[opcode[2]]:
            val = 1
        else:
            val = 0
    if opcode[0] == 7:
        val = opcode[1]
    if opcode[0] == 8:
        val = register[opcode[1]] | register[opcode[2]]
    if opcode[0] == 9:
        val = register[opcode[1]] & opcode[2]
    if opcode[0] == 10:
        if opcode[1] == register[opcode[2]]:
            val = 1
        else:
            val = 0
    if opcode[0] == 11:
        if register[opcode[1]] == register[opcode[2]]:
            val = 1
        else:
            val = 0
    if opcode[0] == 12:
        if register[opcode[1]] > opcode[2]:
            val = 1
        else:
            val = 0
    if opcode[0] == 13:
        val = register[opcode[1]] + opcode[2]
    if opcode[0] == 14:
        val = register[opcode[1]] * opcode[2]
    if opcode[0] == 15:
        val = register[opcode[1]] * register[opcode[2]]
    
    register[opcode[3]] = val

opcodes = []

with open('input_2.txt') as fp:
    for input in fp:
        opcode = input.strip().split()
        op_list = []
        for num in opcode:
            op_list.append(int(num))
        opcodes.append(op_list)

for opcode_instruction in opcodes:
    performOperation(opcode_instruction)

print(register[0])