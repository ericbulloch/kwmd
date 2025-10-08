import argparse


def main(args):
    with open(args.shell_path, 'r') as fp:
        text = fp.read()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A script create multiple reverse shell files')
    parser.add_argument('host', help='The host name of the attacker machine.')
    parser.add_argument('port', help='The port of the attacker machine.')
    parser.add_argument('--shell_path', type=str, default='/usr/share/webshells/php/php-reverse-shell.php', help='The path of the original shell')
    args = parser.parse_args()
    main(args)
