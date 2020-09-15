
from vsg.vhdlFile.classify_new import range_constraint


def detect(iToken, lObjects):
    '''
    integer_type_definition ::=
        range_constraint
    '''

    return range_constraint.detect(iToken, lObjects)
