# -*- coding: utf-8 -*-
"""
Defines unit tests for :mod:`colour_datasets.loaders.zhao2009` module.
"""

import unittest

from colour import SpectralShape

from colour_datasets.loaders import DatasetLoader_Zhao2009, build_Zhao2009

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2021 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['TestDatasetLoader_Zhao2009', 'TestBuildZhao2009']


class TestDatasetLoader_Zhao2009(unittest.TestCase):
    """
    Defines :class:`colour_datasets.loaders.zhao2009.DatasetLoader_Zhao2009`
    class unit tests methods.
    """

    def test_required_attributes(self):
        """
        Tests presence of required attributes.
        """

        required_attributes = ('ID', )

        for attribute in required_attributes:
            self.assertIn(attribute, dir(DatasetLoader_Zhao2009))

    def test_required_methods(self):
        """
        Tests presence of required methods.
        """

        required_methods = ('__init__', 'load')

        for method in required_methods:
            self.assertIn(method, dir(DatasetLoader_Zhao2009))

    def test_load(self):
        """
        Tests :func:`colour_datasets.loaders.zhao2009.\
DatasetLoader_Zhao2009.load` method.
        """

        dataset = DatasetLoader_Zhao2009()
        self.assertEqual(
            sorted(dataset.load().keys()),
            sorted([
                'SONY DXC 930', 'KODAK DCS 420', 'NIKON D1X', 'SONY DXC 9000',
                'CANON 10D', 'NIKON D70', 'KODAK DCS 460', 'CANON 400D',
                'CANON 5D', 'CANON 5D Mark 2', 'Ladybug2', 'KODAK DCS 200'
            ]))
        self.assertEqual(dataset.content['SONY DXC 930'].shape,
                         SpectralShape(400, 700, 4))


class TestBuildZhao2009(unittest.TestCase):
    """
    Defines :func:`colour_datasets.loaders.zhao2009.build_Zhao2009`
    definition unit tests methods.
    """

    def test_build_Zhao2009(self):
        """
        Tests :func:`colour_datasets.loaders.zhao2009.build_Zhao2009`
        definition.
        """

        self.assertIs(build_Zhao2009(), build_Zhao2009())


if __name__ == '__main__':
    unittest.main()
