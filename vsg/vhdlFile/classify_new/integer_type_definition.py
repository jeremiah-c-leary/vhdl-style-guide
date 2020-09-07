
from vsg.vhdlFile.classify_new import range_constraint

'''
    integer_type_definition ::=
        range_constraint
'''


def detect(iToken, lObjects):
    return range_constraint.detect(iToken, lObjects)
