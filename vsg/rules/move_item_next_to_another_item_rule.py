
from vsg import rule_item
from vsg import utils
from vsg import parser


class move_item_next_to_another_item_rule(rule_item.Rule):
    '''
    Moves an item next to another.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    left : parser object type
       The anchor object the other object must be moved next to

    right : parser object type
       The object that will be moved next to the anchor object
    '''
    def __init__(self, name, identifier, left, right):
        rule_item.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 1
        self.subphase = 1
        self.left = left
        self.right = right

    def analyze(self, oFile):
        self._print_debug_message('Analyzing rule: ' + self.name + '_' + self.identifier)
        lContexts = self._get_regions(oFile)
        for dContext in lContexts:
            iLeftLineNumber = None
            iRightLineNumber = None
            sLeftValue = None
            sRightValue = None
            bBreak = False
            for iLine, oLine in enumerate(dContext['lines']):
                lObjects = oLine.get_objects()
                for oObject in lObjects:
                    if isinstance(oObject, self.left):
                        iLeftLineNumber = iLine
                        sLeftValue = oObject.get_value()
                    if isinstance(oObject, self.right):
                        iRightLineNumber = iLine
                        sRightValue = oObject.get_value()
                        bBreak = True
                if bBreak:
                    break
            if iRightLineNumber is None or iLeftLineNumber is None:
                continue
            if iLeftLineNumber != iRightLineNumber:
                dViolation = utils.create_violation_dict(dContext['metadata']['iStartLineNumber'] + iRightLineNumber)
                dViolation['iLeftLineNumber'] = iLeftLineNumber + dContext['metadata']['iStartLineNumber']
                dViolation['solution'] = f'Move "{sRightValue}" to the right of "{sLeftValue}" on line ' + str(dViolation['iLeftLineNumber'])
                self.add_violation(dViolation)

    def _fix_violation(self, oFile, dViolation):
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
