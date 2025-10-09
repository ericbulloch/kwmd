import argparse
import datetime


def get_host_file():
    with open('/etc/hosts', 'r') as fp:
        lines = [l.strip() for l in fp.readlines()]
    return lines


def process_host_file(target_ip, target_host, lines):
    new_lines = []
    messages = []
    for line in lines:
        if not line or line.startswith('#'):
            # blank or comment line
            new_lines.append(line)
            continue
        splits = line.split()
        if len(splits) < 2:
            # line that doesn't have the ip hostname format
            new_lines.append(line)
        ip = splits[0]
        hosts = [l.lower() for l in splits[1:]]
        if target_host in hosts:
            if target_ip == ip:
                # already exists
                if 'already_exists' in messages:
                    # this line occurred more than once
                    continue
                messages.append('already_exists')
                new_lines.append(line)
            else:
                # hostname mapped to another ip address
                if len(hosts) > 1:
                    hosts.remove(target_host)
                    messages.append('removed')
                    new_lines.append(f'{ip}   {" ".join(hosts)}')
                else:
                    # the ip address only had this hostname
                    messages.append('removed')
        else:
            new_lines.append(line)
    return messages, new_lines


def main(ip, host, dry_run):
    lines = get_host_file()
    messages, new_lines = process_host_file(ip, host, lines)
    # max length of ipv4 address (4 octets and 3 dots) plus one space
    max_length = 16
    spacing = ' ' * (max_length - len(ip))
    entry = f'{ip}{spacing}{host}'
    if 'already_exists' not in messages:
        new_lines.append(entry)
    else:
        print(f'"{entry}" already exists. Exiting...')
        exit()
    if 'removed' in messages:
        print('Another entry was found for this hostname. It has been removed')
    if dry_run:
        print('Dry run: no changes written')
        exit()

    print('Backing up the host file.')
    time_stamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    with open(f'hosts.bak.{time_stamp}', 'w') as fp:
        fp.writelines('\n'.join(lines))
    print('Done backing up the host file.')

    print('Writing new host file')
    with open('/etc/hosts', 'w') as fp:
        fp.writelines('\n'.join(new_lines))
    print('Done writing new host file')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Add/update an entry in the hosts file.")
    parser.add_argument("ip", help="IP address to map (e.g. 10.201.13.37)")
    parser.add_argument("--host", default='target.thm', help="Hostname to map, defaults to target.thm")
    parser.add_argument("--dry-run", action="store_true", help="Show actions but don't modify the hosts file")
    args = parser.parse_args()
    target_ip = args.ip.strip().lower()
    target_host = args.host.strip().lower()
    dry_run = args.dry_run
    main(target_ip, target_host, dry_run)
