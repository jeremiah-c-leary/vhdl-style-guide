
import rule
import re


class sequential_rule(rule.rule):
    
    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'sequential'

# TODO:
# 4) Check for alignment of <= based on some form of grouping (sequential lines, process, whole file?)

class rule_001(sequential_rule):
    '''Sequential rule 001 checks for the proper indentation at the beginning of the line.'''

    def __init__(self):
        sequential_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Ensure proper indentation.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSequential:
                self._check_indent(oLine, iLineNumber)


class rule_002(sequential_rule):
    '''Sequential rule 002 checks for a single space after the "<=" keyword.'''

    def __init__(self):
        sequential_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Ensure a single space exists after the "<=" keyword.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSequential:
                if not re.match('^.*<=\s\S', oLine.line):
                    self.add_violation(iLineNumber)


class rule_003(sequential_rule):
    '''Sequential rule 003 checks for a single space before the "<=" keyword.'''

    def __init__(self):
        sequential_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Ensure a single space exists before the "<=" keyword.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSequential:
                if not re.match('^.*\s+<=', oLine.line):
                    self.add_violation(iLineNumber)


class rule_004(sequential_rule):
    '''Sequential rule 004 ensures the alignment of multiline sequential statements.'''

    def __init__(self):
        sequential_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Align with space after the "<=" keyword.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSequential and oLine.isSequentialEnd:
                continue
            if oLine.isSequential:
                iAlignmentColumn = oLine.line.find('<=') + len('<= ')
                continue
            if oLine.insideSequential:
                self._check_multiline_alignment(iAlignmentColumn, oLine, iLineNumber)


