import re

# Open the UG.txt file and store contents to variable
f = open("UG.txt", "r")
song_text = f.read()


# Remove the empty lines
lines = song_text.split("\n")
song_text = "\n".join([line for line in lines if line != ''])


# Replace '[Heading]' with 'Heading:' using RegEx. Adds empty line before each heading
headings = re.findall(r"\[(.*)\]", song_text)

for heading in headings:
    song_text = song_text.replace("[" + heading + "]", "\n" + heading.capitalize() + ":")


# Remove text before Intro:
if 'Intro:' in song_text:
    song_text = song_text[song_text.find("Intro:"):]


# Replace repeated choruses with (Repeat Chorus)
n = 1
sections = song_text.split("\n\n")
for position, section in enumerate(sections):
    if 'Chorus:' in section:
        if n > 1:
            sections[position] = '(Repeat Chorus)'
        n += 1
song_text = ("\n\n").join(sections)

# Save text to 'OnSong.txt'
with open("OnSong.txt", "w") as f:
    f.write(song_text)

