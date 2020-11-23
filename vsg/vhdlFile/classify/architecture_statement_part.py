
from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import concurrent_statement


def classify_until(lUntils, iToken, lObjects):
    '''
    architecture_statement_part ::=
        { concurrent_statement }
    '''

    return utils.detect_subelement_until(lUntils[0], concurrent_statement, iToken, lObjects)
