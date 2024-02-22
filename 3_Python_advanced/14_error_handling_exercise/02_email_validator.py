class NameTooShortError(Exception):
    pass


class NameTooLongError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneSymbol(Exception):
    pass


class InvalidNameError(Exception):
    pass


ALLOWED_USERNAME_SPECIAL_CHR = ['_', '.', '-']
ALLOWED_DOMAIN_SPECIAL_CHR = ['-']
VALID_DOMAINS = ('com', 'bg', 'org', 'net')
MIN_USERNAME_LENGTH = 4
MAX_USERNAME_LENGTH = 20
MAX_DOMAIN_LENGTH = 10
MAX_EMAIL_CHR = 30

user_email = input()

while user_email != 'End':

    if len(user_email) > MAX_EMAIL_CHR:
        raise NameTooLongError('This Email exceeds the maximum allowed length.')

    elif ' ' in user_email:
        raise InvalidNameError('Email cannot contain spaces.')

    if user_email.count('@') > 1:
        raise MoreThanOneSymbol('Your Email should contain only one @ symbol.')

    elif '@' not in user_email:
        raise MustContainAtSymbolError("Email must contain @ symbol.")

    user_name, domain = user_email.split('@')
    domain_parts = domain.split('.')

    if len(user_name) > MAX_USERNAME_LENGTH:
        raise InvalidNameError('Username exceeds the maximum allowed length.')

    elif len(domain) > MAX_DOMAIN_LENGTH:
        raise InvalidDomainError('Domain exceeds the maximum allowed length.')

    elif len(user_name) <= MIN_USERNAME_LENGTH:
        raise NameTooShortError('Name must be more than 4 characters.')

    elif domain_parts[-1] not in VALID_DOMAINS:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join('.' + d for d in VALID_DOMAINS)}.")

    elif not all(char.isalnum() or char in ALLOWED_USERNAME_SPECIAL_CHR for char in user_name):
        raise InvalidNameError('Invalid characters in the username part of the email.')

    elif domain_parts[0].startswith('.') or domain_parts[0].endswith('.'):
        raise InvalidDomainError('Domain cannot start or end with a dot.')

    elif user_name.startswith('.') or user_name.endswith('.'):
        raise InvalidDomainError('Username cannot start or end with a dot.')

    elif any(any(char not in ALLOWED_DOMAIN_SPECIAL_CHR and not char.isalnum() for char in part) for part in
             domain_parts):
        raise InvalidDomainError('Invalid characters in the domain part of the email.')

    elif any(part.startswith('-') or part.endswith('-') or '..' in part or '__' in part or '--' in part for part in
             domain_parts):
        raise InvalidDomainError('Consecutive dots, hyphens, or underscores in the domain are not allowed.')

    elif (user_name.startswith('-') or user_name.endswith('-') or '..' in user_name or '__' in user_name or '--' in
          user_name):
        raise InvalidDomainError('Consecutive dots, hyphens, or underscores in the Username are not allowed.')

    print('Email is valid!\nType in email to validate or type "End" to exit.')

    user_email = input()
