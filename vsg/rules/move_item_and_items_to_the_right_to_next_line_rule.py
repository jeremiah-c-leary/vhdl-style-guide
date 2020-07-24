
import copy

from vsg import rule
from vsg import parser
from vsg import utils


class move_item_and_items_to_the_right_to_next_line_rule(rule.rule):
    '''
    Splits the line at items and moves items after it to the next line.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    sObjectType : string
       The object to check the space after.

    Attributes
    ----------

    self.phase : integer = 2
       Sets the phase the rule will run in.

    self.solution : string = None
       Instructions on how to fix the violation.
    '''

    def __init__(self, name, identifier, trigger):
        rule.rule.__init__(self, name=name, identifier=identifier)
        self.phase = 1
        self.subphase = 1
        self.solution = None
        self.trigger = trigger

    def analyze(self, oFile):
        self._print_debug_message('Analyzing rule: ' + self.name + '_' + self.identifier)
        lContexts = oFile.get_context_declarations()
        for dContext in lContexts:
            bFound = False
            bBreak = False
            for iLine, oLine in enumerate(dContext['lines']):
                lObjects = oLine.get_objects()
                for iObject, oObject in enumerate(lObjects):
                    if iObject > 1:
                        if isinstance(oObject, self.trigger):
                            dViolation = utils.create_violation_dict(dContext['metadata']['iStartLineNumber'] + iLine)
                            dViolation['iObject'] = iObject
                            dViolation['solution'] = 'Move "' + oObject.get_value() + '" and the code to the right to the next line.'
                            self.add_violation(dViolation)


    def _fix_violations(self, oFile):
        for dViolation in self.violations[::-1]:
            oLine = utils.get_violating_line(oFile, dViolation)
            oNewLine = copy.deepcopy(oLine)
            lObjects = oLine.get_objects()
            iLineNumber = utils.get_violation_line_number(dViolation)

            lOldObjects = lObjects[:dViolation['iObject']]
            lNewObjects = lObjects[dViolation['iObject']:]
            oLine.update_objects(lOldObjects)
            oNewLine.update_objects(lNewObjects)
            oFile.insert_line(iLineNumber + 1, oNewLine)

    def _get_solution(self, iLineNumber):
        return utils.get_violation_solution_at_line_number(self.violations, iLineNumber)
