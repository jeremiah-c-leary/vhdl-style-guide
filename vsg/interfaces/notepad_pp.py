
from vsg import config
from vsg import vhdlFile
from vsg import rule_list
from vsg import apply_rules


class New():

    def __init__(self):
        self.identifier = 'notepad++ interface'
        self.deleteme = False
        self.inputArguments = None
        self.results = None


    def get_input_arguments(self):
        if self.inputArguments is None:
            return InputArguments()
        return self.inputArguments


    def set_input_arguments(self, oInputArguments):
        self.inputArguments = oInputArguments


    def execute(self):
        lText = self.inputArguments.text.splitlines()
        iIndex = 0
        sFileName = 'changeThis'
        commandLineArguments = command_line_args()
        oConfig = config.New(commandLineArguments)
        fix_only = oConfig.dFixOnly
        configuration = oConfig.dConfig
        dIndent = oConfig.dIndent
        oVhdlFile = vhdlFile.vhdlFile(lText, 'changeThis', None)
        oVhdlFile.set_indent_map(dIndent)

        oRules = rule_list.rule_list(
            oVhdlFile, oConfig.severity_list, commandLineArguments.local_rules
        )

        apply_rules.configure_rules(oConfig, oRules, configuration, iIndex, sFileName)

        oRules.fix(
            commandLineArguments.fix_phase, commandLineArguments.skip_phase, fix_only
        )

        sOutput = '\n'.join(oVhdlFile.get_lines()[1:])

        oResults = Results()
        oResults.set_text(sOutput)
        self.results = oResults

    def get_results(self):
        return self.results
      


class InputArguments():

    def __init__(self):
        self.text = None
        self.fix_enabled = False

    def set_text(self, sText):
        self.text = sText

    def enable_fix(self):
        self.fix_enabled = True

    def disable_fix(self):
        self.fix_enabled = False


class Results():

    def __init__(self):
        self.text = None

    def set_text(self, sText):
        self.text = sText

    def get_text(self):
        return self.text


class command_line_args():
    def __init__(self):
        self.fix = False
        self.style = None
        self.configuration = None
        self.debug = None
        self.fix_only = None
        self.local_rules = None
        self.fix_phase = 7
