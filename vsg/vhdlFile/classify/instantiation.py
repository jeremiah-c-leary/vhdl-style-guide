import re


def instantiation(dVars, oLine):

    if re.match('^\s*\w+\s*:\s*\w+', oLine.line):
        oLine.isInstantiationDeclaration = True
        oLine.insideInstantiation = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        dVars['iCurrentIndentLevel'] += 1

    if oLine.insideInstantiation:
        if re.match('^.*\s*port\s+map', oLine.lineLower):
            if not oLine.indentLevel:
                oLine.indentLevel = dVars['iCurrentIndentLevel']
            dVars['iCurrentIndentLevel'] += 1
            oLine.isInstantiationPortKeyword = True
            oLine.insideInstantiationPortMap = True
        if re.match('^.*\s*generic\s+map', oLine.lineLower):
            if not oLine.indentLevel:
                oLine.indentLevel = dVars['iCurrentIndentLevel']
            oLine.insideInstantiationGenericMap = True
            dVars['iCurrentIndentLevel'] += 1
            oLine.isInstantiationGenericKeyword = True
        if re.match('^.*=>', oLine.line):
            if not oLine.indentLevel:
                oLine.indentLevel = dVars['iCurrentIndentLevel']
            if oLine.insideInstantiationPortMap:
                oLine.isInstantiationPortAssignment = True
            else:
                oLine.isInstantiationGenericAssignment = True
        if ');' in oLine.line and oLine.insideInstantiationPortMap:
            oLine.isInstantiationPortEnd = True
            if not oLine.indentLevel:
                oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
            dVars['iCurrentIndentLevel'] -= 2
        if ')' in oLine.line and oLine.insideInstantiationGenericMap:
            oLine.isInstantiationGenericEnd = True
            if not oLine.indentLevel:
                oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
            dVars['iCurrentIndentLevel'] -= 1
