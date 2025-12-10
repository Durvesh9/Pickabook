# Pickabook 🖼️

**Pickabook** — a small mini-project where a user uploads a “pick” (image) and the system converts it into a user-selected style.

Live demo: [https://pickabook-pi.vercel.app/](https://pickabook-pi.vercel.app/)

---

## 📁 Project Structure

```
Pickabook/
├── app/               # main application files (HTML / JS / CSS / Python backend etc.)
├── run.py             # entry point to start the app
├── requirements.txt   # Python dependencies (if applicable)
├── .gitignore
└── README.md          # this file
```

---

## ✅ What it Does

* Takes an image uploaded by the user (“a pick”)
* Applies a style transformation (as selected by the user)
* Returns the stylized result to the user

In short: image-style conversion via user upload + stylization processing.

---

## 🚀 How to Run

1. Clone the repo:

   ```
   git clone https://github.com/Durvesh9/Pickabook.git
   cd Pickabook
   ```

2. (Optional but recommended) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate     # on Linux / macOS
   venv\Scripts\activate        # on Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python run.py
   ```

5. Open the browser and go to the local URL shown in terminal (e.g. `http://localhost:5000`) — upload a picture, choose a style, and get the stylized image.

---

## 🛠️ Configuration

* If your app uses any **API keys or secrets** (for example, for external style-transfer services), store them in a `.env` file in the project root (and DO NOT commit `.env`).
* Then ensure your code reads the key appropriately (e.g. via `os.getenv(...)`).

> ⚠️ If `.env` is missing or key is not set, the app may raise an error or fail to run.

---

## 💡 Why This Project

* Quick demo of **image upload + style transformation** workflow
* Good for learning backend + frontend integration (upload, processing, response)
* Can be extended to support multiple style models, user-defined styles, bulk conversion

---

## 🔧 Potential Improvements / Extensions

* Add **authentication/user accounts** so users can save their uploads or history
* Allow **multiple style choices** or **style preview thumbnails**
* Add **error handling** and **input validation** (e.g. max file size, file types)
* Use a **queue / asynchronous processing** if style transfer is compute-heavy, to improve responsiveness
* Add a **gallery feature** for users to view their past stylized images

---

## 📄 License & Credits

This is an open-source personal project. Feel free to reuse or extend it under whatever licensing you see fit.

