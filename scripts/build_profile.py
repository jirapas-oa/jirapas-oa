"""Build GitHub-safe RPG interface panels; no dependencies required."""
from pathlib import Path
from html import escape

ASSETS = Path(__file__).resolve().parents[1] / 'assets'
BG, PANEL, LINE = '#101024', '#19172f', '#51416c'
WHITE, MUTED, PURPLE, CYAN, GOLD = '#f0eaff', '#b1a7c9', '#c4a2ff', '#8ce5e5', '#efcf95'

def text(x, y, value, size=20, color=WHITE, bold=False):
    return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{700 if bold else 400}">{escape(value)}</text>'

def rect(x, y, w, h, fill=PANEL, stroke=LINE):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'

def diamond(x, y, color=PURPLE):
    return f'<path d="M{x} {y-7}l7 7-7 7-7-7z" fill="{color}"/>'

def save(name, height, title, number, content, label):
    corners = ''.join(rect(x, y, 6, 6, GOLD, GOLD) for x, y in [(12,12),(942,12),(12,height-18),(942,height-18)])
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="{height}" viewBox="0 0 960 {height}" role="img" aria-label="{escape(label)}">
<title>{escape(label)}</title><rect width="960" height="{height}" fill="{BG}"/>
<g font-family="ui-monospace, SFMono-Regular, Consolas, Liberation Mono, monospace">
{rect(9,9,942,height-18,BG)}{corners}{text(32,48,number,17,GOLD)}{text(85,48,title,23,WHITE,True)}
<path d="M32 67H928" stroke="{LINE}"/>{content}</g></svg>'''
    (ASSETS / name).write_text(svg)

c = rect(32,90,272,224)
c += text(54,120,'CHARACTER CLASS',15,MUTED) + text(54,157,'DEMON LORD',27,PURPLE,True)
c += text(54,198,'REAL-WORLD ROLE',15,MUTED) + text(54,229,'Data Engineer',22,CYAN,True)
c += diamond(61,274,CYAN) + text(80,280,'Cyan slime companion',15,MUTED)
c += text(334,119,'PLAYER / jirapas-oa',18,GOLD) + text(334,162,'Data is my realm.',29,WHITE,True)
c += text(334,201,'Welcome to my corner of GitHub.',20,MUTED)
c += text(334,236,'Microsoft Fabric. AI Agents.',20,MUTED)
c += text(334,271,'And a new journey into DevOps.',20,MUTED)
c += text(334,307,'EXPLORE  /  BUILD  /  LEVEL UP',16,PURPLE)
save('character-sheet.svg',344,'CHARACTER SHEET','01',c,'jirapas-oa: Data Engineer. Demon Lord avatar. Microsoft Fabric, AI Agents, and a beginning DevOps journey.')

def skill_card(x,y,code,title,sub,status,color):
    return (rect(x,y,436,132) + rect(x+16,y+19,48,48,BG,color)
        + text(x+28,y+50,code,19,color,True) + text(x+82,y+43,title,22,WHITE,True)
        + text(x+82,y+73,sub,16,MUTED) + diamond(x+24,y+105,color) + text(x+43,y+111,status,15,color))

c = skill_card(32,90,'DE','Data Engineering','The core of my realm','MAIN ROLE',CYAN)
c += skill_card(492,90,'MF','Microsoft Fabric','My data platform focus','PLATFORM',PURPLE)
c += skill_card(32,240,'AI','AI Agent','Exploring the agent realm','INTEREST',GOLD)
c += skill_card(492,240,'DO','DevOps','A new skill tree begins','BEGINNING','#e7a3c4')
c += text(32,407,'SKILL TREE / Every new skill opens another path.',16,MUTED)
save('skill-inventory.svg',436,'SKILL INVENTORY','02',c,'Data Engineering: main role. Microsoft Fabric: platform. AI Agent: interest. DevOps: beginning.')

c = text(32,108,'THREE PATHS THROUGH THE REALM',16,MUTED)
paths = [('I','THE DATA REALM','Microsoft Fabric & data engineering',CYAN),('II','THE SUMMONING CIRCLE','AI Agents',PURPLE),('III','THE FORGE','DevOps / Beginning',GOLD)]
for i,(n,title,sub,col) in enumerate(paths):
    y = 130+i*101
    c += rect(32,y,896,85) + text(53,y+49,n,23,col,True)
    c += text(125,y+33,title,20,col,True) + text(125,y+62,sub,18,MUTED) + diamond(899,y+43,col)
c += text(32,465,'Explore my repositories through the Quest Log below.',17,MUTED)
save('quest-board.svg',494,'QUEST BOARD','03',c,'Three interests: Microsoft Fabric and data engineering; AI Agents; DevOps, beginning. These paths are not claims of completed projects.')

c = text(32,110,'CHOOSE YOUR DESTINATION',16,MUTED)
for x,code,title,sub,col in [(32,'01','QUEST LOG','Repositories',CYAN),(338,'02','TREASURE CHEST','Starred repositories',GOLD),(644,'03','THE GATEWAY','GitHub profile',PURPLE)]:
    c += rect(x,132,284,106) + text(x+18,162,code,16,col)
    c += text(x+18,192,title,20,col,True) + text(x+18,218,sub,16,MUTED)
c += text(32,279,'The portals below lead to my public GitHub pages.',17,MUTED)
save('world-map.svg',310,'WORLD MAP','04',c,'Choose repositories, starred repositories, or GitHub profile using the links below this panel.')

c = diamond(280,108,GOLD)+text(304,115,'SAVE POINT REACHED',27,GOLD,True)+diamond(665,108,GOLD)
c += text(204,158,'Thanks for visiting my realm, traveler.',21,WHITE)
c += text(252,196,'Until our paths cross again.',20,MUTED)
c += text(283,245,'jirapas-oa / END OF CHAPTER',17,PURPLE)
save('save-point.svg',282,'REST AT THE SAVE POINT','05',c,'Save point reached. Thanks for visiting my realm, traveler. Until our paths cross again. jirapas-oa.')
print('Built 5 SVG panels.')
