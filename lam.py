import globalVars


def lamFunc(com):
    if com[0] == "lam" and com[1] == "=" and not globalVars.listOp:
        for i in range(int(com[2])):
            globalVars.lists["l{0}".format(i + 1)] = []
        globalVars.listOp = True
