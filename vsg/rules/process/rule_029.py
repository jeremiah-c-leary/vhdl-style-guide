
from vsg import rule

import re


class rule_029(rule.rule):
    '''
    Process rule 029 checks for "rising_edge" and "falling_edge" in processes.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'process'
        self.identifier = '029'
        self.solution = 'Use \'event for clocks.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.insideProcess and re.match('^.*ing_edge\s*\(', oLine.lineLower):
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub(r'rising_edge\s*\(\s*(\w+)\s*\)', r'\1"event and \1 = "1"', oLine.line, re.IGNORECASE).replace('"', '\''))
            oLine.update_line(re.sub(r'falling_edge\s*\(\s*(\w+)\s*\)', r'\1"event and \1 = "0"', oLine.line, re.IGNORECASE).replace('"', '\''))
