"""Unit tests for the lambda function."""

import cartola_budget
import utils.test


def test_handler():
    """Test if returns an existing value."""
    res = cartola_budget.handler(event=None, context=None)
    assert 0 < res["budget"] < 250


def test_is_serializable():
    """Test if return is serializable."""
    res = cartola_budget.handler(event=None, context=None)
    assert utils.test.is_serializable(res)
