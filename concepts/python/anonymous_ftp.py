from ftplib import FTP


def ftp_handler(host, port):
    print(f'ftp_handler called for port {port}')
    try:
        ftp = FTP(host, port)
        ftp.login()
        files = ftp.nlst()
        ftp.quit()
        print('Anonymous login successful. Here are the files on the ftp server:')
        for file in files:
            print(file)
    except Exception:
        pass
