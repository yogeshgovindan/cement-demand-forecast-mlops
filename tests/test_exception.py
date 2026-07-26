import sys
import pytest

from src.exception.exception import CustomException


def test_custom_exception():

    try:

        value = 10 / 0

    except Exception as e:

        custom_exception = CustomException(
            e,
            sys
        )

        assert "division by zero" in str(custom_exception)
