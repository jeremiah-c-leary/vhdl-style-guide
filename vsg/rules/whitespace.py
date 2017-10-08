
from vsg import rule
import re

class whitespace_rule(rule.rule):
    
    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'whitespace'
        self.phase = 2


class rule_001(whitespace_rule):
    '''Whitespace rule 001 checks spaces at the end of lines.'''

    def __init__(self):
        whitespace_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Remove trailing whitespace.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.line.endswith(' '):
                self.add_violation(iLineNumber)


class rule_002(whitespace_rule):
    '''Whitespace rule 002 checks for tabs in lines'''

    def __init__(self):
        whitespace_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Replace tabs with spaces.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if '\t' in oLine.line:
                self.add_violation(iLineNumber)


class rule_003(whitespace_rule):
    '''Whitespace rule 003 checks for spaces before semicolons'''

    def __init__(self):
        whitespace_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Remove spaces before semicolons.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if ' ;' in oLine.line:
                self.add_violation(iLineNumber)


class rule_004(whitespace_rule):
    '''Whitespace rule 004 checks for spaces before commas.'''

    def __init__(self):
        whitespace_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Remove spaces before commas.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if ' ,' in oLine.line:
                self.add_violation(iLineNumber)


class rule_005(whitespace_rule):
    '''Whitespace rule 005 checks for spaces after an open parenthesis.'''

    def __init__(self):
        whitespace_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Remove spaces after open (.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if re.match('^.*\(\s+', oLine.line):
                if not re.match('^.*\(\s+[0-9]',oLine.line):
                    self.add_violation(iLineNumber)


class rule_006(whitespace_rule):
    '''Whitespace rule 006 checks for spaces after an open parenthesis.'''

    def __init__(self):
        whitespace_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Remove spaces before close ).'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if re.match('^.*\s+\)', oLine.line) and not re.match('^\s+\)', oLine.line):
                self.add_violation(iLineNumber)


class rule_007(whitespace_rule):
    '''Whitespace rule 007 checks for spaces after a comma.'''

    def __init__(self):
        whitespace_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'Add a space after the comma.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if re.match('^.*,\S', oLine.line) and not re.match('^.*--.*,\S', oLine.line):
                self.add_violation(iLineNumber)
