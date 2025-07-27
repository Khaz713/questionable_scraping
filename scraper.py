def find_text(text, first, last):
    left = text.index(first) + len(first)
    right = left + text[left:].index(last)
    return text[left:right], text[right:]


def get_title(text):
    return find_text(text, "<title>", "</title>")


def get_chapters_number(text):
    return find_text(text, '<span class="">Statistics (', " threadmarks")


def get_chapter_title(text):
    span, cut_off = find_text(text, '<div class="message-cell message-cell--threadmark-header">', '</span>')
    return span.split(">")[-1], cut_off


def get_chapter(text):
    return find_text(text, '<div class="bbWrapper">',
                     '<div class="js-selectToQuoteEnd">&nbsp;</div>')
