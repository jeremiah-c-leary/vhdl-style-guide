import re


def generate(dVars, oLine):

    if re.match('^\s*\w+\s*:\s*if', oLine.lineLower) or re.match('^\s*\w+\s*:\s*for\s.*\sgenerate', oLine.lineLower):
        oLine.insideGenerate = True
    if oLine.insideGenerate:
        if re.match('^\s*\w+\s*:\s*if\s.*\sgenerate', oLine.lineLower) or re.match('^\s*\w+\s*:\s*for\s.*\sgenerate', oLine.lineLower):
            oLine.isGenerateKeyword = True
            oLine.indentLevel = dVars['iCurrentIndentLevel']
            dVars['iCurrentIndentLevel'] += 1
        if re.match('^\s*begin', oLine.lineLower):
            oLine.isGenerateBegin = True
            oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
        if re.match('^\s*end\s+generate', oLine.lineLower):
            oLine.isGenerateEnd = True
            dVars['iCurrentIndentLevel'] -= 1
            oLine.indentLevel = dVars['iCurrentIndentLevel']
