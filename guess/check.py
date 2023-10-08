def check_answer(raw, hid):
    num_of_correct = 0
    for i in range(0, len(raw)):
        if raw[i] != hid[i]:
            num_of_correct += 1
    if num_of_correct == 0:
        return True, num_of_correct
    else:
        return False, num_of_correct

def check_index(raw, qq_list, guess_word):
    for i in range(0, len(raw)):
        if guess_word.lower() == raw[i].lower():
            return qq_list[i]
    return 0