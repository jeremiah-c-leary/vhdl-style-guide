
from vsg import fix
from vsg import check
from vsg import rule
from vsg import utils
from vsg import parser


class rule_004(rule.rule):
    '''
    Checks for blank lines above a line and will insert a blank line if one does not exist.

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
        rule.rule.__init__(self, name='context', identifier='004')
        self.solution = None
        self.phase = 6
        self.case = 'lower'
        self.configuration.append('case')
        self.trigger = parser.context_keyword

    def analyze(self, oFile):
        lContexts = oFile.get_context_declarations()
        for dContext in lContexts:
            for oLine in dContext['lines']:
                lObjects = oLine.get_objects()
                for oObject in lObjects:
                    if isinstance(oObject, self.trigger):
                        if self.case == 'lower':
                            if oObject.get_value() != oObject.get_value().lower():
                                self.add_violation(utils.create_violation_dict(dContext['metadata']['iStartLineNumber']))
                        if self.case == 'upper':
                            if oObject.get_value() != oObject.get_value().upper():
                                self.add_violation(utils.create_violation_dict(dContext['metadata']['iStartLineNumber']))

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

        
#    def _fix_violations(self, oFile):
#        for dViolation in self.violations[::-1]:
#            fix.insert_blank_line_above(self, oFile, utils.get_violation_line_number(dViolation))
