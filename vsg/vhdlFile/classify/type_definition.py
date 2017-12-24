import re


def type_definition(dVars, oLine):

    if re.match('^\s*type\s+\w+\s+is\s+array', oLine.line, re.IGNORECASE):
        oLine.isTypeKeyword = True
        oLine.isTypeArrayKeyword = True
        oLine.insideTypeArray = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
    elif re.match('^\s*type\s+\w+\s+is\s+record', oLine.line, re.IGNORECASE):
        oLine.isTypeKeyword = True
        oLine.isTypeRecordKeyword = True
        oLine.insideTypeRecord = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        dVars['iCurrentIndentLevel'] += 1
    elif re.match('^\s*type\s', oLine.line, re.IGNORECASE):
        oLine.isTypeKeyword = True
        oLine.insideType = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        dVars['iCurrentIndentLevel'] += 1
    assign_array_attributes(oLine)
    assign_record_attributes(dVars, oLine)
    assign_enumerated_attributes(dVars, oLine)


def assign_array_attributes(oLine):
    if oLine.insideTypeArray:
        if ';' in oLine.line:
            oLine.isTypeArrayEnd = True
            oLine.isTypeEnd = True


def assign_record_attributes(dVars, oLine):
    if oLine.insideTypeRecord:
        if not oLine.isTypeRecordKeyword and not oLine.isBlank:
            oLine.indentLevel = dVars['iCurrentIndentLevel']
        if re.match('^\s*end\s+record', oLine.line, re.IGNORECASE):
            oLine.isTypeRecordEnd = True
            oLine.isTypeEnd = True
            dVars['iCurrentIndentLevel'] -= 1
            oLine.indentLevel = dVars['iCurrentIndentLevel']


def assign_enumerated_attributes(dVars, oLine):
    if oLine.insideType:
        if not oLine.isTypeKeyword and not oLine.isBlank:
            oLine.indentLevel = dVars['iCurrentIndentLevel']
        if ';' in oLine.line:
            oLine.isTypeEnd = True
            dVars['iCurrentIndentLevel'] -= 1
            if re.match('^\s*\)\s*;', oLine.line):
                oLine.indentLevel = dVars['iCurrentIndentLevel']
