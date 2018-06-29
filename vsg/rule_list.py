
import os
import importlib
import inspect

import junit


def get_python_modules_from_directory(sDirectoryName, lModules):

    try:
        lDirectoryContents = os.listdir(sDirectoryName)
        for sFileName in lDirectoryContents:
            if sFileName.endswith('.py') and not sFileName.startswith('__'):
                lModules.append(sFileName.replace('.py', ''))
    except OSError:
        print('ERROR: specified local rules directory ' + sDirectoryName + ' could not be found.')
        exit()


def get_rules_from_module(lModules, lRules):

    for sModuleName in lModules:
        for name, obj in inspect.getmembers(importlib.import_module(sModuleName)):
            if name.startswith('rule_'):
                lRules.append(obj())


def load_local_rules(sDirectoryName):
    '''
    Loads rules from the directory passed to this routine.
    '''

    lLocalModules = []
    get_python_modules_from_directory(sDirectoryName, lLocalModules)

    lRules = []
    get_rules_from_module(lLocalModules, lRules)
    return lRules


def load_rules():
    '''
    Loads rules from the vsg/rules directory.
    '''

    lRules = []
    for name, oPackage in inspect.getmembers(importlib.import_module('vsg.rules')):
        if inspect.ismodule(oPackage):
            for name, oRule in inspect.getmembers(oPackage):
                if inspect.isclass(oRule) and name.startswith('rule_'):
                    lRules.append(oRule())

    return lRules


def maximum_phase(lRules):
    maximumPhaseNumber = 0
    for oRule in lRules:
        if oRule.phase > maximumPhaseNumber:
            maximumPhaseNumber = oRule.phase
    return maximumPhaseNumber


class rule_list():
    '''
    Contains a list of all rules to be checked.
    It loads all base rules.
    If localized rules are loaded if given.

    Parameters:

      oVhdlFile: (vhdlFile object)

      sLocalRulesDirectory: (string) (optional)
    '''
    def __init__(self, oVhdlFile, sLocalRulesDirectory=None):
        self.rules = (load_rules())
        if sLocalRulesDirectory:
            self.rules.extend(load_local_rules(sLocalRulesDirectory))
        self.iNumberRulesRan = 0
        self.lastPhaseRan = 0
        self.oVhdlFile = oVhdlFile
        self.maximumPhase = maximum_phase(self.rules)

    def fix(self, iPhase):
        '''
        Applies fixes to all violations found.
        '''
        for phase in range(1, int(iPhase) + 1):
            for oRule in self.rules:
                if oRule.phase == phase and not oRule.disable:
                    oRule.fix(self.oVhdlFile)

    def check_rules(self):
        '''
        Analyzes all rules in increasing phase order.
        If there is a violation in a phase, furthere analysis is stopped.
        '''
        self.iNumberRulesRan = 0
        iFailures = 0
        for phase in range(1, 10):
            iPhaseRuleCount = 0
            for oRule in self.rules:
                if oRule.phase == phase and not oRule.disable:
                    oRule.analyze(self.oVhdlFile)
                    iFailures += len(oRule.violations)
                    self.iNumberRulesRan += 1
                    iPhaseRuleCount += 1
                    self.lastPhaseRan = phase
            if iFailures > 0 or iPhaseRuleCount == 0:
                break

    def report_violations(self, sOutputFormat):
        '''
        Prints out violations to stdout.
        '''
        if sOutputFormat == 'vsg':
            sFileTitle = 'File:  ' + self.oVhdlFile.filename
            print(sFileTitle)
            print('=' * len(sFileTitle))
        iFailures = 0
        for phase in range(1, self.maximumPhase + 1):
            if phase <= self.lastPhaseRan:
                if sOutputFormat == 'vsg':
                    print('Phase ' + str(phase) + '... Reporting')
                for iLineNumber in range(1, len(self.oVhdlFile.lines)):
                    for oRule in self.rules:
                        if oRule.phase == phase:
                            iFailures += oRule.report_violations(iLineNumber, sOutputFormat, self.oVhdlFile.filename)
            else:
                if sOutputFormat == 'vsg':
                    print('Phase ' + str(phase) + '... Not executed')

        if sOutputFormat == 'vsg':
            print('=' * len(sFileTitle))
            print('Total Rules Checked: ' + str(self.iNumberRulesRan))
            print('Total Violations:    ' + str(iFailures))

    def configure(self, configurationFile):
        '''
        Configures individual rules based on dictionary passed.

        Parameters:

          configurationFile: (dictionary)
        '''
        if configurationFile:
            for oRule in self.rules:
                oRule.configure(configurationFile)

    def extract_junit_testcase(self, sVhdlFileName):
        oTestcase = junit.testcase(sVhdlFileName, str(0), 'failure')
        oFailure = junit.failure('Failure')
        for oRule in self.rules:
            if len(oRule.violations) > 0:
                for iLinenumber in oRule.violations:
                    oFailure.add_text(oRule.name + '_' + oRule.identifier + ': ' + str(iLinenumber) + ' : ' + oRule.solution)
        oTestcase.add_failure(oFailure)

        return oTestcase
