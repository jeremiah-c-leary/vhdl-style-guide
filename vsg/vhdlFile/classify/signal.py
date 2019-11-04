import re


def signal(dVars, oLine):

    if (re.match('^\s*signal\s', oLine.lineLower) or re.match('^\s*signal$', oLine.lineLower)) and \
       not oLine.insideFunction and not oLine.insideProcedure:
        oLine.isSignal = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        oLine.insideSignal = True

    if oLine.insideSignal:
        if re.match('.*;', oLine.lineNoComment):
            oLine.isEndSignal = True
        
