
from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import entity_statement


def detect(iToken, lObjects):
    '''
    entity_statement_part ::=
        { entity_statement }
    '''

    return utils.detect_submodule(iToken, lObjects, entity_statement)
