import arithmatics
import lam
import pri
import E
import globalVars
import inp
from switch import Switch
import notE
import iffy


def commentremove(com):
    comment = False
    for a in range(len(com)):
        for b in com[a]:
            if b == "///":
                comment = True
            elif b == "\\\\\\":
                comment = False
                com[a].clear()
        if comment:
            com[a].clear()
    empty = filter(lambda x: (x != []), com)
    return list(empty)


def letFunc(com):
    if com[0] == "let" and com[2] == "=":
        var = ''
        val = com[3][3:len(com[3])]

        if com[3][0:3] == "int":
            var = 'i'

        elif com[3][0:3] == "str":
            var = 's'

        elif com[3][0:3] == "flo":
            var = 'f'

        elif com[3][0:3] == "chr":
            var = 'c'

        elif com[3][0:3] == "bol":
            var = 'b'

        with Switch(var) as case:
            if case('i'):
                exec("globalVars.variables['" + str(com[1]) + "'] = int(" + val + ")")
            if case('s'):
                exec("globalVars.variables['" + str(com[1]) + "'] = str(" + val + ")")
            if case('f'):
                exec("globalVars.variables['" + str(com[1]) + "'] = float(" + val + ")")
            if case('c'):
                exec("globalVars.variables['" + str(com[1]) + "'] = str(" + val + ")")
            if case('b'):
                exec("globalVars.variables['" + str(com[1]) + "'] = bool(" + val + ")")


def main(name):
    running = True
    wilst = open("sample.wilst", "r")
    wilst = str(wilst.read())

    # Tokenizer
    line = wilst.split('\n')
    tokenize = filter(lambda x: (x != "" and x[0] != "#"), line)
    line = list(tokenize)
    commands = list()
    for i in range(len(line)):
        if '"' in line[i]:
            start = True
            newList = []
            sstart = int()
            sstop = int()
            for x in range(len(line[i])):
                if line[i][x] == '"':
                    if start:
                        sstart = x
                        start = False
                    else:
                        sstop = x
            tmp = ''
            ind = int(0)
            for c in line[i]:
                ind += 1
                if c == ' ' and not sstart <= ind <= sstop:
                    newList.append(tmp)
                    tmp = ''
                else:
                    tmp += c
            if tmp:
                newList.append(tmp)
            commands.append(newList)
        else:
            commands.append(line[i].split())
    # print(commands)
    commands = commentremove(commands)
    #print(commands)

    # Interpreter loop
    while running:
        for com in commands:
            lam.lamFunc(com)
            letFunc(com)
            iffy.ifFunc(com)
            # print(globalVars.lists)
            E.EFunc(com)
            pri.priFunc(com)    
            inp.inpFunc(com)
            notE.notEFunc(com)
            
            arithmatics.arithmaticsFunc(com)
        running = False
    # print(dir())


if __name__ == '__main__':
    main('PyCharm')
