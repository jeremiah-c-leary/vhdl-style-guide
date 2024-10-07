# -*- coding: utf-8 -*-
import os
import unittest

import vsg.vhdlFile as vhdlFile
from tests import utils


def get_list_of_lrm_unit_names():
    lReturn = []
    with os.scandir(os.path.dirname(__file__)) as lTokenFiles:
        lReturn = [entry.name for entry in lTokenFiles if (entry.is_dir() and entry.name != "__pycache__")]
    return lReturn


class TestClassificationMeta(type):
    __test__ = False

    def __new__(oClass, sName, oBases, dNamespace):
        def generate_test(sLrmUnit):
            def test_classification(self):
                lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(os.path.dirname(__file__), sLrmUnit, "classification_test_input.vhd"))
                oFile = vhdlFile.vhdlFile(lFile)

                self.maxDiff = None

                sTestDir = os.path.join(os.path.dirname(__file__), sLrmUnit)

                lExpected = []
                utils.read_file(os.path.join(sTestDir, "classification_results.txt"), lExpected, False)

                lActual = []

                for oObject in utils.extract_objects(oFile, True):
                    lActual.append(str(oObject))

                self.assertEqual(lExpected, lActual)

            return test_classification

        for sLrmUnit in get_list_of_lrm_unit_names():
            test_name = "test_" + sLrmUnit
            dNamespace[test_name] = generate_test(sLrmUnit)
        return type.__new__(oClass, sName, oBases, dNamespace)


class TestClassification(unittest.TestCase, metaclass=TestClassificationMeta):
    __metaclass__ = TestClassificationMeta
    __test__ = True
