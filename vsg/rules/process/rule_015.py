
from vsg.rules.process import process_rule


class rule_015(process_rule):
    '''
    Process rule 015 checks for a blank line or a comment line above the "process" keyword.
    '''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '015'
        self.solution = 'Add a space or a comment above the "process" keyword.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isProcessKeyword:
                if not oFile.lines[iLineNumber - 1].isBlank and not oFile.lines[iLineNumber - 1].isComment:
                      self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            self._insert_blank_line_above(oFile, iLineNumber)
