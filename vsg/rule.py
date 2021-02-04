

from vsg import severity
from vsg import utils


class Rule():

    def __init__(self, name=None, identifier=None):
        self.name = name
        self.identifier = identifier
        self.unique_id = str(name) + '_' + str(identifier)
        self.solution = None
        self.violations = []
        self.indentSize = 2
        self.phase = None
        self.subphase = 1
        self.disable = False
        self.fixable = True
        self.severity = severity.set_error_severity
        self.debug = False
        self.dFix = {}
        self.dFix['violations'] = {}
        self.configuration = ['indentSize', 'phase', 'disable', 'fixable', 'severity']

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

    def _build_violation_dict_from_violation_object(self, violation):
        dViolation = {}
        dViolation['severity'] = {}
        dViolation['severity']['name'] = self.severity.name
        dViolation['severity']['type'] = self.severity.type
        dViolation['rule'] = self.get_unique_id()
        dViolation['lineNumber'] = str(violation.get_line_number())
        dViolation['solution'] = violation.get_solution()
        return dViolation

    def get_unique_id(self):
        return self.name + '_' + self.identifier

    def get_violations_at_linenumber(self, iLineNumber):
        '''
        Returns a list of formatted violations.

        Parameters:

          iLineNumber (integer)

        Returns: (list of dictionaries)
        '''
        lReturn = []

        for violation in self.violations:
            if violation.get_line_number() == iLineNumber:
                lReturn.append(self._build_violation_dict_from_violation_object(violation))

        return lReturn

    def get_violations(self):
        lReturn = []

        for violation in self.violations:
            lReturn.append(self._build_violation_dict_from_violation_object(violation))

        return lReturn

    def fix(self, oFile, dFixOnly=None):
        '''
        Applies fixes for any rule violations.
        '''
        if self.fixable:
            self.analyze(oFile)
            self._print_debug_message('Fixing rule: ' + self.unique_id)
            self._filter_out_fix_only_violations(dFixOnly)
            for oViolation in self.violations[::-1]:
                self._fix_violation(oViolation)
            oFile.update(self.violations)
            self.clear_violations()

    def _filter_out_fix_only_violations(self, dFixOnly):
        if dFixOnly is None:
            return

        try:
            if 'all' in dFixOnly['fix']['rule'][self.unique_id]:
                return
        except KeyError:
            self.violations = []

        lTemp = []
        for oViolation in self.violations:
            if oViolation.get_line_number() in dFixOnly['fix']['rule'][self.unique_id]:
                lTemp.append(oViolation)
        self.violations = lTemp

    def add_violation(self, lineNumber):
        '''
        Adds a linenumber to a violations list.
        '''
        if not lineNumber.has_code_tag(self.unique_id):
            self.violations.append(lineNumber)
            self.severity.count += 1

    def analyze(self, oFile):
        '''
        Performs the analysis.
        '''
        self._print_debug_message('Analyzing rule: ' + self.unique_id)
        lToi = self._get_tokens_of_interest(oFile)
        self._analyze(lToi)

    def _configure_global_rule_attributes(self, dConfiguration):
        '''
        Updates rule attributes based on configuration input files
        '''
        try:
            for sAttributeName in dConfiguration['rule']['global']:
                if sAttributeName == 'severity':
                    self.severity = dConfiguration['severity_list'].get_severity_named(dConfiguration['rule']['global']['severity'])
                elif sAttributeName in self.__dict__:
                    self.__dict__[sAttributeName] = dConfiguration['rule']['global'][sAttributeName]
        except KeyError:
            pass

    def _configure_rule_attributes(self, dConfiguration):
        '''
        Updates rule attributes based on configuration input files
        '''
        try:
            for sAttributeName in dConfiguration['rule'][self.get_unique_id()]:
                if sAttributeName == 'severity':
                    self.severity = dConfiguration['severity_list'].get_severity_named(dConfiguration['rule'][self.get_unique_id()]['severity'])
                elif sAttributeName in self.__dict__:
                    self.__dict__[sAttributeName] = dConfiguration['rule'][self.get_unique_id()][sAttributeName]
        except KeyError:
            pass

    def get_configuration(self):
        '''
        Returns a dictionary of every configurable attribute of the rule.
        '''
        dConfig = {}
        for sParameter in self.configuration:
            dConfig[sParameter] = getattr(self, sParameter)
        dConfig['severity'] = self.severity.name
        return dConfig

    def _get_solution(self, iLineNumber):
        '''
        Returns the solution for a violation.
        '''
        return utils.get_violation_solution_at_line_number(self.violations, iLineNumber)

    def clear_violations(self):
        self.violations = []

    def set_debug(self):
        '''
        This method sets the debug attribute to True.
        '''
        self.debug = True

    def _print_debug_message(self, sString):
        '''
        Prints a debug message to stdio.

        Parameters:

          sString : (string)

        Returns: Nothing
        '''
        if self.debug:
            print('INFO: ' + sString)

    def _fix_violation(self, oViolation):
        '''
        Default if rule is not fixable
        '''
        return

    def _sort_violations(self):
        '''
        Sorts self.violations based on the start index of each violation.
        Sort order is increasing start index.
        '''
#        print('-->sort_violations')
#        print(f'Num_violations = {len(self.violations)}')
#        print(self.violations)
        if not self.violations:
            return
        lNewViolations = []
        lNewViolations.append(self.violations[0])
        for oViolation in self.violations[1:]:
            iStartIndex = oViolation.get_start_index()
            for iInsertIndex, oNewViolation in enumerate(lNewViolations):
                iNewIndex = oNewViolation.get_start_index()
                if iStartIndex < iNewIndex:
                    lNewViolations.insert(iInsertIndex, oViolation)
                    break
            else:
                lNewViolations.append(oViolation)
        self.violations = lNewViolations       
#        print(self.violations)
#        print(f'Num_violations = {len(self.violations)}')
#        for oViolation in self.violations:
#            print(oViolation.get_line_number())
