import re

comment_only_re = re.compile(r'^\s*--')

def comment(dVars, oLine):
    inQuote = False
    for i, char in enumerate(oLine.line):
        if char == '"':
            inQuote = not inQuote
        minusminus = (i != 0 and oLine.line[i] == "-" and oLine.line[i - 1] == "-")
        if minusminus and not inQuote:
            found_comment(dVars, oLine, i - 1)
            return
    return
def found_comment(dVars, oLine, i):
    oLine.hasComment = True
    oLine.commentColumn = i
    if comment_only_re.match(oLine.line) is not None:
        oLine.isComment = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
    else:
        oLine.hasInlineComment = True
