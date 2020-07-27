
from vsg import rule_item
from vsg import parser
from vsg import utils


class space_between_items_rule(rule_item.Rule):
    '''
    Checks for and fixes none or multiple spaces after a word.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    left : parser object
       The object on the left of the spaces.

    right : parser object
       The object on the right of the spaces.

    word : string
       Outputed as part of the solution.

    Attributes
    ----------

    self.phase : integer = 2
       Sets the phase the rule will run in.

    self.solution : string = None
       Instructions on how to fix the violation.
    '''

    def __init__(self, name, identifier, left, right):
        rule_item.Rule.__init__(self, name=name, identifier=identifier)
        self.phase = 2
        self.solution = None
        self.spaces = 1
        self.configuration.append('spaces')
        self.left = left
        self.right = right
        self.regionBegin = None
        self.regionEnd = None

    def _analyze_region(self, oFile, iLine, oLine, dRegion):
        lObjects = oLine.get_objects()
        lAnalysis = []
        bLeftFound = False
        for iObject, oObject in enumerate(lObjects):
            if isinstance(oObject, self.left):
                bLeftFound = True
            if bLeftFound:
                lAnalysis.append(oObject)
            if isinstance(oObject, self.right):
                if len(lAnalysis) == 3:
                    if isinstance(lAnalysis[1], parser.whitespace):
                        if lAnalysis[1].get_value() != ' ' * self.spaces:
                            dViolation = utils.create_violation_dict(dRegion['metadata']['iStartLineNumber'] + iLine)
                            dViolation['solution'] = 'Ensure there are only ' + str(self.spaces) + ' space(s) between "' + lAnalysis[0].get_value() + '" and "' + lAnalysis[2].get_value() + '"'
                            self.add_violation(dViolation)

    def _fix_violation(self, oFile, dViolation):
        oLine = utils.get_violating_line(oFile, dViolation)
        lObjects = oLine.get_objects()
        for iObject, oObject in enumerate(lObjects):
            if isinstance(oObject, self.left):
                lObjects[iObject + 1].set_value(' ' * self.spaces)
                oLine.update_objects(lObjects)
                break
