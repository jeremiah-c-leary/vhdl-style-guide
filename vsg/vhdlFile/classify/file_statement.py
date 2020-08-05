import re


def file_statement(dVars, lTokens, lObjects, oLine):
    '''
    file identifier_list : subtype_indication [ [ open file_open_kind_expression ] is file_logic_name ]
    '''

    classify_file_keyword(dVars, oLine)
    if oLine.insideFile:
        if not oLine.isFileKeyword:
            oLine.indentLevel = dVars['iCurrentIndentLevel']
            oLine.insideFile = True
        classify_file_end(dVars, oLine)


def classify_file_keyword(dVars, oLine):
    if re.match('^\s*file\s', oLine.line, re.IGNORECASE):
        oLine.isFileKeyword = True
        oLine.insideFile = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        dVars['iCurrentIndentLevel'] += 1


def classify_file_end(dVars, oLine):
    if ';' in oLine.lineNoComment:
        oLine.isFileEnd = True
        dVars['iCurrentIndentLevel'] -= 1
