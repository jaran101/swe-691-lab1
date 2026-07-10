# swe-691-lab1
# บทที่ 1: ภูมิทัศน์วิศวกรรมซอฟต์แวร์ยุคใหม่ (Landscape of Modern Software Engineering)

## ภาพรวม

บทนี้อธิบายวิวัฒนาการของวิศวกรรมซอฟต์แวร์ ตั้งแต่ยุค Waterfall จนถึงยุค **Agentic Development** ที่ AI สามารถช่วยเขียน แก้ไข และทดสอบโค้ดได้อัตโนมัติ โดยเน้นว่า AI ไม่ได้มาแทนที่หลักการเดิมของ Software Engineering แต่เป็นเครื่องมือที่ช่วยเพิ่มประสิทธิภาพการทำงาน

---

# 1. วิวัฒนาการของ Software Engineering

```
1968
Software Crisis
      │
      ▼
SDLC / OOP
      │
      ▼
Agile (2001)
      │
      ▼
DevOps (2010s)
      │
      ▼
AI Coding Tools (2021+)
      │
      ▼
Agentic Development (2024+)
```

### แนวคิดสำคัญ

- AI เป็น "วิวัฒนาการ" ของ Software Engineering
- หลักการเดิม เช่น
  - การออกแบบระบบ
  - การทดสอบ
  - Git
  - Code Review
  ยังมีความสำคัญเหมือนเดิม

---

# 2. AI กลายเป็นมาตรฐานของการพัฒนา Software

ปัจจุบัน AI Coding Tool กลายเป็นส่วนหนึ่งของ Workflow

คำถามไม่ใช่

> "ใช้ AI หรือไม่"

แต่คือ

> "ใช้ AI อย่างไรให้ได้คุณภาพ"

รายงาน DORA ระบุว่า

AI จะขยายสิ่งที่ทีมมีอยู่แล้ว

ทีมที่มีกระบวนการดี
→ ได้ประโยชน์มาก

ทีมที่กระบวนการไม่ดี
→ งานเร็วขึ้นแต่ Bug มากขึ้น

---

# 3. Software Engineering คืออะไร

Software Engineering ไม่ใช่แค่การเขียนโปรแกรม

แต่เป็นศาสตร์ที่รวม

- การออกแบบระบบ
- การสื่อสารในทีม
- การบริหารโครงการ
- การทดสอบ
- การบำรุงรักษา
- จริยธรรม

เป้าหมายคือ

> สร้างซอฟต์แวร์ที่วัดผลได้ มีคุณภาพ และดูแลระยะยาวได้

---

# 4. SDLC ที่ควรรู้จัก

โมเดลหลักของ Software Development Life Cycle

| Model | จุดเด่น |
|---------|----------|
| Waterfall | ทำงานเป็นลำดับขั้น |
| V-Model | พัฒนาควบคู่กับการทดสอบ |
| Incremental | เพิ่มความสามารถทีละส่วน |
| Spiral | เน้นการบริหารความเสี่ยง |
| Agile | ส่งมอบเร็ว ปรับตัวไว |

---

# 5. Brooks : ความซับซ้อนมี 2 แบบ

## Accidental Complexity

คือความยุ่งยากที่ไม่ได้เกิดจากปัญหาจริง เช่น

- จำ Syntax
- Boilerplate Code
- หา API
- Config

AI ช่วยได้มาก

---

## Essential Complexity

คือความยากของปัญหาจริง เช่น

- Requirement ไม่ชัด
- การออกแบบระบบ
- Trade-off
- Business Logic

AI ช่วยได้น้อย

เพราะยังต้องใช้การตัดสินใจของมนุษย์

---

## สรุป

AI ลด

✅ Accidental Complexity

แต่ยังแทบลด

❌ Essential Complexity

ไม่ได้

---

# 6. AI Coding Tool 4 Generation

| Generation | ความสามารถ |
|------------|-------------|
| Gen 1 | Auto Complete |
| Gen 2 | LLM เติมโค้ดในไฟล์ |
| Gen 3 | Chat + เข้าใจทั้ง Repository |
| Gen 4 | AI Agent ทำงานหลายขั้นตอนเอง |

---

## Gen 1

- เดาคำถัดไป
- ยังไม่เข้าใจ Project

ตัวอย่าง

- Tabnine
- Kite

---

## Gen 2

LLM เริ่มช่วยเติมโค้ด

ตัวอย่าง

- GitHub Copilot

สามารถ

- เติม Function
- เติม Code Block

---

## Gen 3

AI อ่านได้หลายไฟล์

สามารถ

- อธิบาย Codebase
- หา Bug
- Refactor

ตัวอย่าง

- Cursor
- Copilot Chat

---

## Gen 4

Agentic Development

AI สามารถ

- วางแผน
- รันคำสั่ง
- แก้หลายไฟล์
- Run Test
- เปิด Pull Request

ตัวอย่าง

- Claude Code
- Devin

---

# 7. Productivity ของ AI

ผลวิจัยให้ผลต่างกัน

