
from vsg.rules import lower_case_rule


class rule_009(lower_case_rule):
    '''
    Process rule 009 checks the "end" keyword is lowercase.
    '''

    def __init__(self):
        lower_case_rule.__init__(self, 'generate', '009', 'isGenerateEnd', 'end')
        self.solution = 'Lowercase the "end" keyword.'
