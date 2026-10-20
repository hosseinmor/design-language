---
id: content.components.overview
collection: content
type: content-overview
title: Content Component Contracts
summary: Routes copy decisions that are specific to reusable Design System components without duplicating component behavior or product truth.
knowledge_state: verified
document_maturity: draft
related:
  - content.content-guidelines
  - content.product-voice
  - content.terminology
  - content.localization
---

# قراردادهای محتوایی کامپوننت‌ها

این پوشه قواعدی را نگه می‌دارد که فقط در ترکیب محتوا با یک کامپوننت reusable
معنا پیدا می‌کنند.

```text
Content foundation
→ صدا، اصطلاحات و localization

Content pattern
→ منطق پیام یا وضعیت در چند کامپوننت

Content component contract
→ نقش و محدودیت copy در یک کامپوننت مشخص

Design System component
→ ساختار، رفتار، state، style و accessibility مکانیکی
```

قرارداد محتوایی نباید رفتار محصول، variant دیداری یا interaction جدید بسازد.
اگر تصمیم به یک flow یا object محصول وابسته است، Product Knowledge یا pattern
مربوط باید آن را تعیین کند.

## موجودی فعلی

| کامپوننت | سند انسانی | منبع machine-readable | ارزیابی |
|---|---|---|---|
| Button | [`button.md`](button.md) | [`button.yml`](button.yml) | [`../../../ai/evals/content/button-content-cases.yml`](../../../ai/evals/content/button-content-cases.yml) |
| Text Input | [`text-input.md`](text-input.md) | [`text-input.yml`](text-input.yml) | [`../../../ai/evals/content/text-input-content-cases.yml`](../../../ai/evals/content/text-input-content-cases.yml) |
| Modal | [`modal.md`](modal.md) | [`modal.yml`](modal.yml) | [`../../../ai/evals/content/modal-content-cases.yml`](../../../ai/evals/content/modal-content-cases.yml) |
| Notification | [`notification.md`](notification.md) | [`notification.yml`](notification.yml) | [`../../../ai/evals/content/notification-content-cases.yml`](../../../ai/evals/content/notification-content-cases.yml) |

## قاعدهٔ رشد

فقط وقتی contract تازه بسازید که یک تصمیم محتوایی واقعاً component-specific
باشد و در foundation یا pattern عمومی حل نشود. برای نامزدهای بعدی پیش از داشتن
نیاز واقعی و قرارداد مبتنی بر منبع، scaffold خالی نسازید.

## اعتبارسنجی

```bash
python tooling/validators/check_content_components.py
```

این اعتبارسنج موجودی ثبت‌شده، هویت فایل‌ها، منبع قواعد، شناسه‌ها و پوشش همهٔ
قواعد blocking در evalها را بررسی می‌کند.
