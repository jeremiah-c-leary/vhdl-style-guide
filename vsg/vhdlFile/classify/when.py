import re


def when(dVars, oLine, oLinePrevious):

    if re.match('^\s*\S+\s*<=\s*\S+\swhen', oLine.lineNoComment, re.IGNORECASE):
        oLine.insideWhen = True

    if oLine.insideWhen or (oLinePrevious.insideWhen and not oLinePrevious.isWhenEnd):
        if re.match('^.*\swhen', oLine.lineNoComment, re.IGNORECASE):
            oLine.isWhenKeyword = True
        if re.match('^.*\selse', oLine.lineNoComment, re.IGNORECASE):
            oLine.isWhenElseKeyword = True
        if re.match('^.*;', oLine.lineNoComment, re.IGNORECASE):
            oLine.isWhenEnd = True
