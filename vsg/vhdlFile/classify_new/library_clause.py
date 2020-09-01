
from vsg import parser
from vsg.token import library_clause as token

from vsg.vhdlFile.classify_new import logical_name_list

from vsg.vhdlFile import utils


def detect(iCurrent, lObjects):
    '''
    library_clause ::=
        library logic_name_list ;
    '''
    if utils.object_value_is(lObjects, iCurrent, 'library'):
        return classify(iCurrent, lObjects)
    return iCurrent


def classify(iCurrent, lObjects):

    iStart, iEnd = utils.get_range(lObjects, iCurrent, ';')

    utils.assign_token(lObjects, iStart, token.keyword)

    logical_name_list.classify(iStart + 1, iEnd, lObjects)
#
    utils.classify_token(';', token.semicolon, iEnd, lObjects)
    return iEnd
