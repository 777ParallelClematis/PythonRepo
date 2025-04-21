from dataclasses import dataclass, field
from uuid import uuid4, UUID

@dataclass
class Note:
    id: UUID = field(init=False)
    title: str
    body: str

    def __post_init__(self) -> None:
        self.id = uuid4()

class NoteApp:
    def __init__(self, author: str, notes: list[Note] | None = None) -> None:
        self.author = author
        self._notes = notes if notes is not None else []
        self.display_instructions()
        self._run()  # <-- run loop

    @staticmethod
    def display_instructions() -> None:
        print('Welcome to Notes!')
        print('Here are the commands: ')
        print('1 - Add a new note')
        print('2 - Edit note')
        print('3 - Delete note')
        print('4 - Display all notes')
        print('5 - Exit')

    def _add_note(self) -> None:
        title: str = input('Title: ')
        body: str = input('Body: ')
        note: Note = Note(title, body)
        self._notes.append(note)
        print('Note was added!')

    def _edit_note(self) -> None:
        print('Which note would you like to edit?')
        self._show_notes()
        try:
            note_index: int = int(input('Index: ')) - 1
            current: Note = self._notes[note_index]
            new_title: str = input('New title: ')
            new_body: str = input('New body: ')
            current.title = new_title
            current.body = new_body
            print('Note was updated!')
        except IndexError:
            print('Please select a valid note index')
            self._edit_note()
        except ValueError:
            print('Index cannot be empty or invalid')
            print('Aborting...')

    def _delete_note(self) -> None:
        print('Which note would you like to delete?')
        self._show_notes()
        try:
            note_index: int = int(input('Index: ')) - 1
            del self._notes[note_index]
            print('Note was deleted')
        except IndexError:
            print('Please select a valid note index')
            self._delete_note()
        except ValueError:
            print('Index cannot be empty or invalid')
            print('Aborting...')

    def _show_notes(self) -> None:
        if not self._notes:
            print('There are no notes')
            return

        for i, note in enumerate(self._notes, start=1):
            print(f'[{i}] {note.title}: {note.body}')

    def _select_option(self, user_input: str) -> None:
        if user_input not in ['1', '2', '3', '4']:
            print('Please pick a valid response')
            return

        if user_input == '1':
            self._add_note()
        elif user_input == '2':
            self._edit_note()
        elif user_input == '3':
            self._delete_note()
        elif user_input == '4':
            self._show_notes()

    def _run(self) -> None:
        while True:
            user_input = input('\nChoose a command (1–5): ').strip()
            if user_input == '5':
                print('Goodbye!')
                break
            self._select_option(user_input)

def main() -> None:
    NoteApp('Anonymous')

if __name__ == '__main__':
    main()
