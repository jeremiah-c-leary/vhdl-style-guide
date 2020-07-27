
from vsg import fix
from vsg import rule_item
from vsg import utils


class insert_blank_line_above_line_containing_item_rule(rule_item.Rule):
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

    def __init__(self, name, identifier, trigger, allowComment=False):
        rule_item.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = 'Insert blank line above.'
        self.phase = 3
        self.trigger = trigger
        self.allowComment = allowComment
        self.configuration.append('allowComment')

    def _get_regions(self, oFile):
        return oFile.get_region_bounded_by_items(self.regionBegin, self.regionEnd)

    def _analyze_region(self, oFile, iLine, oLine, dRegion):
        oPreviousLine = oFile.lines[dRegion['metadata']['iStartLineNumber'] - 1 + iLine]
        lObjects = oLine.get_objects()
        for oObject in lObjects:
            if isinstance(oObject, self.trigger) and not oPreviousLine.is_blank():
                if not oPreviousLine.is_comment() or not self.allowComment:
                    dViolation = utils.create_violation_dict(dRegion['metadata']['iStartLineNumber'] + iLine)
                    dViolation['solution'] = 'Insert blank line above.'
                    self.add_violation(dViolation)
        
    def _fix_violation(self, oFile, dViolation):
        fix.insert_blank_line_above(self, oFile, utils.get_violation_line_number(dViolation))
