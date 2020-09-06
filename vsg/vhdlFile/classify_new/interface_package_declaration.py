
from vsg.token import interface_package_declaration as token

from vsg.vhdlFile.classify_new import identifier
from vsg.vhdlFile.classify_new import interface_package_generic_map_aspect

from vsg.vhdlFile import utils


def detect(iToken, lObjects):
    '''
    interface_package_declaration ::=
        package identifier is
            new *uninstantiated_package*_name interface_package_generic_map_aspect
    '''
    iCurrent = utils.find_next_token(iToken, lObjects)
    if utils.object_value_is(lObjects, iCurrent, 'package'):
        return classify(iCurrent, lObjects)
    return iToken


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_if('package', token.package_keyword, iToken, lObjects)
    iCurrent = identifier.classify(iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if('is', token.is_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if('new', token.new_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token(token.uninstantiated_package_name, iCurrent, lObjects)
    iCurrent = interface_package_generic_map_aspect.detect(iCurrent, lObjects)
    return iCurrent
