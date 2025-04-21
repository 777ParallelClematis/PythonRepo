import logging

def new_print(text: str) -> None:
    logging.warning(text)

def main() -> None:
    print = new_print  # Assign function, not call it
    print('Hello World!')  # This will log a warning

if __name__ == '__main__':
    main()
