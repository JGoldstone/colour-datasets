# -*- coding: utf-8 -*-
"""
Defines unit tests for :mod:`colour_datasets.loaders.Abramowitzxxxx` module.
"""

from __future__ import division, unicode_literals

import unittest

from colour import SpectralShape

from colour_datasets.loaders import (DatasetLoader_Abramowitzxxxx,
                                     build_Abramowitzxxxx)

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['TestDatasetLoader_Abramowitzxxxx', 'TestBuildAbramowitzxxxx']


class TestDatasetLoader_Abramowitzxxxx(unittest.TestCase):
    """
    Defines :class:`colour_datasets.loaders.abramowitzxxxx.\
DatasetLoader_Abramowitzxxxx class unit tests methods.
    """

    def test_required_attributes(self):
        """
        Tests presence of required attributes.
        """

        required_attributes = ('ID', )

        for attribute in required_attributes:
            self.assertIn(attribute, dir(DatasetLoader_Abramowitzxxxx))

    def test_required_methods(self):
        """
        Tests presence of required methods.
        """

        required_methods = ('__init__', 'load')

        for method in required_methods:
            self.assertIn(method, dir(DatasetLoader_Abramowitzxxxx))

    def test_load(self):
        """
        Tests :func:`colour_datasets.loaders.abramowitzxxxx.\
DatasetLoader_ABramowitzxxxx.load` method.
        """

        dataset = DatasetLoader_Abramowitzxxxx()

        self.assertEqual(len(dataset.load()), 36)

        self.assertEqual(
            dataset.content['CC05B'].shape, SpectralShape(400, 700, 10))
        self.assertEqual(
            dataset.content['CC05C'].shape, SpectralShape(400, 800, 10))


class TestBuildAbramowitzxxxx(unittest.TestCase):
    """
    Defines :func:`colour_datasets.loaders.abramowitzxxxx.build_Abramowitzxxxx`
    definition unit tests methods.
    """

    def test_build_Abramowitzxxxx(self):
        """
        Tests :func:`colour_datasets.loaders.abramowitzxxxx.build_Abramowitz2020`
        definition.
        """

        self.assertIs(build_Abramowitzxxxx(), build_Abramowitzxxxx())


if __name__ == '__main__':
    unittest.main()
