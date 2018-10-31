"""
Unit and regression test for the sermacs_workshop package.
"""

# Import package, test suite, and other packages as needed
import sermacs_workshop as su
import pytest
import sys

def test_title_case():
    """Sample test, will always pass so long as import statement worked"""
    title = 'FunCTIon tEsT'
    title = su.title_case(title)
    assert title == 'Function Test'

@pytest.mark.skip
def test_type_error():
    title = ['hi','there']
    with pytest.raises(TypeError):
        title = su.title_case(title)

def test_empty_str():
    title = ''
    title = su.title_case(title)
    assert title == ''
