"""Given a string representing an ordered list item in Markdown, return the equivalent HTML string.

A valid ordered list item in Markdown must:

    Start with zero or more spaces, followed by
    A number (1 or greater) and a period (.), followed by
    At least one space, and then
    The list item text.

If the string doesn't have the exact format above, return "Invalid format". Otherwise, wrap the list item text in li tags and return the string.

For example, given "1. My item", return "<li>My item</li>".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included"""
import re

def convert_list_item(markdown):
    markdown = markdown.lstrip()
    match = re.match(r'^(\d+)\.\s+(.+)$', markdown)
    if not match:
        return "Invalid format"
    number, text = match.groups()
    if int(number) < 1:
        return "Invalid format"
    return f"<li>{text}</li>"