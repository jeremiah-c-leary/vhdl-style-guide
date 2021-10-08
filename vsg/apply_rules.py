
import shutil

from . import config
from . import rule_list
from . import utils
from . import vhdlFile


def create_backup_file(sFileName):
    '''Copies existing file and adds .bak to the end.'''
    shutil.copy2(sFileName, sFileName + '.bak')


def configure_rules(oConfig, oRules, configuration, iIndex, sFileName):

    oRules.configure(oConfig)
    if is_filename_in_file_list(configuration, sFileName):
        iMyIndex = get_index_of_filename_in_file_list(configuration, sFileName)
        oRuleConfig = config.config()
        if does_file_have_rule_configuration(configuration, iMyIndex, sFileName):
            oRuleConfig.dConfig = configuration["file_list"][iMyIndex][sFileName]
            oRules.configure(oRuleConfig)


def is_filename_in_file_list(configuration, sFileName):
    try:
        lFileNames = utils.extract_file_names_from_file_list(configuration["file_list"])
        if sFileName in lFileNames:
            return True
        return False
    except KeyError:
        return False


def get_index_of_filename_in_file_list(configuration, sFileName):
    lFileNames = utils.extract_file_names_from_file_list(configuration["file_list"])
    return lFileNames.index(sFileName)


def does_file_have_rule_configuration(configuration, iMyIndex, sFileName):
    try:
        sTemp = configuration["file_list"][iMyIndex][sFileName]
        return True
    except:
        return False


# This function is in a separate module from __main__ as a workaround for https://bugs.python.org/issue25053
# see also https://stackoverflow.com/questions/41385708/multiprocessing-example-giving-attributeerror/42383397#42383397
def apply_rules(commandLineArguments, oConfig, tIndexFileName):
    configuration = oConfig.dConfig

    dIndent = oConfig.dIndent
    fix_only = oConfig.dFixOnly

    iIndex, sFileName = tIndexFileName
    dJsonEntry = {}
    lFileContent, eError = vhdlFile.utils.read_vhdlfile(sFileName)
    oVhdlFile = vhdlFile.vhdlFile(lFileContent, sFileName, eError)
    oVhdlFile.set_indent_map(dIndent)
    try:
        oRules = rule_list.rule_list(
            oVhdlFile, oConfig.severity_list, commandLineArguments.local_rules
        )
    except OSError as e:
        sOutputStd = (
            f"ERROR: encountered {e.__class__.__name__}, {e.args[1]} "
            + commandLineArguments.local_rules
            + " when trying to open local rules file."
        )
        sOutputErr = None
        return 1, None, dJsonEntry, sOutputStd, sOutputErr

    configure_rules(oConfig, oRules, configuration, iIndex, sFileName)

    if commandLineArguments.fix:
        if commandLineArguments.backup:
            create_backup_file(sFileName)
        oRules.fix(
            commandLineArguments.fix_phase, commandLineArguments.skip_phase, fix_only
        )
        write_vhdl_file(oVhdlFile)

    oRules.clear_violations()
    oRules.check_rules(
        bAllPhases=commandLineArguments.all_phases,
        lSkipPhase=commandLineArguments.skip_phase,
    )
    sOutputStd, sOutputErr = oRules.report_violations(
        commandLineArguments.output_format
    )
    fExitStatus = oRules.violations

    if commandLineArguments.junit:
        testCase = oRules.extract_junit_testcase(sFileName)
    else:
        testCase = None

    if commandLineArguments.json:
        dJsonEntry["file_path"] = sFileName
        dJsonEntry["violations"] = oRules.extract_violation_dictionary()["violations"]

    return fExitStatus, testCase, dJsonEntry, sOutputStd, sOutputErr


def write_vhdl_file(oVhdlFile):
    try:
        with open(oVhdlFile.filename, 'w') as oFile:
            for sLine in oVhdlFile.get_lines()[1:]:
                oFile.write(sLine + '\n')
    except PermissionError as err:
        print (err, "Could not write fixes back to file.")


