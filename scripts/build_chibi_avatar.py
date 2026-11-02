"""Assemble generated animation frames into a GIF and a static avatar."""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets' / 'avatar'
sheet = Image.open(OUT / 'chibi-demon-sprites.png').convert('RGB')
w, h = sheet.size
frames = []
for row in range(2):
    for col in range(4):
        box = (round(col*w/4), round(row*h/2), round((col+1)*w/4), round((row+1)*h/2))
        frames.append(sheet.crop(box).resize((320, 320), Image.Resampling.NEAREST))

# One shared palette avoids color flicker across frames.
atlas = Image.new('RGB', (320*4, 320*2))
for i, frame in enumerate(frames):
    atlas.paste(frame, ((i%4)*320, (i//4)*320))
palette = atlas.quantize(colors=192)
indexed = [f.quantize(palette=palette, dither=Image.Dither.NONE) for f in frames]
indexed[0].save(OUT / 'chibi-demon-avatar.gif', save_all=True,
    append_images=indexed[1:], duration=[1100, 250, 90, 110, 90, 250, 250, 350],
    loop=0, disposal=2, optimize=True)
frames[0].save(OUT / 'chibi-demon-avatar.png', optimize=True)

gif = Image.open(OUT / 'chibi-demon-avatar.gif')
assert gif.n_frames == 8 and gif.size == (320, 320)
assert (OUT / 'chibi-demon-avatar.gif').stat().st_size < 1_000_000
assert (OUT / 'chibi-demon-avatar.png').stat().st_size < 1_000_000
print(f'GIF: {gif.n_frames} frames, 320 x 320, {(OUT / "chibi-demon-avatar.gif").stat().st_size:,} bytes')
print(f'PNG: 320 x 320, {(OUT / "chibi-demon-avatar.png").stat().st_size:,} bytes')
