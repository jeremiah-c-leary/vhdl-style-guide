
from vsg.vhdlFile.classify import expression


def classify_until(lUntils, iToken, lObjects):
    '''
    condition ::=
        expression
    '''
    return expression.classify_until(lUntils, iToken, lObjects)
