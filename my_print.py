def my_print(path, text):
    with open(path, 'a') as f:
        print(text, file=f)
