
from vsg import rule
from vsg import parser
from vsg import violation

from vsg.token import process_statement as token

from vsg.vhdlFile import utils


class rule_026(rule.Rule):
    '''
    Process rule 026 checks for blank lines between the end of the sensitivity list and process declarative lines.
    '''

    def __init__(self):
        rule.Rule.__init__(self, 'process', '026')
        self.solution = 'Insert blank line below'
        self.phase = 3

    def analyze(self, oFile):
        lToi = oFile.get_tokens_bounded_by(token.process_keyword, token.begin_keyword)
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            if not are_there_process_declarative_items(lTokens):
                continue
            iLine, iSearch, oLeftToken = find_beginning_of_process_declarative_region(oToi.get_line_number(), lTokens)

            if does_a_blank_line_exist(iSearch, lTokens):
                continue

            dAction = {}
            dAction['insert'] = find_carriage_return(iSearch, lTokens) + 1

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


def are_there_process_declarative_items(lTokens):
    for iToken, oToken in enumerate(lTokens):

        if utils.are_next_consecutive_token_types_ignoring_whitespace([token.process_keyword, token.begin_keyword], iToken, lTokens):
            return False
        if utils.are_next_consecutive_token_types_ignoring_whitespace([token.close_parenthesis, token.begin_keyword], iToken, lTokens):
            return False
        if utils.are_next_consecutive_token_types_ignoring_whitespace([token.is_keyword, token.begin_keyword], iToken, lTokens):
            return False

    return True


def find_beginning_of_process_declarative_region(iLine, lTokens):
    oReturn = lTokens[0]
    iReturn = 1
    iMyLine = iLine
    iReturnLine = iLine
    for iToken, oToken in enumerate(lTokens):
        iMyLine = utils.increment_line_number(iMyLine, oToken)
        if isinstance(oToken, token.close_parenthesis):
            iReturnLine = iMyLine
            oReturn = oToken
            iReturn = iToken + 1
        if isinstance(oToken, token.is_keyword):
            iReturnLine = iMyLine
            oReturn = oToken
            iReturn = iToken + 1
            break
    return iReturnLine, iReturn, oToken


def does_a_blank_line_exist(iToken, lTokens):
    if utils.are_next_consecutive_token_types([parser.whitespace, parser.comment, parser.carriage_return, parser.blank_line], iToken, lTokens):
        return True
    if utils.are_next_consecutive_token_types([parser.comment, parser.carriage_return, parser.blank_line], iToken, lTokens):
        return True
    if utils.are_next_consecutive_token_types([parser.carriage_return, parser.blank_line], iToken, lTokens):
        return True
    return False


def find_carriage_return(iToken, lTokens):
    for iIndex in range(iToken, len(lTokens)):
        if isinstance(lTokens[iIndex], parser.carriage_return):
            return iIndex
    return None
