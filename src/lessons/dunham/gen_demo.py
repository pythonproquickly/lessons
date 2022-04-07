def gen_str():
    words = ["first", "second", "fourth"]
    i = 0
    while True:
        word = words[i]
        # following line behaves normally until .send is called
        # then is assigns the value in the send parameter to w
        w = yield word
        # w is not None only after a send
        if w is not None:
            # append w into the list and then yield it
            words.append(w)
            yield w
        i += 1


names = gen_str()
print(next(names))  # first
print(next(names))  # second
names.send("third")
print(next(names))  # third
print(next(names))  # fourth
