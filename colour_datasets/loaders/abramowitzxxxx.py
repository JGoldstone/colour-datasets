# -*- coding: utf-8 -*-
"""
Kodak Color Compensating Filters - Abramowitz (xxxx)
================================================

Defines the objects implementing support for *Olympus (xxxx)*
*Kodak Color Compensating Filters* dataset loading:

-   :class:`colour_datasets.loaders.DatasetLoader_Abramowitzxxxx`
-   :func:`colour_datasets.loaders.build_Abramowitzxxxx`

References
----------
-   :cite:`Abramowitzxxxx` : Abramowitz, M., & Davidson, M. W. (xxxx). Kodak Color Compensating Filters.
    Retrieved November 28, 2020, from
    https://olympus_lifescience.com/en/microscope-resource/primer/photomicrography/ccfilters/ccblue/
    https://olympus_lifescience.com/en/microscope-resource/primer/photomicrography/ccfilters/cccyan/
    https://olympus_lifescience.com/en/microscope-resource/primer/photomicrography/ccfilters/ccgreen/
    https://olympus_lifescience.com/en/microscope-resource/primer/photomicrography/ccfilters/ccyellow/
    https://olympus_lifescience.com/en/microscope-resource/primer/photomicrography/ccfilters/ccred/
    https://olympus_lifescience.com/en/microscope-resource/primer/photomicrography/ccfilters/ccmagenta/
"""

from __future__ import division, unicode_literals

import pandas as pd
import os

from collections import OrderedDict

from colour import MultiSpectralDistributions

from colour_datasets.records import datasets
from colour_datasets.loaders import AbstractDatasetLoader

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['DatasetLoader_Abramowitzxxxx', 'build_Abramowitzxxxx']


class DatasetLoader_Abramowitzxxxx(AbstractDatasetLoader):
    """
    Defines the *Abramowitz (nnnn)* *Kodak Color Compensating Filters* dataset
    loader.

    Attributes
    ----------
    ID

    Methods
    -------
    load

    References
    ----------
    :cite:`Abramowitznnnn`
    """

    ID = 'nnnnnnn'
    """
    Dataset record id, i.e. the *Zenodo* record number.

    ID : unicode
    """

    def __init__(self):
        # TODO get rid of this hotwiring when we are up on Zenodo
        # super(DatasetLoader_Abramowitzxxxx,
        #       self).__init__(datasets()[DatasetLoader_Abramowitzxxxx.ID])
        pass

    def _add_csv_contents_to_dict(self, repository, cc_filename, skiprows):
        csv_path = os.path.join(repository, cc_filename)
        df = pd.read_csv(csv_path, skiprows=skiprows, header=0, index_col=0).T
        mds = MultiSpectralDistributions(df)
        for label in mds.labels:
            self._content[label] = mds.signals[label]

    def load(self):
        """
        Syncs, parses, converts and returns the *Abramowitz (2020)*
        *Kodak Compensating Color Filters* dataset content.

        Returns
        -------
        OrderedDict
            *Abramowitz (2020)* *Kodak Color Compensating Filters* dataset content.

        Examples
        --------
        >>> from colour_datasets.utilities import suppress_stdout
        >>> dataset = DatasetLoader_Abramowitzxxxx()
        >>> with suppress_stdout():
        ...     dataset.load()
        >>> len(dataset.content.keys())
        29
        """

        # TODO restore when we are up on Zenodo
        # super(DatasetLoader_Abramowitzxxxx, self).sync()

        self._content = OrderedDict()
        # TODO clean up when we are up on Zenodo
        # these are for when we get the data uploaded and don't have to cheat
        # repo_dir = os.path.join(self.record.repository, 'dataset')
        # self._add_csv_contents_to_dict(repo_dir, "kodak_cc_400_700.csv", 4)
        # self._add_csv_contents_to_dict(repo_dir, "kodak_cc_400_800.csv", 3)
        # but for now...
        REPO_DIR_HOTWIRE = os.path.join("/Users/jgoldstone/.colour-science/colour-datasets/nnnnnnn", "dataset")
        self._add_csv_contents_to_dict(REPO_DIR_HOTWIRE, "kodak_cc_400_700.csv", 4)
        self._add_csv_contents_to_dict(REPO_DIR_HOTWIRE, "kodak_cc_400_800.csv", 3)
        return self._content


_DATASET_LOADER_ABRAMOWITZxxxx = None
"""
Singleton instance of the *Abramowitz (xxxx)* *Kodak Compensating Color Filters*
dataset loader.

_DATASET_LOADER_ABRAMOWITZxxxx : DatasetLoader_Abramowitzxxxx
"""


def build_Abramowitzxxxx(load=True):
    """
    Singleton factory that builds the *Abramowitz (xxxx)*
    *Kodak Compensating Color Filters* dataset loader.

    Parameters
    ----------
    load : bool, optional
        Whether to load the dataset upon instantiation.

    Returns
    -------
    DatasetLoader_Abramowitzxxxx
        Singleton instance of the *Abramowitz (xxxx)*
        *Kodak Compensating Color Filters* dataset loader.

    References
    ----------
    :cite:`Abramowitzxxxx`
    """

    global _DATASET_LOADER_ABRAMOWITZxxxx

    if _DATASET_LOADER_ABRAMOWITZxxxx is None:
        _DATASET_LOADER_ABRAMOWITZxxxx = DatasetLoader_Abramowitzxxxx()
        if load:
            _DATASET_LOADER_ABRAMOWITZxxxx.load()

    return _DATASET_LOADER_ABRAMOWITZxxxx
