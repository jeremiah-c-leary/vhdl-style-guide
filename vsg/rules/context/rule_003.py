
from vsg import fix
from vsg import check
from vsg import rule
from vsg import utils


class rule_003(rule.rule):
    '''
    Checks for blank lines above a line and will insert a blank line if one does not exist.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    sTrigger : string
       The line attribute the rule applies to.
    '''

    def __init__(self):
        rule.rule.__init__(self, name='context', identifier='003')
        self.solution = 'Insert blank line above.'
        self.phase = 3

    def analyze(self, oFile):
        lContexts = oFile.get_context_declarations()
        for dContext in lContexts:
            oPreviousLine = oFile.lines[dContext['metadata']['iStartLineNumber'] - 1]
            if not oPreviousLine.is_blank():
                if not oPreviousLine.is_comment():
                    self.add_violation(utils.create_violation_dict(dContext['metadata']['iStartLineNumber']))
        
    def _fix_violations(self, oFile):
        for dViolation in self.violations[::-1]:
            fix.insert_blank_line_above(self, oFile, utils.get_violation_line_number(dViolation))
