from drunken_bishop import drunken_bishop


def test_drunken_bishop():
    fingerprint = "37e46a2d48381a0af3726dd9176bbd5e"
    expected_art = """+-----------------+
|                 |
|                 |
|          .      |
|     .   o       |
|o . o . S +      |
|.+ + = . B .     |
|o + + o B o E    |
| o .   + . o     |
|         .o      |
+-----------------+
"""
    assert drunken_bishop(fingerprint) == expected_art
