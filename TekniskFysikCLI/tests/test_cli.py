"""Tests for our main TekniskFysikCLI module."""

from subprocess import getoutput
from unittest import TestCase

from TekniskFysikCLI import __version__ as VERSION

class TestHelp(TestCase):
    def test_returns_usage_information(self):
        output = getoutput('TekniskFysikCLI -h')
        self.assertTrue('Usage:' in output)

        output = getoutput('TekniskFysikCLI --help')
        self.assertTrue('Usage:' in output)


class TestVersion(TestCase):
    def test_returns_version_information(self):
        output = getoutput('TekniskFysikCLI --version')
        self.assertEqual(output.strip(), VERSION)
