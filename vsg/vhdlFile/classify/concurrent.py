import re


def concurrent(dVars, oLine):
    if re.match('^\s*\w+\s*<=', oLine.line) or re.match('^\s*\w+\s*:\s*\w+\s*<=', oLine.line):
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        oLine.isConcurrentBegin = True
        oLine.insideConcurrent = True
    if oLine.insideConcurrent:
        if re.match('.*;', oLine.line):
            oLine.isEndConcurrent = True
