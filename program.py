import os
import subprocess

import cat_service


def header():
    print('--------------------------')
    print('-----------cats-----------')
    print('--------------------------')


def get_folder():
    base = os.path.dirname(__file__)
    folder = 'cats'
    path = os.path.abspath(os.path.join(base, folder))

    if not os.path.exists(path) or not os.path.isdir(path):
        print('creating... {}'.format(path))
        os.mkdir(folder)
        
    return path


def download(folder):
    count = 8
    for i in range(count + 1):
        file = 'cat_{}'.format(i)
        cat_service.get_cat(folder, file)


def display(folder):
    subprocess.call(['open', folder])


def main():
    header()
    folder = get_folder()
    print('found or created cat folder: {}'.format(folder))
    download(folder)
    display(folder)
    


if __name__ == '__main__':
    main()
