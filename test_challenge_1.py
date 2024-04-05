"""Tests for challenge 1."""

# pylint: skip-file

import pytest


def test_gets_storage_ids_for_namespace(test_user, run_shell_command):

    output = run_shell_command(f"python3 storetoise_1.py --username {test_user}")

    assert "100\n200\n300" in output


def test_gets_storage_ids_for_namespace_short_name(test_user, run_shell_command):

    output = run_shell_command(f"python3 storetoise_1.py -u {test_user}")

    assert "100" in output
    assert "200" in output
    assert "300" in output
    assert "100\n200\n300" in output


def test_gets_number_storage_ids_for_namespace(test_user, run_shell_command):

    output = run_shell_command(
        f"python3 storetoise_1.py --username {test_user} --number 2")

    assert output.count("\n") == 2, "Wrong number of newline characters in output."


def test_gets_number_storage_ids_for_namespace_short_name(test_user, run_shell_command):

    output = run_shell_command(
        f"python3 storetoise_1.py --username {test_user} -n 1")

    assert output.count("\n") == 1, "Wrong number of newline characters in output."


def test_gets_number_storage_ids_for_namespace_short_names(test_user, run_shell_command):

    output = run_shell_command(f"python3 storetoise_1.py -n 1 -u {test_user}")

    assert output.count("\n") == 1, "Wrong number of newline characters in output."


@pytest.mark.parametrize("inp", ["-1", "2000", "horse", "_", "8.60", "-0.2", ",,,", "two", "nineninenine"])
def test_gets_storage_ids_rejects_invalid_number_for_getting_storage_ids(test_user, run_shell_command, inp):

    output = run_shell_command(
        f"python3 storetoise_1.py --username {test_user} --number {inp}")

    assert "Number must be an integer between 0 and 1000." in output
