
from vsg import rule
from vsg import utils
from vsg import parser


class case_item_rule(rule.rule):
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
        rule.rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 6
        self.case = 'lower'
        self.configuration.append('case')
        self.trigger = trigger

    def analyze(self, oFile):
        self._print_debug_message('Analyzing rule: ' + self.name + '_' + self.identifier)
        lContexts = oFile.get_context_declarations()
        for dContext in lContexts:
            for iLine, oLine in enumerate(dContext['lines']):
                lObjects = oLine.get_objects()
                for oObject in lObjects:
                    if isinstance(oObject, self.trigger):
                        sObjectValue = oObject.get_value()
                        if self.case == 'lower':
                            if sObjectValue != sObjectValue.lower():
                                dViolation = utils.create_violation_dict(dContext['metadata']['iStartLineNumber'] + iLine)
                                dViolation['solution'] = 'Change "' + sObjectValue + '" to "' + sObjectValue.lower() + '"'
                                self.add_violation(dViolation)
                        if self.case == 'upper':
                            if sObjectValue != sObjectValue.upper():
                                dViolation = utils.create_violation_dict(dContext['metadata']['iStartLineNumber'] + iLine)
                                dViolation['solution'] = 'Change "' + sObjectValue + '" to "' + sObjectValue.upper() + '"'
                                self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            oLine = utils.get_violating_line(oFile, dViolation)
            lObjects = oLine.get_objects()
            for iObject, oObject in enumerate(lObjects):
                if isinstance(oObject, self.trigger):
                    if self.case == 'lower':
                        oObject.set_value(oObject.get_value().lower())
                    if self.case == 'upper':
                        oObject.set_value(oObject.get_value().upper())
                    oLine.update_objects(lObjects)
                    break

    def _get_solution(self, iLineNumber):
        return utils.get_violation_solution_at_line_number(self.violations, iLineNumber)
