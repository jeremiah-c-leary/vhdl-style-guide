import re


def signal(dVars, oLine):

    if re.match('^\s*signal\s', oLine.lineLower) and \
       not oLine.insideFunction and not oLine.insideProcedure:
        oLine.isSignal = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
