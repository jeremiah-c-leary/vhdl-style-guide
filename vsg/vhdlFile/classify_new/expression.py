
from vsg import parser

from vsg.vhdlFile import utils


def classify(iStart, iEnd, lObjects):
    '''
    expression ::=
        condition_operator primary
      | logical_expression
    '''
    for iToken in range(iStart, iEnd):
        if utils.is_item(lObjects, iToken):
                utils.assign_token(lObjects, iToken, parser.todo)

    return iEnd
