import argparse
import socket
import time


def parse_args():
    parser = argparse.ArgumentParser(description="SMTP VRFY enumeration script")

    parser.add_argument("TARGET", help="Target IP or hostname")
    parser.add_argument("DOMAIN", help="Domain to use in EHLO")
    parser.add_argument("WORDLIST", help="Path to user wordlist")

    parser.add_argument(
        "-p", "--port",
        type=int,
        default=25,
        help="SMTP port (default: 25)"
    )

    parser.add_argument(
        "-d", "--delay",
        type=float,
        default=0.3,
        help="Delay between requests in seconds (default: 0.3)"
    )

    return parser.parse_args()


def recv_smtp_lines(f):
    lines = []

    while True:
        line = f.readline()
        if not line:
            break

        line = line.strip()
        lines.append(line)

        if len(line) >= 4 and line[3] == " ":
            break

    return "\n".join(lines)


def send_cmd(sock, f, cmd):
    sock.sendall((cmd + "\r\n").encode())
    return recv_smtp_lines(f)


def connect(target, port, domain):
    sock = socket.socket()
    sock.settimeout(10)
    sock.connect((target, port))

    f = sock.makefile("r", newline="\r\n")

    banner = recv_smtp_lines(f)
    print(f"[BANNER]\n{banner}\n")

    ehlo_resp = send_cmd(sock, f, f"EHLO {domain}")
    print(f"[EHLO]\n{ehlo_resp}\n")

    return sock, f


def main():
    args = parse_args()

    TARGET = args.TARGET
    PORT = args.port
    DOMAIN = args.DOMAIN
    WORDLIST = args.WORDLIST
    DELAY = args.delay

    valid_users = []

    with open(WORDLIST, "r") as f:
        users = [u.strip() for u in f if u.strip()]

    sock, f = connect(TARGET, PORT, DOMAIN)

    i = 0
    while i < len(users):
        user = users[i]

        try:
            resp = send_cmd(sock, f, f"VRFY {user}")

            if resp.startswith("421"):
                print(f"[!] Rate limit hit (421). Reconnecting...\n")
                sock.close()
                sock, f = connect(TARGET, PORT, DOMAIN)
                continue

            if resp.startswith("252") or resp.startswith("250"):
                print(f"[+] VALID: {user} --> {resp}")
                valid_users.append(user)
            else:
                print(f"[-] INVALID: {user} --> {resp}")

            i += 1
            time.sleep(DELAY)

        except (socket.timeout, ConnectionResetError, BrokenPipeError) as e:
            print(f"[!] Connection dropped ({e}). Reconnecting...\n")
            sock.close()
            sock, f = connect(TARGET, PORT, DOMAIN)

    try:
        quit_resp = send_cmd(sock, f, "QUIT")
        print(f"\n[QUIT]\n{quit_resp}")
    except:
        pass

    sock.close()

    print("=" * 25)
    print("Valid users:")
    for user in valid_users:
        print(f" - {user}")


if __name__ == "__main__":
    main()
