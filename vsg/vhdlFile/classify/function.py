import re


def function(dVars, oLine):

    classify_function_keyword(dVars, oLine)
    if oLine.insideFunction:
        classify_begin_keyword(dVars, oLine)
        classify_return_keyword(dVars, oLine)
        classify_end_keyword(dVars, oLine)
        classify_parameter(dVars, oLine)


def classify_function_keyword(dVars, oLine):
    if re.match('^\s*function\s', oLine.lineLower) or re.match('^\s*impure\s', oLine.lineLower):
        oLine.isFunctionKeyword = True
        oLine.insideFunction = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        dVars['iCurrentIndentLevel'] += 1


def classify_begin_keyword(dVars, oLine):
    if re.match('^\s*begin', oLine.lineLower):
        oLine.isFunctionBegin = True
        oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1


def classify_return_keyword(dVars, oLine):
    if re.match('^\s*return', oLine.lineLower):
        oLine.isFunctionReturn = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        if oLine.insidePackage:
            oLine.isFunctionEnd = True
            oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
            dVars['iCurrentIndentLevel'] -= 1


def classify_end_keyword(dVars, oLine):
    if re.match('^\s*end', oLine.lineLower) and not oLine.isEndIfKeyword and \
       not oLine.isEndCaseKeyword and not oLine.isForLoopEnd and not oLine.isWhileLoopEnd:
        oLine.isFunctionEnd = True
        oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
        dVars['iCurrentIndentLevel'] -= 1


def classify_parameter(dVars, oLine):
    if re.match('^.*\w+\s*:\s*\w+', oLine.line):
        oLine.isFunctionParameter = True
        if not oLine.indentLevel:
            oLine.indentLevel = dVars['iCurrentIndentLevel']
