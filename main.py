import requests

from scraper import find_text





def main():
    session = requests.Session()
    response = session.get(
        "https://forum.questionablequesting.com/threads/with-this-ring-young-justice-si-thread-fourteen.8938/reader")
    html_text = find_text(response.text, "<html", ">")
    logged_in = find_text(html_text, 'data-logged-in="', '"\n')
    if logged_in == "false":
        logged_in = False
    else:
        logged_in = True
    title = find_text(response.text, "<title>", "</title>")
    chapters_num = int(find_text(response.text, '<span class="">Statistics (', " threadmarks"))
    print(logged_in)
    print(title)
    print(chapters_num)



if __name__ == "__main__":
    main()
