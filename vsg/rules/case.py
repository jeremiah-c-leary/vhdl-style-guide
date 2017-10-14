
from vsg import rule
import re


class case_rule(rule.rule):
    
    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'case'


class rule_001(case_rule):
    '''Case rule 001 checks for the proper indentation at the beginning of the line.'''

    def __init__(self):
        case_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isCaseKeyword or oLine.isCaseWhenKeyword or oLine.isEndCaseKeyword:
                self._check_indent(oLine, iLineNumber)


class rule_002(case_rule):
    '''Case rule 002 checks for a single space after the "case" keyword.'''

    def __init__(self):
        case_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Ensure a single space exists after the "case" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isCaseKeyword:
                if not re.match('^\s*case\s\S', oLine.lineLower):
                    self.add_violation(iLineNumber)


class rule_003(case_rule):
    '''Case rule 003 checks for a single space before the "is" keyword.'''

    def __init__(self):
        case_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Ensure a single space exists before the "is" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isCaseIsKeyword:
                self._is_single_space_before('is', oLine, iLineNumber)


class rule_004(case_rule):
    '''Case rule 004 checks for a single space after the "when" keyword.'''

    def __init__(self):
        case_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Ensure a single space exists after the "when" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isCaseWhenKeyword:
                self._is_single_space_after('when', oLine, iLineNumber)


class rule_005(case_rule):
    '''Case rule 005 checks for a single space before the "=>" keyword.'''

    def __init__(self):
        case_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Ensure a single space exists before the "=>" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isCaseWhenEnd:
                self._is_single_space_before('=>', oLine, iLineNumber)


class rule_006(case_rule):
    '''Case rule 006 checks for a single space between the "end" and "case" keywords.'''

    def __init__(self):
        case_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Ensure a single space exists between the "end" and "case" keywords.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndCaseKeyword:
                if not re.match('^\s*end\scase', oLine.lineLower):
                    self.add_violation(iLineNumber)


class rule_007(case_rule):
    '''Case rule 007 ensures a blank line exists before the "case" keyword.'''

    def __init__(self):
        case_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'Ensure a blank line exists before the "case" keyword.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isCaseKeyword:
                self._is_blank_line_before(oFile, iLineNumber)


class rule_008(case_rule):
    '''Case rule 008 ensures a blank line exists below the "case" keyword.'''

    def __init__(self):
        case_rule.__init__(self)
        self.identifier = '008'
        self.solution = 'Ensure a blank line exists below the "case" keyword.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isCaseIsKeyword:
                self._is_blank_line_after(oFile, iLineNumber)


class rule_009(case_rule):
    '''Case rule 009 ensures a blank line exists above the "end case" keywords.'''

    def __init__(self):
        case_rule.__init__(self)
        self.identifier = '009'
        self.solution = 'Ensure a blank line exists above the "end case" keywords.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndCaseKeyword:
                self._is_blank_line_before(oFile, iLineNumber)


class rule_010(case_rule):
    '''Case rule 010 ensures a blank line exists below the "end case" keywords.'''

    def __init__(self):
        case_rule.__init__(self)
        self.identifier = '010'
        self.solution = 'Ensure a blank line exists below the "end case" keywords.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndCaseKeyword:
                self._is_blank_line_after(oFile, iLineNumber)


class rule_011(case_rule):
    '''Case rule 011 ensures the alignment of multiline "when" statements.'''

    def __init__(self):
        case_rule.__init__(self)
        self.identifier = '011'
        self.solution = 'Align with space after the "when" keyword.'
        self.phase = 5

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isCaseWhenKeyword and oLine.isCaseWhenEnd:
                continue
            if oLine.isCaseWhenKeyword:
                iAlignmentColumn = (oLine.indentLevel * self.indentSize) + len('when ')
                continue
            if oLine.insideCaseWhen:
                self._check_multiline_alignment(iAlignmentColumn, oLine, iLineNumber)


class rule_012(case_rule):
    '''Case rule 012 ensures code does not exist after the => operator.'''

    def __init__(self):
        case_rule.__init__(self)
        self.identifier = '012'
        self.solution = 'Move code after the => operator to it\'s own line.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isCaseWhenEnd:
                if re.match('^.*=>\s*\w', oLine.line):
                    self.add_violation(iLineNumber)


#TODO:
# multiline case alignment
# keywords are lower case



