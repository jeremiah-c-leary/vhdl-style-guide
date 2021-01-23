import shutil
import os
import subprocess
import pathlib


import unittest

from vsg.tests import utils

sEntityFileName = 'entity.vhd'
sArchitectureFileName = 'architecture.vhd'
sJUnitFileName = 'junit_output.xml'

sEntityFile = os.path.join(os.path.dirname(__file__), sEntityFileName)
sArchitectureFile = os.path.join(os.path.dirname(__file__), sArchitectureFileName)
sJUnitFile = os.path.join(os.path.dirname(__file__), sJUnitFileName)
sConfigFile = os.path.join(os.path.dirname(__file__),'config.yaml')
sOutputFileWoConfig = os.path.join(os.path.dirname(__file__),'output_wo_config.txt')
sOutputFileWithConfig = os.path.join(os.path.dirname(__file__),'output_w_config.txt')
sOutputFileWithConfigFixed = os.path.join(os.path.dirname(__file__),'output_w_config_fixed.txt')
sArchitectureOutputFileWoConfig = os.path.join(os.path.dirname(__file__),'output_wo_config.architecture.txt')
sArchitectureOutputFileWithConfig = os.path.join(os.path.dirname(__file__),'output_w_config.architecture.txt')
sArchitectureOutputFileWithConfigFixed = os.path.join(os.path.dirname(__file__),'output_w_config_fixed.architecture.txt')


class test_severity_using_main(unittest.TestCase):

    def setUp(self):
        if os.path.isfile(sEntityFileName):
            os.remove(sEntityFileName)
        if os.path.isfile(sArchitectureFileName):
            os.remove(sArchitectureFileName)
        if os.path.isfile(sJUnitFileName):
            os.remove(sJUnitFileName)
        shutil.copyfile(sEntityFile, sEntityFileName)
        shutil.copyfile(sArchitectureFile, sArchitectureFileName)
        shutil.copyfile(sJUnitFile, sJUnitFileName)

    def tearDown(self):
        os.remove(sEntityFileName)
        os.remove(sArchitectureFileName)
        os.remove(sJUnitFileName)

    def test_entity_without_configuration(self):
        try:
            subprocess.check_output(['bin/vsg', '-f', sEntityFileName])
        except subprocess.CalledProcessError as e:
            lActual = e.output.decode('utf-8').split('\n')
            iExitStatus = e.returncode

        lExpected = pathlib.Path(sOutputFileWoConfig).read_text().split('\n')

        self.assertEqual(iExitStatus, 1)
        self.assertEqual(utils.replace_total_count(lActual), lExpected)

    def test_entity_with_configuration(self):
        try:
            subprocess.check_output(['bin/vsg', '-f', sEntityFileName, '-c', sConfigFile])
        except subprocess.CalledProcessError as e:
            lActual = e.output.decode('utf-8').split('\n')
            iExitStatus = e.returncode

        lExpected = pathlib.Path(sOutputFileWithConfig).read_text().split('\n')

        self.assertEqual(iExitStatus, 1)
        self.assertEqual(utils.replace_total_count(lActual), lExpected)

    def test_entity_with_configuration_and_fixed(self):
        lActual = subprocess.check_output(
                ['bin/vsg', '-f', sEntityFileName, '-c', sConfigFile, '--fix']
                ).decode('utf-8').split('\n')

        lExpected = pathlib.Path(sOutputFileWithConfigFixed).read_text().split('\n')

        self.assertEqual(utils.replace_total_count(lActual), lExpected)

    def test_architecture_without_configuration(self):
        try:
            subprocess.check_output(['bin/vsg', '-f', sArchitectureFileName])
        except subprocess.CalledProcessError as e:
            lActual = e.output.decode('utf-8').split('\n')
            iExitStatus = e.returncode

        lExpected = pathlib.Path(sArchitectureOutputFileWoConfig).read_text().split('\n')

        self.assertEqual(iExitStatus, 1)
        self.assertEqual(utils.replace_total_count(lActual), lExpected)

    def test_architecture_with_configuration(self):
        try:
            subprocess.check_output(['bin/vsg','-f', sArchitectureFileName, '-c', sConfigFile])
        except subprocess.CalledProcessError as e:
            lActual = e.output.decode('utf-8').split('\n')
            iExitStatus = e.returncode

        lExpected = pathlib.Path(sArchitectureOutputFileWithConfig).read_text().split('\n')

        self.assertEqual(iExitStatus, 1)
        self.assertEqual(utils.replace_total_count(lActual), lExpected)

    def test_architecture_with_configuration_and_fixed(self):
        lActual = subprocess.check_output(
                ['bin/vsg','-f', sArchitectureFileName, '-c', sConfigFile, '--fix']
                ).decode('utf-8').split('\n')

        lExpected = pathlib.Path(sArchitectureOutputFileWithConfigFixed).read_text().split('\n')

        self.assertEqual(utils.replace_total_count(lActual), lExpected)

    def test_both_with_configuration(self):
        try:
            subprocess.check_output(['bin/vsg', '-f', sEntityFileName, sArchitectureFileName, '-c', sConfigFile])
        except subprocess.CalledProcessError as e:
            lActual = e.output.decode('utf-8').split('\n')
            iExitStatus = e.returncode

        lExpected1 = pathlib.Path(sOutputFileWithConfig).read_text().rstrip('\n').split('\n')
        lExpected2 = pathlib.Path(sArchitectureOutputFileWithConfig).read_text().split('\n')

        self.assertEqual(iExitStatus, 1)
        self.assertEqual(utils.replace_total_count(lActual), lExpected1 + lExpected2)

    def test_both_with_configuration_and_fixed(self):
        lActual = subprocess.check_output(
                ['bin/vsg', '-f', sEntityFileName, sArchitectureFileName, '-c', sConfigFile, '--fix']
                ).decode('utf-8').split('\n')

        lExpected1 = pathlib.Path(sOutputFileWithConfigFixed).read_text().rstrip('\n').split('\n')
        lExpected2 = pathlib.Path(sArchitectureOutputFileWithConfigFixed).read_text().split('\n')

        self.assertEqual(utils.replace_total_count(lActual), lExpected1 + lExpected2)

    def test_oc_option(self):
        lActual = subprocess.check_output(['bin/vsg', '-oc', 'blah.json']).decode('utf-8').split('\n')
        self.assertEqual(lActual, [''])

    def test_junit_output(self):
        try:
            subprocess.check_output(['bin/vsg', '-f', sEntityFileName, '-c', sConfigFile, '-j', sJUnitFileName])
        except subprocess.CalledProcessError as e:
            iExitStatus = e.returncode

        lActual = pathlib.Path(sJUnitFileName).read_text().split('\n')
        lExpected = pathlib.Path(sJUnitFile).read_text().split('\n')

        self.assertEqual(iExitStatus, 1)

        self.assertEqual(len(lActual), len(lExpected))

        for iIndex, sLine in enumerate(lExpected):
            if not iIndex == 1:
                self.assertEqual(lActual[iIndex], sLine)
