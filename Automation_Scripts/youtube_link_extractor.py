import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    s=s.strip().replace(" ","")
    if matches := re.search(r'^<iframe(?:width="\d*")?(?:height="\d*")?src="(?:https?://)?(?:www\.)?(youtube\.com/embed/[a-z0-9]+)"(?:title=".*")?(?:frameborder="\d*")?(?:allow=".*")?(?:allowfullscreen)?></iframe>$', s, re.IGNORECASE):
        link=matches.group(1)
        link=link.replace("youtube.com/embed", "")
        link="https://youtu.be"+link
        return link
    else:
        return None
# '^(?:<iframe)(?:.+)?(?:https?://)?(?:www\.)?(?:src=)("youtube\.com/embed/[.]+")(?:.+)?(?:</iframe>)$'
#<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
#<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>

if __name__ == "__main__":
    main()

# check50 cs50/problems/2022/python/watch
# submit50 cs50/problems/2022/python/watch
