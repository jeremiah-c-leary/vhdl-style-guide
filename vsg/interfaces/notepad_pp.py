
import vsg

from vsg import config
from vsg import vhdlFile
from vsg import rule_list
from vsg import apply_rules


class New():

    def __init__(self):
        self.identifier = 'notepad++ interface'

    def get_input_arguments(self):
        return InputArguments()

    def fix(self, oInputArguments):
        lText = oInputArguments.text.splitlines()
        iIndex = 0
        sFileName = oInputArguments.filename
        commandLineArguments = command_line_args()
        commandLineArguments.style = oInputArguments.style
        commandLineArguments.configuration = oInputArguments.configuration
        oConfig = config.New(commandLineArguments)

        oResults = Results()

        try:
            oVhdlFile = vhdlFile.vhdlFile(lText, sFileName, None)
        except vsg.exceptions.ClassifyError as e:
            oResults.error = True
            oResults.set_violations(False)
            oResults.set_text(oInputArguments.text)
            sOutput = e.message
            oResults.set_stdout(sOutput)
            return oResults

        oVhdlFile.set_indent_map(oConfig.dIndent)

        oRules = rule_list.rule_list(oVhdlFile, oConfig.severity_list, commandLineArguments.local_rules)

        try:
            apply_rules.configure_rules(oConfig, oRules, oConfig.dIndent, iIndex, sFileName)
        except vsg.exceptions.ConfigurationError as e:
            oResults.error = True
            oResults.set_violations(False)
            oResults.set_text(oInputArguments.text)
            sOutput = e.message
            oResults.set_stdout(sOutput)
            return oResults

        oRules.fix(commandLineArguments.fix_phase, commandLineArguments.skip_phase, oConfig.dFixOnly)

        sOutput = '\n'.join(oVhdlFile.get_lines()[1:])

        oResults.set_text(sOutput)

        oRules.clear_violations()
        oRules.check_rules(
            bAllPhases=commandLineArguments.all_phases,
            lSkipPhase=commandLineArguments.skip_phase,
        )
        sStdOut, sIgnore = oRules.report_violations(commandLineArguments.output_format)
        oResults.set_stdout(sStdOut)

        oResults.set_violations(oRules.violations)

        return oResults


class InputArguments():

    def __init__(self):
        self.filename = str(None)
        self.text = None
        self.style = None
        self.configuration = []

    def set_text(self, sText):
        self.text = sText

    def set_style(self, sText):
        self.style = sText

    def add_configuration(self, sText):
        self.configuration.append(sText)


class Results():

    def __init__(self):
        self.text = None
        self.stdout = None
        self.violations = True
        self.error = False

    def set_text(self, sText):
        self.text = sText

    def get_text(self):
        return self.text

    def set_stdout(self, sText):
        self.stdout = sText

    def get_stdout(self):
        return self.stdout

    def has_violations(self):
        return self.violations

    def set_violations(self, bViolations):
        self.violations = bViolations

    def error_status(self):
        return self.error


class command_line_args():
    def __init__(self):
        self.fix = False
        self.style = None
        self.configuration = None
        self.debug = None
        self.fix_only = None
        self.local_rules = None
        self.fix_phase = 7
        self.junit = None
        self.output_format = 'vsg'
        self.all_phases = False
        self.skip_phase = None
