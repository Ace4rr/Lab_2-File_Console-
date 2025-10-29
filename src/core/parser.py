#from src.constants import ERROR_MESSAGES


class ShellParseError(Exception):
    """Ошибка при разборе пользовательского ввода."""
    pass


def parse_command(line: str) -> tuple[str, list[str], list[str]]:
    """
    Разбирает строку команды вручную без shlex.

    Пример:
        'cp -r "My Folder" NewFolder'
        → ('cp', ['My Folder', 'NewFolder'], ['-r'])

    Возвращает:
        (command_name, args, flags)
    """
    line = line.strip()
    if not line:
        raise ShellParseError(ERROR_MESSAGES.get("empty_command", "Пустая команда"))

    tokens = tokenize(line)
    if not tokens:
        raise ShellParseError(ERROR_MESSAGES.get("invalid_syntax", "Ошибка синтаксиса"))

    command = tokens[0]
    args = []
    flags = []

    for token in tokens[1:]:
        if token.startswith('-'):
            flags.append(token)
        else:
            args.append(token)

    return command, args, flags


def tokenize(line: str) -> list[str]:
    """
    Преобразует строку в список токенов (без shlex).
    Поддерживает:
        - Кавычки "..." и '...'
        - Экранирование \"
        - Разделение по пробелам вне кавычек
    """
    tokens = []
    current = []
    in_quotes = False
    quote_char = None
    escaped = False

    for ch in line:
        if escaped:
            current.append(ch)
            escaped = False
            continue

        if ch == '\\':
            escaped = True
            continue

        if in_quotes:
            if ch == quote_char:
                in_quotes = False
                quote_char = None
                continue
            else:
                current.append(ch)
        else:
            if ch in ("'", '"'):
                in_quotes = True
                quote_char = ch
                continue
            elif ch.isspace():
                if current:
                    tokens.append(''.join(current))
                    current = []
            else:
                current.append(ch)

    if in_quotes:
        raise ShellParseError(ERROR_MESSAGES.get("unclosed_quotes", "Незакрытые кавычки"))

    if current:
        tokens.append(''.join(current))

    return tokens
print(parse_command('ls -l /home/user'))