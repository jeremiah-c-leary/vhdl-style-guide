

class rule():

    def __init__(self, name=None, identifier=None):
        self.name = name
        self.identifier = identifier
        self.solution = None
        self.violations = []
        self.indentSize = 2
        self.phase = None
        self.disable = False
        self.fixable = True
        self.dFix = {}
        self.dFix['violations'] = {}
        self.configuration = ['indentSize', 'phase', 'disable', 'fixable']

    def configure(self, dConfiguration):
        '''Configures attributes on rules using a dictionary of the following form:

            dConfiguration['rule'] = {}
            dConfiguration['rule']['xyz_001'] = {}
            dConfiguration['rule']['xyz_001']['disable'] = True
            dConfiguration['rule']['xyz_001']['solution'] = 'This is the new solution'
            dConfiguration['rule']['xyz_002'] = {}
            dConfiguration['rule']['xyz_002']['disable'] = False
            dConfiguration['rule']['global'] = {}
            dConfiguration['rule']['global']['indentSize'] = 4

          The rule:global dictionary will apply to all rules.
          Individual rule attributes can be modified with [self.name_self.identifier].
        '''

        self._configure_global_rule_attributes(dConfiguration)
        self._configure_rule_attributes(dConfiguration)

    def report_violations(self, iLineNumber, sOutputFormat, sFileName, fQuiet=False):
        '''
        Reports any rule violations to stdout.
        '''
        for sViolation in self.violations:
            if str(sViolation).startswith(str(iLineNumber) + '-') or str(iLineNumber) == str(sViolation):
                if not fQuiet:
                    if sOutputFormat == 'vsg':
                        sOutputString = '  '
                        sOutputString += (self.name + '_' + self.identifier).ljust(25)
                        sOutputString += ' | '
                        sOutputString += str(sViolation).rjust(10)
                        sOutputString += ' | '
                        sOutputString += self._get_solution(iLineNumber)
                    else:
                        sOutputString = 'ERROR: '
                        sOutputString += sFileName
                        sOutputString += '('
                        sOutputString += str(iLineNumber)
                        sOutputString += ')'
                        sOutputString += self.name + '_' + self.identifier
                        sOutputString += ' -- '
                        sOutputString += self._get_solution(iLineNumber)
                    print(sOutputString)
                return 1
        return 0

    def fix(self, oFile):
        '''
        Applies fixes for any rule violations.
        '''
        if self.fixable:
            self.analyze(oFile)
            self._fix_violations(oFile)
            self.violations = []
            self.dFix = {}
            self.dFix['violations'] = {}

    def add_violation(self, lineNumber):
        '''
        Adds a linenumber to a violations list.
        '''
        if lineNumber not in self.violations:
            self.violations.append(lineNumber)

    def analyze(self, oFile):
        '''
        Performs the analysis.
        '''
        self._pre_analyze()
        for iLineNumber, oLine in enumerate(oFile.lines):
            if not self._is_vsg_off(oLine):
                self._analyze(oFile, oLine, iLineNumber)

    def _configure_global_rule_attributes(self, dConfiguration):
        '''
        Updates rule attributes based on configuration input files
        '''
        try:
            for sAttributeName in dConfiguration['rule']['global']:
                if sAttributeName in self.__dict__:
                    self.__dict__[sAttributeName] = dConfiguration['rule']['global'][sAttributeName]
        except KeyError:
            pass

    def _configure_rule_attributes(self, dConfiguration):
        '''
        Updates rule attributes based on configuration input files
        '''
        try:
            for sAttributeName in dConfiguration['rule'][self.name + '_' + self.identifier]:
                if sAttributeName in self.__dict__:
                    self.__dict__[sAttributeName] = dConfiguration['rule'][self.name + '_' + self.identifier][sAttributeName]
        except KeyError:
            pass

    def _is_vsg_off(self, oLine):
        '''
        Checks if the rule has been disabled for a given line.
        '''
        if 'vsg_off' in oLine.codeTags:
            if len(oLine.codeTags['vsg_off']) == 0 or self.name + '_' + self.identifier in oLine.codeTags['vsg_off']:
                return True
        return False

    def get_configuration(self):
        '''
        Returns a dictionary of every configurable attribute of the rule.
        '''
        dConfig = {}
        for sParameter in self.configuration:
            dConfig[sParameter] = getattr(self, sParameter)
        return dConfig

    def _get_solution(self, iLineNumber):
        '''
        By default this method return self.solution.
        This method can be overloaded by a rule if a more complex solution output is required.
        '''
        return self.solution

    def _pre_analyze(self):
        '''
        This method is called before the _analyze method and allows each rule to setup any variables needed.
        '''
        return
