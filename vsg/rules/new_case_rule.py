
from vsg import fix
from vsg import check
from vsg import rule
from vsg import utils
from vsg import parser


class new_case_rule(rule.rule):
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
#        self.trigger = trigger
        self.trigger = trigger

    def analyze(self, oFile):
        lContexts = oFile.get_context_declarations()
        for dContext in lContexts:
            for iLine, oLine in enumerate(dContext['lines']):
                lObjects = oLine.get_objects()
                for oObject in lObjects:
                    if isinstance(oObject, self.trigger):
                        if self.case == 'lower':
                            if oObject.get_value() != oObject.get_value().lower():
                                self.add_violation(utils.create_violation_dict(dContext['metadata']['iStartLineNumber'] + iLine))
                        if self.case == 'upper':
                            if oObject.get_value() != oObject.get_value().upper():
                                self.add_violation(utils.create_violation_dict(dContext['metadata']['iStartLineNumber'] + iLine))

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
