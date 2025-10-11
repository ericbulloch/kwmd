import argparse
from ftplib import FTP


def main(args):
    print(f'ftp_handler called for port {args.port}')
    ftp = FTP()
    try:
        ftp.connect(args.host, args.port, timeout=args.timeout)
        ftp.login(user='anonymous', passwd='me@me.com')
        ftp.set_pasv(True)
        files = ftp.nlst()
        ftp.quit()
        print('Anonymous login successful. Here are the files on the ftp server:')
        for file in files:
            print(file)
    except Exception as e:
        print(f'FTP error: {e}', file=sys.stderr)
    finally:
        try:
            ftp.quit()
        except Exception:
            try:
                ftp.close()
            except Exception:
                pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A script to log into ftp with anonymous user and show the contents of all files')
    parser.add_argument('host', help='The host name of the attacker machine.')
    parser.add_argument('--port', type=int, default=21, help='The port of the attacker machine.')
    parser.add_argument('--timeout', type=int, default=10, help='The default timeout in seconds to connect.')
    args = parser.parse_args()
    main(args)
