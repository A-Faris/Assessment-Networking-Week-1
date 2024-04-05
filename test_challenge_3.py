"""Tests for challenge 3."""

# pylint: skip-file

import pytest


def test_add_message_returns_expected_result(test_user, run_shell_command):

    output = run_shell_command(
        f"python3 storetoise_3.py -u {test_user} -s 200 -m test")

    assert "Message added to Storage ID 200 successfully." in output


def test_add_message_to_new_storage_returns_expected_result(test_user, run_shell_command):

    output = run_shell_command(
        f"python3 storetoise_3.py -u {test_user} -s 900 -m test")

    assert "Message added to Storage ID 900 successfully." in output

    output = run_shell_command(f"python3 storetoise_3.py -u {test_user}")

    assert "900" in output


@pytest.mark.parametrize("inp", ["23", "2000", "-12", "-123", "knives"])
def test_add_message_rejects_invalid_storage_id(test_user, run_shell_command, inp):

    output = run_shell_command(
        f"python3 storetoise_3.py --username {test_user} --s {inp} -m test")

    assert "Storage ID must be a three-digit integer." in output


@pytest.mark.parametrize("inp", ["YYYYY", ",-", "./1'23", "aBcDeF", "readad."])
def test_add_message_rejects_invalid_message(test_user, run_shell_command, inp):

    output = run_shell_command(
        f"python3 storetoise_3.py --username {test_user} --s 200 -m {inp}")

    assert "Message must consist only of lowercase letters and spaces." in output


def test_add_message_rejects_long_message(test_user, run_shell_command):

    long = "f" * 145

    output = run_shell_command(
        f"python3 storetoise_3.py --username {test_user} --s 200 -m {long}")

    assert "Message must be 140 characters or fewer." in output


def test_add_message_rejects_eleventh_message(test_user, run_shell_command):

    for i in range(10):
        output = run_shell_command(
            f"python3 storetoise_3.py --username {test_user} --s 601 -m another")
        assert "Message added to Storage ID 601 successfully." in output

    output = run_shell_command(
        f'python3 storetoise_3.py --username {test_user} --s 601 -m lots')
    assert "Cannot add more than 10 messages to a storage ID." in output
