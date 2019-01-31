# whatsapp2md

Parses whatsapp chat exports and generates a document.

You can export a whatsapp chat by means of option
_More → Export Chat_ in the char's menu, and choose
to send it by email to yourself (including images).

This gives you a text file with the messages in the
chat plus a number of image files (whatsapp2md does
not support other type of documents).

This simple python script can take the whatsapp chat
export and generate a markdown file (.md) with
the contents of the chat.

You can then use your favourite markdown viewer to
print the it to PDF to get a self-contained document
that you can archive or share.


# Technical details

`whatsapp2md` is a python3 script with no dependencies.
Just clone the repository and invoke it, passing the
chat text file as command line argument.

```
python3 whatsapp2md.py ../chat/chat.txt > ../chat/chat.md
```

The complete command line interface can be checked
invoking it with `--help`:

```
usage: Whatsapp chat export parser into markdown [-h] [--hide-days]
                                                 [--show-sender]
                                                 [--hide-timestamp]
                                                 chat_file

positional arguments:
  chat_file         Chat text file

optional arguments:
  -h, --help        show this help message and exit
  --hide-days       Hides the day headers
  --show-sender     Shows the sender of each message
  --hide-timestamp  Hides message timestamps
```

# FAQ

### Why my markdown file does not show my images?

`whatsapp2md` assumes your image files are in the same
directory as the markdown file. Probably your .md file
is in a different folder than the images.

### My chat text file is not properly parsed, what to do?

Whatsapp chat exports use different formats for
dates and times depending on your phone configuration.
Most probably `whatsapp2md` does not support your
configuration. Open an issue with an example chat export
text file along with information about which language
your phone is configured in. We will try to support it.
