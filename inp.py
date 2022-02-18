import globalVars


def inpFunc(com):
    if com[0][0:4] == "inp(" and com[0][-1] == ")":
        #print(com[0][4:-1])
        exec("globalVars.variables['" + com[0][4:-1] + "'] = input()")
