
from vsg import rule_item
from vsg import parser
from vsg import violation

from vsg.token import process_statement as token

from vsg.vhdlFile import utils


class rule_027(rule_item.Rule):
    '''
    Checks for blank lines between the process declarative lines and the "begin" keyword.
    '''

    def __init__(self):
        rule_item.Rule.__init__(self, 'process', '027')
        self.solution = 'Insert blank line above begin keyword'
        self.phase = 3

    def analyze(self, oFile):
        lToi = oFile.get_tokens_bounded_by(token.process_keyword, token.begin_keyword)
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            iLine = oToi.get_line_number() + utils.count_carriage_returns(lTokens)
            lTokens.reverse()
            if utils.are_next_consecutive_token_types_ignoring_whitespace([token.begin_keyword, token.is_keyword], 0, lTokens):
                continue
            if utils.are_next_consecutive_token_types_ignoring_whitespace([token.begin_keyword, token.close_parenthesis], 0, lTokens):
                continue
            if utils.are_next_consecutive_token_types_ignoring_whitespace([token.begin_keyword, token.process_keyword], 0, lTokens):
                continue
            if utils.are_next_consecutive_token_types([token.begin_keyword, parser.whitespace, parser.carriage_return, parser.blank_line], 0, lTokens):
                continue
            if utils.are_next_consecutive_token_types([token.begin_keyword, parser.carriage_return, parser.blank_line], 0, lTokens):
                continue
            dAction = {}
            if isinstance(lTokens[1], parser.whitespace):
                dAction['insert'] = len(lTokens) - 2
            else:
                dAction['insert'] = len(lTokens) - 1
            lTokens.reverse()
            oViolation = violation.New(iLine, oToi, self.solution)
            oViolation.set_action(dAction)
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
            lTokens = oViolation.get_tokens()
            dAction = oViolation.get_action()
            lTokens.insert(dAction['insert'], parser.carriage_return())
            lTokens.insert(dAction['insert'], parser.blank_line())
            oViolation.set_tokens(lTokens)
        oFile.update(self.violations)
