
import rule

class whitespace_rule(rule.rule):
    
    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'whitespace'


class rule_001(whitespace_rule):
    '''Whitespace rule 001 checks spaces at the end of lines.'''

    def __init__(self):
        whitespace_rule.__init__(self)
        self.identifier = '001'
        self.description = 'Remove trailing whitespace.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if sLine.endswith(' '):
                lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines


class rule_002(whitespace_rule):
    '''Whitespace rule 002 checks for tabs in lines'''

    def __init__(self):
        whitespace_rule.__init__(self)
        self.identifier = '002'
        self.description = 'Replace tabs with spaces.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if '\t' in sLine:
                lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines


class rule_003(whitespace_rule):
    '''Whitespace rule 003 checks for spaces before semicolons'''

    def __init__(self):
        whitespace_rule.__init__(self)
        self.identifier = '003'
        self.description = 'Remove spaces before semicolons.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if ' ;' in sLine:
                lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines


class rule_004(whitespace_rule):
    '''Whitespace rule 004 checks for spaces before commas.'''

    def __init__(self):
        whitespace_rule.__init__(self)
        self.identifier = '004'
        self.description = 'Remove spaces before commas.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if ' ,' in sLine:
                lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines

