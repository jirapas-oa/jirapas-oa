"""Render a dated contribution-map snapshot; pass GitHub GraphQL JSON as argv[1]."""
import json, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

root = Path(__file__).resolve().parents[1]
data = json.loads(Path(sys.argv[1]).read_text())
calendar = data['data']['user']['contributionsCollection']['contributionCalendar']
weeks = calendar['weeks']
days = [d for w in weeks for d in w['contributionDays']]
font_paths = ['/System/Library/Fonts/Menlo.ttc', '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf']
font_path = next(p for p in font_paths if Path(p).exists())
def font(size): return ImageFont.truetype(font_path, size)
base = Image.new('RGB', (960, 300), '#101024')
d = ImageDraw.Draw(base)
d.rectangle((9,9,950,290), outline='#51416c', width=2)
d.text((30,27),'THE CONTRIBUTION REALM',font=font(24),fill='#f0eaff')
d.text((30,66),f"{calendar['totalContributions']} contributions / {days[0]['date']} to {days[-1]['date']}",font=font(16),fill='#c4a2ff')
palette=['#242039','#51416c','#7954a6','#b887ee','#8ce5e5']
max_count=max(1,max(day['contributionCount'] for day in days))
for x, week in enumerate(weeks):
    for day in week['contributionDays']:
        count=day['contributionCount']; color=palette[0 if count==0 else min(4,1+int(3*count/max_count))]
        px=34+x*17;py=103+day['weekday']*17
        d.rectangle((px,py,px+12,py+12),fill=color)
d.text((30,240),'Actual GitHub activity / moving light is decorative',font=font(15),fill='#b1a7c9')
d.text((30,266),'SNAPSHOT '+days[-1]['date'],font=font(13),fill='#b1a7c9')
for i,color in enumerate(palette):d.rectangle((786+i*26,254,803+i*26,271),fill=color)
base.save(root/'assets/contribution-realm.png')
frames=[]
for index in range(40):
    frame=base.copy(); draw=ImageDraw.Draw(frame)
    x=34+int(index/39*(len(weeks)-1))*17
    draw.line((x,96,x+12,96),fill='#efcf95',width=3)
    draw.line((x,225,x+12,225),fill='#efcf95',width=3)
    frames.append(frame.quantize(colors=64))
frames[0].save(root/'assets/contribution-realm.gif',save_all=True,append_images=frames[1:],duration=90,loop=0,optimize=True,disposal=2)
print('Created contribution-realm.gif and PNG snapshot.')
