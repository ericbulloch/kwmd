import argparse
from ftplib import FTP


def main(args):
    print(f'ftp_handler called for port {args.port}')
    ftp = FTP()
    try:
        ftp.connect(args.host, args.port, timeout=args.timeout)
        ftp.login(user='anonymous', passwd='me@me.com')
        ftp.set_pasv(True)
        print('Anonymous login successful.')
        walk(ftp, '.')
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


def walk(ftp, path, indent=0):
    print('Walking FTP server.')
    prefix = ' ' * indent
    entries = []

    try:
        entries = list(ftp.mlsd(path))
    except (error_perm, AttributeError):
        # MLSD not available; fall back to LIST parsing
        lines = []
        # Try to include hidden files with LIST -a, but not all servers accept "-a"
        for cmd in (f'LIST -a {path}', f'LIST {path}'):
            try:
                ftp.retrlines(cmd, lines.append)
                break
            except all_errors:
                lines.clear()
        # leading 'd' indicates directory
        for line in lines:
            parts = line.split(maxsplit=8)
            if len(parts) >= 9:
                name = parts[8]
            else:
                # fallback: last token
                name = parts[-1] if parts else ''
            is_dir = line.startswith('d')
            type = 'dir' if is_dir else 'file'
            entries.append((name, {'type': type}))

    # Process entries
    for name, facts in entries:
        if name in ('.', '..') or name == '':
            continue

        remote_path = name if path in ('.', '') else f"{path.rstrip('/')}/{name}"
        type = facts.get('type', '').lower()  # 'file' or 'dir' for MLSD

        if type == 'dir' or type == 'cdir' or type == 'pdir':
            print(f"{prefix}[DIR] {remote_path}")
            # recurse into directory. Wrap in try to continue on error.
            try:
                walk(ftp, remote_path, indent=indent + 2)
            except all_errors as e:
                print(f"{prefix}  (skipping directory {remote_path}: {e})", file=sys.stderr)
        else:
            print(f"{prefix}[FILE] {remote_path}")
            print_file_content(ftp, remote_path, indent=indent + 2)


def print_file_contents(ftp, remote_path, indent=0):
    prefix = ' ' * indent
    buf = io.BytesIO()
    downloaded = 0

    def _binary_callback(chunk):
        nonlocal downloaded
        buf.write(chunk)
        downloaded += len(chunk)

    try:
        ftp.retrbinary(f"RETR {remote_path}", _binary_callback)
    except Exception as e:
        print(f"{prefix}(error while retrieving {remote_path}: {e})", file=sys.stderr)

    # Display content: attempt to decode as UTF-8 (replace errors), but if looks binary, note that.
    data = buf.getvalue()
    if not data:
        print(f"{prefix}(empty file or could not read content)")
        return

    # Heuristic: if there are many null bytes, consider it binary
    null_ratio = data.count(b'\x00') / max(1, len(data))
    if null_ratio > 0.02:
        print(f"{prefix}(binary file, {len(data)} bytes downloaded; not printing binary content)")
        return

    try:
        text = data.decode('utf-8', errors='replace')
    except Exception:
        text = data.decode('latin1', errors='replace')

    # Print text content with indentation
    for line in text.splitlines():
        print(f"{prefix}{line}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A script to log into ftp with anonymous user and show the contents of all files')
    parser.add_argument('host', help='The host name of the attacker machine.')
    parser.add_argument('--port', type=int, default=21, help='The port of the attacker machine.')
    parser.add_argument('--timeout', type=int, default=10, help='The default timeout in seconds to connect.')
    args = parser.parse_args()
    main(args)
