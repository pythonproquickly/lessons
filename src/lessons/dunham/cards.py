from contextlib import contextmanager


@contextmanager
def generic(card_type, sender, recipient):
    card = open(card_type, "r")
    new_card = open(f"{sender}_generic.txt", "w")
    try:
        yield new_card

    finally:
        new_card.write("Dear \n")
        new_card.write("\n")
        new_card.write("Sincerely, ")
        card.close()
        new_card.close()
    return True


with generic("thankyou_card.txt", "Mwenda", "Amanda") as card_gen:
    print("Card Generated!")

with open("Mwenda_generic.txt") as card_read:
    card = card_read.readlines()
    print(card)


class Personalized:
    def __init__(self, sender, recipient, new_creation):
        self.sender = sender
        self.recipient = recipient
        self.new_creation = new_creation
        self.new_file = open(f"{self.sender}_personalized.txt", "w")

    def __enter__(self):
        self.new_file.write(f"Dear {self.recipient}")
        return self.new_file

    def __exit__(self, exc_type, exc_value, Traceback):
        self.new_file.write(f"Sincerely {self.sender}")
        self.new_file.close()


text = "I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don’t say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always."

with Personalized("John", "Michael", text) as p:
    p.write(text)

textA = "Happy Birthday!! I love you to the moon and back. Even though you’re a pain sometimes, you’re a pain I can't live without. I am incredibly proud of you and grateful to have you as a sister. Cheers to 25!! You’re getting old!"

with generic("happy_bday.txt", "Josiah", "Remy") as p:
    with Personalized("Josiah", "Esther", textA) as q:
        p.write(textA)
        q.write(textA)
