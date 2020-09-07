
from vsg.vhdlFile.classify_new import subtype_indication

'''
    element_subtype_definition ::=
        subtype_indication
'''


def classify(iToken, lObjects):
    return subtype_indication.classify(iToken, lObjects)
