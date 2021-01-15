import pytest
from solution import validate_isbn


@pytest.mark.parametrize('isbn,result', [
    ('', False),
    ('12345', False),
    ('9780262038003', True),
    ('978026203800', False),
    ('9-7-8b0-2a6-2.0-3?8-0!0-3', True),
    ('9780262038002', False)])
def test_isbn(isbn, result):
    assert validate_isbn(isbn) == result
