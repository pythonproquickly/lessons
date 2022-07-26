import pytest

from spells import cast_spell

def test_valid_type():
    with pytest.raises(ValueError):
        cast_spell(62442)
