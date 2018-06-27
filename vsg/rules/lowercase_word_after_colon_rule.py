
from vsg import rule
from vsg import fix
from vsg import check
from vsg import utilities

import re


class lowercase_word_after_colon_rule(rule.rule):
    '''
    This class checks the word after a : is lowercase.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    sTrigger : string
       The line attribute the rule applies to.

    bVhdlKeyword : boolean
       Check whether word is a VHDL keyword
 
    '''

    def __init__(self, name=None, identifier=None, sTrigger=None, bVhdlKeyword=False):
        rule.rule.__init__(self, name, identifier)
        self.solution = None
        self.phase = 6
        self.sTrigger = sTrigger
        self.dVars = {}
        self.bVhdlKeyword = bVhdlKeyword

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.__dict__[self.sTrigger] and re.match('^.*:\s*\w', oLine.lineLower):
                sLine = oLine.line.split(':')[1].lstrip().split()[0].split('(')[0]
                if self.bVhdlKeyword:
                    if utilities.is_vhdl_keyword(sLine):
                        self.dVars[iLineNumber] = sLine
                        check.is_lowercase(self, sLine, iLineNumber)
                else:
                    self.dVars[iLineNumber] = sLine
                    check.is_lowercase(self, sLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            fix.lower_case(self, oLine, self.dVars[iLineNumber])
        self.dVars = {}
