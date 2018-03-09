# http://www.practicepython.org/exercise/2014/05/28/16-password-generator.html

import string
import random

alphabet = string.ascii_letters + string.digits + string.punctuation

length = int(input('Please provide desired password length: '))

# https://docs.python.org/3/library/secrets.html#module-secrets
# Generate a ten-character alphanumeric password with
# at least one lowercase character,
# at least one uppercase character, and
# at least three digits:
while True:
    password = ''.join(random.choice(alphabet) for i in range(length))
    if (any(letter.islower() for letter in password)
            and any(letter.isupper() for letter in password)
            and sum(letter.isdigit() for letter in password) >= 3):
        break

print(password)