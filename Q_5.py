def valid_url(url):
    """
    Check if a string is a valid URL.

    :param url: string representing the URL
    :return: True if valid, False if its not a valid URL
    """

    if url.startswith("http://"):
        domain = url[7:]
    elif url.startswith("https://"):
        domain = url[8:]
    else:
        return False

    if "." not in domain:
        return False

    parts = domain.split(".")

    if len(parts[0]) == 0 or len(parts[-1]) == 0:
        return False

    return True

print(valid_url("https://google.com"))