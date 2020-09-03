
from vsg import parser
from vsg.vhdlFile import utils

from vsg.token import case_generate_alternative as token

from vsg.vhdlFile.classify_new import choices
from vsg.vhdlFile.classify_new import generate_statement_body

'''
    case_generate_alternative ::=
        when [ alternative_label : ] choices =>
            generate_statement_body
'''


def detect(iObject, lObjects):

    iToken = utils.find_next_token(iObject, lObjects)
    if utils.object_value_is(lObjects, iToken, 'when'):
        return classify(iToken, lObjects)
    return iToken


def classify(iObject, lObjects):

    iToken = iObject
    utils.classify_token('when', token.when_keyword, iToken, lObjects)
    iToken += 1

    iStart, iEnd = utils.get_range(lObjects, iToken, '=>')
    iToken = choices.classify(iStart, iEnd, lObjects)

    utils.classify_token('=>', token.assignment, iToken, lObjects)
    iToken += 1

    iToken = generate_statement_body.classify(iToken, lObjects)

    return iToken
