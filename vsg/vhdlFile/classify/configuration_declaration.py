
from vsg.token import configuration_declaration as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import configuration_declarative_part
#from vsg.vhdlFile.classify import architecture_statement_part


def detect(iToken, lObjects):
    '''
    configuration_declaration ::=
      configuration identifier of *entity*_name is
        configuration_declarative_part
        { verification_unit_binding_indication ; }
      block_configuration
      end [ configuration ] [ *configuration*_simple_name ] ;
    '''

    if utils.is_next_token('configuration', iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = classify_opening_declaration(iToken, lObjects)

    iCurrent = configuration_declarative_part.detect(iCurrent, lObjects)
#
#    iCurrent = architecture_statement_part.classify_until(['end'], iCurrent, lObjects)

    iCurrent = classify_closing_declaration(iToken, lObjects)

    return iCurrent


def classify_opening_declaration(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('configuration', token.configuration_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token(token.identifier, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('of', token.of_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token(token.entity_name, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('is', token.is_keyword, iCurrent, lObjects)

    return iCurrent


def classify_closing_declaration(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('end', token.end_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_if('configuration', token.end_configuration_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if_not(';', token.configuration_simple_name, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
