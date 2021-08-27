from . import validators
page_register_mapper = {
    'submit': validators.email_validation,
    'verify': validators.code_verification_validator
}
