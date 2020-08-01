import re

from vsg import parser


def attribute(dVars, lTokens, lObjects, oLine):

    classify_attribute_keyword(dVars, oLine)
    if oLine.insideAttribute:
        classify_attribute_line(dVars, oLine)
        classify_attribute_end(dVars, oLine)

    for iToken, sToken in enumerate(lTokens):
        if not dVars['bAttributeKeywordFound']:

            classify_keyword(sToken, iToken, lObjects, dVars)

        else:

            if not dVars['bAttributeColonFound']:
                classify_colon(sToken, iToken, lObjects, dVars)
                classify_identifier(sToken, iToken, lObjects)
            else:
                classify_type_mark(sToken, iToken, lObjects)
                classify_semicolon(sToken, iToken, lObjects, dVars)


def classify_keyword(sToken, iToken, lObjects, dVars):
    if sToken.lower() == 'attribute':
        lObjects[iToken] = parser.attribute_keyword(sToken)
        dVars['bAttributeKeywordFound'] = True 


def classify_identifier(sToken, iToken, lObjects):
    if not isinstance(lObjects[iToken], parser.whitespace) and not isinstance(lObjects[iToken], parser.comment) and \
       sToken != ':':
        lObjects[iToken] = parser.attribute_identifier(sToken)


def classify_colon(sToken, iToken, lObjects, dVars):
    if sToken == ':':
        lObjects[iToken] = parser.attribute_colon()
        dVars['bAttributeColonFound'] = True


def classify_type_mark(sToken, iToken, lObjects):
    if not isinstance(lObjects[iToken], parser.whitespace) and not isinstance(lObjects[iToken], parser.comment):
        lObjects[iToken] = parser.attribute_type_mark(sToken)


def classify_semicolon(sToken, iToken, lObjects, dVars):
    if sToken == ';':
        lObjects[iToken] = parser.attribute_semicolon()
        dVars['bAttributeKeywordFound'] = False
        dVars['bAttributeColonFound'] = False





def classify_attribute_keyword(dVars, oLine):
    if re.match('^\s*attribute', oLine.line, re.IGNORECASE):
        oLine.isAttributeKeyword = True
        oLine.insideAttribute = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        dVars['iCurrentIndentLevel'] += 1


def classify_attribute_end(dVars, oLine):
    if ';' in oLine.line:
        oLine.isAttributeEnd = True
        dVars['iCurrentIndentLevel'] -= 1


def classify_attribute_line(dVars, oLine):
    if not oLine.isAttributeKeyword:
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        oLine.insideAttribute = True
