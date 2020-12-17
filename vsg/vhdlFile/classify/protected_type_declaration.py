
from vsg.token import protected_type_declaration as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import protected_type_declarative_part


def detect(iToken, lObjects):
    '''
    protected_type_declaration ::=
        **protected**
        protected_type_declarative_part
        **end** **protected** [ protected_type_simple_name ]
    '''

    if utils.is_next_token('protected', iToken, lObjects):
        if not utils.are_next_consecutive_tokens(['protected', 'body'], iToken, lObjects):
            return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('protected', token.protected_keyword, iToken, lObjects)

    iCurrent = protected_type_declarative_part.detect(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required('end', token.end_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_required('protected', token.end_protected_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_if_not(';', token.protected_type_simple_name, iCurrent, lObjects)

    return iCurrent
