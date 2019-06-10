import re


def after(dVars, oLine):

    if oLine.isEndConcurrent or oLine.isSequentialEnd:
        if re.match('^.*\safter\s', oLine.lineNoComment, flags=re.IGNORECASE):
            oLine.hasAfterKeyword = True
