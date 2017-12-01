import re


def process(dVars, oLine):
    if re.match('^\s*process', oLine.lineLower) or re.match('^\s*\S+\s*:\s*process', oLine.lineLower) and not oLine.isComment:
        oLine.isProcessKeyword = True
        oLine.insideProcess = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
    if oLine.insideProcess:
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
        if re.match('^.*\s+begin', oLine.lineLower) or re.match('^\s*begin', oLine.lineLower):
            oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
            oLine.isProcessBegin = True
            dVars['fFoundProcessBegin'] = True
        if re.match('^\s*end\s+process', oLine.lineLower):
            oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
            oLine.isEndProcess = True
            dVars['fFoundProcessBegin'] = False
            dVars['iCurrentIndentLevel'] = dVars['iCurrentIndentLevel'] - 1
            dVars['SensitivityListFound'] = False
