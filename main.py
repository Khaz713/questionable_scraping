import requests
import sys


from scraper import find_text, get_title, get_chapters_number, get_chapter_title, get_chapter


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <url>")
    if "reader" not in sys.argv[1].split('/')[-1]:
        sys.argv[1] += '/reader'


    response = requests.get(sys.argv[1])
    response_text = response.text
    title, response_text = get_title(response_text)
    chapters_num, response_text = get_chapters_number(response_text)
    chapters_num = int(chapters_num)

    for i in range(1, chapters_num + 1):
        chapter_title, response_text = get_chapter_title(response_text)
        chapter, response_text = get_chapter(response_text)
        print(title)
        print(chapters_num)
        print(chapter_title)
        print(chapter)
        #if chapters_num % i == 0:



if __name__ == "__main__":
    main()
