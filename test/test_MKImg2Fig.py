# MK-Img2fig: Markdown Img to Figure
#
# Copyright (c) 2019 Mandaris Moore
#
# GNU License
import markdown
import unittest

import MKImg2Fig


class MKImg2FigTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_empty_input(self):
        inString = ""
        outString = markdown.markdown(
            inString, extensions=[MKImg2Fig.MKImg2FigExtension()])
        self.assertEqual(inString, outString)

    def test_no_images(self):
        inString = """\
This is a test text.

It contains multiple paragraphs as well as [links](https://example.com).

* Itemize
* is
* used,
* as well.

# This is a headline.

Taken from yafg test suite"""
        expectedString = markdown.markdown(inString)
        outString = markdown.markdown(
            inString, extensions=[MKImg2Fig.MKImg2FigExtension()])
        self.assertEqual(expectedString, outString)
