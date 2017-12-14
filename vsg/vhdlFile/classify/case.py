import re


def case(self, dVars, oLine):

    if re.match('^\s*case[\s|\(]', oLine.lineLower):
        oLine.isCaseKeyword = True
        oLine.insideCase = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        dVars['iCurrentIndentLevel'] += 2
    if oLine.insideCase:
        if re.match('^\s*.*[\s|\)]is\s', oLine.lineLower) or re.match('^\s*.*[\s|\)]is$', oLine.lineLower):
            oLine.isCaseIsKeyword = True
    if re.match('^\s*when\s', oLine.lineLower):
        oLine.isCaseWhenKeyword = True
        oLine.insideCaseWhen = True
        oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
    if oLine.insideCaseWhen:
        oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
        if re.match('^\s*.*=>', oLine.line):
            oLine.isCaseWhenEnd = True
    if re.match('^\s*end\s+case', oLine.lineLower):
        oLine.isEndCaseKeyword = True
        oLine.indentLevel = dVars['iCurrentIndentLevel'] - 2
        dVars['iCurrentIndentLevel'] -= 2

    # Check for null statements
    if re.match('^\s*null\s*;', oLine.lineLower):
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        oLine.isCaseNull = True
