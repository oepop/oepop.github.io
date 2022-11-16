import os

img_list = sorted(os.listdir('./cover'))
for img in img_list:
    if img[-4:] != '.png':
        os.remove("./cover/"+img)


with open('./js/playlist.js', 'w') as f:
    f.write('trackList = \n')
    f.write('[ \n')
    idx = 1
    music_list = sorted(os.listdir('./music'))
    for music in music_list:
        if music[-4:] != '.mp3':
            os.remove("./music/"+music)
            continue
        f.write(f'{{"icon":"cover/{music.replace("mp3", "png")}", "title":"{music}", "file":"music/{music}"}}')
        f.write(',\n') if music != music_list[-1] else f.write('\n')

    f.write(']; \n')

with open('./js/oil.js', 'w') as f:
    f.write('trackList = \n')
    f.write('[ \n')
    idx = 1
    music_list = sorted(os.listdir('./oil_music'))
    for music in music_list:
        if music[-4:] != '.mp3':
            os.remove("./oil_music/"+music)
            continue
        f.write(f'{{"icon":"cover/{music.replace("mp3", "png")}", "title":"{music}", "file":"oil_music/{music}"}}')
        f.write(',\n') if music != music_list[-1] else f.write('\n')

    f.write(']; \n')