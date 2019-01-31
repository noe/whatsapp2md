#!/usr/bin/env python3

# Copyright (c) 2019-present, Noe Casas
# All rights reserved.
#
# This source code is licensed under the license found in the LICENSE file in
# the root directory of this source tree.


import argparse
from datetime import datetime
from typing import List, Iterable, Tuple, Optional


class Entry:
    """
    Collects the data associated with a whatsapp message.
    """

    def __init__(self, timestamp: datetime, sender: str, text: str, image: str):
        """
        Constructor.
        :param timestamp: Timestamp for the whatsapp message.
        :param sender: sender of the whatsapp message.
        :param text: text of the message.
        :param image: image in the message.
        """
        self.timestamp = timestamp
        self.sender = sender
        self.text = text
        self.image = image

    def format_md(self, show_timestamp: bool=True, show_sender: bool=False):
        """
        Formats the entry as a piece of markdown text.
        :param show_timestamp: whether to show the timestamp of the entry.
        :param show_sender: whether to show the sender of the message.
        :return: markdown-formatted text of the entry.
        """
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


def parse_timestamp(line: str) -> Tuple[Optional[datetime], str]:
    """
    Extracts the leading timestamp of a chat line
    :param line: Line to parse
    :return: a tuple with the timestamp (if any) and the rest of the line.
    """
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
    """
    Extracts the sender of a line (the timestamp should already be removed)
    :param line: Line to parse.
    :return: a tuple with the sender (if any) and the rest of the line.
    """
    if ':' not in line:
        return "", line   # It's a system message

    sender, rest_of_line = line.split(':', 1)
    rest_of_line = rest_of_line[1:]  # remove leading space
    return sender, rest_of_line


def parse_entry(line:str, timestamp: datetime, sender: str) -> Entry:
    """
    Extracts an entry from a line and the previously extracted info.
    :param line: Line with the message (without timestamp or sender)
    :param timestamp: timestamp for the entry.
    :param sender: sender for the entry.
    :return: newly created Entry from the given line.
    """
    if line.startswith('\u200e'):
        image, _ = line[1:].split(' ', 1)
        return Entry(timestamp, sender, None, image)
    else:
        return Entry(timestamp, sender, line, None)


def parse_lines(lines: Iterable[str]) -> List[Entry]:
    """
    Parses the lines in a whatsapp chat export.
    :param lines: lines to prse.
    :return: list of entries.
    """
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
    parser = argparse.ArgumentParser('Whatsapp chat export parser into markdown')
    parser.add_argument('chat_file', help='Chat text file')
    parser.add_argument('--hide-days', action='store_true', help='Hides the day headers')
    parser.add_argument('--show-sender', action='store_true', help='Shows the sender of each message')
    parser.add_argument('--hide-timestamp', action='store_true', help='Hides message timestamps')
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
