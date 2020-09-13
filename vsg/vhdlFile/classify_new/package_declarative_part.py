
from vsg.vhdlFile.classify_new import package_declarative_item


def detect(iToken, lObjects):
    '''
    package_declarative_part ::=
        { package_declarative_item }
    '''

    return package_declarative_item.detect(iToken, lObjects)
