from __future__ import annotations

import argparse
import sys
import re

JIRA_REGEX = "(\w+)-(\d+)"

def main():
    args = sys.argv
    if len(sys.argv) < 2:
        print("Invalid number of arguments")
        sys.exit(1)

    file = open(sys.argv[1])
    for line in file.readlines():
        line = line.strip()
        temp = re.match(JIRA_REGEX, line)
        if temp:
            print("Validated presence of jira id: %s in commit" % (temp.group(0)))
            sys.exit(0)

    print("Jira identifier not found. Git Commit Message should start with Jira id like, "
          "<JIRA ID>: <Commit Message>")
    sys.exit(1)


if __name__ == "__main__":
    raise SystemExit(main())
