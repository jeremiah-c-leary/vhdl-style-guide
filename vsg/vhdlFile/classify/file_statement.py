import re


def file_statement(dVars, oLine):

    classify_file_keyword(dVars, oLine)
    if oLine.insideFile:
        if not oLine.isFileKeyword:
            oLine.indentLevel = dVars['iCurrentIndentLevel']
            oLine.insideFile = True
        classify_file_end(dVars, oLine)


def classify_file_keyword(dVars, oLine):
    if re.match('^\s*file', oLine.line, re.IGNORECASE):
        oLine.isFileKeyword = True
        oLine.insideFile = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        dVars['iCurrentIndentLevel'] += 1


def classify_file_end(dVars, oLine):
    if ';' in oLine.line:
        oLine.isFileEnd = True
        dVars['iCurrentIndentLevel'] -= 1
