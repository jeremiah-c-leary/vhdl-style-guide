
import os
import sys
import re
import importlib
import inspect


def get_python_modules_from_directory(sDirectoryName, lModules):

    try:
        lDirectoryContents = os.listdir(sDirectoryName)
        for sFileName in lDirectoryContents:
            if sFileName.endswith('.py') and not sFileName.startswith('__'):
                lModules.append(sFileName.replace('.py',''))
    except:
        print ('ERROR: directory ' + sDirectoryName + ' could not be found.')
        exit()


def get_rules_from_module(lModules, lRules):

    for sModuleName in lModules:
        print sModuleName
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


def load_base_rules():
    pysearchre = re.compile('.py$', re.IGNORECASE)
    rulefiles = filter(pysearchre.search, os.listdir(os.path.join(os.path.dirname(__file__),'rules')))
    form_module = lambda fp: '.' + os.path.splitext(fp)[0]
    rulesList = map(form_module, rulefiles)
    # import paraent module / namespace
    importlib.import_module('vsg.rules')
    modules = []
    for rule in rulesList:
        if not rule.startswith('.__'):
            modules.append(importlib.import_module(rule, package="vsg.rules"))

    lRules = []
    for module in modules:
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj):
                if not obj.__name__.startswith('__') and not obj.__name__.endswith('_rule'):
                    lRules.append(obj())
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
        self.rules = load_base_rules()
        if sLocalRulesDirectory:
            self.rules.extend(load_local_rules(sLocalRulesDirectory))
        self.iNumberRulesRan = 0
        self.lastPhaseRan = 0
        self.oVhdlFile = oVhdlFile
        self.maximumPhase = maximum_phase(self.rules)

    def check_rules(self):
        self.iNumberRulesRan = 0
        iFailures = 0
        for phase in range(1,10):
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
        for phase in range(1,self.maximumPhase + 1):
            if phase <= self.lastPhaseRan:
                print ('Phase ' + str(phase) + '... Reporting')
                for iLineNumber in range (1, len(self.oVhdlFile.lines)):
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

