import globalVars

def add(com):
    if "+" in com and com[1] == "=":
        for x in range(len(com)):
            if com[x] == "+":
                try:
                    exec("globalVars.variables['" + com[0] + "'] = " + com[x - 1] + "+" + com[x + 1])
                except NameError:
                    try:
                        exec("globalVars.variables['" + com[0] + "'] = " + com[x - 1] +
                             " + globalVars.variables['" + com[x + 1] + "']")
                    except NameError:
                        try:
                            exec("globalVars.variables['" + com[0] + "'] = globalVars.variables['" + com[x - 1] +
                                 "'] + " + com[x + 1])
                        except NameError:
                            exec("globalVars.variables['" + com[0] + "'] = globalVars.variables['" + com[x - 1] +
                                 "'] + globalVars.variables['" + com[x + 1] + "']")


def subtract(com):
    if "-" in com and com[1] == "=":
        for x in range(len(com)):
            if com[x] == "-":
                try:
                    exec("globalVars.variables['" + com[0] + "'] = " + com[x - 1] + "-" + com[x + 1])
                except NameError:
                    try:
                        exec("globalVars.variables['" + com[0] + "'] = " + com[x - 1] + " - globalVars.variables['" + com[x + 1] + "']")
                    except NameError:
                        try:
                            exec("globalVars.variables['" + com[0] + "'] = globalVars.variables['" + com[x - 1] + "'] - " + com[x + 1])
                        except NameError:
                            exec("globalVars.variables['" + com[0] + "'] = globalVars.variables['" + com[x - 1] + "'] - globalVars.variables['" + com[x + 1] + "']")


def multiply(com):
    if "*" in com and com[1] == "=":
        for x in range(len(com)):
            if com[x] == "*":
                try:
                    exec("globalVars.variables['" + com[0] + "'] = " + com[x - 1] + " * " + com[x + 1])
                except NameError:
                    try:
                        exec("globalVars.variables['" + com[0] + "'] = " + com[x - 1] + " * globalVars.variables['" + com[x + 1] + "']")
                    except NameError:
                        try:
                            exec("globalVars.variables['" + com[0] + "'] = globalVars.variables['" + com[x - 1] + "'] * " + com[x + 1])
                        except NameError:
                            exec("globalVars.variables['" + com[0] + "'] = globalVars.variables['" + com[x - 1] + "'] * globalVars.variables['" + com[x + 1] + "']")


def divide(com):
    if "/" in com and com[1] == "=":
        for x in range(len(com)):
            if com[x] == "/":
                try:
                    exec("globalVars.variables['" + com[0] + "'] = " + com[x - 1] + "/" + com[x + 1])
                except NameError:
                    try:
                        exec("globalVars.variables['" + com[0] + "'] = " + com[x - 1] + " / globalVars.variables['" + com[x + 1] + "']")
                    except NameError:
                        try:
                            exec("globalVars.variables['" + com[0] + "'] = globalVars.variables['" + com[x - 1] + "'] / " + com[x + 1])
                        except NameError:
                            exec("globalVars.variables['" + com[0] + "'] = globalVars.variables['" + com[x - 1] + "'] / globalVars.variables['" + com[x + 1] + "']")


def mod(com):
    if "mod" in com and com[1] == "=":
        for x in range(len(com)):
            if com[x] == "mod":
                try:
                    exec("globalVars.variables['" + com[0] + "'] = " + com[x - 1] + "%" + com[x + 1])
                except NameError:
                    try:
                        exec("globalVars.variables['" + com[0] + "'] = " + com[x - 1] + " % globalVars.variables['" + com[x + 1] + "']")
                    except NameError:
                        try:
                            exec("globalVars.variables['" + com[0] + "'] = globalVars.variables['" + com[x - 1] + "'] % " + com[x + 1])
                        except NameError:
                            exec("globalVars.variables['" + com[0] + "'] = globalVars.variables['" + com[x - 1] + "'] % globalVars.variables['" + com[x + 1] + "']")


def exponent(com):
    if "^" in com and com[1] == "=":
        for x in range(len(com)):
            if com[x] == "^":
                try:
                    exec("globalVars.variables['" + com[0] + "'] = " + com[x - 1] + "**" + com[x + 1])
                except NameError:
                    try:
                        exec("globalVars.variables['" + com[0] + "'] = " + com[x - 1] + " ** globalVars.variables['" + com[x + 1] + "']")
                    except NameError:
                        try:
                            exec("globalVars.variables['" + com[0] + "'] = globalVars.variables['" + com[x - 1] + "'] ** " + com[x + 1])
                        except NameError:
                            exec("globalVars.variables['" + com[0] + "'] = globalVars.variables['" + com[x - 1] + "'] ** globalVars.variables['" + com[x + 1] + "']")


def arithmaticsFunc(com):
    exponent(com)
    multiply(com)
    divide(com)
    add(com)
    subtract(com)
