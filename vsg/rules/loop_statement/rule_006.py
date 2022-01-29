
from vsg.token import loop_statement as token
from vsg import violation

from vsg.rule_group import structure


class rule_006(structure.Rule):
    '''
    This rule checks that loop statements have a label.

    **Violation**

    .. code-block:: vhdl

       loop

       while (condition) loop

       for x in range (31 downto 0) loop

    **Fix**

    .. code-block:: vhdl

       LOOP_LABEL : loop

       LOOP_LABEL : while (condition) loop

       LOOP_LABEL : for x in range (31 downto 0) loop
    '''

    def __init__(self):
        structure.Rule.__init__(self, 'loop_statement', '006')
        self.solution = 'Add label for loop statement'
        self.fixable = True
        self.disable = True

    def analyze(self, oFile):
        lKeywords = oFile.get_tokens_matching([token.loop_keyword])
        lLabels = oFile.get_tokens_matching([token.loop_label])

        iPreviousIndex = 0
        for oKeyword in lKeywords:
            iCurrentIndex = oKeyword.get_start_index()
            for oLabel in lLabels:
                iLabelIndex = oLabel.get_start_index()
                if iPreviousIndex < iLabelIndex and iLabelIndex < iCurrentIndex:
                    break
            else:
                oViolation = violation.New(oKeyword.get_line_number(), oKeyword, self.solution)
                self.add_violation(oViolation)
            iPreviousIndex = iCurrentIndex
