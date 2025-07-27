import requests

def find_text(text, first, last):
    left = text.index(first) + len(first)
    right = left + text[left:].index(last)
    return text[left:right]