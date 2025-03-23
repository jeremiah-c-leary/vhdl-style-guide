# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import assertion as token
from vsg.vhdlFile.classify import condition, expression


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    """
    assertion ::=
        assert condition
            [ report expression ]
            [ severity expression ]

    The key to detecting this is looking for the keyword **assert** before a semicolon.
    """

    oDataStructure.replace_next_token_required("assert", token.keyword)

    condition.classify_until(["report", "severity", ";"], oDataStructure)

    if oDataStructure.is_next_token("report"):
        oDataStructure.replace_next_token_with(token.report_keyword)
        expression.classify_until(["severity", ";"], oDataStructure)

    if oDataStructure.is_next_token("severity"):
        oDataStructure.replace_next_token_with(token.severity_keyword)
        expression.classify_until([";"], oDataStructure)
