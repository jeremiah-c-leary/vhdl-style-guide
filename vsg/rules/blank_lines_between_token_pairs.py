

from vsg import parser
from vsg import violation

from vsg.rule_group import blank_line
from vsg.vhdlFile import utils


class blank_lines_between_token_pairs(blank_line.Rule):
    '''
    Checks for a single space between two tokens.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of token type pairs
       The tokens to check for a single space between
    '''

    def __init__(self, name, identifier, lTokenPairs):
        blank_line.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = 'Remove blank line'
        self.lTokenPairs = lTokenPairs

    def _get_tokens_of_interest(self, oFile):
        lToi = []
        for lTokenPair in self.lTokenPairs:
            lToi_a = oFile.get_tokens_bounded_by(lTokenPair[0], lTokenPair[1])
            lToi = utils.combine_two_token_class_lists(lToi, lToi_a)
        return lToi

    def _analyze(self, lToi):
        for oToi in lToi:
            iLine, lTokens = utils.get_toi_parameters(oToi)

            for iToken, oToken in enumerate(lTokens):
                iLine = utils.increment_line_number(iLine, oToken)

                if isinstance(oToken, parser.blank_line):
                    oNewToi = oToi.extract_tokens(iToken, iToken + 1)
                    oViolation = violation.New(iLine, oNewToi, self.solution)
                    self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        oViolation.set_tokens([])
