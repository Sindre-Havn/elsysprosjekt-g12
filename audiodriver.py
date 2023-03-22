from scipy.io.wavfile import read, write

"""

INPUT:           USB: mapper = sanger, en mappe har flere tracks

1. Shuffle av alle sanger, sanger gjentar seg ikkje hyppig, men ekje én bestemt syklus.
Desktop, Documents, Music, usbdisc, minebarnesagner, 

2. Hvor mange tracks er i sangen.

3. Variabel på antall høytelere.



sjekk tracks: hvor mange mono og stereo?

"""

speaker_count = 4
track_count = None

def fetch_song():
    """
    Get usb path
    /media/pi/
    utenom 'system Volume Information'
    """
    songs = dict()
    for song in usb:
        songs[song] = 
        

def preprocess_song(song):
    song = read('Viva la Vida Vocals Mono.wav', 'rb')



def main():
    """
    speaker_count = 4
    files = dict(navn : filepath)
    last_5_songs = list() # Sørger for at ny shuffle liste ikke blir for repetitiv
    play_order = shuffle(files, last_5_songs)
    """





if __name__ == '__main__':
    main()