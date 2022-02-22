class Song:
    def __init__(self, trackid, songid, artist, songtitle):
        self.trackid = trackid
        self.songid = songid
        self.artist = artist
        self.songtitle = songtitle

    def __str__(self):
        return "TrackID: " + str(self.trackid) + "\nSongID: " + str(self.songid) + "\nArtist: " + str(self.artist) + "\nSongtitle: " + str(self.songtitle)

    def __lt__(self, other):
        return self.artist < other.artist

    def getArtist(self):
        return self.artist



if __name__ == "__main__":
    objectlst = []
    txt = open("unique_tracks.txt", "r", encoding = 'utf-8')
    rows = txt.read().split("\n")
    for i in range(len(rows)):
        attributelst = rows[i].split("<SEP>")
        tempobj = Song(attributelst[0], attributelst[1], attributelst[2], attributelst[3])
        objectlst.append(tempobj)
