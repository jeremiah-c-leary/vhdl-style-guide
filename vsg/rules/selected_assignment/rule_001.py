
from vsg.rules import experiment as Rule

from vsg.rules import option
from vsg import token
from vsg.rules import analysis
from vsg.rules import fix

lTokenPairs = []
lTokenPairs.append([token.concurrent_selected_signal_assignment.with_keyword, token.concurrent_selected_signal_assignment.semicolon])
lTokenPairs.append([token.selected_force_assignment.with_keyword, token.selected_force_assignment.semicolon])
lTokenPairs.append([token.selected_variable_assignment.with_keyword, token.selected_variable_assignment.semicolon])
lTokenPairs.append([token.selected_waveform_assignment.with_keyword, token.selected_waveform_assignment.semicolon])


class rule_001(Rule):
    '''
    jcl - fix this
    '''

    def __init__(self):
        Rule.__init__(self, 'selected_assignment', '001')
        self.lTokenPairs = lTokenPairs
        self.add_option(newLineAfterWithKeywordOption())
        self.add_option(newLineBeforeSelectKeywordOption())
        self.add_option(newLineAfterSelectKeywordOption())
        self.add_option(newLineBeforeAssignmentOption())

        self.add_option(singleLineWithExpressionOption())


def newLineAfterWithKeywordOption():
    oOption = option.New('new_line_after_with_keyword')
    oOption.value = 'no'
    oOption.analyze_function = analysis.check_for_carriage_return_after_token
    
    lOptions = []
    lOptions.append(token.concurrent_selected_signal_assignment.with_keyword)
    lOptions.append(token.selected_force_assignment.with_keyword)
    lOptions.append(token.selected_variable_assignment.with_keyword)
    lOptions.append(token.selected_waveform_assignment.with_keyword)
    
    oOption.analysis_options = lOptions

    return oOption


def newLineBeforeSelectKeywordOption():

    oOption = option.New('new_line_before_select_keyword')
    oOption.value = 'no'
    oOption.analyze_function = analysis.check_for_carriage_return_before_token
    
    lOptions = []
    lOptions.append(token.concurrent_selected_signal_assignment.select_keyword)
    lOptions.append(token.selected_force_assignment.select_keyword)
    lOptions.append(token.selected_variable_assignment.select_keyword)
    lOptions.append(token.selected_waveform_assignment.select_keyword)
    
    oOption.analysis_options = lOptions
    return oOption


def newLineAfterSelectKeywordOption():

    oOption = option.New('new_line_after_select_keyword')
    oOption.value = 'yes'
    oOption.analyze_function = analysis.check_for_carriage_return_after_token
    
    lOptions = []
    lOptions.append(token.concurrent_selected_signal_assignment.select_keyword)
    lOptions.append(token.selected_force_assignment.select_keyword)
    lOptions.append(token.selected_variable_assignment.select_keyword)
    lOptions.append(token.selected_waveform_assignment.select_keyword)
    
    oOption.analysis_options = lOptions
    return oOption


def newLineBeforeAssignmentOption():

    oOption = option.New('new_line_before_assignment')
    oOption.value = 'no'
    oOption.analyze_function = analysis.check_for_carriage_return_before_token
    
    lOptions = []
    lOptions.append(token.concurrent_selected_signal_assignment.assignment)
    lOptions.append(token.selected_force_assignment.assignment)
    lOptions.append(token.selected_variable_assignment.assignment)
    lOptions.append(token.selected_waveform_assignment.assignment)
    
    oOption.analysis_options = lOptions
    return oOption

def singleLineWithExpressionOption():

    oOption = option.New('single_line_with_expression')
    oOption.value = 'ignore'
    oOption.analyze_function = analysis.check_for_carriage_returns_between_tokens_ignoring_leading_and_trailing_whitespace
    
    lOptions = []
    lOptions.append([token.concurrent_selected_signal_assignment.with_keyword, token.concurrent_selected_signal_assignment.select_keyword])
    lOptions.append([token.selected_force_assignment.with_keyword, token.selected_force_assignment.select_keyword])
    lOptions.append([token.selected_variable_assignment.with_keyword, token.selected_variable_assignment.select_keyword])
    lOptions.append([token.selected_waveform_assignment.with_keyword, token.selected_waveform_assignment.select_keyword])
    
    oOption.analysis_options = lOptions
    return oOption
