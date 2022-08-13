
from vsg.token import binding_indication as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import entity_aspect
from vsg.vhdlFile.classify import generic_map_aspect
from vsg.vhdlFile.classify import port_map_aspect


def detect(iToken, lObjects):
    if utils.is_next_token('use', iToken, lObjects):
        return classify(iToken, lObjects)
    if utils.is_next_token('generic', iToken, lObjects):
        return classify(iToken, lObjects)
    if utils.is_next_token('port', iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):
    '''
    binding_indication ::=
        [ **use** entity_aspect ]
        [ generic_map_aspect ]
        [ port_map_aspect ]
    '''
    iCurrent = iToken

    if utils.is_next_token('use', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required('use', token.use_keyword, iCurrent, lObjects)
        iCurrent = entity_aspect.classify(iCurrent, lObjects)

    iCurrent = generic_map_aspect.detect(iCurrent, lObjects)

    iCurrent = port_map_aspect.detect(iCurrent, lObjects)

    return iCurrent
