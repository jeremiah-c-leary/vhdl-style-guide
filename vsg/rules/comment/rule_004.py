
from vsg import rule
import re

# Regex to find comments that ignores contents of double quoted strings,
# for example, "--" : a two bit std_logic_vector literal of don't cares.
has_comment_re = re.compile(r'^(?:".*"|[^"\n])*?(?P<comment>--.*)', re.IGNORECASE)

class rule_004(rule.rule):
    '''
    Comment rule 004 ensures there is at least one space before comments on a line with code.
    '''

    def __init__(self):
        rule.rule.__init__(self, name='comment', identifier='004')
        self.phase = 2
        self.solution = 'Add a space before the comment --'

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.__dict__['hasInlineComment']:
            match = has_comment_re.match(oLine.line)
            if match is None:
                return
            idx = match.start("comment")
            if oLine.line[idx - 1] != ' ':
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            match = has_comment_re.match(oLine.line)
            idx = match.start("comment")
            oLine.update_line(" ".join((oLine.line[:idx], oLine.line[idx:])))


