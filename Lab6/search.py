from songs import Song
import timeit
def main():

    filename = "unique_tracks.txt"

    lista = readfile(filename)
    n = len(lista)
    print("Antal element =", n)

    sista = lista[n-1]
    testartist = sista.artist

    linjtid = timeit.timeit(stmt = lambda: linsok(lista, testartist), number = 100000)
    print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")

def readfile(filename):
    objectlst = []
    txt = open(filename, "r", encoding = 'utf-8')
    rows = txt.read().split("\n")
    for i in range(len(rows)):
        attributelst = rows[i].split("<SEP>")
        tempobj = Song(attributelst[0], attributelst[1], attributelst[2], attributelst[3])
        objectlst.append(tempobj)
    return objectlst

def linsok(list, artist):
    for i in range(len(list)):
        if(artist == list[i].getArtist()):
            return

main()
