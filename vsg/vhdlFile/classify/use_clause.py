
from vsg.token import use_clause as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import utils as classify_utils


def detect(iToken, lObjects):
    '''
    use_clause ::=
        use selected_name { , selected_name } ;
    '''
    if utils.is_next_token('use', iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('use', token.keyword, iToken, lObjects)

    while not utils.is_next_token(';', iCurrent, lObjects):
        iCurrent = classify_utils.classify_selected_name(iCurrent, lObjects, token)
    
        if utils.is_next_token(',', iCurrent, lObjects):
            iCurrent = utils.assign_next_token_required(',', token.comma, iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)
    return iCurrent
