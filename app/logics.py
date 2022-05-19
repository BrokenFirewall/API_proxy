import log


def check_name(name):
    if not name.replace(" ", "").isalpha():
        raise Exception("Input name is invalid")


def define_most_probable(list_county):
    try:
        log.log_info("initialize the variable to determine the greatest probability")
        most_probable_country = {'probability': 0}
        log.log_info("determine the greatest probability")
        for country in list_county:
            if country['probability'] > most_probable_country['probability']:
                most_probable_country = country
        return most_probable_country
    except Exception as e:
        raise Exception(e)


def define_out_message(most_probable_country, name, country_name):
    if most_probable_country < 0.3:
        return "It seems that " + name.capitalize() + " is from " + country_name + ". But I'm just guessing!"
    elif 0.3 < most_probable_country < 0.6:
        return name.capitalize() + " may be from " + country_name
    else:
        return name.capitalize() + " is mostly certain to be from " + country_name
