def eat_mangoes(count):
    if count == 0:
        print("Hand is empty, done")
        return

    print(f"I hhave {count} mangoes, eating one")
    eat_mangoes(count - 1)

eat_mangoes(13) 

