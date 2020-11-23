
from vsg.token import interface_package_declaration as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import identifier
from vsg.vhdlFile.classify import interface_package_generic_map_aspect


def detect(iToken, lObjects):
    '''
    interface_package_declaration ::=
        package identifier is
            new *uninstantiated_package*_name interface_package_generic_map_aspect
    '''
    if utils.is_next_token('package', iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('package', token.package_keyword, iToken, lObjects)

    iCurrent = identifier.classify(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required('is', token.is_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('new', token.new_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token(token.uninstantiated_package_name, iCurrent, lObjects)

    iCurrent = interface_package_generic_map_aspect.detect(iCurrent, lObjects)

    return iCurrent
