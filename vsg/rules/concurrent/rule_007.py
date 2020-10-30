
from vsg import rule
from vsg import utils

import re
import copy


class rule_007(rule.rule):
    '''
    Concurrent rule 007 checks for code after the "else" keyword.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'concurrent'
        self.identifier = '007'
        self.solution = 'Move code after "else" to the next line.'
        self.phase = 1
        self.allow_single_line = False
        self.configuration.append('allow_single_line')

    def _analyze(self, oFile, oLine, iLineNumber):
        if not self.allow_single_line:
            sLine = oLine.lineNoComment.lower()
            if oLine.insideConcurrent and re.match('^.*\selse\s+[\w|\']', sLine):
                _update_violation(self, iLineNumber, sLine)
        if self.allow_single_line and oLine.isConcurrentBegin:
            sLine = oLine.lineNoComment.lower()
            if re.match('^.*\selse\s+.*\selse', sLine):
                _update_violation(self, iLineNumber, sLine)

    def _fix_violations(self, oFile):
        for dViolation in self.violations[::-1]:
            iLineNumber = utils.get_violation_line_number(dViolation)
            for iSliceIndex in dViolation['slice_index'][::-1]:
                oLine = oFile.lines[iLineNumber]
                utils.copy_line(oFile, iLineNumber)
                _modify_existing_line(oLine, iSliceIndex)
                _modify_copied_line(oFile, iLineNumber, iSliceIndex, dViolation)


def _update_violation(self, iLineNumber, sLine):
    dViolation = utils.create_violation_dict(iLineNumber)
    dViolation['slice_index'] = []
    iStartIndex = 0
    while sLine.find(' else', iStartIndex) > 0:
        iIndex = sLine.find(' else', iStartIndex) + len(' else')
        dViolation['slice_index'].append(iIndex)
        iStartIndex = iIndex
    self.add_violation(dViolation)


def _modify_existing_line(oLine, iSliceIndex):
    utils.remove_comment_attributes_from_line(oLine)
    oLine.isEndConcurrent = False
    oLine.update_line(oLine.line[:iSliceIndex])


def _modify_copied_line(oFile, iLineNumber, iSliceIndex, dViolation):
    oLine = oFile.lines[iLineNumber + 1]
    oLine.isConcurrentBegin = False
    if iSliceIndex == dViolation['slice_index'][-1]:
        oLine.isEndConcurrent = True
    else:
        oLine.isEndConcurrent = False
    sLine = oLine.line[iSliceIndex:]
    try:
        oLine.commentColumn = sLine.index('--')
    except ValueError:
        oLine.commentColumn = None
    oLine.update_line(sLine)

from vsg import rule_item
from vsg import parser
from vsg import token
from vsg import violation

from vsg.vhdlFile import utils


lSplitTokens = []
lSplitTokens.append(token.conditional_waveforms.else_keyword)

lTokenPairs = []
lTokenPairs.append([token.concurrent_conditional_signal_assignment.assignment, token.concurrent_conditional_signal_assignment.semicolon])


class rule_007(rule_item.Rule):
    '''
    Checks the when and else keywords are on the same line
    '''

    def __init__(self):
        rule_item.Rule.__init__(self, 'concurrent', '007')
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
                    bBreak = False
                    if utils.count_token_types_in_list_of_tokens(oSplitToken, lTokens) > 1:
                        bBreak = True
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

