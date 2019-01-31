#!/usr/bin/env python3
import argparse
from datetime import datetime
from typing import List, Iterable, Tuple, Optional


def parse_timestamp(line: str) -> Tuple[Optional[datetime], str]:
    if '-' not in line:
        return None, line  # Not a proper date

    date_time, rest_of_line = line.split('-', 1)
    datetime_format = '%d/%m/%y %H:%M '
    try:
        t = datetime.strptime(date_time, datetime_format)
        rest_of_line = rest_of_line[1:]  # remove leading space
        return t, rest_of_line
    except ValueError:
        return None, line  # Not a proper date


def parse_sender(line: str) -> Tuple[str, str]:
    if ':' not in line:
        return "", line   # It's a system message

    sender, rest_of_line = line.split(':', 1)
    rest_of_line = rest_of_line[1:]  # remove leading space
    return sender, rest_of_line


def parse_entry(line:str, timestamp: datetime, sender: str):
    if line.startswith('\u200e'):
        image, _ = line[1:].split(' ', 1)
        return Entry(timestamp, sender, None, image)
    else:
        return Entry(timestamp, sender, line, None)


class Entry:
    def __init__(self, timestamp, sender, text, image):
        self.timestamp = timestamp
        self.sender = sender
        self.text = text
        self.image = image

    def format_md(self, show_timestamp=True, show_sender=False):
        formatted_sender = '`{}`'.format(self.sender)
        formatted_timestamp = '`{}`'.format(self.timestamp.strftime('%H:%M'))
        formatted_image = ('' if self.image is None
                           else '![{}]({} "{}")'.format(self.image, self.image, self.text))
        formatted_text = '{}'.format(self.text)

        result = ''
        if show_timestamp:
            result += formatted_timestamp + ' '
        if show_sender:
            result += formatted_sender + ' '

        if self.image is not None:
            result += '\n' + formatted_image
        else:
            result += formatted_text

        return result + '\n'


def parse_lines(lines: Iterable[str]) -> List[Entry]:
    entries = []
    for lineno, line in enumerate(lines, 1):
        line = line.strip()

        timestamp, line = parse_timestamp(line)

        if not timestamp:
            # this line is continuation of a previous one
            if not entries or entries[-1].text is None:
                msg = "Malformed file: line {} is a continuation of no previous line"
                raise ValueError(msg.format(lineno))

            entries[-1].text += '\n' + line
            continue

        sender, line = parse_sender(line)
        entry = parse_entry(line, timestamp, sender)
        entries.append(entry)

    return entries


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('chat_file')
    parser.add_argument('--hide-days', action='store_true')
    parser.add_argument('--show-sender', action='store_true')
    parser.add_argument('--hide-timestamp', action='store_true')
    args = parser.parse_args()
    with open(args.chat_file) as f:
        entries = parse_lines(f)

    last_day = None
    for entry in entries:
        entry_day = '{}/{}/{}'.format(entry.timestamp.year,
                                      entry.timestamp.month,
                                      entry.timestamp.day)

        if not args.hide_days and last_day != entry_day:
            print('## {}'.format(entry_day))

        print(entry.format_md(show_sender=args.show_sender,
                              show_timestamp=not args.hide_timestamp))

        last_day = entry_day


if __name__ == '__main__':
    main()
