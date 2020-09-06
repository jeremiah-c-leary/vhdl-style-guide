
from vsg import parser

from vsg.vhdlFile import utils

'''
    subtype_indication ::=
        [ resolution_indication ] type_mark [ constraint ]
'''


def classify(iToken, lObjects):
    return utils.assign_token(lObjects, iToken, parser.todo)
