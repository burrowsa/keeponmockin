from collections import Sequence
from six import string_types


def is_non_string_sequence(what):
    return isinstance(what, Sequence) and not isinstance(what, string_types)
