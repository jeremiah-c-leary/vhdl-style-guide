import re


def port(dVars, oLine):
    if re.match('^\s*port', oLine.lineLower) and not oLine.insidePortMap:
        oLine.isPortKeyword = True
        oLine.insidePortMap = True
        if oLine.insideEntity:
            oLine.indentLevel = 1
            dVars['iCurrentIndentLevel'] = 2
        else:
            oLine.indentLevel = 2
            dVars['iCurrentIndentLevel'] = 3

    if oLine.insidePortMap:
        if re.match('^\s*\w+.*:', oLine.line) and not oLine.isComment and not oLine.isPortKeyword:
            oLine.isPortDeclaration = True
            if oLine.insideEntity:
                oLine.indentLevel = 2
            else:
                oLine.indentLevel = 3
        dVars['iOpenParenthesis'] += oLine.line.count('(')
        dVars['iCloseParenthesis'] += oLine.line.count(')')
        if dVars['iOpenParenthesis'] == dVars['iCloseParenthesis']:
            dVars['iOpenParenthesis'] = 0
            dVars['iCloseParenthesis'] = 0
            oLine.isEndPortMap = True
            if oLine.insideEntity:
                oLine.indentLevel = 1
                dVars['iCurrentIndentLevel'] = 1
            else:
                oLine.indentLevel = 2
                dVars['iCurrentIndentLevel'] = 2
