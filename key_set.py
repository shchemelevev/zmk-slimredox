#!/Users/e_shchemelev/.virtualenvs/zmk_keyring/bin/python
import sys
import keyring


def string_to_zmk_keycodes(input_string):
    # Static mapping only for special characters
    keycode_map = {
        ' ': '&kp SPACE', '\n': '&kp ENTER', '\t': '&kp TAB',
        '.': '&kp DOT', ',': '&kp COMMA', ':': '&kp LS(SEMI)', ';': '&kp SEMI',
        '!': '&kp LS(N1)', '?': '&kp LS(SLASH)', '/': '&kp SLASH', '\\': '&kp BSLH',
        '\'': '&kp SQT', '"': '&kp LS(SQT)', '-': '&kp MINUS', '_': '&kp LS(MINUS)',
        '=': '&kp EQUAL', '+': '&kp LS(EQUAL)', '[': '&kp LBKT', ']': '&kp RBKT',
        '{': '&kp LS(LBKT)', '}': '&kp LS(RBKT)', '(': '&kp LS(N9)', ')': '&kp LS(N0)'
    }

    zmk_keycodes = []
    for char in input_string:
        if char.isupper():
            zmk_keycodes.append(f'&kp LS({char.lower()})')
        elif char.islower():
            zmk_keycodes.append(f'&kp {char.upper()}')
        elif char.isdigit():
            zmk_keycodes.append(f'&kp N{char}')
        elif char in keycode_map:
            zmk_keycodes.append(keycode_map[char])
        else:
            zmk_keycodes.append(f'/* Unsupported: {char} */')

    return ' '.join(zmk_keycodes)


def main():
    if len(sys.argv) < 2:
        print("Usage: python key_set.py \"storage name[bitpass|windows|system]\"")
        sys.exit(1)

    storage_name = sys.argv[1]
    input_string = input("password> ")
    result = string_to_zmk_keycodes(input_string)
    assert storage_name in ["bitpass", "windows", "system"], f"Invalid storage name: {storage_name}"
    keyring.set_password(storage_name, "e_shchemelev", f"<{result}>")

if __name__ == "__main__":
    main()
