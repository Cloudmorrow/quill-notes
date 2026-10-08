"""Notes' tests: the real record store, files and gate, and quill.py, on this machine."""

import pytest

from cloudmorrow.quill.testing import Harness


@pytest.fixture()
def q():
    with Harness(".") as harness:
        yield harness


IN_NOTES = {"share": "my-files", "within": "Notes", "suffix": ".md"}


def test_everybody_gets_a_welcome_note(q):
    pages = q.list("file", **IN_NOTES)
    assert [p["path"] for p in pages] == ["Notes/Welcome.md"], "the welcome note is seeded the first time Notes is listed"


def test_a_line_is_added_to_the_end_and_nothing_else_changes(q):
    note = q.seed("file", share="my-files", path="Notes/ideas/garden.md", text="# Garden\n\n- tomatoes")
    result = q.act("add-to-the-end", note, text="- beans")
    assert result.ok and result.toast == "Added to garden"
    assert q.get("file", note.id)["text"] == "# Garden\n\n- tomatoes\n- beans\n"


def test_there_must_be_something_to_add(q):
    note = q.seed("file", share="my-files", path="Notes/log.md", text="")
    assert q.act("add-to-the-end", note).error == "Text is needed"
