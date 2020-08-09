
from vsg import rule_item
from vsg import check
from vsg import fix_item
from vsg import utils
from vsg.token import use_clause


class rule_009(rule_item.Rule):
    '''
    Library rule 009 checks consecutive comment lines above a "use" keyword are aligned.
    '''

    def __init__(self):
        rule_item.Rule.__init__(self, 'library', '009')
        self.solution = 'Align comment with "use" keyword.'
        self.phase = 4
        self.trigger = use_clause.keyword

    def _get_regions(self, oFile):
        return oFile.get_lines_starting_with_item_or_whitespace_and_then_item(self.trigger)

    def _analyze_region(self, oFile, iLine, oLine, dRegion):
        if oLine.begins_with_token(use_clause.keyword, True):
            check.indent_of_comments_above_item(self, oFile, iLine + dRegion['metadata']['iStartLineNumber'], oLine.get_indent_level())

    def _fix_violation(self, oFile, dViolation):
        iLineNumber = utils.get_violation_line_number(dViolation)
        oFile.lines[iLineNumber].indentLevel = dViolation['indent']
        fix_item.indent(self, oFile.lines[iLineNumber])
