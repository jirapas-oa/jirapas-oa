# วิธีใช้โปรไฟล์ GitHub

ธีม Pixel RPG × Anime สำหรับ `jirapas-oa` พร้อมตัวละครจอมมาร

1. สร้าง repository แบบ **Public** ชื่อ **jirapas-oa** ในบัญชี `jirapas-oa`
2. อัปโหลด `README.md` และโฟลเดอร์ `assets` โดยรักษาชื่อและตำแหน่งไฟล์ไว้
3. Commit ไฟล์ แล้วเปิดหน้า `https://github.com/jirapas-oa` เพื่อดูโปรไฟล์

GitHub จะแสดง README เมื่อ repository เป็น public มีชื่อเดียวกับ username และมี `README.md` ที่ไม่ว่างอยู่ที่รากของ repository

เอกสารอ้างอิง: https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme

## ไฟล์ภาพ

- `assets/hero-demon-lord.png` — แบนเนอร์ที่ README ใช้อยู่
- `assets/hero-pixel-rpg.png` — แบนเนอร์ต้นฉบับตัวละครนักผจญภัย เก็บไว้เป็นทางเลือก

หน้าโปรไฟล์มีแบนเนอร์จอมมาร, Character Sheet, Skill Inventory, Quest Board, World Map และ Save Point ครบทั้งหน้า

ข้อมูลที่ใช้: Data Engineer, Microsoft Fabric, AI Agent และ DevOps ระดับเริ่มต้น ตามที่เจ้าของโปรไฟล์ระบุ ไม่มีคะแนนสกิลหรือผลงานสมมติ

## แก้ไขดีไซน์

- แก้ข้อความแนะนำด้านบนและลิงก์ใน `README.md`
- แก้ข้อความหรือสีของการ์ดใน `scripts/build_profile.py` แล้วรัน `python3 scripts/build_profile.py`
- SVG เป็นภาพนิ่ง ไม่มี JavaScript หรือฟอนต์ภายนอก
- ลิงก์กดได้อยู่ใน README ใต้ภาพ World Map และ Quest Board
- อัปโหลด README และโฟลเดอร์ assets ทั้งหมดเพื่อให้รูปแสดงครบ

Repository โปรไฟล์: https://github.com/jirapas-oa/jirapas-oa

## ชุด Animation และกราฟ

- `assets/avatar/demon-lord-avatar.gif` — จอมมารกะพริบตาและออร่าใน README
- `assets/avatar/demon-lord-avatar.png` — ภาพนิ่งสำหรับตั้ง avatar ของบัญชี
- กราฟ 31 วันใช้บริการ https://github.com/Ashutosh00710/github-readme-activity-graph โดยโหลดข้อมูลจาก username สาธารณะ อาจมี cache หรือหยุดให้บริการชั่วคราว
- `assets/contribution-realm.gif` — แผนที่ contribution จริง ณ วันที่ระบุในภาพ มีไฟวิ่งตกแต่ง ไม่ใช่ข้อมูลสด
- อัปเดตภาพ snapshot: เรียก GitHub GraphQL เพื่อรับ `user.contributionsCollection.contributionCalendar` พร้อม `totalContributions`, `weeks.contributionDays` ที่มี `date`, `contributionCount`, `weekday`; บันทึก JSON แล้วรัน `python3 scripts/build_activity.py path/to/data.json` (ต้องมี Pillow)
- อัปโหลด `README.md` และโฟลเดอร์ `assets` ไปที่ repository เดิมเพื่อใช้รุ่นนี้
- การอัปโหลด README ไม่เปลี่ยน avatar ของบัญชี: ตั้งรูปที่ GitHub Settings → Public profile → Profile picture
- `profile-preview.png` เป็นภาพตัวอย่างรุ่นก่อนเพิ่ม Animation/กราฟ

หน้าโปรไฟล์: https://github.com/jirapas-oa