บางงาน

เร็วขึ้น 55%

บางงาน

ช้าลง 19%

เหตุผลหลัก

## 1. ประเภทของงาน

งานเขียนใหม่

AI ช่วยมาก

งานแก้ระบบเดิม

AI ช่วยน้อย

---

## 2. ความคุ้นเคยกับ Codebase

ถ้ารู้ระบบดีอยู่แล้ว

AI อาจไม่ช่วยมาก

---

## 3. Process ของทีม

ทีมที่มี

- Test
- Code Review
- CI/CD

จะได้ประโยชน์จาก AI มากกว่า

---

## บทเรียน

อย่าเชื่อตัวเลข Productivity เพียงตัวเลขเดียว

ต้องดูบริบทของงานด้วย

---

# 8. Trust Level ของ AI

กำหนดระดับความไว้ใจ AI

| Level | ความหมาย |
|--------|-----------|
| 1 | ไม่ใช้ AI |
| 2 | AI ให้คำแนะนำ |
| 3 | AI เติมโค้ด มนุษย์ตรวจทุกครั้ง |
| 4 | AI สร้าง Function/Class มนุษย์ตรวจ Logic |
| 5 | AI Agent ทำงานเอง มนุษย์ตรวจผลลัพธ์ |

---

## หลักการเลือก Trust Level

ขึ้นอยู่กับ

**Failure Cost**

ถ้าพลาดแล้วเสียหายมาก

ใช้ Trust Level ต่ำ

เช่น

- Security
- Database
- Production

ถ้าพลาดแล้วแก้ได้ง่าย

ใช้ระดับสูงได้

เช่น

- Prototype
- Script
- Refactoring

---

# 9. ทักษะที่ตลาดแรงงานต้องการ

## ทักษะใหม่

- Prompt Engineering
- Context Engineering
- RAG
- AI Evaluation
- AI Agent Development

---

## ทักษะพื้นฐานที่ยังสำคัญ

- System Design
- SQL
- Database Design
- Refactoring
- Testing
- Git
- Security
- Observability

---

# 10. ข้อผิดพลาดที่พบบ่อย

### 1. เชื่อ Prompt จาก Social Media

ควรทดลองกับงานของตนเองก่อน

---

### 2. เปลี่ยน Tool บ่อยเกินไป

ควรใช้ Tool หลักให้คล่องก่อน

---

### 3. เชื่อตัวเลข Productivity

ผลวิจัยแต่ละงานมีบริบทต่างกัน

---

### 4. เชื่อ AI มากเกินไป

งานสำคัญ เช่น

- Delete Database
- Deploy
- Force Push

ต้องมีมนุษย์ตรวจสอบเสมอ

---

# Key Takeaways

- AI เป็นวิวัฒนาการของ Software Engineering ไม่ใช่สิ่งที่มาแทนที่
- หลักการพื้นฐาน เช่น SDLC, Testing, Git และ System Design ยังคงสำคัญ
- AI ช่วยลด **Accidental Complexity** ได้มาก แต่ยังช่วย **Essential Complexity** ได้จำกัด
- AI Coding Tools พัฒนาเป็น 4 ยุค ตั้งแต่ Auto Complete จนถึง Agentic Development
- ประสิทธิภาพของ AI ขึ้นกับประเภทงาน ความคุ้นเคยกับระบบ และกระบวนการของทีม
- ควรเลือก **Trust Level** ให้เหมาะกับความเสี่ยงของงาน
- ทักษะสำคัญในยุค AI คือการออกแบบระบบ การทดสอบ การประเมินผล AI และการทำงานร่วมกับ AI อย่างมีวิจารณญาณ

---

# คำศัพท์สำคัญ

| คำศัพท์ | ความหมาย |
|----------|-----------|
| Software Engineering | วิศวกรรมซอฟต์แวร์ |
| SDLC | วงจรการพัฒนาซอฟต์แวร์ |
| Waterfall | โมเดลพัฒนาแบบลำดับขั้น |
| Agile | การพัฒนาแบบยืดหยุ่น |
| DevOps | การรวมการพัฒนาและการปฏิบัติการ |
| Agentic Development | การพัฒนาซอฟต์แวร์โดยใช้ AI Agent |
| Accidental Complexity | ความซับซ้อนจากเครื่องมือหรือกระบวนการ |
| Essential Complexity | ความซับซ้อนที่เกิดจากปัญหาจริง |
| Trust Level | ระดับความไว้ใจในการให้ AI ทำงาน |
| Boilerplate Code | โค้ดโครงสร้างที่ต้องเขียนซ้ำ ๆ |
| Refactoring | การปรับปรุงโค้ดโดยไม่เปลี่ยนพฤติกรรม |
| Code Review | การตรวจสอบโค้ดโดยมนุษย์ |
| Productivity | ประสิทธิภาพในการทำงาน |
| RAG | Retrieval-Augmented Generation |
| Context Engineering | การจัดเตรียมบริบทให้ AI ทำงานได้มีประสิทธิภาพ |
