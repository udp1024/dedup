# macOS Duplicate Deduper

A high‑performance, native‑feeling macOS application for identifying and safely removing duplicate files across any directory structure — including OneDrive local caches, external drives, and network volumes.

Built with **Python**, **PyObjC**, and a **SQLite‑backed caching engine**, the tool is designed for reliability, clarity, and scale. It handles hundreds of gigabytes and millions of files while keeping the user fully in control.

---

## 🚀 Features

### 🔍 Two‑Stage Deduplication Pipeline
1. **Fast size‑based scan**  
   Quickly identifies potential duplicates without reading file contents.

2. **Targeted hashing**  
   Only hashes files the user approves, dramatically reducing unnecessary work.

### 🖥 Native macOS UI (PyObjC)
- Directory picker  
- Expandable duplicate groups  
- Checkboxes for file selection  
- QuickLook previews  
- “Show in Finder” integration  
- Group‑local sorting (name, path)  
- Summary panel showing reclaimable space  
- Progress bars for scanning and hashing  

### ⚡ SQLite‑Backed Hash Cache
- Stores file metadata + hashes  
- Avoids re‑hashing unchanged files  
- Makes repeat scans dramatically faster  

### 🛡 Safety First
- No automatic deletions  
- All deletions go to macOS Trash  
- User reviews every step  

---

## 🧱 Architecture Overview

The system is composed of three layers:

- **UI Layer (PyObjC)**  
- **Backend Logic (Python)**  
- **SQLite Cache + File System**

Architecture diagrams are available in the `/docs` folder.

---

## 📦 Installation

```bash
git clone https://github.com/<yourname>/macos-duplicate-deduper
cd macos-duplicate-deduper
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python deduper_ui.py


🗂 Roadmap
[ ] Checkbox UI for file selection

[ ] QuickLook preview panel

[ ] “Show in Finder” button

[ ] Group‑local sorting

[ ] Expand/Collapse All

[ ] SQLite caching layer

[ ] Background threading for hashing

[ ] macOS .app bundle

[ ] Notarized distribution

[ ] Mac App Store submission (optional)

📝 License
This project is licensed under the MIT License.
See LICENSE for details.

⭐ Acknowledgments
Built with Python, PyObjC, and a deep respect for deterministic, safe, and transparent tooling.
