# -*- coding: utf-8 -*-

from vsg.rules import create_violation


class New:
    def __init__(self, sName):
        self.name = sName
        self.value = None
        self.analyze_function = None
        self.analysis_options = None

    def analyze(self, oToi):
        return self.analyze_function(self, oToi)
