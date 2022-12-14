import re

# Minimum password length
MIN_LENGTH = 8

# Regex pattern to match common sequences and repetitions
# such as "abcdefg" or "123321"
SEQUENCE_PATTERN = re.compile(r'(.)\1{2,}')

def test_password_strength(password):
  # Test the password length
  if len(password) < MIN_LENGTH:
    print('Password is too short')
    return

  # Test for common sequences and repetitions
  if SEQUENCE_PATTERN.search(password):
    print('Password is too predictable')
    return

  # Password passed all tests
  print('Password is strong')

# Prompt the user for a password
password = input('Enter a password: ')

# Test the password strength
test_password_strength(password)
