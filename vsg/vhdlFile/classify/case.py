import re


def case(self, dVars, oLine):
    '''
    [case_label :] case {expression} is
      ( when {choices} => {sequential_statement} )
      ( when {choices} => {sequential_statement} )
    end case [case_label];
    '''

    if re.match('^\s*case[\s|\(]', oLine.lineLower):
        oLine.isCaseKeyword = True
        oLine.insideCase = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        dVars['iCurrentIndentLevel'] += 2
    if re.match('^\s*\w+\s*:\s*case[\s|\(]', oLine.lineLower):
        oLine.isCaseKeyword = True
        oLine.insideCase = True
        oLine.hasCaseLabel = True
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
    if re.match('^\s*end\s+case\s+\w+\s*;', oLine.lineLower):
        oLine.hasEndCaseLabel = True

    # Check for null statements
    if re.match('^\s*null\s*;', oLine.lineLower):
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        oLine.isCaseNull = True
