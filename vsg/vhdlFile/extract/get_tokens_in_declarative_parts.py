# -*- coding: utf-8 -*-

from vsg import parser
from vsg.vhdlFile import utils
from vsg.vhdlFile.extract import (
    get_tokens_in_architecture_declarative_part,
    get_tokens_in_block_declarative_part,
    get_tokens_in_entity_declarative_part,
    get_tokens_in_package_body_declarative_part,
    get_tokens_in_package_declarative_part,
    get_tokens_in_process_declarative_part,
    get_tokens_in_protected_type_body_declarative_part,
    get_tokens_in_subprogram_declarative_part,
)


def get_tokens_in_declarative_parts(lAllTokens, oTokenMap):
    lProtectedType = get_tokens_in_protected_type_body_declarative_part.extract(lAllTokens, oTokenMap)
    lArchitecture = get_tokens_in_architecture_declarative_part.extract(lAllTokens, oTokenMap)
    lPackageBody = get_tokens_in_package_body_declarative_part.extract(lAllTokens, oTokenMap)
    lSubprogram = get_tokens_in_subprogram_declarative_part.extract(lAllTokens, oTokenMap)
    lPackage = get_tokens_in_package_declarative_part.extract(lAllTokens, oTokenMap)
    lProcess = get_tokens_in_process_declarative_part.extract(lAllTokens, oTokenMap)
    lEntity = get_tokens_in_entity_declarative_part.extract(lAllTokens, oTokenMap)
    lBlock = get_tokens_in_block_declarative_part.extract(lAllTokens, oTokenMap)

    lReturn = utils.combine_two_token_class_lists(lArchitecture, lProtectedType)
    lReturn = utils.combine_two_token_class_lists(lReturn, lPackage)
    lReturn = utils.combine_two_token_class_lists(lReturn, lPackageBody)
    lReturn = utils.combine_two_token_class_lists(lReturn, lSubprogram)
    lReturn = utils.combine_two_token_class_lists(lReturn, lProcess)
    lReturn = utils.combine_two_token_class_lists(lReturn, lEntity)
    lReturn = utils.combine_two_token_class_lists(lReturn, lBlock)

    return lReturn
