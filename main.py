import requests
import sys
import os


from scraper import find_text, get_title, get_chapters_number, get_chapter_title, get_chapter


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <url>")
    if "reader" not in sys.argv[1].split('/')[-1]:
        sys.argv[1] += '/reader'

    os.system('clear')


    response = requests.get(sys.argv[1])
    response_text = response.text
    title, response_text = get_title(response_text)
    chapters_num, response_text = get_chapters_number(response_text)
    chapters_num = int(chapters_num)
    chapters = []
    j = 1
    for i in range(1, chapters_num + 1):
        chapter_title, response_text = get_chapter_title(response_text)
        chapter, response_text = get_chapter(response_text)
        #print(chapter_title)
        #print(chapter)
        chapters.append([chapter_title, chapter])
        print(f'Scraping chapter {i} of {chapters_num}...')
        if i % 30 == 0:
            j += 1
            response = requests.get(sys.argv[1] + f'/page-{j}')
            response_text = response.text
        os.system('clear')



if __name__ == "__main__":
    main()
