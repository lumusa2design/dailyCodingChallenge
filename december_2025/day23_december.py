"""Re: Fwd: Fw: Count

Given a string representing the subject line of an email, determine how many times the email has been forwarded or replied to.

For simplicity, consider an email forwarded or replied to if the string contains any of the following markers (case-insensitive):

    "fw:"
    "fwd:"
    "re:"

Return the total number of occurrences of these markers.
"""

def email_chain_count(subject):
    markers = ["fw:", "fwd:", "re:"]
    subject_lower = subject.lower()
    count = 0

    for marker in markers:
        count += subject_lower.count(marker)

    return count