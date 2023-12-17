import os
zshrc_config_file = 'zshrc_path.txt'  # Назва файлу для збереження шляху до .zshrc
def find_zshrc():
    home_directory = os.path.expanduser("~")
    zshrc_path = os.path.join(home_directory, '.zshrc')
    if os.path.isfile(zshrc_path):
        return zshrc_path
    else:
        print("Файл .zshrc не знайдено в домашній директорії.")
        custom_path = input("Будь ласка, введіть шлях до файлу .zshrc: ")
        return custom_path

def save_zshrc_path():
    zshrc_path = find_zshrc()
    with open(zshrc_config_file, 'w') as config_file:
        config_file.write(zshrc_path)

def find_and_save_zshrc_path():
    find_zshrc()
    save_zshrc_path()
def load_zshrc_path():
    try:
        with open(zshrc_config_file, 'r') as config_file:
            return config_file.read().strip()
    except FileNotFoundError:
        return None
