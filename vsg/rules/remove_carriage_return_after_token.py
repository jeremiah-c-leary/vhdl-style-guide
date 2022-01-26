
from vsg import parser
from vsg import violation

from vsg.rules import utils as rules_utils
from vsg.rule_group import structure
from vsg.vhdlFile import utils


class remove_carriage_return_after_token(structure.Rule):
    '''
    Checks for a carriage return within the next two tokens after the one given.

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
    '''

    def __init__(self, name, identifier, lTokens, bInsertSpace=False):
        structure.Rule.__init__(self, name=name, identifier=identifier)
        self.lTokens = lTokens
        self.bInsertSpace = bInsertSpace

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_n_tokens_after_token(4, self.lTokens)

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            for iToken, oToken in enumerate(lTokens[:len(lTokens)]):
                if iToken < 3:
                    if isinstance(oToken, parser.carriage_return):
                        oViolation = violation.New(oToi.get_line_number(), oToi, self.solution)
                        self.add_violation(oViolation)
                        break

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()

        lTokens = utils.remove_carriage_returns_from_token_list(lTokens)
        lTokens = utils.remove_consecutive_whitespace_tokens(lTokens)
        if self.bInsertSpace:
            if not isinstance(lTokens[1], parser.whitespace):
                rules_utils.insert_whitespace(lTokens, 1)

        oViolation.set_tokens(lTokens)
