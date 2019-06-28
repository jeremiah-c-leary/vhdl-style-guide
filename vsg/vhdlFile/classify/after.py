import re


def after(dVars, oLine):

    if oLine.isEndConcurrent or oLine.isSequentialEnd or oLine.insideSequential:
        if re.match('^.*\s+after\s', oLine.lineNoComment, flags=re.IGNORECASE):
            oLine.hasAfterKeyword = True
        if re.match('^.*after$', oLine.lineNoComment, flags=re.IGNORECASE):
            oLine.hasAfterKeyword = True

