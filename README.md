
---

# 🖌 Interactive Contour Approximation with OpenCV

## 📌 Description

This project is an **interactive OpenCV application** that allows users to **draw shapes with the mouse** and observe how different **contour detection and polygon approximation parameters** affect the results in real time.

You can draw using the **left mouse button**, erase using the **right mouse button**, and control contour approximation settings using **trackbars**.

### 🎯 Features

* Mouse-based drawing and erasing
* Real-time contour detection
* Comparison between:

  * **Internal contours (RETR_LIST)**
  * **External contours (RETR_EXTERNAL)**
* Adjustable parameters:

  * Approximation accuracy
  * Contour chain approximation method
  * Arc length calculation mode
  * Approximation type
* Live visualization using OpenCV windows

---

## ⚙️ Requirements

* Python 3.x
* OpenCV
* NumPy

Install dependencies:

```bash
pip install opencv-python numpy
```

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🖱 Controls

| Action               | Mouse / Control    |
| -------------------- | ------------------ |
| Draw                 | Left Mouse Button  |
| Erase                | Right Mouse Button |
| Adjust approximation | Trackbars          |
| Exit                 | ESC key            |

---

## 🧠 What You Learn

* Mouse callbacks in OpenCV
* Contour detection methods
* Polygon approximation using `approxPolyDP`
* Effect of contour retrieval modes
* Interactive computer vision experiments

---

## 📷 Output Windows

* **Window**: Drawing canvas
* **Result**: Comparison of internal and external contour approximations

---

## 📄 License

This project is for **educational purposes** and free to use or modify.

---

# ✏️ تقریب تعاملی کانتور با OpenCV

## 📌 توضیحات

این پروژه یک **برنامه تعاملی با OpenCV** است که به کاربر اجازه می‌دهد با ماوس **روی تصویر نقاشی کند** و تأثیر تنظیمات مختلف **تشخیص کانتور و تقریب چندضلعی** را به‌صورت زنده مشاهده کند.

با **کلیک چپ** می‌توان رسم کرد و با **کلیک راست** پاک کرد. پارامترهای پردازش تصویر نیز از طریق **اسلایدرها (Trackbar)** قابل تغییر هستند.

---

## 🎯 قابلیت‌ها

* رسم و پاک‌کردن با ماوس
* تشخیص کانتور به‌صورت بلادرنگ
* مقایسه:

  * کانتورهای داخلی (RETR_LIST)
  * کانتورهای خارجی (RETR_EXTERNAL)
* تنظیم پارامترها:

  * میزان دقت تقریب
  * نوع Chain Approximation
  * نحوه محاسبه طول کمان
  * نوع الگوریتم تقریب
* نمایش زنده نتایج در پنجره‌های OpenCV

---

## ⚙️ پیش‌نیازها

* پایتون ۳
* OpenCV
* NumPy

نصب کتابخانه‌ها:

```bash
pip install opencv-python numpy
```

---

## ▶️ نحوه اجرا

```bash
python main.py
```

---

## 🖱 راهنمای کنترل

| عملکرد        | کنترل          |
| ------------- | -------------- |
| رسم           | کلیک چپ ماوس   |
| پاک کردن      | کلیک راست ماوس |
| تغییر تنظیمات | اسلایدرها      |
| خروج          | کلید ESC       |

---

## 🧠 مباحث آموزشی

* کار با Mouse Callback در OpenCV
* تشخیص کانتور
* تقریب چندضلعی با `approxPolyDP`
* تفاوت روش‌های بازیابی کانتور
* پردازش تصویر تعاملی

---

## 📷 پنجره‌های خروجی

* **Window**: محیط رسم
* **Result**: مقایسه کانتورهای داخلی و خارجی

---

## 📄 مجوز

این پروژه **آموزشی** است و استفاده یا ویرایش آن آزاد می‌باشد.

---

