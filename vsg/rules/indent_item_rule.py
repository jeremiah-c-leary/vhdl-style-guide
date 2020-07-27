
from vsg import rule_item
from vsg import utils
from vsg import parser


class indent_item_rule(rule_item.Rule):
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
        rule_item.Rule.__init__(self, name, identifier)
        self.solution = 'Indent.'
        self.phase = 4
        self.trigger = trigger

    def _get_regions(self, oFile):
        return oFile.get_lines_starting_with_item_or_whitespace_and_then_item(self.trigger)

    def _analyze_region(self, oFile, iLine, oLine, dRegion):
        if oLine.get_indent_level() is None:
            pass
        elif oLine.get_indent_level() == 0 and isinstance(oLine.get_object(0), parser.whitespace):
            dViolation = utils.create_violation_dict(dRegion['metadata']['iStartLineNumber'])
            dViolation['action'] = 'remove'
            dViolation['solution'] = 'Remove spaces before "' + oLine.get_object(1).get_value() + '"'
            self.add_violation(dViolation)
        elif oLine.get_indent_level() == 0:
            pass
        elif oLine.get_indent_level() > 0 and not isinstance(oLine.get_object(0), parser.whitespace):
            dViolation = utils.create_violation_dict(dRegion['metadata']['iStartLineNumber'])
            dViolation['action'] = 'insert'
            dViolation['iSpaces'] = ' ' * oLine.indentLevel * self.indentSize
            dViolation['solution'] = 'Indent ' + str(len('  ' * oLine.indentLevel)) + ' spaces'
            self.add_violation(dViolation)
        elif oLine.get_indent_level() * self.indentSize * ' ' != oLine.get_object(0).get_value():
            dViolation = utils.create_violation_dict(dRegion['metadata']['iStartLineNumber'])
            dViolation['action'] = 'change'
            dViolation['iSpaces'] = ' ' * oLine.indentLevel * self.indentSize
            dViolation['solution'] = 'Indent ' + str(len('  ' * oLine.indentLevel)) + ' spaces'
            self.add_violation(dViolation)

    def _fix_violation(self, oFile, dViolation):
        oLine = utils.get_violating_line(oFile, dViolation)
        lObjects = oLine.get_objects()
        if dViolation['action'] == 'insert':
            lObjects.insert(0, parser.whitespace(dViolation['iSpaces']))
        elif dViolation['action'] == 'remove':
            lObjects.pop(0)
        else:
            lObjects[0].set_value(dViolation['iSpaces'])
        oLine.update_objects(lObjects)
