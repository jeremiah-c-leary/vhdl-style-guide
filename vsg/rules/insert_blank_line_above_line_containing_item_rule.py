
from vsg import fix
from vsg import rule
from vsg import utils


class insert_blank_line_above_line_containing_item_rule(rule.rule):
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

    def __init__(self, name, identifier, trigger, allowComment=False):
        rule.rule.__init__(self, name=name, identifier=identifier)
        self.solution = 'Insert blank line above.'
        self.phase = 3
        self.trigger = trigger
        self.allowComment = allowComment
        self.configuration.append('allowComment')

    def analyze(self, oFile):
        lContexts = oFile.get_context_declarations()
        for dContext in lContexts:
            oPreviousLine = oFile.lines[dContext['metadata']['iStartLineNumber'] - 1]
            for iLine, oLine in enumerate(dContext['lines']):
                lObjects = oLine.get_objects()
                for oObject in lObjects:
                    if isinstance(oObject, self.trigger) and not oPreviousLine.is_blank():
                        if not oPreviousLine.is_comment() or not self.allowComment:
                            self.add_violation(utils.create_violation_dict(dContext['metadata']['iStartLineNumber'] + iLine))
                oPreviousLine = oLine
        
    def _fix_violations(self, oFile):
        for dViolation in self.violations[::-1]:
            fix.insert_blank_line_above(self, oFile, utils.get_violation_line_number(dViolation))
