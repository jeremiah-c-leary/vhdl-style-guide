import re


def subtype(dVars, oLine):

    check_for_subtypes(dVars, oLine)
    assign_subtype_attributes(dVars, oLine)


def check_for_subtypes(dVars, oLine):
    if re.match('^\s*subtype\s', oLine.line, re.IGNORECASE):
        oLine.isSubtypeKeyword = True
        oLine.insideSubtype = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        dVars['iCurrentIndentLevel'] += 1


def assign_subtype_attributes(dVars, oLine):
    if oLine.insideSubtype:
        if not oLine.isSubtypeKeyword and not oLine.isBlank:
            oLine.indentLevel = dVars['iCurrentIndentLevel']
        if ';' in oLine.line:
            oLine.isSubtypeEnd = True
            dVars['iCurrentIndentLevel'] -= 1
