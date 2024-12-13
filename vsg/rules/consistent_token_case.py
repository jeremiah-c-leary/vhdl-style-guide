# -*- coding: utf-8 -*-

from vsg import parser, token, violation
from vsg.rule_group import case
from vsg.rules import consistent_case_utils as cc_utils
from vsg.vhdlFile import utils
from vsg.vhdlFile.extract import tokens


class consistent_token_case(case.Rule):
    """
    Checks the case for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens: list of token type objects
       token type to apply the case check against
    """

    def __init__(self, lTokens, lNames, lIgnore=None):
        super().__init__()
        self.subphase = 2
        self.lTokens = lTokens
        self.lNames = lNames
        self.bIncludeDeclarativePartNames = False
        self.bIncludeArchitectureBodyDeclarationsInSubprogramBody = False
        if lIgnore is None:
            self.lIgnoreTokens = []
        else:
            self.lIgnoreTokens = lIgnore
        self.configuration_documentation_link = None

    def _get_tokens_of_interest(self, oFile):
        lNameTokens = cc_utils.get_all_name_tokens(oFile, self.lNames)
        Identifiers = cc_utils.get_all_identifiers(oFile, self.lTokens)
        lProcessDicts = cc_utils.get_process_indexes(oFile)
        lArchitectureDicts = cc_utils.get_architecture_indexes(oFile)
        lSubprogramBodyDicts = cc_utils.get_subprogram_body_indexes(oFile)
        lBlockDicts = cc_utils.get_block_indexes(oFile)

        lComponentDicts = cc_utils.get_component_declaration_indexes(oFile)

        lAllDicts = cc_utils.merge_dict_lists(lArchitectureDicts, lProcessDicts)
        lAllDicts = cc_utils.merge_dict_lists(lAllDicts, lSubprogramBodyDicts)
        lAllDicts = cc_utils.merge_dict_lists(lAllDicts, lBlockDicts)
        lAllDicts = cc_utils.merge_dict_lists(lAllDicts, lComponentDicts)

        lAllDicts = cc_utils.populate_identifiers(lAllDicts, Identifiers)
        if self.bIncludeDeclarativePartNames:
            lAllDicts = cc_utils.populate_declarative_part_names(lAllDicts, lNameTokens)
        lAllDicts = cc_utils.populate_statement_part_names(lAllDicts, lNameTokens)

        lAllDicts = cc_utils.remove_duplicate_identifiers("architecture_body", "subprogram_body", lAllDicts)
        lAllDicts = cc_utils.remove_duplicate_names("architecture_body", "subprogram_body", lAllDicts)

        lAllDicts = cc_utils.remove_duplicate_identifiers("architecture_body", "process", lAllDicts)
        lAllDicts = cc_utils.remove_duplicate_names("architecture_body", "process", lAllDicts)

        lAllDicts = cc_utils.remove_duplicate_names("architecture_body", "component_declaration", lAllDicts)

        lAllDicts = cc_utils.remove_duplicate_identifiers("process", "subprogram_body", lAllDicts)
        lAllDicts = cc_utils.remove_duplicate_names("process", "subprogram_body", lAllDicts)

        lAllDicts = cc_utils.remove_duplicate_identifiers("block_statement", "subprogram_body", lAllDicts)
        lAllDicts = cc_utils.remove_duplicate_names("block_statement", "subprogram_body", lAllDicts)

        lAllDicts = cc_utils.remove_duplicate_identifiers("block_statement", "process", lAllDicts)
        lAllDicts = cc_utils.remove_duplicate_names("block_statement", "process", lAllDicts)

        lAllDicts = cc_utils.add_identifiers_from_to("block_statement", "process", lAllDicts)
        lAllDicts = cc_utils.add_identifiers_from_to("architecture_body", "process", lAllDicts)

        if self.bIncludeArchitectureBodyDeclarationsInSubprogramBody:
            lAllDicts = cc_utils.add_identifiers_from_to("architecture_body", "subprogram_body", lAllDicts)

        return cc_utils.create_tois(lAllDicts, oFile)

    def _analyze(self, lToi):
        for oToi in lToi:
            iLine, lTokens = utils.get_toi_parameters(oToi)
            sExpected = oToi.get_meta_data("expected")
            sActual = lTokens[0].get_value()
            sSolution = f"Change {sActual} to {sExpected}"
            oViolation = violation.New(iLine, oToi, sSolution)
            dAction = {}
            dAction["expected"] = sExpected
            oViolation.set_action(dAction)
            self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dActions = oViolation.get_action()
        lTokens[0].set_value(dActions["expected"])
        oViolation.set_tokens(lTokens)
