import os


def create_txt(chapters, title):
    with open(f"epubs/{title}.txt", 'w', encoding='utf-8') as f:
        f.write(f"% {title}\n")
        for chapter in chapters:
            f.write(f"# {chapter[0]}\n")
            f.write(f"{chapter[1]}\n\n")


def create_epub(chapters, title):
    title = title.replace(' ', '_').replace('(', '_').replace(')', '_')
    create_txt(chapters, title)
    os.system(f'pandoc epubs/{title}.txt -o epubs/{title}.epub --quiet')
    os.remove(f'epubs/{title}.txt')
