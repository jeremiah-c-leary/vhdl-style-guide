
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

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if sLine.endswith(' '):
                lFailureLines.append(iLineNumber)
        return {self.name: {self.identifier: lFailureLines}}


class rule_002(whitespace_rule):
    '''Whitespace rule 002 checks for tabs in lines'''

    def __init__(self):
        whitespace_rule.__init__(self)
        self.identifier = '002'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if '\t' in sLine:
                lFailureLines.append(iLineNumber)
        return {self.name: {self.identifier: lFailureLines}}

