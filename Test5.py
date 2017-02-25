import urllib


def read_file():
    file = open("movie_quotes.txt")
    content = file.read()
    print content
    file.close()
    check_profanity(content)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    connection.close()
    if "true" in output:
        print "Alert!"
    elif "false" in output:
        print "No bad words :)"

    else :
        print "Error scanning the file."

contect = read_file()