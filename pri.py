import globalVars


def priFunc(com):
    if com[0][0:4] == "pri(" and com[0][-1] == ")":
        #print(com[0][-3])
        if com[0][6] == "[" and com[0][-2] == "]":
            exec("print(globalVars.lists['" + com[0][4:-4] + "'][" + com[0][-3] + "])")
            #print(com[0][5:len(com[0])-1])
        elif str(com[0][6]) == ")":
            exec("print(globalVars.lists['" + com[0][4:-1] + "'])")







