import globalVars



def EFunc(com):
    if len(com) > 1:
        if com[1] == "E":
            index = com[2][3:len(com[2])-1]
            #print(index)
            exec("globalVars.lists['" + com[2][0:2] + "'].insert(int(" + index + "),globalVars.variables['" + str(com[0]) + "'])")
            #print(globalVars.lists[com[2][0:2]])


#globalVars.lists['l1'].insert(globalVars.variables['a'], 0)

