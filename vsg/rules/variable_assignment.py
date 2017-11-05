
from vsg import rule
from vsg import line
import re


class variable_assignment_rule(rule.rule):
    
    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'variable_assignment'


# TODO:
# 4) Check for alignment of := based on some form of grouping (variable_assignment lines, process, whole file?)

class rule_001(variable_assignment_rule):
    '''Variable assignment rule 001 checks for the proper indentation at the beginning of the line.'''

    def __init__(self):
        variable_assignment_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isVariableAssignment:
                self._check_indent(oLine, iLineNumber)


class rule_002(variable_assignment_rule):
    '''Variable assignment rule 002 checks for a single space after the ":=" keyword.'''

    def __init__(self):
        variable_assignment_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Ensure a single space exists after the ":=" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isVariableAssignment:
                if re.match('^.*:=\s*\S', oLine.line):
                  if not re.match('^.*:=\s\S', oLine.line):
                      self.add_violation(iLineNumber)


class rule_003(variable_assignment_rule):
    '''Variable assignment rule 003 checks for a single space before the ":=" keyword.'''

    def __init__(self):
        variable_assignment_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Ensure a single space exists before the ":=" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isVariableAssignment:
                if not re.match('^.*\s+:=', oLine.line):
                    self.add_violation(iLineNumber)


class rule_004(variable_assignment_rule):
    '''Variable assignment rule 004 ensures the alignment of multiline variable_assignment statements.'''

    def __init__(self):
        variable_assignment_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Align with space after the ":=" keyword.'
        self.phase = 5

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isVariableAssignment and oLine.isVariableAssignmentEnd:
                continue
            if oLine.isVariableAssignment:
                iAlignmentColumn = oLine.line.find(':=') + len(':= ')
                continue
            if oLine.insideVariableAssignment and not oLine.isComment:
                self._check_multiline_alignment(iAlignmentColumn, oLine, iLineNumber)


class rule_005(variable_assignment_rule):
    '''Variable assignment rule 005 ensures the alignment of the ":=" keyword over multiple lines.'''

    def __init__(self):
        variable_assignment_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Inconsistent alignment of ":=" in group of lines.'
        self.phase = 5

    def analyze(self, oFile):
        lGroup = []
        fGroupFound = False
        iStartGroupIndex = None
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isVariableAssignment and not fGroupFound:
                fGroupFound = True
                iStartGroupIndex = iLineNumber
            if not oLine.insideVariableAssignment and fGroupFound:
                fGroupFound = False
                self._check_keyword_alignment(iStartGroupIndex, ':=', lGroup)
                lGroup = []
                iStartGroupIndex = None
            if fGroupFound:
                if oLine.isComment:
                    lGroup.append(line.line('Removed line'))
                else:
                    lGroup.append(oLine)


class rule_006(variable_assignment_rule):
    '''Variable assignment rule 006 checks for commented out lines within a multiline variable_assignment statement.'''

    def __init__(self):
        variable_assignment_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Remove comment.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.insideVariableAssignment and oLine.isComment:
                self.add_violation(iLineNumber)
           


