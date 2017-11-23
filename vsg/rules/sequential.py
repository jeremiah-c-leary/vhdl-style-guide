
from vsg import rule
from vsg import line
import re


class sequential_rule(rule.rule):

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'sequential'


class rule_001(sequential_rule):
    '''
    Sequential rule 001 checks for the proper indentation at the beginning of the line.
    '''

    def __init__(self):
        sequential_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSequential:
                self._check_indent(oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._fix_indent(oFile.lines[iLineNumber])


class rule_002(sequential_rule):
    '''
    Sequential rule 002 checks for a single space after the "<=" keyword.
    '''

    def __init__(self):
        sequential_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Ensure a single space exists after the "<=" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSequential:
                if re.match('^.*<=\s*\S', oLine.line):
                    if not re.match('^.*<=\s\S', oLine.line):
                        self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_after_word(oFile.lines[iLineNumber], '<=')


class rule_003(sequential_rule):
    '''
    Sequential rule 003 checks for a single space before the "<=" keyword.
    '''

    def __init__(self):
        sequential_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Ensure a single space exists before the "<=" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSequential:
                if not re.match('^.*\s+<=', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_before_word(oFile.lines[iLineNumber], '<=')


class rule_004(sequential_rule):
    '''
    Sequential rule 004 ensures the alignment of multiline sequential statements.
    '''

    def __init__(self):
        sequential_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Align with space after the "<=" keyword.'
        self.phase = 5

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSequential and oLine.isSequentialEnd:
                continue
            if oLine.isSequential:
                iAlignmentColumn = oLine.line.find('<=') + len('<= ')
                continue
            if oLine.insideSequential and not oLine.isComment:
                self._check_multiline_alignment(iAlignmentColumn, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.dFix['violations']:
            self._fix_multiline_alignment(oFile, iLineNumber)


class rule_005(sequential_rule):
    '''
    Sequential rule 005 ensures the alignment of the "<=" keyword over multiple lines.
    '''

    def __init__(self):
        sequential_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Inconsistent alignment of "<=" in group of lines.'
        self.phase = 5

    def analyze(self, oFile):
        lGroup = []
        fGroupFound = False
        iStartGroupIndex = None
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSequential and not fGroupFound:
                fGroupFound = True
                iStartGroupIndex = iLineNumber
            if not oLine.insideSequential and fGroupFound:
                fGroupFound = False
                self._check_keyword_alignment(iStartGroupIndex, '<=', lGroup)
                lGroup = []
                iStartGroupIndex = None
            if fGroupFound:
                if oLine.isComment:
                    lGroup.append(line.line('Removed line'))
                else:
                    lGroup.append(oLine)

    def _fix_violations(self, oFile):
        self._fix_keyword_alignment(oFile)


class rule_006(sequential_rule):
    '''
    Sequential rule 006 checks for commented out lines within a multiline sequential statement.
    '''

    def __init__(self):
        sequential_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Remove comment.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.insideSequential and oLine.isComment:
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            oFile.lines.pop(iLineNumber)
