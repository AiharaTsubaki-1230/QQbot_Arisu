def guess_song_char(raw_song_list, hidden_song_list, char, ans_array, correct):
    score_final = 0
    for i in range(0, len(raw_song_list)):
        hidden_song_list[i], score_add = song_char_change(raw_song_list[i], hidden_song_list[i], char)
        score_final += score_add
        if ans_array[i] == 0 and raw_song_list[i] == hidden_song_list[i]:
            ans_array[i] = len(raw_song_list) - correct + 1
            correct -= 1
    return raw_song_list, hidden_song_list, score_final, ans_array, correct

def song_char_change(name, hidden_name, char):
    string = ""
    score = 0
    for i in range(0, len(name)):
        if hidden_name[i] != "-":
            string += hidden_name[i]
            continue
        if name[i] == char:
            string += char
            score += 1
        elif name[i] == " ":
            string += " "
        else:
            string += "-"
    return string, score