import install_zsh, zshrc_path_finder, zsh_plugin_manager, subprocess, os, platform, argparse, art

# comments Lang: UA/ENG
if __name__ == "__main__":
    main()
    print_ASCII_programm_name_art()
    print_ASCII_version_art()
def main():

     # Створення об'єкту парсера/Create object parser
    parser = argparse.ArgumentParser(description='Опис програми сокоро буде тут...')

    # Додавання позиційного та опційного аргументів/Add positional and optional arguments
    #parser.add_argument()
    parser.add_argument('--print-author')
    parser.add_argument('--print-version')

    # Парсинг аргументів командного рядка/Parse the command-line arguments
    args = parser.parse_args()

    # Доступ до значень аргументів/Access the argument values
    mode = args.mode

def Easter_egg(): #Easter egg coming soon...
    pass

def print_ASCII_programm_name_art(): #Виводить назву програми артом з ASCII символів / Prints programm name ASCII symvols
    art.tprint("AX_CLI_ZSH_Manager")

def print_ASCII_version_art(): #Виводить версію програми артом з ASCII символів / Prints programm version ASCII symvols
    art.tprint("v0.1.0")

def print_ASCII_author_art(): #Виводить автора програми артом з ASCII символів / Prints programm author ASCII symvols
    art.tprint("<nicalo786>")