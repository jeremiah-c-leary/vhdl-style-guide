
from vsg import rule
from vsg import utils
from vsg import parser


class remove_blank_lines_above_item_rule(rule.rule):
    '''
    Checks for excessive blank lines above a line containing an item.

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
        self.solution = 'Remove all but one blank line above this line.'
        self.phase = 3
        self.trigger = trigger

    def analyze(self, oFile):
        lContexts = oFile.get_context_declarations()
        for dContext in lContexts:
            bItemFound = False
            iRemove = -1
            for iLine, oLine in enumerate(dContext['lines'][::-1]):
                lObjects = oLine.get_objects()
                if bItemFound:
                    
                    if oLine.is_blank():
                        iRemove += 1
                    else:
                        if iRemove > 0:
                            dViolation = utils.create_violation_dict(iItemLineNumber)
                            dViolation['iRemove'] = iRemove
                            self.add_violation(dViolation)
                        bItemFound = False
                        iRemove = -1
                else:
                    for oObject in lObjects:
                        if isinstance(oObject, self.trigger):
                            iItemLineNumber = dContext['metadata']['iEndLineNumber'] - iLine
                            bItemFound = True

    def _fix_violations(self, oFile):
        for dViolation in self.violations[::-1]:
            iStartLineNumber = utils.get_violation_line_number(dViolation) - 1
            for i in range (dViolation['iRemove']):
                oFile.remove_line(iStartLineNumber)
