
from vsg.token import component_instantiation_statement as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import generic_map_aspect
from vsg.vhdlFile.classify import instantiated_unit
from vsg.vhdlFile.classify import port_map_aspect


def detect(iToken, lObjects):
    '''
    component_instantiation_statement ::=
        instantiation_label :
            instantiated_unit
                [ generic_map_aspect ]
                [ port_map_aspect ] ;
    '''
    iCurrent = utils.find_next_token(iToken, lObjects)
    iCurrent = utils.increment_token_count(iCurrent)
    iCurrent = utils.find_next_token(iCurrent, lObjects)
    if not utils.object_value_is(lObjects, iCurrent, ':'):
        return iToken
    iCurrent = utils.increment_token_count(iCurrent)
    if instantiated_unit.detect(iCurrent, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.tokenize_label(iToken, lObjects, token.instantiation_label, token.label_colon)

    iCurrent = instantiated_unit.classify(iCurrent, lObjects)

    iCurrent = generic_map_aspect.detect(iCurrent, lObjects)

    iCurrent = port_map_aspect.detect(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
