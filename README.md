# Notes

A Quill for [Cloudmorrow](https://github.com/Cloudmorrow/cloudmorrow): your
notes, in Markdown, in folders, with pictures — on the phone, the web app,
the terminal and the command line.

- A note is a title and a page of Markdown. Folders hold notes and other
  folders.
- Pictures go in a note by pasting, dropping or picking them, and show where
  they are.
- Search finds a note by its name or by any line in it.
- Every note is a plain Markdown file in the Notes folder of your drive on
  the server — the same file My Files, WebDAV, your assistant and any editor
  reach. Notes is an editor over those files and nothing more. Removing this
  Quill takes the tab away, never a note.

## Using it

A note is a Markdown file in the `Notes` folder of your drive on the
server: a plain file, in My Files, on WebDAV, in a backup of the folder,
and open to any editor. A path with slashes in it is folders. Notes is the
kit's **editor** over those files, on every surface, and nothing more.

**Writing one:**

#### In the web app

The **Notes** tab is three screens, the way a phone's notes app is:
**Folders**, the notes in one (newest first, with the first lines of each),
and the note; on a computer the list and the note are side by side. The pen
beside the title starts a new note in the folder you are looking at. The
title is the file name — a new note starts with a `# Title` heading
matching it, shown as the title rather than as a line of the body; rename
the title and the file is renamed — and the note saves itself as you type.
Back out of a note you never wrote anything in and it is thrown away.
Delete is the bin in the top corner, and asks first. Search looks inside
the notes, not only at their names.

#### In the terminal app

The **Notes** card (`f1`), the first in the workspace: the tree on the
left, with every folder, empty ones too, and the live editor on the right —
the line the cursor is on stays raw Markdown, every other line renders as
you leave it. `ctrl+n` makes a note, `ctrl+o` a folder, `r` renames or
moves what is selected in the tree (a folder takes what is in it along),
`d` deletes it, `ctrl+f` searches, `ctrl+s` saves now. `f6` imports a file
from this machine into the selected folder and `f7` writes the open note
back out.

#### On the command line

```bash
cm notes list
cm notes show ideas/garden          # the Markdown, as it is
cm notes add ideas/garden           # from stdin, or $EDITOR
cm notes edit ideas/garden
cm notes search tomatoes            # names and every line
cm notes delete ideas/garden
cm notes add-to-the-end ideas/garden text="Water on Sundays"
```

Text comes from stdin when there is any, and from `$EDITOR` when there is
not. `show` writes the raw text to stdout, so redirection and pipes work:

```bash
cat architecture.md | cm notes add architecture
cm notes show architecture > architecture.md
```

---

**Pictures.** A note can carry pictures. Either way the picture is sent to
the server as it is, kept beside your notes, and a line is written where
the cursor was:

```markdown
![rack front](img/20260917-135026-8e642c-rack.png)
```

#### In the web app

The photo button in the bar, or paste one, or drop one on the note. Each
picture shows where the note has it, between the text above and below;
tap one to see it full size.

#### In the terminal app

**Photo** (`ctrl+p`) asks for a file on this machine. The editor draws the
picture the cursor is on — or the note's first, when the cursor is
elsewhere — in a panel beside the text: the real picture where the terminal
speaks Kitty's graphics protocol or Sixel (Kitty, Ghostty, WezTerm, foot,
iTerm2), coloured half-cells anywhere else. The line itself shows as
`🖼 rack front`, since the editor draws one line per line of source.

#### On the command line

A picture is a file beside the notes and a line in the Markdown: put the
file in the notes' `img` folder with `cm files put my-files Notes/img
./rack.png`, and write the line.

---

**Where they are.** `Notes/img/`, one flat folder. The name says when the
picture arrived, carries six random characters so two pastes in a second
cannot collide, and ends with what the file was called, so `ls img/` still
reads. The type is taken from the bytes, never from the name: PNG, JPEG,
GIF and WebP, up to 25 MB. The folder never shows in the note list — a
picture is something a note shows, not a thing to find — and a copy of the
notes folder takes the pictures with it. Nothing deletes a picture yet:
take the line out of the note and the file stays in `img/`.

Everybody with no notes at all gets one the first time they open Notes, on
how the editor works. An assistant reaches the same files through the
record tools on `file`, and the **Add to the end** action. Removing the
Quill takes the tab away, never a note.

## What it adds to your Cloudmorrow

| | |
| --- | --- |
| Datamodels | uses the foundational `file` (domain *Files*): the Markdown files under Notes in your own drive, which the core serves as records with their text, folders and pictures |
| Screens | one editor — folders and notes beside the page — on the phone, the web app, the terminal, `cm notes`, and to your assistant |
| Jobs | none |
| Datasets | `welcome`: a note on how the editor works, the first time somebody with no notes opens Notes |
| Actions | **Add to the end** of a note — on its sheet, `cm notes add-to-the-end <note> text=…`, and to your assistant |
| Services, webhooks, APIs | none |

Its code is [`quill.py`](quill.py): the one action, run in the sandbox as whoever presses it. Everything else is declared in [`quill.toml`](quill.toml).

## Working on it

See [CLAUDE.md](CLAUDE.md) and the skills in `.claude/skills/`. In short:

```
uv sync                  # .venv with Cloudmorrow and pytest
cm quill check           # the manifest, as a server would install it
cm quill test            # tests/, against the real record store and gate
cm quill test --sandbox  # the same, with the code in the sandbox
cm quill dev --local     # a throwaway server here, reinstalled as you save
```

## Licence

AGPL-3.0-or-later.
