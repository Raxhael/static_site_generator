from textnode import TextNode, TextType

def main():
    text = "this is some anchor text"
    text_type = TextType.LINK
    url = "https://www.website.com.au"

    print(TextNode(text,text_type,url))


if __name__ == "__main__":
    main()