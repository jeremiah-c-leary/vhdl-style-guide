# -*- coding: utf-8 -*-

from vsg.token import concurrent_selected_signal_assignment as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import delay_mechanism, expression, selected_waveforms


def detect(oDataStructure):
    """
    concurrent_selected_signal_assignment ::=
        with expression select [ ? ]
            target <= [ guarded ] [ delay_mechanism ] selected_waveforms ;

    The key to detecting this is looking for the **with** keyword before the **select** keyword.
    """
    if oDataStructure.exists_in_next_n_tokens("with", 4):
        if not oDataStructure.exists_in_next_n_tokens("end", 1):
            return True
    return False


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required("with", token.with_keyword, iToken, lObjects)

    iCurrent = expression.classify_until(["select"], iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required("select", token.select_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if("?", token.question_mark, iCurrent, lObjects)

    iCurrent = utils.assign_tokens_until("<=", token.target, iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required("<=", token.assignment, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if("guarded", token.guarded_keyword, iCurrent, lObjects)

    iCurrent = delay_mechanism.detect(iCurrent, lObjects)

    selected_waveforms.classify_until([";"], iToken, lObjects)

    iCurrent = utils.assign_next_token_required(";", token.semicolon, iCurrent, lObjects)

    return iCurrent
