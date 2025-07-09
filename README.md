
# BMIVitals – Advanced BMI Calculator with Health Insights & Visualization

**BMIVitals** is a responsive, feature-rich BMI calculator web app built with **Flask**. It helps users calculate their **Body Mass Index (BMI)** using metric or imperial units and visually displays the result using an **interactive gauge**, along with health risk, BMI Prime, Ponderal Index, and more.

🌐 **Live Demo**: [https://bmivitals.vercel.app](https://bmivitals.vercel.app)

---

## 🔧 Features

- 🧮 BMI calculation with both:
  - **Centimeter / Kilograms**
  - **Feet & Inches / Pounds**
- 🎯 **Interactive BMI Gauge**: visually shows the user's BMI range
- 📊 Displays additional insights:
  - **BMI Prime**
  - **Ponderal Index**
  - **Healthy Weight Range**
- ⚠️ Health risk categories (Normal, Overweight, Obese I, etc.)
- 📸 **Save Result as PNG Image** with one click (html2canvas)
- 📚 Educational section on BMI limitations and explanation
- ✅ Flash messages for form feedback
- 🧪 **Automated Selenium testing** for real input validation
- 🎨 Clean, responsive UI using **Bootstrap 5** + custom CSS
- 🔁 Toggle between height input types dynamically

---

## 🧰 Tech Stack

| Layer         | Tools / Libraries                            |
|---------------|-----------------------------------------------|
| Frontend      | HTML, CSS, JS (Vanilla), Bootstrap 5          |
| Backend       | Python 3, Flask                               |
| Visualization | CSS Gauge UI + Needle Rotation Logic          |
| Screenshot    | [html2canvas](https://html2canvas.hertzen.com) |
| Testing       | Selenium, ChromeDriver, unittest               |
| Deployment    | Vercel / Netlify (via config files)            |

---

## 📁 Folder Structure

```
bmivitals/
├── static/                  # style.css, script.js, icons/
├── templates/               # index.html, about.html
├── app.py                   # Main Flask backend
├── test_bmi.py              # Selenium UI testing script
├── requirements.txt
├── runtime.txt              # For Netlify
├── vercel.json              # For Vercel deployment
├── netlify.toml             # Optional Netlify settings
└── README.md
```

---

## 🚀 Run the Project Locally

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/bmivitals.git
cd bmivitals
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scriptsctivate
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Run the Flask App
```bash
python app.py
```

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧪 UI Testing (Selenium)

Automated UI tests are located in `test_bmi.py`. It simulates real form inputs and verifies results.

### ▶️ To Run:
```bash
python test_bmi.py
```

📝 Test results are saved in a `test_results_YYYYMMDD_HHMMSS.txt` file with input, expected category, and PASS/FAIL status.

---

## 🎯 BMI Visualization Logic

- A **gauge-style semi-circle** shows ranges:
  - Underweight, Normal, Overweight, Obese I/II/III
- The needle rotates based on calculated BMI using custom JS logic
- Users can **save the result section as an image** using a built-in download button (`html2canvas`)

---

## 📚 Built-in Info Sections

- BMI formula: `BMI = weight (kg) / height² (m²)`
- Visual table of categories:
  - Underweight: < 18.5
  - Normal: 18.5 – 24.9
  - Overweight: 25 – 29.9
  - Obese I: 30 – 34.9
  - Obese II: 35 – 39.9
  - Obese III: ≥ 40
- BMI Prime & Ponderal Index explained
- Limitations of BMI clearly described

---

## 🚀 Deployment

Project is ready for:

- ✅ **Vercel** (uses `vercel.json`)
- ✅ **Netlify** (uses `netlify.toml`, `runtime.txt`)

You can also deploy to:
- Render / Railway / Heroku using `python app.py` and `requirements.txt`

---

## 🖼️ Screenshots

> _(Optional: Add screenshots here using `assets/` folder if you have them)_

---

## 👨‍💻 Author

**Tejas Bagal**  
📫 [bagaltejas47@gmail.com](mailto:bagaltejas47@gmail.com)  
🔗 [LinkedIn](https://linkedin.com/in/tejas-bagal)  
📍 Chhatrapati Sambhajinagar, Maharashtra

---

## 📄 License

This project is licensed under the **MIT License**.

---

> _Disclaimer: This tool is for educational and informational purposes only. Always consult a healthcare provider for medical decisions._
