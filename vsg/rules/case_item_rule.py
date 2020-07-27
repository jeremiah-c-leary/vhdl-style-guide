

from vsg import rule_item
from vsg import utils
from vsg import parser


class case_item_rule(rule_item.Rule):
    '''
    Checks the case for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    trigger : parser object type
       object type to apply the case check against
    '''

    def __init__(self, name, identifier, trigger):
        rule_item.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 6
        self.case = 'lower'
        self.configuration.append('case')
        self.trigger = trigger
        self.regionBegin = None
        self.regionEnd = None

    def _get_regions(self, oFile):
        return oFile.get_region_bounded_by_items(self.regionBegin, self.regionEnd)

    def _analyze_region(self, oFile, iLine, oLine, dRegion):
                lObjects = oLine.get_objects()
                for oObject in lObjects:
                    if isinstance(oObject, self.trigger):
                        sObjectValue = oObject.get_value()
                        if self.case == 'lower':
                            if sObjectValue != sObjectValue.lower():
                                dViolation = utils.create_violation_dict(dRegion['metadata']['iStartLineNumber'] + iLine)
                                dViolation['solution'] = 'Change "' + sObjectValue + '" to "' + sObjectValue.lower() + '"'
                                self.add_violation(dViolation)
                        if self.case == 'upper':
                            if sObjectValue != sObjectValue.upper():
                                dViolation = utils.create_violation_dict(dRegion['metadata']['iStartLineNumber'] + iLine)
                                dViolation['solution'] = 'Change "' + sObjectValue + '" to "' + sObjectValue.upper() + '"'
                                self.add_violation(dViolation)

    def _fix_violation(self, oFile, dViolation):
            oLine = utils.get_violating_line(oFile, dViolation)
            lObjects = oLine.get_objects()
            for iObject, oObject in enumerate(lObjects):
                if isinstance(oObject, self.trigger):
                    if self.case == 'lower':
                        oObject.set_value(oObject.get_value().lower())
                    if self.case == 'upper':
                        oObject.set_value(oObject.get_value().upper())
                    oLine.update_objects(lObjects)
