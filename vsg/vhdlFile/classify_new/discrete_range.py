
from vsg import parser

from vsg.vhdlFile import utils

'''
    discrete_range ::=
        *discrete*_subtype_indication | range
'''


def classify(iToken, lObjects):
    return utils.assign_token(lObjects, iToken, parser.todo)
