def book_validate(author, email, text):
    errors = {}
    if not author:
        errors["author"] = "Поле обязательное"
    elif len(author) > 50:
        errors["author"] = "Максимальная длина 50 символов"

    if not email:
        errors["email"] = "Поле обязательное"
    elif len(email) > 20:
        errors["email"] = "Максимальная длина 2000 символов"

    if not text:
        errors["text"] = "Поле обязательное"
    elif len(text) > 2000:
        errors["text"] = "Максимальная длина 50 символов"

    return errors