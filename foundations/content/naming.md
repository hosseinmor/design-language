---
id: content.naming
collection: content
type: content-foundation
title: Naming New Concepts
summary: Defines how a user-facing label is chosen for a concept that exists neither in Product Knowledge nor in the Design Language terminology, before it is published and extracted into Product Knowledge.
knowledge_state: unverified
document_maturity: draft
related:
  - content.terminology
  - content.copy-brief
  - content.product-voice
  - content.localization
topics:
  - naming
  - terminology
  - ux-writing
  - persian
---

# نام‌گذاری مفهوم تازه

این سند می‌گوید برای مفهومی که هنوز نه در Product Knowledge هست و نه در
[واژه‌نامه](terminology.md)، برچسب کاربرپسند چطور انتخاب شود. قرارداد
machine-readable در [`naming.yml`](naming.yml) و caseها در
[`../../ai/evals/content/naming-cases.yml`](../../ai/evals/content/naming-cases.yml)
قرار دارند.

## چرخهٔ یک نام تازه

1. هارنس در ساخت [copy brief](copy-brief.md) به مفهومی می‌رسد که مدخل ندارد و
   آن را `new_concept` با ارجاع PRD ثبت می‌کند.
2. نام با قواعد این سند پیشنهاد می‌شود؛ wording نهایی با Designer است. copy
   وابسته در `draft_dependencies` می‌آید.
3. نام همراه `new_concept.id` و ارجاع PRD در Design Artifact یا PRD ثبت می‌شود،
   تا مقایسهٔ بعد از publish بتواند آن را به صفحهٔ Product Knowledge وصل کند.
4. بعد از publish، استخراج Product Knowledge مفهوم و برچسب را از کد برمی‌دارد.
   نام تازه به واژه‌نامهٔ Design Language اضافه نمی‌شود.

## قرارداد قطعی

<!-- generated:content-rules source=naming.yml -->
<!-- این بخش از فایل YAML تولید می‌شود؛ دستی ویرایش نکنید. پس از تغییر قواعد اجرا کنید: python tooling/generate_content_rule_sections.py generate -->

### باید

- `NAM-001` پیش از نام‌گذاری بررسی شود که مفهومی با همین معنی در Product Knowledge یا واژه‌نامه هست یا نه؛ اگر هست، برچسب همان مفهوم به کار رود و نام تازه ساخته نشود.
- `NAM-003` مفهوم وابسته با هستهٔ نام خانوادهٔ خود نام‌گذاری شود و یک نام برای دو سطح یک خانواده به کار نرود.
- `NAM-005` نام آنچه کاربر می‌بیند یا به دست می‌آورد را بگوید، نه سازوکار پیاده‌سازی را.

### بهتر است

- `NAM-004` فارسی رایج بر وام‌واژه ترجیح دارد؛ وام‌واژه فقط وقتی به کار رود که اصطلاح جاافتادهٔ همان مخاطب باشد و معادل روشنی نداشته باشد.

### نباید

- `NAM-002` نام تازه با برچسب فعلی، قدیمی یا ممنوع یک مفهوم دیگر یکی نباشد.
- `NAM-006` نام قابلیت یا رفتاری مانند «خودکار»، «هوشمند» یا «فوری» را القا نکند که PRD تعریف نکرده است.

<!-- /generated:content-rules -->

## نمونه‌ها

| موقعیت | نام | چرا |
|---|---|---|
| مفهوم همان «تلنت پول» است | «تلنت پول»، نه «مخزن رزومه» | `NAM-001` |
| نوع تازه‌ای از آگهی برای کارآموزی | «آگهی کارآموزی»، نه «فرصت کارآموزی» | `NAM-003` |
| فهرست کوتاه‌شدهٔ کارجوها | «فهرست منتخب»، نه «شورت‌لیست» | `NAM-004` |
| کارجوهایی که سیستم پیشنهاد می‌دهد | «کارجوهای پیشنهادی»، نه «پایپ‌لاین غربالگری» | `NAM-005` |
| کارفرما دعوت را دستی می‌فرستد | «ارسال دعوت»، نه «ارسال خودکار دعوت» | `NAM-006` |

## مرزها

- معنی و رفتار مفهوم مال PRD (رفتار تازه) و Product Knowledge (رفتار فعلی) است؛
  این سند فقط برچسب را پوشش می‌دهد.
- قواعد موجود تکرار نمی‌شوند: واژهٔ کدی
  ([`VOICE-010`](product-voice.md))، شکل کوتاه نام (`policy.context_rules` در
  [`terms.yml`](terminology/terms.yml))، «دستیار» برای قابلیت ساده
  ([`AIC-002`](patterns/ai-content-and-disclosure.md)) و نام محصول و برند
  ([بومی‌سازی](localization.md)).
- نام یک محصول به محصول دیگر منتقل نمی‌شود. Cando تا ثبت لایهٔ هویت کلامی آن
  نام تازه نمی‌گیرد ([copy brief](copy-brief.md)، `BRF-005`).

## ارزیابی

```bash
python tooling/validators/check_content_terminology.py
```

این بررسی، علاوه بر واژه‌نامه، کنترل می‌کند که هر قاعدهٔ blocking `NAM` دست‌کم
یک case در `naming-cases.yml` داشته باشد. caseها با evaluator معنایی report-only
اجرا می‌شوند.
