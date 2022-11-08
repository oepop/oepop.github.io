import os
print(os.listdir('./music')[-1])

with open('./scripts/playlist.js', 'w') as f:
    f.write('tracklist = \n')
    f.write('[ \n')
    idx = 1
    for music in os.listdir('./music'):
        f.write(f'{{name:"{music}", src:"{music}"}}')
        f.write(',\n') if music != os.listdir('./music')[-1] else f.write('\n')

    f.write(']; \n')