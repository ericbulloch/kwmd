import argparse
from subprocess import call


def main(args):
    host = args.host.strip().lower()
    file_name = args.file_name.strip()
    speed = args.speed.strip()
    ports = args.ports.strip()
    command = f'nmap -T{speed} -n -sC -sV -Pn -v0 -p{ports} {host} -oX {file_name}.xml -oN {file_name}.txt'
    call(command, shell=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A script to run an nmap scan')
    parser.add_argument('host', help='The host name of the attacker machine.')
    parser.add_argument('--file-name', type=str, default='nmap', help='The base file name where the scan will be stored. Defaults to "nmap".')
    parser.add_argument('--speed', type=int, default=4, choices=range(1, 6), help='The speed of the nmap scan on a scale of 1-5, with 5 being the fastest. Defaults to 4.')
    parser.add_argument('--ports', type=str, default='-', help='What ports to scan. Defaults to "-" which is all ports.')
    args = parser.parse_args()
    main(args)
