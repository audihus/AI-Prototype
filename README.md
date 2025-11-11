# 🏛️ LegalMate Assistant

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**LegalMate** is a location-aware, jurisdiction-specific legal chatbot assistant designed to help Indonesian users quickly find relevant local and national regulations. Built with Python and Tkinter, this prototype demonstrates a simple but powerful approach to making legal information more accessible.

---

## 🎯 Features

- **📍 Location-Aware**: Automatically filters regulations based on your selected city/region
- **🤖 Smart Agent Character**: Friendly judge mascot (👨‍⚖️) that guides you through legal queries
- **🔍 Natural Language Processing**: Understands casual queries in natural language
- **📜 Citation & Status**: Every answer includes official legal basis, document ID, effective date, and current status
- **⚡ Quick Action Buttons**: Fast access to popular legal topics
- **🎨 Modern GUI**: Clean, professional interface with color-coded responses
- **🌐 Multi-jurisdiction**: Supports both local (city/regency) and national regulations

---

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- Tkinter (usually comes pre-installed with Python)

### Steps

1. **Clone or download the repository**
```bash
git clone https://github.com/yourusername/legalmate-assistant.git
cd legalmate-assistant
```

2. **Run the application**
```bash
python chatbot_hukum.py
```

That's it! No additional dependencies required.

---

## 📖 How to Use

### Starting the Application

1. Run `python chatbot_hukum.py`
2. The chatbot will greet you with a welcome message
3. Your default location is set to **Yogyakarta**

### Changing Location

Use the **dropdown menu** at the top to select your city:
- Jakarta
- Bandung
- Yogyakarta
- Surabaya
- National (for nationwide regulations)

The bot will automatically filter relevant regulations for your location.

### Asking Questions

You can ask questions in **two ways**:

#### 1. Type Your Query
Simply type your question in natural language in the input field and press **Enter** or click **Send**.

#### 2. Quick Action Buttons
Click on one of the quick topic buttons:
- 🚬 **Vape** - Vaping regulations
- 💰 **THR** - Holiday pay rules
- 🅿️ **Parking** - Parking regulations

---

## 💬 Query Examples

### Vaping / E-Cigarette Regulations

**Sample Queries:**
```
Is vaping allowed here?
Can I use e-cigarettes in public?
Are there vape restrictions?
What's the rule on vaping?
Is vaping banned in Bandung?
```

**Expected Response:**
```
💡 Information about VAPE in Bandung:

Vaping is banned in all indoor public places.

📜 Legal Basis: Perda Kota Bandung No.12/2023, Article 7(2)
✅ Status: In Force
📅 Effective since: 2023-06-01
🆔 Document ID: PERDA-BDG-12-2023
```

---

### THR (Holiday Pay) Regulations

**Sample Queries:**
```
When must THR be paid?
What are the rules for holiday pay?
THR payment deadline?
How much is THR?
When should employers pay holiday bonus?
```

**Expected Response:**
```
💡 Information about THR nationally:

THR must be paid at least 7 days before the holiday; 1 month salary for >=12 months worked.

📜 Legal Basis: Permenaker 5/2025 Article 3
✅ Status: In Force
📅 Effective since: 2025-03-01
🆔 Document ID: PERMEN-THR-2025
```

---

### Parking Regulations

**Sample Queries:**
```
What are the parking rules?
Can I park here?
Parking fines in Jakarta?
Is sidewalk parking allowed?
What's the penalty for illegal parking?
```

**Expected Response (Jakarta):**
```
💡 Information about PARKING in Jakarta:

Illegal parking on sidewalks is subject to a fine of Rp 500,000.

📜 Legal Basis: Perda DKI Jakarta No.8/2024, Article 15
✅ Status: In Force
📅 Effective since: 2024-01-15
🆔 Document ID: PERDA-JKT-08-2024
```

---

### Annual Leave / Employee Rights

**Sample Queries:**
```
How much leave am I entitled to?
What are my annual leave rights?
Employee vacation days?
How many days off can I take?
```

**Expected Response:**
```
💡 Information about LEAVE nationally:

Employees are entitled to at least 12 working days of annual leave after 12 months of employment.

📜 Legal Basis: Law No.13/2003 Article 79(c)
✅ Status: In Force
📅 Effective since: 2003-03-25
🆔 Document ID: UU-KETENAGAKERJAAN
```

---

### Location-Specific Queries

#### Example 1: Vaping in Yogyakarta
**Location:** Yogyakarta  
**Query:** `Is vaping allowed in tourist areas?`

**Response:**
```
💡 Information about VAPE in Yogyakarta:

Vaping is prohibited in tourist areas and places of worship.

📜 Legal Basis: Perda DIY No.5/2024, Article 12
✅ Status: In Force
📅 Effective since: 2024-03-01
🆔 Document ID: PERDA-YK-05-2024
```

#### Example 2: Parking in Surabaya (No Local Rule)
**Location:** Surabaya  
**Query:** `What are the parking rules here?`

**Response:**
```
❌ No regulations found about parking for Surabaya. Try changing location or check official sources.
```

---

### Unsupported Topic Queries

**Query:** `What about copyright law?`

**Response:**
```
🤔 Sorry, I don't understand your question yet. Try asking about:
- Vaping/e-cigarettes
- THR (Holiday Pay)
- Parking
- Employee leave
```

---

## 🗂️ Data Structure

The chatbot uses a simple JSON-like structure stored in data.json:

```python
{
    "doc_id": "PERDA-BDG-12-2023",
    "area": "Bandung",
    "topic": "vape",
    "snippet": "Vaping is banned in all indoor public places.",
    "citation": "Perda Kota Bandung No.12/2023, Article 7(2)",
    "status": "in_force",
    "effective_date": "2023-06-01"
}
```

### Adding New Rules

To add more regulations:

1. Open data.json
2. Add new entries to the data.json list
3. Update `TOPIC_KEYWORDS` in chatbot.py if adding new topics
4. Restart the application

---

## 🎨 Interface Guide

### Color Coding

- **🟢 User Messages**: Green, bold text
- **🔵 Bot Messages**: Dark blue text
- **🔴 Citations**: Red, italic text
- **💙 Status Info**: Blue text

### Components

1. **Header**: Shows the agent mascot and app title
2. **Location Selector**: Dropdown to choose your city
3. **Chat Display**: Scrollable conversation history
4. **Quick Buttons**: Fast access to popular topics
5. **Input Field**: Type your questions here

---

## 🔧 Technical Details

### Supported Topics

| Topic | Keywords | Regions |
|-------|----------|---------|
| Vaping | vape, vaping, e-cigarette | Bandung, Yogyakarta, National |
| THR | thr, holiday pay, bonus | National |
| Parking | parking, park | Jakarta |
| Leave | leave, annual leave, vacation | National |

### Algorithm

```
1. Receive user query + current location
2. Detect topic using keyword matching
3. Filter rules by topic
4. Prefer local rules for selected city
5. Fallback to national rules if no local match
6. Return formatted response with citation
```

---

## ⚠️ Disclaimer

**Important:** This is a prototype demonstration tool for educational purposes only. 

- Always verify legal information with official sources
- Consult licensed legal professionals for legal advice
- The bot may not have the most current regulations
- This tool does not constitute legal advice