import re


def instantiation(dVars, oLine):

    if re.match('^\s*\w+\s*:\s*\w+', oLine.line):
        if re.match('^\s*\w+\s*:\s*entity', oLine.line, re.IGNORECASE):
            oLine.isDirectInstantiationDeclaration = True
        else:
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
        if re.match('^.*\)\s*;', oLine.lineNoComment) and oLine.insideInstantiationPortMap:
            oLine.isInstantiationPortEnd = True
            if not oLine.indentLevel:
                oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
            dVars['iCurrentIndentLevel'] -= 2
        if oLine.insideInstantiationGenericMap:
            dVars['iOpenParenthesis'] += oLine.lineNoComment.count('(')
            dVars['iCloseParenthesis'] += oLine.lineNoComment.count(')')

        if ')' in oLine.lineNoComment and oLine.insideInstantiationGenericMap:
            if dVars['iOpenParenthesis'] == dVars['iCloseParenthesis']:
                oLine.isInstantiationGenericEnd = True
                if not oLine.indentLevel:
                    oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
                dVars['iCurrentIndentLevel'] -= 1
                dVars['iOpenParenthesis'] = 0
                dVars['iCloseParenthesis'] = 0
