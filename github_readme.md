#  AI Customer Support Assistant with Function Calling & Chainlit

یک دستیار هوشمند و تعاملی پشتیبانی مشتری که با استفاده از **LangChain**، قابلیت **Function Calling (Tool Calling)** و رابط کاربری وب مدرن **Chainlit** توسعه داده شده است. این سیستم به زبان طبیعی با کاربر تعامل کرده و به صورت خودکار توابع پایتونی را برای استعلام سفارش‌ها و ثبت تیکت‌های پشتیبانی فراخوانی می‌کند.

---

##  ویژگی‌های کلیدی (Key Features)

- **فراخوانی خودکار ابزارها (Function Calling):** مدل با ارزیابی درخواست کاربر، به طور خودکار ابزار مناسب (`get_order_status` یا `submit_ticket`) را با پارامترهای استخراج‌شده اجرا می‌کند.
- **رابط کاربری مدرن با Chainlit:** نمایش مراحل تفکر مدل و اجرای ابزارها به صورت زنده (`Step Tracking`) در محیط چت وب.
- **چرخه کامل رفت‌وبرگشت (Full Loop Execution):** ارسال خروجی توابع در قالب `ToolMessage` به مدل برای تولید پاسخی طبیعی، انسانی و دقیق.
- **مدیریت سشن‌های مجزا:** ذخیره مستقل تاریخچه گفت‌وگو برای هر کاربر به صورت ایزوله.
- **یکپارچه‌سازی انعطاف‌پذیر با OpenRouter:** امکان اتصال و سوئیچ بین مدل‌های مختلف زبانی (OpenAI, Meta Llama, Google Gemma و...).

---

##  فناوری‌های استفاده‌شده (Tech Stack)

- **Language:** Python 3.10+
- **Frameworks:** LangChain, Chainlit
- **LLM Provider:** OpenRouter API (`langchain-openrouter` / `langchain-openai`)
- **Protocol:** Tool Calling / JSON Schema

---

##  ساختار پروژه (Project Structure)

```text
├── main.py              # منطق هسته: دیتابیس ساختگی، توابع عملیاتی و چرخه کنسول
├── app.py               # رابط کاربری تحت وب چین‌لیت (Event-driven)
├── .env.example         # نمونه فایل متغیرهای محیطی
├── requirements.txt     # پکیج‌ها و وابستگی‌های پایتونی
└── README.md            # مستندات پروژه
```

---

##  راهنمای نصب و راه‌اندازی (Quickstart)

### ۱. کلون کردن مخزن و ایجاد محیط مجازی
```bash
git clone https://github.com/your-username/ai-customer-support-agent.git
cd ai-customer-support-agent

# ساخت محیط مجازی
python -m venv .venv

# فعال‌سازی در ویندوز
.venv\Scripts\activate

# فعال‌سازی در لینوکس / مک
source .venv/bin/activate
```

### ۲. نصب پیش‌نیازها
```bash
pip install -r requirements.txt
```

### ۳. تنظیم کلید API
فایل `.env.example` را کپی کرده و به `.env` تغییر نام دهید:
```bash
cp .env.example .env
```
سپس کلید OpenRouter خود را در آن وارد کنید:
```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

### ۴. اجرای برنامه
برای اجرای برنامه تحت وب:
```bash
chainlit run app.py -w
```
سپس مرورگر خود را در آدرس `http://localhost:8000` باز کنید.

---

## 💡 سناریوهای نمونه جهت تست (Example Prompts)

- **استعلام وضعیت سفارش:**
  > «سلام، من علی محمدی هستم. وضعیت سفارش ORD-101 من به کجا رسید؟»
- **ثبت تیکت پشتیبانی:**
  > «می‌خوام یه تیکت پشتیبانی ثبت کنم. اسمم سارا کریمی هست و مشکلم اینه که سفارشم هنوز دستم نرسیده.»
- **مکالمه عمومی:**
  > «شما چه خدماتی ارائه می‌دید؟»