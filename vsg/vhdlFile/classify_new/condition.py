
from vsg.vhdlFile.classify_new import expression


def classify_until(lUntils, iToken, lObjects):
    '''
    condition ::=
        expression
    '''
    return expression.classify_until(lUntils, iToken, lObjects)
