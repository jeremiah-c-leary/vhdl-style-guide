
from vsg import parser

from vsg.vhdlFile import utils

'''
    choice ::=
        simple_expression
      | discrete_range
      | *element*_simple_name
      | others
'''


def classify_until(lUntils, iToken, lObjects):

    for iIndex in range(iToken, len(lObjects)):
        if not utils.is_item(lObjects, iIndex):
            continue
        if lObjects[iIndex].get_value() in lUntils:
            return iIndex
        else:
            utils.assign_next_token(parser.todo, iIndex, lObjects)

    return iToken
