
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
            if oLine.insideConcurrent and re.match('^.*\selse\s+[\w|\']', oLine.lineNoComment.lower()):
                sLine = oLine.lineNoComment.lower()
                dViolation = utils.create_violation_dict(iLineNumber)
                dViolation['slice_index'] = []
                iStartIndex = 0
                while sLine.find(' else', iStartIndex) > 0:
                    iIndex = sLine.find(' else', iStartIndex) + len(' else')
                    dViolation['slice_index'].append(iIndex)
                    iStartIndex = iIndex
                self.add_violation(dViolation)
        if self.allow_single_line and oLine.isConcurrentBegin:
            sLine = oLine.lineNoComment.lower()
            if re.match('^.*\selse\s+.*\selse', sLine):
                dViolation = utils.create_violation_dict(iLineNumber)
                dViolation['slice_index'] = []
                iStartIndex = 0
                while sLine.find(' else', iStartIndex) > 0:
                    iIndex = sLine.find(' else', iStartIndex) + len(' else')
                    dViolation['slice_index'].append(iIndex)
                    iStartIndex = iIndex
                self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations[::-1]:
            iLineNumber = dViolation['lineNumber']
            for iSliceIndex in dViolation['slice_index'][::-1]:
                oLine = oFile.lines[iLineNumber]
                sLine = oLine.line
                oFile.lines.insert(iLineNumber + 1, copy.deepcopy(oLine))
                utils.remove_comment_attributes_from_line(oLine)
                oLine.isEndConcurrent = False
                oLine.update_line(oLine.line[:iSliceIndex])
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
