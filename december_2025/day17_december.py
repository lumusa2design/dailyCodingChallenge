"""Markdown Blockquote Parser

Given a string that includes a blockquote in Markdown, return the equivalent HTML string.

A blockquote in Markdown is any line that:

    Starts with zero or more spaces
    Followed by a greater-than sign (>)
    Then, one or more spaces
    And finally, the blockquote text.

Return the blockquote text surrounded by opening and closing HTML blockquote tags.

For example, given "> This is a quote", return <blockquote>This is a quote</blockquote>.

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.
"""

def parse_blockquote(markdown):
    lines = markdown.splitlines()
    blockquote_lines = []

    for line in lines:
        stripped = line.lstrip()

        if stripped.startswith('>'):
            rest = stripped[1:] 
            if len(rest) > 0 and rest[0].isspace():
                blockquote_lines.append(rest.lstrip())

    if blockquote_lines:
        return "<blockquote>" + "\n".join(blockquote_lines) + "</blockquote>"

    return markdown
