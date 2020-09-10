'''
Ever tried to send a secret message to someone without using the postal service? You could use newspapers to tell your secret. Even if someone finds your message, it's easy to brush them off as paranoid and as a conspiracy theorist. One of the simplest ways to hide a secret message is to use capital letters. Let's find some of these secret messages.

You are given a chunk of text. Gather all capital letters in one word in the order that they appear in the text.

For example: text = "How are you? Eh, ok. Low or Lower? Ohhh.", if we collect all of the capital letters, we get the message "HELLO".

Input: A text as a string (unicode).

Output: The secret message as a string or an empty string.
'''


def secret_mess(string):

    answer = []

    for i in string:
        if i.isupper():
            answer.append(i)
        else:
            continue
    answer = ''.join(answer)
    return answer





print(secret_mess("How are you? Eh, ok. Low or Lower? Ohhh.")) #  "HELLO"
print(secret_mess("hello world!")) # ""
