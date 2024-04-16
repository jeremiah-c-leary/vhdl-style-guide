# -*- coding: utf-8 -*-

from vsg import parser


class entity_tag(parser.identifier):
    """
    unique_id = entity_designator : entity_tag
    """

    def __init__(self, sString):
        super().__init__(sString)
