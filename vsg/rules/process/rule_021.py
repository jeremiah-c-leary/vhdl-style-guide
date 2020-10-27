
from vsg import rule_item
from vsg import parser
from vsg import violation

from vsg.token import process_statement as token

from vsg.vhdlFile import utils


class rule_021(rule_item.Rule):
    '''
    Checks for blank lines before the begin keyword if there are no process declarative items.
    '''

    def __init__(self):
        rule_item.Rule.__init__(self, 'process', '021')
        self.solution = 'Remove blank lines above begin keyword'
        self.phase = 1

    def analyze(self, oFile):
        lToi = oFile.get_tokens_bounded_by(token.process_keyword, token.begin_keyword)
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            iLine = oToi.get_line_number() + utils.count_carriage_returns(lTokens)
            for iToken, oToken in enumerate(lTokens):
                if utils.are_next_consecutive_token_types_ignoring_whitespace([token.process_keyword, token.begin_keyword], iToken, lTokens):
                    if blank_lines_exist(iToken, lTokens):
                        oViolation = violation.New(iLine, oToi, self.solution)
                        self.add_violation(oViolation)
                        break
                if utils.are_next_consecutive_token_types_ignoring_whitespace([token.close_parenthesis, token.begin_keyword], iToken, lTokens):
                    if blank_lines_exist(iToken, lTokens):
                        oViolation = violation.New(iLine, oToi, self.solution)
                        self.add_violation(oViolation)
                        break
                if utils.are_next_consecutive_token_types_ignoring_whitespace([token.is_keyword, token.begin_keyword], iToken, lTokens):
                    if blank_lines_exist(iToken, lTokens):
                        oViolation = violation.New(iLine, oToi, self.solution)
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
            lTokens.reverse()
            lNewTokens = []
            for iToken, oToken in enumerate(lTokens):
                if isinstance(oToken, parser.blank_line):
                    lNewTokens.pop()
                    continue
                lNewTokens.append(oToken)
            lNewTokens.reverse()
            oViolation.set_tokens(lNewTokens)
        oFile.update(self.violations)


def blank_lines_exist(iToken, lTokens):
    for iIndex in range(iToken, len(lTokens)):
        if isinstance(lTokens[iIndex], parser.blank_line):
            return True
    return False
