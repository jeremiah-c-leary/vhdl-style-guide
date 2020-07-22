
from vsg import fix
from vsg import rule
from vsg import utils


class insert_blank_line_below_line_containing_item_rule(rule.rule):
    '''
    Checks for blank lines below a line and will insert a blank line if one does not exist.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    sTrigger : string
       The line attribute the rule applies to.
    '''

    def __init__(self, name, identifier, trigger):
        rule.rule.__init__(self, name=name, identifier=identifier)
        self.solution = 'Insert blank line below.'
        self.phase = 3
        self.trigger = trigger

    def analyze(self, oFile):
        lContexts = oFile.get_context_declarations()
        for dContext in lContexts:
            for iLine, oLine in enumerate(dContext['lines']):
                try:
                    oNextLine = oFile.lines[dContext['metadata']['iStartLineNumber'] + iLine + 1]
                except IndexError:
                    break
                lObjects = oLine.get_objects()
                for oObject in lObjects:
                    if isinstance(oObject, self.trigger) and not oNextLine.is_blank():
                        self.add_violation(utils.create_violation_dict(dContext['metadata']['iStartLineNumber'] + iLine))
        
    def _fix_violations(self, oFile):
        for dViolation in self.violations[::-1]:
            fix.insert_blank_line_below(self, oFile, utils.get_violation_line_number(dViolation))
