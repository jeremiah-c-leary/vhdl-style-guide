
from vsg import rule
from vsg import utilities

import re


class search_for_and_replace_keyword_rule(rule.rule):
    '''
    Port rule 018 checks the **generic** keyword is on the same line as the (.
    '''

    def __init__(self, name=None, identifier=None):
        rule.rule.__init__(self, name, identifier)
        self.solution = None
        self.phase = 2
        self.sKeyword = None
        self.sTrigger = None
        self.sKeyword2 = None

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.__dict__[self.sTrigger] and self.sKeyword not in oLine.lineNoComment:
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub('' + self.sKeyword2, '' + self.sKeyword2 + ' ' + self.sKeyword, oLine.line, 1, re.IGNORECASE))
            utilities.search_for_and_remove_keyword(oFile, iLineNumber, '\(')
