
from vsg import token
from vsg import violation

from vsg.rule_group import structure


class rule_016(structure.Rule):
    '''
    This rule checks the process has a label.

    **Violation**

    .. code-block:: vhdl

       process (rd_en, wr_en, data_in, data_out,
                rd_full, wr_full
               ) is
       begin

    **Fix**

    .. code-block:: vhdl

       proc_a : process (rd_en, wr_en, data_in, data_out,
                         rd_full, wr_full
                        ) is
       begin
    '''

    def __init__(self):
        structure.Rule.__init__(self, 'process', '016')
        self.solution = 'Add label for process'
        self.fixable = False

    def analyze(self, oFile):
        lKeywords = oFile.get_tokens_matching([token.process_statement.process_keyword])
        lLabels = oFile.get_tokens_matching([token.process_statement.process_label])

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
