
from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import block_declarative_item


def detect(iToken, lObjects):
    '''
    block_declarative_part ::=
        { block_declarative_item }
    '''

    return utils.detect_submodule(iToken, lObjects, block_declarative_item)
