"""Tests for challenge 1."""

# pylint: skip-file

import pytest


def test_delete_valid_storage_id(test_user, run_shell_command):

    output = run_shell_command(
        f"python3 storetoise_4.py --username {test_user} --storage 601 --delete")

    assert "Storage ID 601 deleted successfully." in output


def test_delete_valid_storage_id_short_names(test_user, run_shell_command):

    output = run_shell_command(
        f"python3 storetoise_4.py -u {test_user} -s 900 -d")

    assert "Storage ID 900 deleted successfully." in output


@pytest.mark.parametrize("inp", ["23", "2000", "-12", "-123", "knives"])
def test_delete_rejects_invalid_storage_id(test_user, run_shell_command, inp):

    output = run_shell_command(
        f"python3 storetoise_4.py --username {test_user} -s {inp}")

    assert "Storage ID must be a three-digit integer." in output


@pytest.mark.parametrize("inp", ["101", "201", "907", "001", "080"])
def test_delete_rejects_non_existent_storage_id(test_user, run_shell_command, inp):

    output = run_shell_command(
        f"python3 storetoise_4.py --username {test_user} --storage {inp} --delete")

    assert "Cannot delete a non-existent storage ID." in output


def test_delete_removes_messages(test_user, run_shell_command, test_url):

    output = run_shell_command(
        f"python3 storetoise_4.py --username {test_user} -s 504 -m another")
    assert "Message added to Storage ID 504 successfully." in output

    output = run_shell_command(
        f"python3 storetoise_4.py --storage 504 -u {test_user}")
    assert "0) another\n" in output

    output = run_shell_command(
        f"python3 storetoise_4.py -d -u {test_user} --storage 504")
    assert "Storage ID 504 deleted successfully." in output

    output = run_shell_command(
        f"python3 storetoise_4.py --username {test_user} -s 504 -m another")
    assert "Message added to Storage ID 504 successfully." in output

    run_shell_command(f"curl -X DELETE {test_url}/storage/{test_user}/504/0")

    output = run_shell_command(
        f"python3 storetoise_4.py --storage 504 -u {test_user}")
    assert "No messages found for storage ID 504." in output


def test_delete_removes_message_limit(test_user, run_shell_command):

    for i in range(10):
        output = run_shell_command(
            f"python3 storetoise_4.py --username {test_user} -s 503 -m another")
        assert "Message added to Storage ID 503 successfully." in output

    output = run_shell_command(
        f'python3 storetoise_4.py --username {test_user} -s 503 -m lots')
    assert "Cannot add more than 10 messages to a storage ID." in output

    output = run_shell_command(
        f"python3 storetoise_4.py -u {test_user} --storage 503 -d")
    assert "Storage ID 503 deleted successfully." in output

    output = run_shell_command(
        f'python3 storetoise_4.py --username {test_user} -s 503 -m lots')

    assert "Message added to Storage ID 503 successfully." in output


def test_get_messages_when_no_messages(test_user, run_shell_command, test_url):

    output = run_shell_command(
        f"python3 storetoise_4.py --username {test_user} -s 505 -m another")
    assert "Message added to Storage ID 505 successfully." in output

    run_shell_command(f"curl -X DELETE {test_url}/storage/{test_user}/505/0")

    output = run_shell_command(
        f"python3 storetoise_4.py --storage 505 -u {test_user}")
    assert "No messages found for storage ID 505." in output
