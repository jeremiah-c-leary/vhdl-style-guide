
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
        sFileName = 'changeThis'
        commandLineArguments = command_line_args()
        commandLineArguments.style = oInputArguments.style
        commandLineArguments.configuration = oInputArguments.configuration
        oConfig = config.New(commandLineArguments)
        oVhdlFile = vhdlFile.vhdlFile(lText, sFileName, None)
        oVhdlFile.set_indent_map(oConfig.dIndent)

        oRules = rule_list.rule_list(oVhdlFile, oConfig.severity_list, commandLineArguments.local_rules)

        apply_rules.configure_rules(oConfig, oRules, oConfig.dIndent, iIndex, sFileName)

        oRules.fix(commandLineArguments.fix_phase, commandLineArguments.skip_phase, oConfig.dFixOnly)

        sOutput = '\n'.join(oVhdlFile.get_lines()[1:])

        oResults = Results()
        oResults.set_text(sOutput)

        return oResults


class InputArguments():

    def __init__(self):
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
        self.junit = None
