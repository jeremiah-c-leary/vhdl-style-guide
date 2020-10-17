
from vsg import parser
from vsg import rule_item
from vsg import violation

from vsg.vhdlFile import utils


class remove_lines_starting_with_token_between_token_pairs(rule_item.Rule):
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

    def __init__(self, name, identifier, oRemoveToken, lTokens):
        rule_item.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 2
        self.oRemoveToken = oRemoveToken
        self.lTokens = lTokens

    def analyze(self, oFile):
        lToi = []
        for lTokenPair in self.lTokens:
            lToi_a = oFile.get_tokens_bounded_by(lTokenPair[0], lTokenPair[1])
            lToi = utils.combine_two_token_class_lists(lToi, lToi_a)

        for oToi in lToi:
            lTokens = oToi.get_tokens()
            iLine = oToi.get_line_number()
            for iToken, oToken in enumerate(lTokens):
                if isinstance(oToken, parser.carriage_return):
                    iLine += 1
                    if utils.are_next_consecutive_token_types([parser.whitespace, self.oRemoveToken], iToken + 1, lTokens):
                        oSubToi = oToi.extract_tokens(iToken, iToken + 2)
                        oViolation = violation.New(iLine, oSubToi, self.solution)
                        self.add_violation(oViolation)
                    if utils.are_next_consecutive_token_types([self.oRemoveToken], iToken + 1, lTokens):
                        oSubToi = oToi.extract_tokens(iToken, iToken + 1)
                        oViolation = violation.New(iLine, oSubToi, self.solution)
                        self.add_violation(oViolation)

    def fix(self, oFile):
        '''
        Applies fixes for any rule violations.
        '''
        if self.fixable:
            self.analyze(oFile)
            self._print_debug_message('Fixing rule: ' + self.name + '_' + self.identifier)
            self._fix_violation(oFile)
            self.violations = []

    def _fix_violation(self, oFile):
        for oViolation in self.violations:
            oViolation.set_tokens([])
        oFile.update(self.violations)


