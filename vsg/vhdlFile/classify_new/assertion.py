
from vsg import parser

from vsg.token import assertion as token

from vsg.vhdlFile import utils


def detect(iCurrent, lObjects):
    '''
    assertion ::=
        assert condition
            [ report expression ]
            [ severity expression ]

    The key to detecting this is looking for the keyword **assert** before a semicolon.
    '''

    iToken = iCurrent

    while lObjects[iToken].get_value() != ';':
        if utils.is_item(lObjects, iToken):
            if utils.object_value_is(lObjects, iToken, 'assert'):
                return True
        iToken += 1
    else:
        return False



def tokenize(iCurrent, lObjects):
    '''
    assertion ::=
        assert condition
            [ report expression ]
            [ severity expression ]
    '''
    iStart, iEnd = utils.get_range(lObjects, iCurrent, ';')

    # Classify target and assignment operator
    for iToken, oObject in enumerate(lObjects[iStart:iEnd], start=iStart):
        if type(oObject) == parser.item:
            if utils.object_value_is(lObjects, iToken, 'assert'):
                utils.assign_token(lObjects, iToken, token.keyword)
            elif utils.object_value_is(lObjects, iToken, 'report'):
                utils.assign_token(lObjects, iToken, token.report_keyword)
            elif utils.object_value_is(lObjects, iToken, 'severity'):
                utils.assign_token(lObjects, iToken, token.severity_keyword)
            else:
                utils.assign_token(lObjects, iToken, parser.todo)
    return iToken
