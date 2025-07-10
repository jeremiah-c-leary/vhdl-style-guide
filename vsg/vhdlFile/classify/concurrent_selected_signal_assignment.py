# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import concurrent_selected_signal_assignment as token
from vsg.vhdlFile.classify import delay_mechanism, expression, selected_waveforms, utils


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    concurrent_selected_signal_assignment ::=
        with expression select [ ? ]
            target <= [ guarded ] [ delay_mechanism ] selected_waveforms ;

    The key to detecting this is looking for the **with** keyword before the **select** keyword.
    """
    if oDataStructure.does_string_exist_in_next_n_tokens("with", 4):
        if not oDataStructure.does_string_exist_in_next_n_tokens("end", 1):
            return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_required("with", token.with_keyword)

    expression.classify_until(["select"], oDataStructure)

    oDataStructure.replace_next_token_required("select", token.select_keyword)
    oDataStructure.replace_next_token_with_if("?", token.question_mark)

    utils.assign_tokens_until("<=", token.target, oDataStructure)

    oDataStructure.replace_next_token_required("<=", token.assignment)

    oDataStructure.replace_next_token_with_if("guarded", token.guarded_keyword)

    delay_mechanism.detect(oDataStructure)

    selected_waveforms.classify_until([";"], oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)
