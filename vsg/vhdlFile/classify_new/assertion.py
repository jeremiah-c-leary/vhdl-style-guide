
from vsg import parser

from vsg.token import assertion as token

from vsg.vhdlFile import utils


def detected(iObject, oObject, lAllObjects, lNewObjects, dVars):
    '''
    assertion ::=
        assert condition
            [ report expression ]
            [ severity expression ]

    The key to detecting this is looking for the keyword **assert** before a semicolon.
    '''

    iToken = iObject

    while lAllObjects[iToken].get_value() != ';':
        if utils.is_item(lAllObjects, iToken):
            if utils.object_value_is(lAllObjects, iToken, 'when'):
                return False
            if utils.object_value_is(lAllObjects, iToken, 'assert'):
                return True
        iToken += 1
    else:
        return False



def tokenize(iObject, oObject, lAllObjects, lNewObjects, dVars):
    '''
    assertion ::=
        assert condition
            [ report expression ]
            [ severity expression ]
    '''
    iStart, iCurrent, iEnd = utils.get_bounds(lAllObjects, iObject, ';')

    # Classify target and assignment operator
    for iToken, oObject in enumerate(lAllObjects[iStart:iEnd], start=iStart):
        if type(oObject) == parser.item:
            if utils.object_value_is(lAllObjects, iToken, 'assert'):
                utils.assign_token(lAllObjects, iToken, token.keyword)
            elif utils.object_value_is(lAllObjects, iToken, 'report'):
                utils.assign_token(lAllObjects, iToken, token.report_keyword)
            elif utils.object_value_is(lAllObjects, iToken, 'severity'):
                utils.assign_token(lAllObjects, iToken, token.severity_keyword)
            else:
                utils.assign_token(lAllObjects, iToken, parser.todo)
    return iToken
