
import os
import sys
import re
import importlib
import inspect

import vsg.rules


def get_python_modules_from_directory(sDirectoryName, lModules):

    try:
        lDirectoryContents = os.listdir(sDirectoryName)
        for sFileName in lDirectoryContents:
            if sFileName.endswith('.py') and not sFileName.startswith('__'):
                lModules.append(sFileName.replace('.py', ''))
    except:
        print ('ERROR: directory ' + sDirectoryName + ' could not be found.')
        exit()


def get_rules_from_module(lModules, lRules):

    for sModuleName in lModules:
        for name, obj in inspect.getmembers(importlib.import_module(sModuleName)):
            if name.startswith('rule_'):
                lRules.append(obj())


def load_local_rules(sDirectoryName):
    '''Loads rules from the directory passed to this routine.'''

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


class list():
    ''' Contains a list of all rules to be checked.  It also contains methods to check the rules.'''

    def __init__(self, oVhdlFile, sLocalRulesDirectory=None):
        self.rules = (load_rules())
        if sLocalRulesDirectory:
            self.rules.extend(load_local_rules(sLocalRulesDirectory))
        self.iNumberRulesRan = 0
        self.lastPhaseRan = 0
        self.oVhdlFile = oVhdlFile
        self.maximumPhase = maximum_phase(self.rules)

    def fix(self):
        for phase in range(1, 10):
            for oRule in self.rules:
                if oRule.phase == phase and not oRule.disable:
                    oRule.fix(self.oVhdlFile)

    def check_rules(self):
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

    def report_violations(self):
        sFileTitle = 'File:  ' + self.oVhdlFile.filename
        print (sFileTitle)
        print ('=' * len(sFileTitle))
        iFailures = 0
        for phase in range(1, self.maximumPhase + 1):
            if phase <= self.lastPhaseRan:
                print ('Phase ' + str(phase) + '... Reporting')
                for iLineNumber in range(1, len(self.oVhdlFile.lines)):
                    for oRule in self.rules:
                        if oRule.phase == phase:
                            iFailures += oRule.report_violations(iLineNumber)
            else:
                print ('Phase ' + str(phase) + '... Not executed')

        print ('=' * len(sFileTitle))
        print ('Total Rules Checked: ' + str(self.iNumberRulesRan))
        print ('Total Failures:      ' + str(iFailures))

    def configure(self, configurationFile):
        '''Configures individual rules based on dictionary passed.'''
        if configurationFile:
            for oRule in self.rules:
                oRule.configure(configurationFile)
