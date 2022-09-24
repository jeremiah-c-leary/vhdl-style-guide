
from vsg.token import block_specification as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import generate_specification


def classify(iToken, lObjects):
    '''
    block_specification ::=
        architecture_name
      | block_statement_label
      | generate_statement_label [ ( generate_specification ) ]
    '''

    if utils.find_in_next_n_tokens('(', 2, iToken, lObjects):
        iCurrent = utils.assign_next_token(token.generate_statement_label, iToken, lObjects)
        iCurrent = utils.assign_next_token_required('(', token.open_parenthesis, iCurrent, lObjects)
        iCurrent = generate_specification.classify(iCurrent, lObjects)
        iCurrent = utils.assign_next_token_required(')', token.close_parenthesis, iCurrent, lObjects)
    else:
        iCurrent = utils.assign_next_token(token.architecture_name, iToken, lObjects)

    return iCurrent
