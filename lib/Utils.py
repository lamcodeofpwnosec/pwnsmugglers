import json
import os
from urllib.error import URLError

from termcolor import cprint, colored
from pyfiglet import figlet_format
from urllib.parse import urlparse
from .Constants import Constants
import colorama

colorama.init()


class Utils:
    def __init__(self):
        self.title = "{:<1}{}".format("", "PwnSmugglers")
        self.author = "PwnOsec Research / @lamcodeofpwnosec"
        self.blog = "https://www.pwn0sec.com/blog/pwnsmugglers-detection-tool"
        self.version = "0.1"

    def print_header(self):
        cprint(figlet_format(self.title.center(20), font='cybermedium'), 'blue', attrs=['bold'])

        header_key_color = Constants().blue
        header_value_color = Constants().yellow

        print("{:<12}{:<23}{:<17}{}".format('', colored('Author', header_key_color, attrs=['bold']),
                                            colored(':', header_key_color, attrs=['bold']),
                                            colored(self.author, header_value_color, attrs=['bold'])))
        print("{:<12}{:<23}{:<17}{}".format('', colored('Blog', header_key_color, attrs=['bold']),
                                            colored(':', header_key_color, attrs=['bold']),
                                            colored(self.blog, header_value_color, attrs=['bold'])))
        print("{:<12}{:<23}{:<17}{}".format('', colored('Version', header_key_color, attrs=['bold']),
                                            colored(':', header_key_color, attrs=['bold']),
                                            colored(self.version, header_value_color, attrs=['bold'])))
        print("{:<1}{}".format('', colored(
            "___________________________________________________________________________________", 'cyan',
            attrs=['bold'])))
        print("\n")

    @staticmethod
    def write_payload(file_name, payload):
        if not os.path.exists(os.path.dirname(file_name)):
            try:
                os.makedirs(os.path.dirname(file_name))
            except OSError as e:
                print(e)
        with open(file_name, "wb") as f:
            f.write(bytes(str(payload), 'utf-8'))

    @staticmethod
    def url_parser(url):
        parser = {}
        try:
            port = 80
            u_parser = urlparse(url)
            if u_parser.scheme == 'https':
                port = 443
            if u_parser.port is not None:
                port = u_parser.port

            host = u_parser.hostname
            parser["host"] = host
            parser["port"] = port

            path = u_parser.path
            query = '?' + u_parser.query if u_parser.query else ''
            fragment = '#' + u_parser.fragment if u_parser.fragment else ''
            uri_path = f'{path}{query}{fragment}'

            if len(path) > 0:
                parser["path"] = uri_path
            else:
                parser["path"] = '/'
            return json.dumps(parser)
        except URLError as e:
            print(f'Invalid URL: {e}')
            return Constants().invalid_target_url

    @staticmethod
    def read_target_list(file_name):
        try:
            with open(file_name) as urls_list:
                return [u.rstrip('\n') for u in urls_list]
        except FileNotFoundError as _:
            return Constants().file_not_found
