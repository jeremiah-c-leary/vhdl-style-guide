
from vsg import rule_item
from vsg import parser
from vsg import utils


class space_after_item_rule(rule_item.Rule):
    '''
    Checks for and fixes none or multiple spaces after a word.

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

    def __init__(self, name, identifier, trigger, word):
        rule_item.Rule.__init__(self, name=name, identifier=identifier)
        self.phase = 2
        self.solution = None
        self.spaces = 1
        self.configuration.append('spaces')
        self.sWord = word
        self.trigger = trigger

    def _analyze(self, oFile, iLine, oLine, dRegion):
        lObjects = oLine.get_objects()
        iNumObjects = len(lObjects)
        for iObject, oObject in enumerate(lObjects):
            if iObject + 1 < iNumObjects:
                if isinstance(oObject, self.trigger) and isinstance(lObjects[iObject + 1], parser.whitespace):
                    if lObjects[iObject + 1].get_value() != ' ' * self.spaces:
                                self.add_violation(utils.create_violation_dict(dRegion['metadata']['iStartLineNumber'] + iLine))

    def _fix_violation(self, oFile, dViolation):
        oLine = utils.get_violating_line(oFile, dViolation)
        lObjects = oLine.get_objects()
        for iObject, oObject in enumerate(lObjects):
            if isinstance(oObject, self.trigger):
                lObjects[iObject + 1].set_value(' ' * self.spaces)
                oLine.update_objects(lObjects)
                break
