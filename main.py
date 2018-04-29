from models import User
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username",
                        help="nazwa uzytkownika",
                        required=True)
    parser.add_argument("-p", "--password",
                        help="haslo uzytkownika",
                        required=True)
    parser.add_argument("-l", "--list",
                        help="wypisuje komunikaty dla uzytkownika",
                        action="store_true")
    parser.add_argument("-t", "--to", help="odbiorca wiadomosci")
    parser.add_argument("-s", "--send",
                        help="wysyla komunikat",
                        action="store_true")
    args = parser.parse_args()

    user = args.username
    password = args.password
    listing_mode = args.list
    sending_mode = args.send
    recipient = args.to
    print(User)
    print("""
        uzytkownik: {}
        password: {}
        list mode: {}
        send mode: {}
        recipient: {}
    """.format(user, password, listing_mode, sending_mode, recipient))


if __name__ == '__main__':
    main()

