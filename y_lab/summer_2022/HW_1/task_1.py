from urllib.parse import urlparse


def domain_name(url: str):
    if not url.startswith("http"):
        url = f"http://{url}"
    netloc = urlparse(url=url).netloc
    name_elements = netloc.split(".")
    if name_elements[0] in ("www", "ww2"):
        return name_elements[1]
    return name_elements[0]


def main():
    assert domain_name("http://google.com") == "google"
    assert domain_name("http://google.co.jp") == "google"
    assert domain_name("www.xakep.ru") == "xakep"
    assert domain_name("https://youtube.com") == "youtube"


if __name__ == "__main__":
    main()
