"""Notes' tests: the real notes store and gate, and quill.py, on this machine."""

import pytest

from cloudmorrow.quill.testing import Harness


@pytest.fixture()
def q():
    with Harness(".") as harness:
        yield harness


def test_everybody_gets_a_welcome_note(q):
    assert q.list("note"), "the welcome note is seeded the first time notes are listed"


def test_a_line_is_added_to_the_end_and_nothing_else_changes(q):
    note = q.seed("note", path="ideas/garden", body="# Garden\n\n- tomatoes")
    result = q.act("add-to-the-end", note, text="- beans")
    assert result.ok and result.toast == "Added to garden"
    assert q.get("note", note.id)["body"] == "# Garden\n\n- tomatoes\n- beans\n"


def test_there_must_be_something_to_add(q):
    note = q.seed("note", path="log", body="")
    assert q.act("add-to-the-end", note).error == "Text is needed"
