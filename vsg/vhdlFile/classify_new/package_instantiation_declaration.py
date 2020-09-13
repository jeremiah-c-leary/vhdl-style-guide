
from vsg.token import package_instantiation_declaration as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import identifier
from vsg.vhdlFile.classify_new import generic_map_aspect


def detect(iToken, lObjects):
    '''
    package_instantiation_declaration ::=
        package identifier is new *uninstantiated_package*_name
            [ generic_map_aspect ] ;
    '''

    iCurrent = utils.find_next_token(iToken, lObjects)
    if utils.object_value_is(lObjects, iCurrent, 'package'):
        if utils.find_in_next_n_tokens('new', 5, iCurrent, lObjects):
            return classify(iToken, lObjects)
        else:
            return iToken
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('package', token.package_keyword, iToken, lObjects)

    iCurrent = identifier.classify(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required('is', token.is_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('new', token.new_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token(token.uninstantiated_package_name, iCurrent, lObjects)

    iCurrent = generic_map_aspect.detect(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
