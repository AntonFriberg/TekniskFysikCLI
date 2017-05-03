"""Tests for our 'TekniskFysikCLI hello' subcommand."""

from subprocess import getoutput
from unittest import TestCase


class TestHello(TestCase):
    def test_returns_multiple_lines(self):
        output = getoutput('TekniskFysikCLI hello')
        lines = output.split('\n')
        self.assertTrue(len(lines) != 1)

    def test_returns_hello_world(self):
        output = getoutput('TekniskFysikCLI hello')
        self.assertTrue('Hello, world!' in output)
