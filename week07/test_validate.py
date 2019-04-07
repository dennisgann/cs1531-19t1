from validate import UserInputError, validate_user_name
import pytest

def test_validate_correct_input():
    input = "apple345"
    assert validate_user_name(input) == True

def test_validate_empty_user_name():
    input = ""
    with pytest.raises(UserInputError) as ex:
        validate_user_name(input)
    assert 'invalid username' in str(ex.value)

def test_validate_incorrect_length():
    input = "somereallyreallylongusername"
    with pytest.raises(UserInputError) as ex:
        validate_user_name(input) 
    assert 'invalid username' in str(ex.value)

def test_validate_space():
    input = "appl 345"
    with pytest.raises(UserInputError) as ex:
        validate_user_name(input) 
    assert 'invalid username' in str(ex.value)

