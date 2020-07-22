
from vsg import rule
from vsg import utils
from vsg import parser


class indent_item_rule(rule.rule):
    '''
    Checks for invalid indent of an item.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    sTrigger : string
       The line attribute the rule applies to.
    '''

    def __init__(self, name, identifier, trigger):
        rule.rule.__init__(self, name=name, identifier=identifier)
        self.solution = 'Remove all but one blank line above this line.'
        self.phase = 3
        self.trigger = trigger

    def analyze(self, oFile):
        lContexts = oFile.get_lines_starting_with_item_or_whitespace_and_then_item(self.trigger)
        for dContext in lContexts:
            for oLine in dContext['lines'][::-1]:
                if oLine.get_indent_level() == 0 and isinstance(oLine.get_object(0), parser.whitespace):
                    dViolation = utils.create_violation_dict(dContext['metadata']['iStartLineNumber'])
                    dViolation['action'] = 'remove'
                    self.add_violation(dViolation)
                    break
                if oLine.get_indent_level() == 0:
                    break
                if oLine.get_indent_level() > 0 and not isinstance(oLine.get_object(0), parser.whitespace):
                    dViolation = utils.create_violation_dict(dContext['metadata']['iStartLineNumber'])
                    dViolation['action'] = 'insert'
                    dViolation['insert_object'] = parser.whitespace(' ' * oLine.indentLevel)
                    self.add_violation(dViolation)
                    break
                if oLine.get_indent_level() * ' ' != oLine.get_object(0).get_value():
                    dViolation = utils.create_violation_dict(dContext['metadata']['iStartLineNumber'])
                    dViolation['action'] = 'change'
                    dViolation['iNewValue'] = ' ' * oLine.indentLevel
                    self.add_violation(dViolation)
                    break

    def _fix_violations(self, oFile):
        for dViolation in self.violations[::-1]:
            oLine = utils.get_violating_line(oFile, dViolation)
            lObjects = oLine.get_objects()
            if dViolation['action'] == 'insert':
                lObjects.insert(0, dViolation['insert_object'])
            elif dViolation['action'] == 'remove':
                lObjects.pop(0)
            else:
                lObjects[0].set_value(dViolation['iNewValue'])
            oLine.update_objects(lObjects)
