
import copy

from vsg import rule
from vsg import parser
from vsg import utils


class copy_item_value_and_insert_new_item_after_item_rule(rule.rule):
    '''
    Copies the value of an item and inserts a new type of item after an existing item.

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

    def __init__(self, name, identifier, begin, end, copyItem, insertItem):
        rule.rule.__init__(self, name=name, identifier=identifier)
        self.phase = 1
        self.subphase = 3
        self.solution = None
        self.begin = begin
        self.end = end
        self.copyItem = copyItem
        self.insertItem = insertItem

    def analyze(self, oFile):
        lContexts = oFile.get_context_declarations()
        for dContext in lContexts:
            bBeginFound = False
            bCopyItemFound = False
            sCopyValue = None
            lAnalysis = []
            for iLine, oLine in enumerate(dContext['lines']):
                lObjects = oLine.get_objects()
                for iObject, oObject in enumerate(lObjects):
                    if isinstance(oObject, self.copyItem):
                        bCopyItemFound = True
                        sCopyValue = oObject.get_value()
                    if isinstance(oObject, self.begin):
                        bBeginFound = True
                        iBeginLine = iLine + dContext['metadata']['iStartLineNumber']
                    if bBeginFound:
                        lAnalysis.append(oObject)
                    if bBeginFound and isinstance(oObject, self.end):
                        bItemFound = False
                        for oItem in lAnalysis:
                            if type(self.insertItem) == type(oItem):
                                bItemFound = True
                        if not bItemFound:
                            dViolation = utils.create_violation_dict(iBeginLine)
                            dViolation['copy_value'] = sCopyValue
                            self.add_violation(dViolation)


    def _fix_violations(self, oFile):
        for dViolation in self.violations[::-1]:
            oLine = utils.get_violating_line(oFile, dViolation)
            lObjects = oLine.get_objects()
            for iObject, oObject in enumerate(lObjects):
                if isinstance(oObject, self.begin):
                    self.insertItem.set_value('blah')
                    oInsertItem = copy.deepcopy(self.insertItem)
                    oInsertItem.set_value(dViolation['copy_value'])
                    lObjects.insert(iObject + 1, oInsertItem)
                    lObjects.insert(iObject + 1, parser.whitespace(' '))
                    oLine.update_objects(lObjects)
                    break
