import re


def instantiation(dVars, oLine):

    classify_instantiation_declaration(dVars, oLine)
    if oLine.insideInstantiation:
        classify_port_map(dVars, oLine)
        classify_generic_map(dVars, oLine)
        classify_assignment(dVars, oLine)
        classify_port_map_end(dVars, oLine)
        if oLine.insideInstantiationGenericMap:
            dVars['iOpenParenthesis'] += oLine.lineNoComment.count('(')
            dVars['iCloseParenthesis'] += oLine.lineNoComment.count(')')
        classify_generic_map_end(dVars, oLine)


def classify_instantiation_declaration(dVars, oLine):
    if re.match('^\s*\w+\s*:\s*\w+', oLine.line) and not oLine.insideTypeRecord:
        if re.match('^\s*\w+\s*:\s*entity', oLine.line, re.IGNORECASE):
            oLine.isDirectInstantiationDeclaration = True
        else:
            oLine.isInstantiationDeclaration = True
        oLine.insideInstantiation = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        dVars['iCurrentIndentLevel'] += 1


def classify_port_map(dVars, oLine):
    if re.match('^.*\s*port\s+map', oLine.lineLower):
        if not oLine.indentLevel:
            oLine.indentLevel = dVars['iCurrentIndentLevel']
        dVars['iCurrentIndentLevel'] += 1
        oLine.isInstantiationPortKeyword = True
        oLine.insideInstantiationPortMap = True


def classify_generic_map(dVars, oLine):
    if re.match('^.*\s*generic\s+map', oLine.lineLower):
        if not oLine.indentLevel:
            oLine.indentLevel = dVars['iCurrentIndentLevel']
        oLine.insideInstantiationGenericMap = True
        dVars['iCurrentIndentLevel'] += 1
        oLine.isInstantiationGenericKeyword = True


def classify_assignment(dVars, oLine):
    if re.match('^.*=>', oLine.lineNoComment):
        if not oLine.indentLevel:
            oLine.indentLevel = dVars['iCurrentIndentLevel']
        if oLine.insideInstantiationPortMap:
            oLine.isInstantiationPortAssignment = True
        else:
            oLine.isInstantiationGenericAssignment = True


def classify_port_map_end(dVars, oLine):
    if re.match('^.*\)\s*;', oLine.lineNoComment) and oLine.insideInstantiationPortMap:
        oLine.isInstantiationPortEnd = True
        if not oLine.indentLevel:
            oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
        dVars['iCurrentIndentLevel'] -= 2


def classify_generic_map_end(dVars, oLine):
    if ')' in oLine.lineNoComment and oLine.insideInstantiationGenericMap:
        if dVars['iOpenParenthesis'] == dVars['iCloseParenthesis']:
            oLine.isInstantiationGenericEnd = True
            if not oLine.indentLevel:
                oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
            dVars['iCurrentIndentLevel'] -= 1
            dVars['iOpenParenthesis'] = 0
            dVars['iCloseParenthesis'] = 0
