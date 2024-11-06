"""
This module contains base classes for dictionaries.
"""

import abc
import os
import numpy as np
from utils import Tokenizer

STATIC_PATH = os.path.join(os.path.dirname(__file__), 'static')


class BaseDict(object):
    """
    A base class for sentiment analysis.
    For now, only 'positive' and 'negative' analysis is supported.

    Subclasses should implement ``init_dict``,
    in which ``_posset`` and ``_negset`` are initialized.

    ``Polarity`` and ``Subjectivity`` are calculated in the same way of Lydia system.
    See also http://www.cs.sunysb.edu/~skiena/lydia/

    The formula for ``Polarity`` is,

    .. math::

        Polarity= \\frac{N_{pos}-N_{neg}}{N_{pos}+N_{neg}}

    The formula for ``Subjectivity`` is,

    .. math::

        Subjectivity= \\frac{N_{pos}+N_{neg}}{N}

    :type tokenizer: obj
    :param tokenizer: An object which provides interface of ``tokenize``.
        If it is ``None``, a default tokenizer, which is defined in ``utils``, will be assigned.
    """

    __metaclass__ = abc.ABCMeta

    TAG_POL = 'Polarity'
    TAG_SUB = 'Subjectivity'
    TAG_POS = 'Positive'
    TAG_NEG = 'Negative'
    TAG_UNC = 'Uncertainty'
    TAG_LIT = 'Litigious'
    TAG_STR = 'Strong_Modal'
    TAG_WEA = 'Weak_Modal'
    TAG_CON = 'Constraining'
    TAG_COM = 'Complexity'
    TAG_COU = 'Word_Count'

    EPSILON = 1e-6

    def __init__(self, tokenizer=None):
        self._posset = set()
        self._negset = set()
        self._uncset = set()
        self._litset = set()
        self._strset = set()
        self._weaset = set()
        self._conset = set()
        self._comset = set()
        if tokenizer is None:
            self._tokenizer = Tokenizer()
        else:
            self._tokenizer = tokenizer
        self.init_dict()

        assert len(self._posset) > 0 and len(self._negset) > 0 and len(self._uncset) > 0 and len(self._litset) > 0 and len(self._strset) > 0 and len(self._weaset) > 0 and len(self._conset) > 0 and len(self._comset) > 0

    def tokenize(self, text):
        """
        :type text: str
        :returns: list
        """

        return self._tokenizer.tokenize(text)

    def tokenize_first(self, x):
        """
        :type x: str
        :returns: str
        """
        tokens = self.tokenize(x)
        if tokens:
            return tokens[0]
        else:
            return None

    @abc.abstractmethod
    def init_dict(self):
        pass

    def _get_score(self, term):
        """Get score for a single term.

        - +1 for positive terms.
        - -1 for negative terms.
        - +2 for uncertainty terms.
        - +3 for litigious terms.
        - +4 for strong modal terms.
        - +5 for weak modal terms.
        - +6 for constraining terms.
        - +7 for complexity terms.
        - 0 for others.

        :returns: int
        """
        if term in self._posset:
            return +1
        elif term in self._negset:
            return -1
        elif term in self._uncset:
            return +2
        elif term in self._litset:
            return +3
        elif term in self._strset:
            return +4
        elif term in self._weaset:
            return +5
        elif term in self._conset:
            return +6
        elif term in self._comset:
            return +7
        else:
            return 0

    def get_score(self, terms):
        """Get score for a list of terms.

        :type terms: list
        :param terms: A list of terms to be analyzed.

        :returns: dict
        """
        assert isinstance(terms, list) or isinstance(terms, tuple)
        score_li = np.asarray([self._get_score(t) for t in terms])

        s_pos = np.sum(score_li[score_li == 1])
        s_neg = -np.sum(score_li[score_li == -1])
        s_unc = np.sum(score_li[score_li == 2]) / 2
        s_lit = np.sum(score_li[score_li == 3]) / 3
        s_str = np.sum(score_li[score_li == 4]) / 4
        s_wea = np.sum(score_li[score_li == 5]) / 5
        s_con = np.sum(score_li[score_li == 6]) / 6
        s_com = np.sum(score_li[score_li == 7]) / 7
        s_cou = len(score_li)

        s_pol = (s_pos - s_neg) * 1.0 / ((s_pos + s_neg) + self.EPSILON)
        s_sub = (s_pos + s_neg) * 1.0 / (len(score_li) + self.EPSILON)

        return {
            self.TAG_POS: s_pos,
            self.TAG_NEG: s_neg,
            self.TAG_UNC: s_unc,
            self.TAG_LIT: s_lit,
            self.TAG_STR: s_str,
            self.TAG_WEA: s_wea,
            self.TAG_CON: s_con,
            self.TAG_COM: s_com,
            self.TAG_POL: s_pol,
            self.TAG_SUB: s_sub,
            self.TAG_COU: s_cou
        }