inputs = []
i = 0
processnext_2 = False
total = 0


def check_opcodes(before, opcode, after):
    got_3_opcode = 0
    #1-gtrr
    if before[opcode[1]] > before[opcode[2]] and after[opcode[3]] == 1:
        got_3_opcode += 1
    else:
        if after[opcode[3]] == 0:
            got_3_opcode += 1

    #2-gtri
    if before[opcode[1]] > opcode[2] and after[opcode[3]] == 1:
        got_3_opcode += 1
    else:
        if after[opcode[3]] == 0:
            got_3_opcode += 1

    #3-gtir
    if opcode[1] > before[opcode[2]] and after[opcode[3]] == 1:
        got_3_opcode += 1
    else:
        if after[opcode[3]] == 0:
            got_3_opcode += 1

    #addr
    val = before[opcode[1]] + before[opcode[2]]
    if val == after[opcode[3]]:
        got_3_opcode += 1

    #addi
    val = before[opcode[1]] + opcode[2]
    if val == after[opcode[3]]:
        got_3_opcode += 1

    #mulr
    val = before[opcode[1]] * before[opcode[2]]
    if val == after[opcode[3]]:
        got_3_opcode += 1

    #muli
    val = before[opcode[1]] * opcode[2]
    if val == after[opcode[3]]:
        got_3_opcode += 1

    #setr
    val = before[opcode[1]]
    if val == after[opcode[3]]:
        got_3_opcode += 1

    #seti
    val = opcode[1]
    if val == after[opcode[3]]:
        got_3_opcode += 1

    #1-eqrr
    if before[opcode[1]] == before[opcode[2]] and after[opcode[3]] == 1:
        got_3_opcode += 1
    else:
        if after[opcode[3]] == 0:
            got_3_opcode += 1

    #2-eqri
    if before[opcode[1]] == opcode[2] and after[opcode[3]] == 1:
        got_3_opcode += 1
    else:
        if after[opcode[3]] == 0:
            got_3_opcode += 1

    #3-eqir
    if opcode[1] == before[opcode[2]] and after[opcode[3]] == 1:
        got_3_opcode += 1
    else:
        if after[opcode[3]] == 0:
            got_3_opcode += 1

    #bitwiseAND
    val = before[opcode[1]] & before[opcode[2]]
    if val == after[opcode[3]]:
        got_3_opcode += 1

    #AND
    val = before[opcode[1]] & opcode[2]
    if val == after[opcode[3]]:
        got_3_opcode += 1


    #bitwiseOR
    val = before[opcode[1]] | before[opcode[2]]
    if val == after[opcode[3]]:
        got_3_opcode += 1

    #Or
    val = before[opcode[1]] | opcode[2]
    if val == after[opcode[3]]:
        got_3_opcode += 1

    return got_3_opcode

def clean_input(row):
    return row.replace('[','').replace(']','').split(':')[1].replace(',','').replace(' ','')

with open('input.txt') as fp:
    sample = []
    for input in fp:
        if 'After' in input:
            processnext_2 = False
            after = clean_input(input.strip())
            after_list = []
            for num in after:
                after_list.append(int(num))
            sample.append(after_list)
            inputs.append(sample)
            sample = []
        if processnext_2:
            opcode = input.strip().split()
            op_list = []
            for num in opcode:
                op_list.append(int(num))
            sample.append(op_list)
        if 'Before' in input:
            processnext_2 = True
            before = clean_input(input.strip())
            before_list = []
            for num in before:
                before_list.append(int(num))
            sample.append(before_list)



for sample in inputs:
    if check_opcodes(sample[0], sample[1], sample[2]) >= 3:
        total += 1
print(total)









