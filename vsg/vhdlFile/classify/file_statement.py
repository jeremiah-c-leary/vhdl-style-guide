import re


def file_statement(dVars, oLine):

    if re.match('^\s*file', oLine.line, re.IGNORECASE):
        oLine.isFileKeyword = True
        oLine.insideFile = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        dVars['iCurrentIndentLevel'] += 1
    if oLine.insideFile and not oLine.isFileKeyword:
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        oLine.insideFile = True
    if oLine.insideFile and ';' in oLine.line:
        oLine.isFileEnd = True
        dVars['iCurrentIndentLevel'] -= 1
