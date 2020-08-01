import re

from vsg import parser


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

    
    for iToken, sToken in enumerate(lTokens):
        if not dVars['bFileKeywordFound']:

            classify_keyword(sToken, iToken, lObjects, dVars)

        else:

            if not dVars['bFileColonFound']:
                classify_colon(sToken, iToken, lObjects, dVars)
                classify_comma(sToken, iToken, lObjects)
                classify_identifier(sToken, iToken, lObjects)
            else:
                if not dVars['bFileOpenKeywordFound'] and not dVars['bFileIsKeywordFound']:
                    classify_subtype_indication(sToken, iToken, lObjects)

                if not dVars['bFileOpenKeywordFound']:
                    classify_open_keyword(sToken, iToken, lObjects, dVars)
                else:
                    classify_file_open_kind_expression(sToken, iToken, lObjects)
              
                if not dVars['bFileIsKeywordFound']:
                    classify_is_keyword(sToken, iToken, lObjects, dVars)
                else:
                    classify_file_logical_name(sToken, iToken, lObjects)
              
                classify_semicolon(sToken, iToken, lObjects, dVars)


def classify_keyword(sToken, iToken, lObjects, dVars):
    if sToken.lower() == 'file':
        lObjects[iToken] = parser.file_keyword(sToken)
        dVars['bFileKeywordFound'] = True 


def classify_identifier(sToken, iToken, lObjects):
    if not isinstance(lObjects[iToken], parser.whitespace) and not isinstance(lObjects[iToken], parser.comment) and \
       sToken != ':' and sToken != ',':
        lObjects[iToken] = parser.file_identifier(sToken)


def classify_comma(sToken, iToken, lObjects):
    if sToken == ',':
        lObjects[iToken] = parser.file_comma()


def classify_colon(sToken, iToken, lObjects, dVars):
    if sToken == ':':
        lObjects[iToken] = parser.file_colon()
        dVars['bFileColonFound'] = True


def classify_subtype_indication(sToken, iToken, lObjects):
    if not isinstance(lObjects[iToken], parser.whitespace) and not isinstance(lObjects[iToken], parser.comment) and \
       sToken != ':=':
        lObjects[iToken] = parser.file_subtype_indication(sToken)


def classify_open_keyword(sToken, iToken, lObjects, dVars):
    if sToken.lower() == 'open':
        lObjects[iToken] = parser.file_open_keyword(sToken)
        dVars['bFileOpenKeywordFound'] = True 
        dVars['bFileIsKeywordFound'] = False


def classify_file_open_kind_expression(sToken, iToken, lObjects):
    if not isinstance(lObjects[iToken], parser.whitespace) and not isinstance(lObjects[iToken], parser.comment) and \
       sToken != 'open' and sToken != 'is':
        lObjects[iToken] = parser.file_open_kind_expression(sToken)


def classify_is_keyword(sToken, iToken, lObjects, dVars):
    if sToken == 'is':
        lObjects[iToken] = parser.file_is_keyword(sToken)
        dVars['bFileOpenKeywordFound'] = False
        dVars['bFileIsKeywordFound'] = True 


def classify_file_logical_name(sToken, iToken, lObjects):
    if not isinstance(lObjects[iToken], parser.whitespace) and not isinstance(lObjects[iToken], parser.comment) and \
       sToken != ';' and sToken != 'is':
        lObjects[iToken] = parser.file_logical_name(sToken)


def classify_semicolon(sToken, iToken, lObjects, dVars):
    if sToken == ';':
        lObjects[iToken] = parser.file_semicolon()
        dVars['bFileKeywordFound'] = False
        dVars['bFileColonFound'] = False
        dVars['bFileOpenKeywordFound'] = False
        dVars['bFileIsKeywordFound'] = False




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
