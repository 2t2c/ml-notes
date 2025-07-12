import re

def on_page_markdown(markdown, page, config, files):
    # pattern matches from the heading ## Section or # Chapters until the end of file
    pattern = r'^(#{1,2})\s+\**(Sections|Chapters)\**.*$(.|\n)*'

    # remove everything from that heading to the end
    cleaned = re.sub(pattern, '', markdown, flags=re.MULTILINE)
    return cleaned