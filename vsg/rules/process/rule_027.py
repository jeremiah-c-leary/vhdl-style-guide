
from vsg import rule
from vsg import parser
from vsg import violation

from vsg.token import process_statement as token

from vsg.rules import utils as rules_utils

from vsg.vhdlFile import utils


class rule_027(rule.Rule):
    '''
    Checks for blank lines between the process declarative lines and the "begin" keyword.
    '''

    def __init__(self):
        rule.Rule.__init__(self, 'process', '027')
        self.phase = 3
        self.style = 'require_blank_line'
        self.configuration.append('style')

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_bounded_by(token.process_keyword, token.begin_keyword)

    def _analyze(self, lToi):
        if self.style == 'require_blank_line':
            _analyze_require_blank_line(self, lToi)
        elif self.style == 'no_blank_line':
            _analyze_no_blank_line(self, lToi)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        if dAction['action'] == 'Insert':
            rules_utils.insert_carriage_return(lTokens, dAction['index'])
            rules_utils.insert_blank_line(lTokens, dAction['index'])
            oViolation.set_tokens(lTokens)
        elif dAction['action'] == 'Remove':
            iStart = dAction['start']
            iEnd = dAction['end']
            lNewTokens = lTokens[:iStart]
            lNewTokens.extend(lTokens[iEnd:])
            oViolation.set_tokens(lNewTokens)


def _analyze_require_blank_line(self, lToi):
    sSolution = 'Insert blank line above *begin* keyword'
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
        dAction['action'] = 'Insert'
        if isinstance(lTokens[1], parser.whitespace):
            dAction['index'] = len(lTokens) - 2
        else:
            dAction['index'] = len(lTokens) - 1
        lTokens.reverse()
        oViolation = violation.New(iLine, oToi, sSolution)
        oViolation.set_action(dAction)
        self.add_violation(oViolation)

def _analyze_no_blank_line(self, lToi):
    sSolution = 'Remove blank line(s) above *begin* keyword'
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
        if not utils.are_next_consecutive_token_types([token.begin_keyword, parser.whitespace, parser.carriage_return, parser.blank_line], 0, lTokens) and \
           not utils.are_next_consecutive_token_types([token.begin_keyword, parser.carriage_return, parser.blank_line], 0, lTokens):
            continue
        dAction = {}
        dAction['action'] = 'Remove'

        if isinstance(lTokens[1], parser.whitespace):
            iEnd = len(lTokens) - 2
        else:
            iEnd = len(lTokens) - 3

        for iToken, oToken in enumerate(lTokens):
            if isinstance(oToken, parser.carriage_return):
                if not isinstance(lTokens[iToken + 1], parser.carriage_return):
                    iStart = len(lTokens) - iToken - 2
                    break

        lTokens.reverse()

        dAction['start'] = iStart
        dAction['end'] = iEnd
        oViolation = violation.New(iLine, oToi, sSolution)
        oViolation.set_action(dAction)
        self.add_violation(oViolation)
