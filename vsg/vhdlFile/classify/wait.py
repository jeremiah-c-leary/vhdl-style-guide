import re


def wait(dVars, oLine):

    if re.match('^\s*wait', oLine.lineLower):
        if not oLine.insideEntity and \
           not oLine.insideComponent and \
           not oLine.insideInstantiation:
            oLine.isWait = True
            oLine.indentLevel = dVars['iCurrentIndentLevel']
