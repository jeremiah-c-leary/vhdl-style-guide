
from vsg import fix
from vsg import check
from vsg import rule
from vsg import utils
from vsg import parser


class rule_005(rule.rule):
    '''
    Checks the context identifier is on the same line as the context keyword.

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
        rule.rule.__init__(self, name='context', identifier='005')
        self.solution = None
        self.phase = 1
        self.subphase = 1
        self.left = parser.context_keyword
        self.right = parser.context_identifier

    def analyze(self, oFile):
        lContexts = oFile.get_context_declarations()
        iLeftLineNumber = None
        iRightLineNumber = None
        for dContext in lContexts:
            bBreak = False
            for iLine, oLine in enumerate(dContext['lines']):
                lObjects = oLine.get_objects()
                for oObject in lObjects:
                    if isinstance(oObject, self.left):
                        iLeftLineNumber = iLine
                    if isinstance(oObject, self.right):
                        iRightLineNumber = iLine
                        bBreak = True
                if bBreak:
                    break
            if iLeftLineNumber != iRightLineNumber:
                dViolation = utils.create_violation_dict(dContext['metadata']['iStartLineNumber'] + iRightLineNumber)
                dViolation['iLeftLineNumber'] = iLeftLineNumber + dContext['metadata']['iStartLineNumber']
                self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations[::-1]:
            # Remove object from right line
            oLine = utils.get_violating_line(oFile, dViolation)
            lObjects = oLine.get_objects()
            for iObject, oObject in enumerate(lObjects):
                if isinstance(oObject, self.right):
                    oMyObject = oObject
                    lObjects.pop(iObject)
                    break
            # Check if line is now essentially blank 
            bOnlyWhitespace = True
            for oObject in lObjects:
                if not isinstance(oObject, parser.whitespace):
                    bOnlyWhitespace = False
            if bOnlyWhitespace:
                lObjects = []
            oLine.update_objects(lObjects)
            # Add object to left line
            oLine =  oFile.get_line(dViolation['iLeftLineNumber'])
            lObjects = oLine.get_objects()
            for iObject, oObject in enumerate(lObjects):
                if isinstance(oObject, self.left):
                    lObjects.insert(iObject + 1, oMyObject)
                    lObjects.insert(iObject + 1, parser.whitespace(' '))
                    oLine.update_objects(lObjects)
                    break
