import logging

# refer to sqlmap third-party


class colorizing_stream_handler(logging.StreamHandler):
    # color names to indices
    color_map = {
        'black': 0,
        'red': 1,
        'green': 2,
        'yellow': 3,
        'blue': 4,
        'magenta': 5,
        'cyan': 6,
        'white': 7,
    }

    effect_map = {
        'default': '0',
        'highlight': '1',
        'underline': '4',
        'blink': '5',
        'inverse': '7',
        'invisible': '8'
    }

    # levels to (background, foreground, bold/intense)
    level_map = {
        logging.DEBUG: (None, 'cyan', None),
        logging.INFO: (None, 'green', None),
        logging.WARNING: (None, 'yellow', None),
        logging.ERROR: (None, 'red', None),
        logging.CRITICAL: ('red', 'white', None)
    }

    csi = '\x1b['
    reset = '\x1b[0m'

    def colorize(self, message, record):
        if record.levelno in self.level_map:
            bg, fg, effect = self.level_map[record.levelno]
            params = self.csi

            if bg in self.color_map:
                params += str(self.color_map[bg] + 40) + ';'

            if fg in self.color_map:
                params += str(self.color_map[fg] + 30) + ';'

            if effect in self.effect_map:
                params += self.effect_map[effect] + ';'

            params += 'm'

            if params and message:
                if message.lstrip() != message:
                    prefix = re.search(r"\s+", message).group(0)
                    message = message[len(prefix):]
                else:
                    prefix = ""

                # message = "%s%s" % (prefix, ''.join((self.csi, ';'.join(params),
                    # 'm', message, self.reset)))
                message = message.replace("$CSI", params)
                message = message.replace("$RESET", self.reset)

        return message

    def format(self, record):
        message = logging.StreamHandler.format(self, record)
        return self.colorize(message, record)
