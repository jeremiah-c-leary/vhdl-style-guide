

class rule():

    def __init__(self, name=None, identifier=None):
        self.name = name
        self.identifier = identifier
        self.solution = None
        self.violations = []
        self.indentSize = 2
        self.phase = None
        self.subphase = 1
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

    def has_violations(self):
        if len(self.violations) == 0:
            return False
        return True

    def _build_violation_dict(self, lReturn, sViolation, iLineNumber):
        if str(sViolation).startswith(str(iLineNumber) + '-') or str(iLineNumber) == str(sViolation):
            dViolation = {}
            dViolation['rule'] = self.name + '_' + self.identifier
            dViolation['lineNumber'] = sViolation
            dViolation['solution'] = self._get_solution(iLineNumber)
            lReturn.append(dViolation)

    def get_violations_at_linenumber(self, iLineNumber):
        '''
        Returns a list of formatted violations.

        Parameters:

          iLineNumber (integer)

        Returns: (list of dictionaries)
        '''
        lReturn = []

        for iIndex, violation in enumerate(self.violations):
            check_for_old_violation_format(violation)
            lKeys = list(violation.keys())
            if 'lineNumber' in lKeys:
                sViolation = str(violation['lineNumber'])
                self._build_violation_dict(lReturn, sViolation, iLineNumber)

            elif 'lines' in lKeys:
                for dLineViolation in violation['lines']:
                    sViolation = str(dLineViolation['number'])
                    self._build_violation_dict(lReturn, sViolation, iLineNumber)
        return lReturn

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


def check_for_old_violation_format(violation):
    # Remove this some time after 2.0.0 has been released
    if isinstance(violation, int):
        print('ERROR:  Violations have changed from an integer to a dictionary.  Skipping this violation')
        print('        Use the function utils.create_violation_dict to update to current format.')
        print('        Refer to documentation on local rules for more information.')
        sys.exit(1)
