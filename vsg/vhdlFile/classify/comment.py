import re

def comment(dVars, oLine):
    inQuote = False
    for i,char in enumerate(oLine.line):
        if char == '"':
            inQuote = not inQuote
        minusminus = (i != 0 and oLine.line[i] == "-" and oLine.line[i - 1] == "-")
        if minusminus and not inQuote: #found comment
            oLine.hasComment = True
            oLine.commentColumn = i
            if i == 0:
                oLine.hasInlineComment = True
            else:
                oLine.isComment = True
                oLine.indentLevel = dVars['iCurrentIndentLevel']
    return
