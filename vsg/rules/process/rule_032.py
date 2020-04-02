
import re

from vsg import rule
from vsg import utils


class rule_032(rule.rule):
    '''
    Process rule 032 checks the label for a process is on the same line as the process keyword.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'process', '032')
        self.solution = 'Move process label to the same line as the process.'
        self.phase = 1
        self.fixable = True    # The user must add the label

    def _pre_analyze(self):
        self.label_found = False
        self.label_name = ''
        self.label_line_number = 0

    def _analyze(self, oFile, oLine, iLineNumber):
        if re.match('^\s*\S+\s*:', oLine.lineNoComment) and not oLine.isSignal and not oLine.insidePortMap and not oLine.insideGenericMap and not oLine.insideInstantiation and not oLine.isConstant and not oLine.isVariable:
            self.label_found = True
            self.label_name = utils.extract_label(oLine)[0]
            self.label_line_number = iLineNumber
        if oLine.isProcessKeyword and not oLine.isProcessLabel and self.label_found:
            dViolation = utils.create_violation_dict(iLineNumber)
            dViolation['label_name'] = self.label_name
            dViolation['label_line_number'] = self.label_line_number
            self.add_violation(dViolation)
        if oLine.isProcessKeyword:
            self.label_found = False
        if oLine.isConcurrentBegin:
            self.label_found = False

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            _remove_label(self, dViolation, oFile)
            _add_label(self, dViolation, oFile)


def _remove_label(self, dViolation, oFile):
    oLine = oFile.lines[dViolation['label_line_number']]
    sLine = oLine.line
    iIndex = sLine.find(':')
    sBlank = ' '*(iIndex + 1)
    oLine.update_line(sBlank + sLine[iIndex+1:])
    if re.match('^\s*$', oLine.line):
        oLine.update_line('')
        oLine.isBlank = True


def _add_label(self, dViolation, oFile):
    oLine = utils.get_violating_line(oFile, dViolation)
    sLine = oLine.line
    oLine.update_line(dViolation['label_name'] + ' : ' + sLine)
    oLine.isProcessLabel = True
