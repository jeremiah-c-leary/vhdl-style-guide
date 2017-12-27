import re


def attribute(dVars, oLine):

    classify_attribute_keyword(dVars, oLine)
    if oLine.insideAttribute:
        classify_attribute_line(dVars, oLine)
        classify_attribute_end(dVars, oLine)


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
