"""Given a multi-line string that uses newline characters (\n) to represent a line break, return a new string where each line is mirrored horizontally and attached to the end of the original line.

    Mirror a line by reversing all of its characters, including spaces.

For example, given "* \n *\n* ", which logs to the console as:

* 
 *
* 

Return "*  *\n ** \n*  *", which logs to the console as:

*  *
 ** 
*  *

Take careful note of the whitespaces in the given and returned strings. Be sure not to trim any of them"""

def generate_snowflake(crystals):
    lines = crystals.split('\n')
    mirrored_lines = [line + line[::-1] for line in lines]
    return '\n'.join(mirrored_lines)