
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
        self.clock = 'event'
        self.configuration.append('clock')

    def _analyze(self, oFile, oLine, iLineNumber):
        if self.clock == 'event':
            if oLine.isClockStatement and re.match('^.*ing_edge\s*\(', oLine.lineLower):
                self.add_violation(iLineNumber)
        else:
            if oLine.isClockStatement and re.match('^.*\'event', oLine.lineLower):
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            if self.clock == 'event':
                oLine.update_line(re.sub(r'rising_edge\s*\(\s*(\w+)\s*\)', r'\1"event and \1 = "1"', oLine.line, re.IGNORECASE).replace('"', '\''))
                oLine.update_line(re.sub(r'falling_edge\s*\(\s*(\w+)\s*\)', r'\1"event and \1 = "0"', oLine.line, re.IGNORECASE).replace('"', '\''))
            else:
                oLine.update_line(re.sub(r'(\w+)\'event\s+and\s+\w+\s*=\s*\'\s*0\s*\'', r'falling_edge(\1)', oLine.line, re.IGNORECASE))
                oLine.update_line(re.sub(r'(\w+)\'event\s+and\s+\w+\s*=\s*\'\s*1\s*\'', r'rising_edge(\1)', oLine.line, re.IGNORECASE))

    def _get_solution(self, iLineNumber):
        if self.clock == 'event':
            return 'Use \'event for clocks.'
        else:
            return 'Use rising_edge or falling_edge for clocks.'
