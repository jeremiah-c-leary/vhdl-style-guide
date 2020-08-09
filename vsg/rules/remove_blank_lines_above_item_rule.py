
from vsg import rule_item
from vsg import utils
from vsg import parser


class remove_blank_lines_above_item_rule(rule_item.Rule):
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

    def __init__(self, name, identifier, trigger, allow_number_of_blank_lines=1):
        rule_item.Rule.__init__(self, name=name, identifier=identifier)
        self.phase = 3
        self.trigger = trigger
        self.allow_number_of_blank_lines = allow_number_of_blank_lines

    def analyze(self, oFile):
        self._print_debug_message('Analyzing rule: ' + self.name + '_' + self.identifier)
        lContexts = self._get_regions(oFile)
        for dContext in lContexts:
            for iLine, oLine in enumerate(dContext['lines'][::-1]):
                lObjects = oLine.get_objects()
                for oObject in lObjects:
                    if isinstance(oObject, self.trigger):
                        iItemLineNumber = dContext['metadata']['iEndLineNumber'] - iLine
                        iNumBlankLines = number_of_blank_lines_above(oFile, iItemLineNumber)
                        iRemove = iNumBlankLines - self.allow_number_of_blank_lines
                        if iRemove > 0:
                            dViolation = utils.create_violation_dict(iItemLineNumber)
                            dViolation['iRemove'] = iRemove
                            dViolation['solution'] = f'Remove {iRemove} blank line(s) above this line.'
                            self.add_violation(dViolation)

    def _fix_violation(self, oFile, dViolation):
        iStartLineNumber = utils.get_violation_line_number(dViolation) - 1
        for i in range (dViolation['iRemove']):
            oFile.remove_line(iStartLineNumber)


def number_of_blank_lines_above(oFile, iLine):
    iReturn = 0
    for i in range(iLine - 1, 0, -1):
        if oFile.lines[i].isBlank:
            iReturn += 1
        else:
            break
    return iReturn
