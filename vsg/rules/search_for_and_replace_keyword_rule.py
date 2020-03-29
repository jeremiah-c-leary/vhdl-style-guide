
from vsg import rule
from vsg import utils

import re


class search_for_and_replace_keyword_rule(rule.rule):
    '''
    This rule will search for and replace words.
    '''

    def __init__(self, name=None, identifier=None):
        rule.rule.__init__(self, name, identifier)
        self.solution = None
        self.phase = 2
        self.sKeyword = None
        self.sTrigger = None
        self.sKeyword2 = None

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.__dict__[self.sTrigger] and self.sKeyword not in oLine.lineNoComment:
            self.add_violation(utils.create_violation_dict(iLineNumber))

    def _fix_violations(self, oFile):
        for dViolation in self.violations[::-1]:
            oLine = oFile.lines[dViolation['lineNumber']]
            oLine.update_line(re.sub('' + self.sKeyword2, '' + self.sKeyword2 + ' ' + self.sKeyword, oLine.line, 1, re.IGNORECASE))
            utils.search_for_and_remove_keyword(oFile, dViolation['lineNumber'], '\(')
