
from vsg import rule
from vsg import check
from vsg import fix
from vsg import parser
from vsg import utils


class rule_002(rule.rule):
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

    def __init__(self):
        rule.rule.__init__(self, name='context', identifier='002')
        self.phase = 2
        self.solution = None
        self.spaces = 1
        self.sWord = 'context'
        self.configuration.append('spaces')

    def analyze(self, oFile):
        lContexts = oFile.get_context_declarations()
        for dContext in lContexts:
            for oLine in dContext['lines']:
                lObjects = oLine.get_objects()
                iNumObjects = len(lObjects)
                for iObject, oObject in enumerate(lObjects):
                    if iObject + 1 < iNumObjects:
                        if isinstance(oObject, parser.context_keyword) and isinstance(lObjects[iObject + 1], parser.whitespace):
                            if lObjects[iObject + 1].get_value() != ' ' * self.spaces:
                                self.add_violation(utils.create_violation_dict(dContext['metadata']['iStartLineNumber']))

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            oLine = utils.get_violating_line(oFile, dViolation)
            lObjects = oLine.get_objects()
            for iObject, oObject in enumerate(lObjects):
                if isinstance(oObject, parser.context_keyword):
                    lObjects[iObject + 1].set_value(' ' * self.spaces)
                    oLine.update_objects(lObjects)
                    break

    def _get_solution(self, iLineNumber):
        return 'Ensure there are only ' + str(self.spaces) + ' space(s) after the "' + self.sWord + '" keyword.'
