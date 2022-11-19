import socket


def get_ip_by_url():
    url = input("Enter URL (just copy it from your browser address line) >>> ")
    clear_url = url[8:-1]
    try:
        if 'https://' in url:
            return f'URL : {clear_url}\nIP address: {socket.gethostbyname(clear_url)}'
        else:
            return f'{url} - is incorrect URL, please, copy it from address line!'
    except socket.gaierror:
        return f'Incorrect URL - {url}'


def main():
    print(get_ip_by_url())


if __name__ == "__main__":
    main()