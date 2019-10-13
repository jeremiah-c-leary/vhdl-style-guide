
from vsg import rule

import re


class rule_013(rule.rule):
    '''Whitespace rule 013 checks for spaces before and after math operators.'''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'whitespace'
        self.identifier = '013'
        self.phase = 2
        self.solution = 'Add a single space before and/or after math operator.'

    def _analyze(self, oFile, oLine, iLineNumber):
        sLine = oLine.lineNoComment
        if re.match('^.*\)[and|nand|or|nor|xor|xnor]', sLine, flags=re.IGNORECASE):
            self.add_violation(iLineNumber)
        if re.match('^.* and\(', sLine, flags=re.IGNORECASE):
            self.add_violation(iLineNumber)
        if re.match('^.* nand\(', sLine, flags=re.IGNORECASE):
            self.add_violation(iLineNumber)
        if re.match('^.* or\(', sLine, flags=re.IGNORECASE):
            self.add_violation(iLineNumber)
        if re.match('^.* nor\(', sLine, flags=re.IGNORECASE):
            self.add_violation(iLineNumber)
        if re.match('^.* xor\(', sLine, flags=re.IGNORECASE):
            self.add_violation(iLineNumber)
        if re.match('^.* xnor\(', sLine, flags=re.IGNORECASE):
            self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            iCommentIndex = oLine.line.find('--')
            if iCommentIndex == -1:
                oLine.update_line(re.sub(r'\)([and|nand|or|nor|xor|xnor])', r') \1', oLine.line, flags=re.IGNORECASE))
                oLine.update_line(re.sub(r'([and|nand|or|nor|xor|xnor])\(', r'\1 (', oLine.line, flags=re.IGNORECASE))
