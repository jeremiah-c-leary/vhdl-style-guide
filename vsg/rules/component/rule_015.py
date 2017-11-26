
from vsg.rules.component import component_rule


class rule_015(component_rule):
    '''
    Component rule 015 checks the "end" keyword, "component" keyword, 
    and component name are on the same line.
    '''

    def __init__(self):
        component_rule.__init__(self)
        self.identifier = '015'
        self.solution = 'The "end" keyword, "component" keyword and component name need to be on the same line.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentEnd:
                lLine = oLine.line.split()
                if not len(lLine) >= 3:
                    if not (lLine[0] == 'end' and lLine[1] == 'component' and not lLine[2].startswith('--')):
                        self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            lLine = oLine.line.split()
            if not lLine[1].lower() == 'component':
                lLine.insert(1, 'component')
                oLine.update_line(' '.join(lLine))
