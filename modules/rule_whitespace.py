
import rule


class rule_001(rule.rule):
    '''Whitespace rule 001 checks spaces at the end of lines.'''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'whitespace'
        self.identifier = '001'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if sLine.endswith(' '):
                lFailureLines.append(iLineNumber)
        return {self.name: {self.identifier: lFailureLines}}
