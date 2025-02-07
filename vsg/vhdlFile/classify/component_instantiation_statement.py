# -*- coding: utf-8 -*-

from vsg.token import component_instantiation_statement as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import generic_map_aspect, instantiated_unit, port_map_aspect


def detect(oDataStructure):
    """
    component_instantiation_statement ::=
        instantiation_label :
            instantiated_unit
                [ generic_map_aspect ]
                [ port_map_aspect ] ;
    """
    oDataStructure.align_seek_index()
    oDataStructure.increment_seek_index()
    oDataStructure.advance_to_next_seek_token()
    if not oDataStructure.seek_token_lower_value_is(":"):
        return False
    return instantiated_unit.detect(oDataStructure)


def classify(iToken, lObjects):
    iCurrent = utils.tokenize_label(iToken, lObjects, token.instantiation_label, token.label_colon)

    iCurrent = instantiated_unit.classify(iCurrent, lObjects)

    iCurrent = generic_map_aspect.detect(iCurrent, lObjects)

    iCurrent = port_map_aspect.detect(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(";", token.semicolon, iCurrent, lObjects)

    return iCurrent
