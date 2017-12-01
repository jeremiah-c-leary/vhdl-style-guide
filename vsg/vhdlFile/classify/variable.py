import re


def variable(dVars, oLine):

    if re.match('^\s*variable', oLine.lineLower):
        oLine.isVariable = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
