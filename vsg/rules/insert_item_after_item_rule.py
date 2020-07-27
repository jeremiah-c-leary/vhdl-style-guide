
from vsg import rule_item
from vsg import parser
from vsg import utils


class insert_item_after_item_rule(rule_item.Rule):
    '''
    Checks for the existance of an item relative to another item and inserts the item if it does not exist.

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

    def __init__(self, name, identifier, begin, end, item):
        rule_item.Rule.__init__(self, name=name, identifier=identifier)
        self.phase = 1
        self.solution = None
        self.insert_space = False
        self.configuration.append('insert_space')
        self.begin = begin
        self.end = end
        self.item = item

    def analyze(self, oFile):
        self._print_debug_message('Analyzing rule: ' + self.name + '_' + self.identifier)
        lContexts = self._get_regions(oFile)
        for dContext in lContexts:
            bBeginFound = False
            lAnalysis = []
            for iLine, oLine in enumerate(dContext['lines']):
                lObjects = oLine.get_objects()
                for iObject, oObject in enumerate(lObjects):
                    if isinstance(oObject, self.begin):
                        bBeginFound = True
                        iBeginLine = iLine + dContext['metadata']['iStartLineNumber']
                        sBeginValue = oObject.get_value()
                    if bBeginFound:
                        lAnalysis.append(oObject)
                    if isinstance(oObject, self.end):
                        bItemFound = False
                        for oItem in lAnalysis:
                            if type(self.item) == type(oItem):
                                bItemFound = True
                        if not bItemFound:
                            dViolation = utils.create_violation_dict(iBeginLine)
                            dViolation['solution'] = 'Add "' + self.item.get_value() + '" after "' + sBeginValue + '"'
                            self.add_violation(dViolation)


    def _fix_violation(self, oFile, dViolation):
        oLine = utils.get_violating_line(oFile, dViolation)
        lObjects = oLine.get_objects()
        for iObject, oObject in enumerate(lObjects):
            if isinstance(oObject, self.begin):
                lObjects.insert(iObject + 1, self.item)
                if self.insert_space:
                    lObjects.insert(iObject + 1, parser.whitespace(' '))
                oLine.update_objects(lObjects)
                break
