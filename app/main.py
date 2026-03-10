import argparse
from app.config import config

def main():

    print("Weather CLI iniciado")

    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest="command")

    addcidade = subparser.add_parser("add")
    addcidade.add_argument("--cidade", required=True)

    listcidade = subparser.add_parser("list")

    removecidade = subparser.add_parser("remove")
    removecidade.add_argument("--id", required=True, type=int)

    weather = subparser.add_parser("weather")
    weather.add_argument("--cidade", required=True, type=str)

    search = subparser.add_parser("search")

    args = parser.parse_args()

    if args.command == "add":
        config.add(args.cidade)

    elif args.command == "list":
        config.list()

    elif args.command == "remove":
        config.delete(args.id)

    elif args.command == "weather":
        config.tempo(args.cidade)

    elif args.command == "search":
        config.historic()

if __name__ == "__main__":
    main()