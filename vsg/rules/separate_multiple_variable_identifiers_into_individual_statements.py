# -*- coding: utf-8 -*-

import copy

from vsg import parser, token, violation
from vsg.rule_group import structure
from vsg.vhdlFile import utils


class separate_multiple_variable_identifiers_into_individual_statements(structure.Rule):
    """
    Checks the case for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of parser object types
       object types to check the prefix

    lPrefixes : string list
       acceptable prefixes
    """

    def __init__(self, lTokens, iAllow=2):
        super().__init__()
        self.solution = "Split variable declaration into individual declarations"
        self.lTokens = lTokens
        self.consecutive = iAllow
        self.configuration.append("consecutive")
        self.configuration_documentation_link = "configuring_number_of_variables_in_variable_declaration_link"

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_bounded_by(
            token.variable_declaration.variable_keyword,
            token.variable_declaration.semicolon,
            bIncludeTillBeginningOfLine=True,
        )

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            iIdentifiers = 0
            iStartIndex = None
            iEndIndex = 0
            bPreTokens = True
            lPreTokens = []
            lIdentifiers = []
            for iToken, oToken in enumerate(lTokens):
                if isinstance(oToken, token.variable_declaration.identifier):
                    lIdentifiers.append(oToken)
                    iIdentifiers += 1
                    if iStartIndex is None:
                        iStartIndex = iToken
                    iEndIndex = iToken
                    bPreTokens = False

                if bPreTokens:
                    lPreTokens.append(oToken)

            if iIdentifiers > self.consecutive:
                oViolation = violation.New(oToi.get_line_number(), oToi, self.solution)
                dAction = {}
                dAction["start"] = iStartIndex
                dAction["end"] = iEndIndex
                dAction["number"] = iIdentifiers
                dAction["identifiers"] = lIdentifiers
                oViolation.set_action(dAction)
                self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()

        lFinalTokens = []
        for oIdentifier in dAction["identifiers"]:
            lNewTokens = []
            for iToken, oToken in enumerate(lTokens):
                if iToken < dAction["start"]:
                    lNewTokens.append(copy.deepcopy(oToken))
                if iToken == dAction["start"]:
                    lNewTokens.append(oIdentifier)
                if iToken > dAction["end"]:
                    lNewTokens.append(copy.deepcopy(oToken))
            lNewTokens = utils.remove_carriage_returns_from_token_list(lNewTokens)
            lFinalTokens.extend(lNewTokens)
            lFinalTokens.append(parser.carriage_return())

        lFinalTokens.pop()
        oViolation.set_tokens(lFinalTokens)
