# CXT453 – Design Process and Perspective: Assignment 2
### Federal Institute of Science and Technology (FISAT)
**Department of Computer Science and Engineering**  
**Academic Year:** 2026-27 | **Course:** Design Process and Perspective (CXT453)  
**Max Marks:** 20 | **Target CO:** CO5 (PO3, PO5, PO9)

---

## 📌 Overview
This repository contains the standalone, individual Front-End User Interfaces (UIs) developed for students with **Roll Numbers: 28, 36, 45, and 53** in accordance with the assignment brief and NBA SAR 2025 rubrics.

As specified in the assignment guidelines, these are **pure presentation/UI-only implementations** (no backend/server functionality required), focusing on high-band evaluation criteria:
- **Concept & Relevance to Brief (5 Marks)**
- **UI/Visual Design & Layout (5 Marks)** (Typography, Color Theory, Visual Hierarchy, Spacing)
- **Functionality & Interaction Layout (4 Marks)** (Navigation structure, card layouts, reading/preview flows)
- **Content & User Communication (3 Marks)** (Authentic thematic copy, clear SDG alignments)
- **Presentation & Finishing (3 Marks)** (Clean, modern aesthetic, responsive on mobile & desktop)

---

## 🎯 Student Roll Number Mappings & Projects

| Roll No. | Assignment Question | Project Name | Brief Description | UN SDG Goal | Live Direct Link |
| :---: | :--- | :--- | :--- | :---: | :---: |
| **28** | **Question 2** *(Roll 15 - 28)* | **InkVerse Comics** | Comic story publication platform with visual narrative panels, chapter lists, character spotlights, and STEM literacy series. | **SDG 4**: Quality Education | [`roll-28/`](./roll-28/index.html) |
| **36** | **Question 3** *(Roll 29 - 42)* | **EduSphere Journal** | Academic educational blog & open resource publishing portal featuring peer-reviewed articles, visual architecture breakdowns, and topic filters. | **SDG 4**: Quality Education | [`roll-36/`](./roll-36/index.html) |
| **45** | **Question 4** *(Roll 43 - 56)* | **CircuTech** | Advertisement showcase for modular, repairable eco-laptops, fairtrade smartphones, and solar peripherals with circular trade-in incentives. | **SDG 12**: Responsible Consumption & Production | [`roll-45/`](./roll-45/index.html) |
| **53** | **Question 4** *(Roll 43 - 56)* | **VoltPulse** | Cyber-acoustic advertising campaign for next-gen ultra-low energy audio gear and wearable electronics utilizing recycled rare-earth components. | **SDG 12**: Responsible Consumption & Production | [`roll-53/`](./roll-53/index.html) |

---

## 🚀 How to Host on GitHub Pages (1-Click Deployment)

The repository has been structured so that GitHub Pages automatically serves the central hub and all four student UIs without any build steps.

1. **Create a new repository** on GitHub (e.g. named `cxt453-assignment-2` or `fisat-cxt453-uis`).
2. **Push this folder to your repository**:
   ```bash
   git init
   git add .
   git commit -m "Add CXT453 Assignment 2 UIs for Roll 28, 36, 45, 53"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<your-repo-name>.git
   git push -u origin main
   ```
3. **Enable GitHub Pages**:
   - Go to your repository on GitHub.
   - Click **Settings** (gear icon) > **Pages** (under Code and automation in the left sidebar).
   - Under **Build and deployment > Source**, select **Deploy from a branch**.
   - Under **Branch**, select `main` and `/ (root)`, then click **Save**.
4. In ~30-60 seconds, your site will be live at:
   ```
   https://<your-username>.github.io/<your-repo-name>/
   ```
   - Main Portal Hub: `https://<your-username>.github.io/<your-repo-name>/`
   - Roll 28 UI: `https://<your-username>.github.io/<your-repo-name>/roll-28/`
   - Roll 36 UI: `https://<your-username>.github.io/<your-repo-name>/roll-36/`
   - Roll 45 UI: `https://<your-username>.github.io/<your-repo-name>/roll-45/`
   - Roll 53 UI: `https://<your-username>.github.io/<your-repo-name>/roll-53/`

---

## 📂 File Directory Structure

```text
c:\report/
├── index.html            # Main Portal Hub (All 4 Roll Numbers & Assignment Info)
├── README.md             # Documentation and GitHub hosting instructions
├── roll-28/
│   └── index.html        # Roll No 28: Comic Story Publication UI (SDG 4)
├── roll-36/
│   └── index.html        # Roll No 36: Educational Posts Publishing UI (SDG 4)
├── roll-45/
│   └── index.html        # Roll No 45: Sustainable Electronics Advert UI (SDG 12)
└── roll-53/
    └── index.html        # Roll No 53: Next-Gen Electronics Advert UI (SDG 12)
```
