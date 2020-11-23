
from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import entity_declarative_item


def detect(iToken, lObjects):
    '''
    entity_declarative_part ::=
        { entity_declarative_item }
    '''

    return utils.detect_submodule(iToken, lObjects, entity_declarative_item)
