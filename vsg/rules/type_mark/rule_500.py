# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import (
    consistent_case_utils as cc_utils,
    token_case_with_prefix_suffix,
    utils,
)
from vsg.vhdlFile.extract import tokens

lTokens = []
lTokens.append(token.type_mark.name)

lDeclarationTokens = []
lDeclarationTokens.append(token.incomplete_type_declaration.identifier)
lDeclarationTokens.append(token.full_type_declaration.identifier)
lDeclarationTokens.append(token.subtype_declaration.identifier)


class rule_500(token_case_with_prefix_suffix):
    """
    This rule checks that the type marks without declarations in the current file have proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

      signal my_sig : MY_TYPE_MARK;

    **Fix**

    .. code-block:: vhdl

      signal my_sig : my_type_mark;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.bIncludeDeclarativePartNames = True
        self.bIncludeArchitectureBodyDeclarationsInSubprogramBody = True
        self.bIncludeEntityDeclarations = True
        self.groups.append("case::name")

    def _get_tokens_of_interest(self, oFile):
        self.case_exceptions_lower = utils.lowercase_list(self.case_exceptions)
        lAllDicts = cc_utils.get_token_of_interest_dicts(
            oFile,
            lTokens,
            lDeclarationTokens,
            self.bIncludeDeclarativePartNames,
            self.bIncludeArchitectureBodyDeclarationsInSubprogramBody,
            self.bIncludeEntityDeclarations,
        )
        lReturn = []
        oTokenMap = oFile.get_token_map()
        for dDict in lAllDicts:
            lLocalDeclarationIdentifiers = [oFile.lAllObjects[iIdentifier].get_value() for iIdentifier in dDict["identifiers"]]
            for iName in dDict["names"]:
                iLine = oTokenMap.get_line_number_of_index(iName)
                sName = oFile.lAllObjects[iName].get_value()
                if sName not in lLocalDeclarationIdentifiers:
                    lReturn.append(tokens.New(iName, iLine, [oFile.lAllObjects[iName]]))

        return lReturn
