"""The Storetoise CLI."""

from argparse import ArgumentParser, Namespace
import string
import requests


BASE_URL = "http://sigma-storetoise-lb-698404422.eu-west-2.elb.amazonaws.com"


def valid_number(number: str | None) -> int | None:
    """Checks if input number is between 0 and 1000"""
    if number:
        if number.isdigit() and 0 < int(number) <= 1000:
            return int(number)

        print("Number must be an integer between 0 and 1000.")
    return None


def valid_storage(storage: str | None) -> int | None:
    """Checks if input storage is a 3-digit number"""
    if storage:
        if storage.isdigit() and len(storage) == 3:
            return int(storage)

        print("Storage ID must be a three-digit integer.")
    return None


def valid_message(message: str | None) -> str | None:
    """Checks if message is less than 140 letters and lowercase"""
    if message:
        if len(message) > 140:
            print("Message must be 140 characters or fewer.")
            return None

        for letter in message:
            if letter not in string.ascii_lowercase + " ":
                print("Message must consist only of lowercase letters and spaces.")
                return None

        return message
    return None


def load_storetoise_data(url: str) -> dict:
    """Returns the data from the Storetoise API"""
    response = requests.get(url, timeout=10)
    return response.json()


def add_message_to_storetoise(url: str, message: str) -> None:
    """Adds message to the Storetoise API to storage ID"""
    requests.post(url, json={"message": message}, timeout=10)


def delete_message(url: str) -> None:
    """Deletes storage ID from the Storetoise API"""
    requests.delete(url, timeout=10)


def list_storage_ids(data: dict, number: int | None = None) -> None:
    """Returns the ids stored in the username"""
    storage_ids = data["ids"]

    if number:
        limit = min(number, len(storage_ids))
        storage_ids = storage_ids[:limit]

    for storage_id in sorted(storage_ids):
        print(storage_id)


def display_messages(data: dict, storage: int) -> None:
    """Shows the messages in storage id"""
    messages = data.get("messages")

    if not messages:
        print(f"No messages found for storage ID {storage}.")
        return

    for num, message in enumerate(messages):
        print(f"{num}) {message}")


def command_line_args() -> Namespace:
    """Inputs from the command line"""
    parser = ArgumentParser(description="Storetoise CLI")

    parser.add_argument("--username", "-u", required=True,
                        help="Username for Storetoise")

    parser.add_argument("--number", "-n",
                        type=valid_number,
                        help="Limit the number of results")

    parser.add_argument("--storage", "-s",
                        type=valid_storage,
                        help="Storage ID number")

    parser.add_argument("--message", "-m",
                        type=valid_message,
                        help="Add message")

    parser.add_argument("--delete", "-d",
                        action="store_true",
                        help="Delete message")

    return parser.parse_args()


if __name__ == "__main__":
    args = command_line_args()

    user_url = f"{BASE_URL}/storage/{args.username}"
    ids_data = load_storetoise_data(user_url)

    list_storage_ids(ids_data, args.number)

    if args.storage:
        id_url = user_url + f"/{args.storage}"
        messages_data = load_storetoise_data(id_url)

        if args.message:
            if messages_data.get("messages") and len(messages_data["messages"]) == 10:
                print("Cannot add more than 10 messages to a storage ID.")
            else:
                add_message_to_storetoise(id_url, args.message)
                print(f"Message added to Storage ID {
                      args.storage} successfully.")

        if str(args.storage) in ids_data["ids"]:
            display_messages(messages_data, args.storage)
        else:
            print("Cannot get messages for a non-existent storage ID.")

        if args.delete:
            print(str(args.storage), ids_data["ids"])
            if str(args.storage) in ids_data["ids"]:
                delete_message(id_url)
                print(f"Storage ID {args.storage} deleted successfully.")
            else:
                print("Cannot delete a non-existent storage ID.")
