
from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import protected_type_declarative_item


def detect(iToken, lObjects):
    '''
    protected_type_declarative_part ::=
      { protected_type_declarative_item }
    '''

    return utils.detect_submodule(iToken, lObjects, protected_type_declarative_item)
