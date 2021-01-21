# -*- coding: utf8 -*-
import re


# Help Function - 수정하지 말 것
def get_morse_code_dict():
    morse_code = {
        "A": ".-", "N": "-.", "B": "-...", "O": "---", "C": "-.-.", "P": ".--.", "D": "-..", "Q": "--.-", "E": ".",
        "R": ".-.", "F": "..-.", "S": "...", "G": "--.", "T": "-", "H": "....", "U": "..-", "I": "..", "V": "...-",
        "K": "-.-", "X": "-..-", "J": ".---", "W": ".--", "L": ".-..", "Y": "-.--", "M": "--", "Z": "--.."
    }
    return morse_code


# Help Function - 수정하지 말 것
def get_help_message():
    message = "HELP - International Morse Code List\n"
    morse_code = get_morse_code_dict()

    counter = 0

    for key in sorted(morse_code):
        counter += 1
        message += "%s: %s\t" % (key, morse_code[key])
        if counter % 5 == 0:
            message += "\n"

    return message


def is_help_command(user_input):
    if user_input.lower() == 'help' or user_input.lower() == 'h':
        return True
    else:
        return False


def is_validated_english_sentence(user_input):
    # print(f'this sentence: {user_input}')
    re_input = re.sub('[.,!?\s]', '', user_input)  # 문장 부호와 공백을 제거
    # print(f'regular sentence: {re_input}')
    # 문장부호(.,!?)를 제외하면 입력값이 없거나 빈칸만 입력한 경우를 거른다.
    if len(re_input) == 0:
        return False
    else:
        # 숫자나 특수문자를 포함하고 있다면 거른다.
        dont_include = '0123456789_@#$%^&*()-+=[]{}"\';:|`~'
        user_input = re.sub('[.,!?]', '', user_input)   # 특수문자만 제거
        # print(f'regular normal sentence: {user_input}')
        for c in user_input:
            if c in dont_include:
                return False
    return True


def is_validated_morse_code(user_input):
    # 1) "-","."," "외 다른 글자가 포함되어 있는 경우 false
    if re.search('[^-.\s]', user_input):
        return False
    # 2) get_morse_code_dict 함수에 정의된 Morse Code 부호외 다른 코드가 입력된 경우 false ex)......
    else:
        morse_code = get_morse_code_dict()
        user_input_arr = user_input.split()
        for inp in user_input_arr:
            if inp not in morse_code.values():
                return False
        return True


def get_cleaned_english_sentence(raw_english_sentence):
    return re.sub('[.,!?]', '', raw_english_sentence).strip()


# morse to eng
def decoding_character(morse_character):
    morse_code_dict = get_morse_code_dict()
    for key, val in morse_code_dict.items():
        if val == morse_character:
            return key


# eng to morse
def encoding_character(english_character):
    morse_code_dict = get_morse_code_dict()
    for key, val in morse_code_dict.items():
        if key == english_character.upper():
            return val


def decoding_sentence(morse_sentence):
    result = []
    morse_list = morse_sentence.split(' ')  # 공백 한칸을 기준으로 단어 분리
    for morse in morse_list:
        if morse == '':
            result.append(' ')
        else:
            result.append(decoding_character(morse))
    return ''.join(result)


def encoding_sentence(english_sentence):
    clean_sentence = get_cleaned_english_sentence(
        english_sentence.strip())  # .,!? 문자 제거
    clean_sentence = ' '.join(clean_sentence.split())   # 여러개의 공백은 하나로 만든다.
    word_list = list(clean_sentence)    # 공백 포함 모든 글자를 리스트화

    result = [encoding_character(word) if word !=
              ' ' else ' ' for word in word_list]

    return ' '.join(result).replace('   ', '  ')


def main():
    print("Morse Code Program!!")
    # ===Modify codes below=============
    while True:
        message = input('Input your message(H - Help, 0 - Exit): ')
        if message == '0':
            break
        elif is_help_command(message):
            print(get_help_message())
        elif is_validated_english_sentence(message):
            print(encoding_sentence(message))
        elif is_validated_morse_code(message):
            print(decoding_sentence(message))
        else:
            print('Wrong Input')
    # ==================================
    print("Good Bye")
    print("Morse Code Program Finished!!")


if __name__ == "__main__":
    main()
