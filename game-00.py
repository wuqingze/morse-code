import random

# 定义摩斯电码字母和对应的编码
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----'
}

# 获取摩斯电码字母列表
morse_code_letters = list(morse_code_dict.keys())

def generate_random_morse_code():
    # 从摩斯电码字母列表中随机选择一个字母
    random_letter = random.choice(morse_code_letters)
    # 获取对应的摩斯电码
    morse_code = morse_code_dict[random_letter]
    return random_letter, morse_code

def main():
    while True:
        random_letter, morse_code = generate_random_morse_code()
        print(f"摩斯电码: {morse_code}")
        
        user_input = input("请输入对应字母的摩斯电码（不区分大小写）: ").upper()
        
        while user_input != random_letter:
            user_input = input("输入错误，重新输入（不区分大小写）: ").upper()
        print("输入正确，继续下一个摩斯电码\n")

if __name__ == "__main__":
    main()
