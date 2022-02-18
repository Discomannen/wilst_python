import globalVars



def notEFunc(com):
    if len(com) > 1:
        if com[1:3] == "!E":
            exec("del globalVars.lists['" + com[2] + "']['" + com[0] + "']")

