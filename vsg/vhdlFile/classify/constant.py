import re


def constant(dVars, oLine):

    if re.match('^\s*constant', oLine.lineLower) and \
       not oLine.insideFunction and not oLine.insideProcedure:
        oLine.isConstant = True
        oLine.indentLevel = 1
