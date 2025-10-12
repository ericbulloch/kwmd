import argparse
from xml.etree import ElementTree


def main(args):
    tree = ElementTree.parse(args.filename)
    root = tree.getroot()
    services = []
    ports = root.find('host').find('ports').findall('port')
    for port in ports:
        number = port.get('portid')
        service = port.find('service')
        name = service.get('name')
        product = service.get('product')
        version = service.get('version')
        services.append(dict(port=number, service=name, product=product, version=version))
    return services


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A script parse an nmap scan and get services.")
    parser.add_argument("ip_address", help="The nmap scan file")
    args = parser.parse_args()
    main(args)
