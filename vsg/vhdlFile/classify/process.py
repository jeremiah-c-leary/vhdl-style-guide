import re


def process(dVars, oLine):
    classify_process_keyword(dVars, oLine)
    if oLine.insideProcess:
        classify_process_sensitivity_list(dVars, oLine)
        classify_process_begin_keyword(dVars, oLine)
        classify_process_end_keyword(dVars, oLine)


def classify_process_keyword(dVars, oLine):
    if re.match('^\s*process', oLine.lineLower):
        oLine.isProcessKeyword = True
        oLine.insideProcess = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
    if re.match('^\s*\S+\s*:\s*process', oLine.lineLower):
        oLine.isProcessKeyword = True
        oLine.insideProcess = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        oLine.isProcessLabel = True


def classify_process_sensitivity_list(dVars, oLine):
    # Check sensitivity list
    if '(' in oLine.line and not oLine.insideSensitivityList and not dVars['fFoundProcessBegin'] and not dVars['SensitivityListFound']:
        oLine.isSensitivityListBegin = True
        oLine.insideSensitivityList = True
        dVars['SensitivityListFound'] = True
    if oLine.insideSensitivityList:
        dVars['iOpenParenthesis'] += oLine.line.count('(')
        dVars['iCloseParenthesis'] += oLine.line.count(')')
        if dVars['iOpenParenthesis'] == dVars['iCloseParenthesis']:
            oLine.isSensitivityListEnd = True
            dVars['iOpenParenthesis'] = 0
            dVars['iCloseParenthesis'] = 0
            dVars['iCurrentIndentLevel'] += 1


def classify_process_begin_keyword(dVars, oLine):
    if re.match('^.*\s+begin', oLine.lineLower) or re.match('^\s*begin', oLine.lineLower):
        oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
        oLine.isProcessBegin = True
        dVars['fFoundProcessBegin'] = True


def classify_process_end_keyword(dVars, oLine):
    if re.match('^\s*end\s+process', oLine.lineLower):
        oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
        oLine.isEndProcess = True
        dVars['fFoundProcessBegin'] = False
        dVars['iCurrentIndentLevel'] = dVars['iCurrentIndentLevel'] - 1
        dVars['SensitivityListFound'] = False
