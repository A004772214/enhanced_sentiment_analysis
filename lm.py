import pandas as pd
from base import STATIC_PATH, BaseDict


class LM(BaseDict):
    """
    Dictionary class for
    Loughran and McDonald Financial Sentiment Dictionaries.

    See also https://www3.nd.edu/~mcdonald/Word_Lists.html

    The terms for the dictionary are stemmed by the default tokenizer.
    """

    PATH = '%s/LM.csv' % STATIC_PATH

    def init_dict(self):
        data = pd.read_csv(self.PATH)
        self._posset = set(data.query('Positive > 0')['Word'].apply(self.tokenize_first).dropna())
        self._negset = set(data.query('Negative > 0')['Word'].apply(self.tokenize_first).dropna())
        self._uncset = set(data.query('Uncertainty > 0')['Word'].apply(self.tokenize_first).dropna())
        self._litset = set(data.query('Litigious > 0')['Word'].apply(self.tokenize_first).dropna())
        self._strset = set(data.query('Strong_Modal > 0')['Word'].apply(self.tokenize_first).dropna())
        self._weaset = set(data.query('Weak_Modal > 0')['Word'].apply(self.tokenize_first).dropna())
        self._conset = set(data.query('Constraining > 0')['Word'].apply(self.tokenize_first).dropna())
        self._comset = set(data.query('Complexity > 0')['Word'].apply(self.tokenize_first).dropna())
