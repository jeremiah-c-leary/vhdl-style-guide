import re


def comment(dVars, oLine):
    # Check for comment lines
    if '--' in oLine.line:
        oLine.hasComment = True
        oLine.commentColumn = oLine.line.find('--')
        if re.match('^\s*--', oLine.line):
            oLine.isComment = True
            oLine.indentLevel = dVars['iCurrentIndentLevel']
        else:
            oLine.hasInlineComment = True
