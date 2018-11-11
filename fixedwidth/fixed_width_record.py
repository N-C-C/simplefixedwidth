def slices(s, *args):
    """
    Slices a string 's' in segments 'args' wide.
    Negative widths represent ignored padding fields.
    :param s: string
    :param args: list of widths for the string
    :return: yields string 's' in a list
    """
    position = 0
    for length in args:
        if length > 0:
            yield s[position:position + length]
        position += abs(length)


def get_line(string, rec_type_start=-1, rec_type_end=-1):
    rec_identifier = ""
    if rec_type_start >= 0 and rec_type_end > 0:
        rec_identifier = string[17:19]
    return rec_identifier, string
