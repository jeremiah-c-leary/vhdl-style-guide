import re


def component(dVars, oLine):

    # Check Component declarations
    if re.match('^\s*component', oLine.lineLower) and not oLine.insideComponent:
        oLine.isComponentDeclaration = True
        oLine.insideComponent = True
        oLine.indentLevel = 1
        dVars['iCurrentIndentLevel'] += 1

    if re.match('^\s*end\s+component', oLine.lineLower):
        oLine.isComponentEnd = True
        oLine.indentLevel = 1
        dVars['iCurrentIndentLevel'] -= 1
