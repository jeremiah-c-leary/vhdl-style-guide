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
        self.bIncludeEntityDeclarations = True
        if lIgnore is None:
            self.lIgnoreTokens = []
        else:
            self.lIgnoreTokens = lIgnore
        self.configuration_documentation_link = None

    def _get_tokens_of_interest(self, oFile):
        lAllDicts = cc_utils.get_token_of_interest_dicts(
            oFile,
            self.lNames,
            self.lTokens,
            self.bIncludeDeclarativePartNames,
            self.bIncludeArchitectureBodyDeclarationsInSubprogramBody,
            self.bIncludeEntityDeclarations,
        )
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
