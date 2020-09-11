
from vsg import parser

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import expression


def classify(iStart, iEnd, lObjects):
    '''
    condition ::=
        expression
    '''
    for iToken in range(iStart, iEnd):
        if utils.is_item(lObjects, iToken):
                utils.assign_token(lObjects, iToken, parser.todo)

    return iEnd


def classify_until(lUntils, iToken, lObjects):
    return expression.classify_until(lUntils, iToken, lObjects)
