import re


def generate(dVars, oLine, oLinePrevious):

    classify_case_generate(dVars, oLine) 
    classify_for_generate(dVars, oLine) 
    classify_if_generate(dVars, oLine) 
    classify_multi_line_generate_statement(dVars, oLine, oLinePrevious)
    if oLine.insideGenerate:
        if re.match('^\s*\w+\s*:\s*if[\s|(].*[\s|)]generate', oLine.lineLower) or re.match('^\s*\w+\s*:\s*for\s.*\sgenerate', oLine.lineLower) or re.match('^\s*\w+\s*:\s*case\s.*\sgenerate', oLine.lineLower):
            oLine.isGenerateKeyword = True
            oLine.isGenerateLabel = True
            oLine.indentLevel = dVars['iCurrentIndentLevel']
            dVars['iCurrentIndentLevel'] += 1
        if re.match('^\s*if[\s|(].*[\s|)]generate', oLine.lineLower) or re.match('^\s*for\s.*\sgenerate', oLine.lineLower) or re.match('^\s*case\s.*\sgenerate', oLine.lineLower):
            oLine.isGenerateKeyword = True
            oLine.indentLevel = dVars['iCurrentIndentLevel']
            dVars['iCurrentIndentLevel'] += 1
        if re.match('^\s*begin', oLine.lineLower) and not oLine.insideProcess:
            oLine.isGenerateBegin = True
            oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
        classify_end_generate(dVars, oLine)

        classify_for_generate_case_when(dVars, oLine)


def classify_end_generate(dVars, oLine):
    if re.match('^\s*end\s+generate', oLine.lineLower):
        oLine.isGenerateEnd = True
        dVars['iCurrentIndentLevel'] -= 1
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        dVars['iGenerateLevel'] -= 1
        if re.match('^\s*end\s+generate\s+\S+\s*;', oLine.lineLower):
            oLine.isGenerateEndLabel = True
        if oLine.insideGenerateCase:
            oLine.indentLevel -= 1
            dVars['iCurrentIndentLevel'] -= 1


def classify_for_generate(dVars, oLine):
    if re.match('^\s*\w+\s*:\s*for\s.*\sgenerate', oLine.lineLower):
        oLine.insideGenerate = True
        dVars['iGenerateLevel'] += 1


def classify_if_generate(dVars, oLine):
    if re.match('^\s*\w+\s*:\s*if', oLine.lineLower):
        oLine.insideGenerate = True
        dVars['iGenerateLevel'] += 1


def classify_case_generate(dVars, oLine):
    if re.match('^\s*\w+\s*:\s*case\s.*\sgenerate', oLine.lineLower):
        oLine.insideGenerate = True
        oLine.insideGenerateCase = True
        dVars['iGenerateLevel'] += 1


def classify_for_generate_case_when(dVars, oLine):
    if oLine.insideGenerateCase:
        if re.match('^\s*when\s+\w+\s+=>', oLine.lineLower):
            oLine.isGenerateCaseWhen = True
            if not dVars['bFirstWhenSeen']:
                oLine.indentLevel = dVars['iCurrentIndentLevel']
                dVars['bFirstWhenSeen'] = True
                dVars['iCurrentIndentLevel'] += 1
            else:
                oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1

def classify_multi_line_generate_statement(dVars, oLine, oLinePrevious):
    if re.match('^\s*\w+\s*:\s*--', oLinePrevious.line) or re.match('^\s*\w+\s*:\s*$', oLinePrevious.line):
        if re.match('^\s*if\s+.*\sgenerate', oLine.lineLower) or re.match('^\s*for\s.*\sgenerate', oLine.lineLower) or re.match('^\s*case\s+.*\sgenerate', oLine.lineLower):
            oLinePrevious.insideGenerate = True
            oLinePrevious.isGenerateLabel = True
            oLine.insideGenerate = True
            dVars['iGenerateLevel'] += 1
            
