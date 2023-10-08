def guess_song_name(raw_song_list, hidden_song_list, guess_song, ans_array, correct):
    flag = False
    for i in range(0, len(raw_song_list)):
        if guess_song.lower() == raw_song_list[i].lower() and raw_song_list[i] != hidden_song_list[i]:
            hidden_song_list[i] = raw_song_list[i]
            flag = True
            if ans_array[i] == 0 and raw_song_list[i] == hidden_song_list[i]:
                ans_array[i] = len(raw_song_list) - correct + 1
                correct -= 1
    return raw_song_list, hidden_song_list, flag, ans_array, correct