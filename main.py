import requests
import sys

from epub import create_epub
from scraper import get_title, get_chapters_number, get_chapter_title, get_chapter


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <url>")
    if "reader" not in sys.argv[1].split('/')[-1]:
        sys.argv[1] += '/reader'

    response = requests.get(sys.argv[1])
    response_text = response.text
    title, response_text = get_title(response_text)
    title = title.split('|')[0]
    chapters_num, response_text = get_chapters_number(response_text)
    chapters_num = int(chapters_num)
    chapters = []
    j = 1
    for i in range(1, chapters_num + 1):
        chapter_title, response_text = get_chapter_title(response_text)
        chapter, response_text = get_chapter(response_text)
        chapters.append([chapter_title, chapter])
        print(f'Scraping chapter {i} of {chapters_num}...', end='\r')
        sys.stdout.flush()
        if i % 30 == 0:
            j += 1
            response = requests.get(sys.argv[1] + f'/page-{j}')
            response_text = response.text
    print(f'Scraped all {chapters_num} chapters...')
    print(f'Converting to EPUB...')
    create_epub(chapters, title)
    print(f'EPUB generated at: epubs/{title.replace(' ', '_').replace('(', '_').replace(')', '_')}.epub')


if __name__ == "__main__":
    main()
