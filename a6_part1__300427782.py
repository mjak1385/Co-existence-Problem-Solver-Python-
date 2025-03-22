import string

def open_file():
    '''None->file object
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    accept = True
    file = ''
    while accept:
        file_name = input("Enter the name of the file: ").strip()
        try:
            file = open(file_name).read()
            accept = False
        except FileNotFoundError:
            print("There is no file with that name. Try again.")
    return file
            
def clean_word(word):
    word = word.translate(str.maketrans('', '', string.punctuation))
    word = word.replace("'", "").replace("-", "")
    return word

def dict_cond(word, lines_dict, index):
    if word.isalpha() and len(word)>=2:
        if word in lines_dict:
            lines_dict[word].add(index)
        else:
            lines_dict[word] = {index}

def read_file(fp):
    '''(file object)->dict
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    lines = fp.lower().splitlines()
    index = 0
    lines_dict = {}
    for line in lines:
        index += 1
        words = line.split()
        for word in words:
            word = clean_word(word)
            dict_cond(word, lines_dict, index)
            
    return dict(lines_dict)
    

def find_coexistance(D, query):
    '''(dict,str)->list
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    old_num = set()
    num = set()
    ans = set()
    index = 0
    query = query.split()
    for word in query:
        word = clean_word(word)
        index += 1
        num = D.get(word)
        if num == None:
            return word
        
        if index == 1 and len(query) > 1:
            old_num = num
        elif len(query) <= 1:
            ans = num
        else:
            ans = old_num.intersection(num)
            old_num = ans
    return ans

def comun():
    num = find_coexistance(d, query)
    if isinstance(num, str):
        print("Word '" + num + "' not in the file.")
    elif len(num) == 0:
        print("The one or more words you entered does not coexist in a same line of the file.")
    else:
        print("The one or more words you entered coexisted in the following lines of the file:")
        print(*num)

##############################
# main
##############################
file=open_file()
d=read_file(file)
query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
# YOUR CODE GOES HERE
while True:
    if query.lower().strip() == 'q':
        break
    elif not query.strip():
        print("Word '" + query + "' not in the file.")
    else:
        comun()

    query = input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()












