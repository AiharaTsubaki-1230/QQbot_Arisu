def song_changeLine(song):
    for i in range(0, len(song)-1):
        song[i] = song[i][:-1]
    return song

song_list = {
    "arc": song_changeLine(list(open("./src/guess_song/arcaea.txt").readlines())),
    "phi": song_changeLine(list(open("./src/guess_song/phi.txt").readlines())),
    "chu": song_changeLine(list(open("./src/guess_song/chuni.txt").readlines())),
    "cy2": song_changeLine(list(open("./src/guess_song/cy2.txt").readlines())),
    "de": song_changeLine(list(open("./src/guess_song/deemo.txt").readlines())),
    "dy": song_changeLine(list(open("./src/guess_song/dynamix.txt").readlines())),
    "la": song_changeLine(list(open("./src/guess_song/lanota.txt").readlines())),
    "mai": song_changeLine(list(open("./src/guess_song/mai.txt").readlines()))
}