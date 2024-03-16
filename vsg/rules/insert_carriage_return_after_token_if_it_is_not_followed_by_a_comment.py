# -*- coding: utf-8 -*-


from vsg import parser, violation
from vsg.rule_group import structure
from vsg.rules import utils as rules_utils
from vsg.vhdlFile import utils


class insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment(structure.Rule):
    """
    Checks for a single space between two tokens.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    token : token object
       The token to insert a carriage return after.
    """

    def __init__(self, lTokens):
        super().__init__()
        self.lTokens = lTokens
        self.configuration_documentation_link = None

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_n_tokens_after_token(2, self.lTokens)

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            if utils.are_next_consecutive_token_types([parser.carriage_return], 1, lTokens):
                continue
            if utils.are_next_consecutive_token_types([parser.whitespace, parser.comment], 1, lTokens):
                continue
            if utils.are_next_consecutive_token_types([parser.comment], 1, lTokens):
                continue
            else:
                self.add_violation(violation.New(oToi.get_line_number(), oToi, self.solution))

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        rules_utils.insert_carriage_return(lTokens, 1)
        oViolation.set_tokens(lTokens)
