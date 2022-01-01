
from vsg import violation

from vsg.rule_group import structure
from vsg.vhdlFile import utils


class remove_tokens(structure.Rule):
    '''
    Removes a token and duplicate whitespace.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : token object type list
       tokens to remove

    '''

    def __init__(self, name, identifier, lTokens):
        structure.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 1
        self.lTokens = lTokens

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_n_tokens_before_and_after_tokens(1, self.lTokens)

    def _analyze(self, lToi):
        for oToi in lToi:
           self.add_violation(violation.New(oToi.get_line_number(), oToi, self.solution))

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        lTokens.pop(1)
        lTokens = utils.remove_consecutive_whitespace_tokens(lTokens)
        oViolation.set_tokens(lTokens)
