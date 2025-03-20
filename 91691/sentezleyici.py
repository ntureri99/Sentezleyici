import pygame  # müzik eklemek için kullanılır 
import play

instrument = 0

# Arayüz
play.set_backdrop('light blue')  # Arkaplan
introduce1 = play.new_text(words='Piano for fun!', x=0, y=250)
introduce2 = play.new_text(words='Create your melody by pressing the keys', x=0, y=200)

# Butonları oluşturduk
key_play_melody = play.new_box(
    color='light green', border_color='black', border_width=1,
    x=-110, y=-80, width=120, height=50)
kpm = play.new_text(words='play melody', x=-110, y=-80, font_size=20)

key_clear_melody = play.new_box(
    color='light pink', border_color='black', border_width=1,
    x=110, y=-80, width=120, height=50)
kcm = play.new_text(words='clear melody', x=110, y=-80, font_size=20)

sound_clear_melody = pygame.mixer.Sound('clear_melody.wav')  # Etkileşim müziği

# Enstrümanlar
ch_p = play.new_circle(color='black', x=-180, y=-150, radius=10, border_color='black', border_width=2)
txt_p = play.new_text(words='piano', x=-145, y=-150, font_size=20)

ch_g = play.new_circle(color='light blue', x=-80, y=-150, radius=10, border_color='black', border_width=2)
txt_g = play.new_text(words='guitar', x=-45, y=-150, font_size=20)

ch_v = play.new_circle(color='light blue', x=20, y=-150, radius=10, border_color='black', border_width=2)
txt_v = play.new_text(words='violin', x=55, y=-150, font_size=20)

ch_f = play.new_circle(color='light blue', x=120, y=-150, radius=10, border_color='black', border_width=2)
txt_f = play.new_text(words='flute', x=155, y=-150, font_size=20)

# Piyano tuşları ve sesler
keys = []
key_labels = []
sounds = []
notes = ["Do", "Re", "Mi", "Fa", "Sol", "La", "Si", "Do"]  # Nota isimleri

for i in range(4):  # 4 enstrüman var
    sounds.append([])

for i in range(8):  # 8 tuş
    key_x = -180 + i * 50
    key = play.new_box(color="white", border_color="black", border_width=3, x=key_x, y=50, width=40, height=100)
    keys.append(key)

    # Nota isimlerini tuşların içine yaz
    label = play.new_text(words=notes[i], x=key_x, y=50, font_size=20, color="black")
    key_labels.append(label)

    # Ses dosyaları ekleniyor
    sounds[0].append(pygame.mixer.Sound(f"pia{i+1}.ogg"))
    sounds[1].append(pygame.mixer.Sound(f"git{i+1}.ogg"))
    sounds[2].append(pygame.mixer.Sound(f"vio{i+1}.ogg"))
    sounds[3].append(pygame.mixer.Sound(f"fl{i+1}.ogg"))

melody = []

@play.when_program_starts
async def start():
    pygame.mixer_music.load("hi-1.mp3")  # Fon müziği
    pygame.mixer_music.play()
    await play.timer(seconds=4.5)

@ch_p.when_clicked
def set_piano():
    global instrument
    instrument = 0 
    ch_p.color = "black"
    ch_g.color = "light blue"
    ch_v.color = "light blue"
    ch_f.color = "light blue"

@ch_g.when_clicked
def set_guitar():
    global instrument
    instrument = 1 
    ch_p.color = "light blue"
    ch_g.color = "black"
    ch_v.color = "light blue"
    ch_f.color = "light blue"

@ch_v.when_clicked
def set_violin():
    global instrument
    instrument = 2
    ch_p.color = "light blue"
    ch_g.color = "light blue"
    ch_v.color = "black"
    ch_f.color = "light blue"

@ch_f.when_clicked
def set_flute():
    global instrument
    instrument = 3
    ch_p.color = "light blue"
    ch_g.color = "light blue"
    ch_v.color = "light blue"
    ch_f.color = "black"

@key_clear_melody.when_clicked
def clear():
    global melody
    melody.clear()
    sound_clear_melody.play()

@key_play_melody.when_clicked
async def play_m():
    global instrument
    for i in melody:
        await play.timer(seconds=0.5)
        sounds[instrument][i].play()

@play.repeat_forever
async def play_piano():
    for i in range(len(keys)):
        if keys[i].is_clicked:
            keys[i].color = 'light grey'
            sounds[instrument][i].play()
            await play.timer(seconds=0.3)
            keys[i].color = 'white'
            melody.append(i)

play.start_program()
