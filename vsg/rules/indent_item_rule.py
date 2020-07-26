
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

    trigger : parser object
       object to indent
    '''

    def __init__(self, name, identifier, trigger):
        rule.rule.__init__(self, name=name, identifier=identifier)
        self.solution = 'Indent.'
        self.phase = 3
        self.trigger = trigger

    def analyze(self, oFile):
        self._print_debug_message('Analyzing rule: ' + self.name + '_' + self.identifier)
        lRegions = oFile.get_lines_starting_with_item_or_whitespace_and_then_item(self.trigger)
        for dRegion in lRegions:
            for oLine in dRegion['lines'][::-1]:
                if oLine.get_indent_level() is None:
                    continue
                if oLine.get_indent_level() == 0 and isinstance(oLine.get_object(0), parser.whitespace):
                    dViolation = utils.create_violation_dict(dRegion['metadata']['iStartLineNumber'])
                    dViolation['action'] = 'remove'
                    dViolation['solution'] = 'Remove spaces before "' + oLine.get_object(1).get_value() + '"'
                    self.add_violation(dViolation)
                    break
                if oLine.get_indent_level() == 0:
                    break
                if oLine.get_indent_level() > 0 and not isinstance(oLine.get_object(0), parser.whitespace):
                    dViolation = utils.create_violation_dict(dRegion['metadata']['iStartLineNumber'])
                    dViolation['action'] = 'insert'
                    dViolation['iSpaces'] = ' ' * oLine.indentLevel * self.indentSize
                    dViolation['solution'] = 'Indent ' + str(len('  ' * oLine.indentLevel)) + ' spaces'
                    self.add_violation(dViolation)
                    break
                if oLine.get_indent_level() * self.indentSize * ' ' != oLine.get_object(0).get_value():
                    dViolation = utils.create_violation_dict(dRegion['metadata']['iStartLineNumber'])
                    dViolation['action'] = 'change'
                    dViolation['iSpaces'] = ' ' * oLine.indentLevel * self.indentSize
                    dViolation['solution'] = 'Indent ' + str(len('  ' * oLine.indentLevel)) + ' spaces'
                    self.add_violation(dViolation)
                    break

    def _fix_violations(self, oFile):
        for dViolation in self.violations[::-1]:
            oLine = utils.get_violating_line(oFile, dViolation)
            lObjects = oLine.get_objects()
            if dViolation['action'] == 'insert':
                lObjects.insert(0, parser.whitespace(dViolation['iSpaces']))
            elif dViolation['action'] == 'remove':
                lObjects.pop(0)
            else:
                lObjects[0].set_value(dViolation['iSpaces'])
            oLine.update_objects(lObjects)

    def _get_solution(self, iLineNumber):
        return utils.get_violation_solution_at_line_number(self.violations, iLineNumber)
