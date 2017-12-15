import re


def concurrent(dVars, oLine):
    if re.match('^\s*\w+.*\s*<=', oLine.lineNoComment) or re.match('^\s*\w+\s*:\s*\w+.*\s*<=', oLine.lineNoComment):
        if not oLine.insideAssert:
            oLine.indentLevel = dVars['iCurrentIndentLevel']
            oLine.isConcurrentBegin = True
            oLine.insideConcurrent = True
    if oLine.insideConcurrent:
        if re.match('.*;', oLine.lineNoComment):
            oLine.isEndConcurrent = True
