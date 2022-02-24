import timeit

class Song:

    def __init__(self, trackID, songTime, artistName, songTitle):
        self.trackID = trackID
        self.songTime = songTime
        self.artistName = artistName
        self.songTitle = songTitle

    def __str__(self):
        return "TrackID: " + self.trackID + "\nLength of song: " + self.songTime + "\nName of Artist: " + self.artistName + "\nSong title: " + self.songTitle + "\n"

    def __lt__(self,other):
        return self.artistName < other.artistName

def linSearch(objectList, artist):
    for i in range(len(objectList)):
        if (objectList[i].artistName == artist):
            return True
    return False

def binSearch(objectList, artist):
    low = 0
    high = len(objectList)-1
    found = False

    while low <= high and not found:
        middle = (low + high)//2
        if(objectList[middle].artistName == artist):
            found = True
        else:
            if(artist < objectList[middle].artistName):
                high = middle - 1
            else:
                low = middle + 1
    return found

def createDictionary(objectList):
    songDict = {}
    for i in range(len(objectList)):
        songDict[objectList[i].artistName] = objectList[i]
    return songDict

def hashSearch(songDict, artist):
    try:
        songDict[artist]
        return True
    except:
        return False


def urvalssortera(data):
    #Taget från föreläsningsanteckningar för Föreläsning 9: sortering
    n = len(data)
    for i in range(n-1):
        minst = i
        for j in range(i+1,n):
            if data[j] < data[minst]:
                minst = j
        data[minst],data[i] = data[i], data[minst]

def mergesort(data):
    #Taget från föreläsningsanteckningar för Föreläsning 9: sortering
    if len(data) > 1:
        mitten = len(data)//2
        vensterHalva = data[:mitten]
        hogerHalva = data[mitten:]

        mergesort(vensterHalva)
        mergesort(hogerHalva)

        i, j, k = 0, 0, 0

        while i < len(vensterHalva) and j < len(hogerHalva):
            if vensterHalva[i] < hogerHalva[j]:
                data[k] = vensterHalva[i]
                i = i + 1
            else:
                data[k] = hogerHalva[j]
                j = j + 1
            k = k + 1

        while i < len(vensterHalva):
            data[k] = vensterHalva[i]
            i = i + 1
            k = k + 1

        while j < len(hogerHalva):
            data[k] = hogerHalva[j]
            j = j + 1
            k = k + 1


def main():
    songObject = []
    n = 500000

    f = open("unique_tracks.txt", "r", encoding='utf-8')
    for line in f:
        tempSong = line.split("<SEP>")
        songObject.append(Song(tempSong[0], tempSong[1], tempSong[2], tempSong[3]))
        #print(songObject[counter])

    newSongObject = songObject[0:n]

    #tid = timeit.timeit(stmt = lambda: linSearch(newSongObject, "isak"), number = 10000)

    newSongObject.sort()
    tid = timeit.timeit(stmt = lambda: binSearch(newSongObject, "isak"), number = 10000)

    #songDict = createDictionary(newSongObject)
    #tid = timeit.timeit(stmt = lambda: hashSearch(songDict, newSongObject[-1].artistName), number = 10000)

    #tid = timeit.timeit(stmt = lambda: urvalssortera(newSongObject), number = 1)

    #tid = timeit.timeit(stmt = lambda: mergesort(newSongObject), number = 1)
    print("Funktionen tog", round(tid, 4) , "sekunder")




main()
