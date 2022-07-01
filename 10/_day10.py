def format_name(first_name, second_name):
    """Take the first and last name and capitalize it"""
    # Docstring: Cuando se escriba format_name() aparecera este string de ayuda del metodo
    if first_name == "" or second_name == "":
        return "Invalid inputs"
    formated_first_name = first_name.title()
    formated_second_name = second_name.title()
    return f"Formated name: {formated_first_name} {formated_second_name}"


print(format_name(input("First Name: "),input("Second Name")))

