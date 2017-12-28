import re


def port(dVars, oLine):
    if not (oLine.insideEntity or oLine.insideComponent):
        return
    classify_port_keyword(dVars, oLine)
    if oLine.isPortKeyword and '(' not in oLine.line:
        return

    if oLine.insidePortMap:
        classify_port_declaration(dVars, oLine)
        classify_port_end_keyword(dVars, oLine)


def classify_port_keyword(dVars, oLine):
    if re.match('^\s*port', oLine.lineLower) and not oLine.insidePortMap:
        oLine.isPortKeyword = True
        oLine.insidePortMap = True
        if oLine.insideEntity:
            oLine.indentLevel = 1
            dVars['iCurrentIndentLevel'] = 2
        else:
            oLine.indentLevel = 2
            dVars['iCurrentIndentLevel'] = 3


def classify_port_declaration(dVars, oLine):
        if re.match('^\s*\w+.*:', oLine.line) and not oLine.isComment and not oLine.isPortKeyword:
            oLine.isPortDeclaration = True
            if oLine.insideEntity:
                oLine.indentLevel = 2
            else:
                oLine.indentLevel = 3


def classify_port_end_keyword(dVars, oLine):
        dVars['iOpenParenthesis'] += oLine.lineNoComment.count('(')
        dVars['iCloseParenthesis'] += oLine.lineNoComment.count(')')
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
