
from vsg import rule
from vsg import check
from vsg import fix
from vsg import utils


class rule_003(rule.rule):
    '''
    Concurrent rule 003 checks the alignment of multiline concurrent assignments.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'concurrent'
        self.identifier = '003'
        self.solution = 'Align first character in row to the column of text one space after the <= or to the open parenthesis in the line above.'
        self.phase = 6

    def _pre_analyze(self):
        self.iAlignmentColumn = 0
        self.dParenthesis = {}

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.insideConcurrent:
            self.dParenthesis[iLineNumber] = {}
            self.dParenthesis[iLineNumber]['open'] = extract_open_parenthesis_locations(oLine.lineNoComment)
            self.dParenthesis[iLineNumber]['closed'] = extract_closed_parenthesis_locations(oLine.lineNoComment)
            self.dParenthesis[iLineNumber]['character'] = utils.begin_of_line_index(oLine)
            self.dParenthesis[iLineNumber]['offset'] = 0
            if oLine.isConcurrentBegin:
                self.dParenthesis[iLineNumber]['begin'] = iLineNumber
                self.dParenthesis[iLineNumber]['align'] = oLine.line.find('<') + 3
                if not oLine.isEndConcurrent:
                    self.iAlignmentColumn = oLine.line.find('<') + 3
            else:
                self.dParenthesis[iLineNumber]['begin'] = self.dParenthesis[iLineNumber - 1]['begin']
                self.dParenthesis[iLineNumber]['align'] = self.dParenthesis[iLineNumber - 1]['align']
                check.multiline_alignment_with_parenthesis(self, self.iAlignmentColumn, oLine, iLineNumber, self.dParenthesis)

            clear_parenthesis_dictionary(self, oLine)

    def _fix_violations(self, oFile):
        for iLineNumber in self.dFix['violations']:
            fix.multiline_alignment(self, oFile, iLineNumber)


def clear_parenthesis_dictionary(self, oLine):
    if oLine.isEndConcurrent:
        self.dParenthesis = {}


def extract_open_parenthesis_locations(sLine):
    lReturn = []
    iIndex = 0
    while True:
        iIndex = sLine.find('(', iIndex)
        if iIndex == -1:
            break
        lReturn.append(iIndex)
        iIndex = iIndex + 1
    return lReturn


def extract_closed_parenthesis_locations(sLine):
    lReturn = []
    iIndex = 0
    while True:
        iIndex = sLine.find(')', iIndex)
        if iIndex == -1:
            break
        lReturn.append(iIndex)
        iIndex = iIndex + 1
    return lReturn
