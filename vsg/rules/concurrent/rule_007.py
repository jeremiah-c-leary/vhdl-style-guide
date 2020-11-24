
from vsg import rule
from vsg import parser
from vsg import token
from vsg import violation

from vsg.vhdlFile import utils


lSplitTokens = []
lSplitTokens.append(token.conditional_waveforms.else_keyword)

lTokenPairs = []
lTokenPairs.append([token.concurrent_conditional_signal_assignment.assignment, token.concurrent_conditional_signal_assignment.semicolon])


class rule_007(rule.Rule):
    '''
    Checks the when and else keywords are on the same line
    '''

    def __init__(self):
        rule.Rule.__init__(self, 'concurrent', '007')
        self.solution = 'move code after else to next line.'
        self.phase = 1
        self.lSplitTokens = lSplitTokens
        self.lTokenPairs = lTokenPairs
        self.allow_single_line = False
        self.configuration.append('allow_single_line')

    def analyze(self, oFile):

        lToi = get_tokens_of_interest(oFile, self.lTokenPairs)

        for oToi in lToi:
            lTokens = oToi.get_tokens()

            if utils.find_carriage_return(lTokens) is None and self.allow_single_line:
                for oSplitToken in self.lSplitTokens:
                    if utils.count_token_types_in_list_of_tokens(oSplitToken, lTokens) > 1:
                        break
                else:
                    continue

            iLine = oToi.get_line_number()
            for iToken, oToken in enumerate(lTokens):
                iLine = utils.increment_line_number(iLine, oToken)
                for oSplitToken in self.lSplitTokens:
                    if isinstance(oToken, oSplitToken):
                        if utils.are_next_consecutive_token_types([parser.whitespace, parser.comment], iToken + 1, lTokens):
                            continue
                        if utils.are_next_consecutive_token_types([parser.comment], iToken + 1, lTokens):
                            continue
                        if utils.are_next_consecutive_token_types([parser.carriage_return], iToken + 1, lTokens):
                            continue
                        oViolation = violation.New(iLine, oToi.extract_tokens(iToken, iToken), self.solution)
                        self.add_violation(oViolation)
                        break

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
            lTokens = oViolation.get_tokens()
            lTokens.append(parser.carriage_return())
            oViolation.set_tokens(lTokens)
        oFile.update(self.violations)


def get_tokens_of_interest(oFile, lTokenPairs):
    lToi = []
    for lTokenPair in lTokenPairs:
        aToi = oFile.get_tokens_bounded_by(lTokenPair[0], lTokenPair[1])
        lToi = utils.combine_two_token_class_lists(lToi, aToi)
    return lToi

