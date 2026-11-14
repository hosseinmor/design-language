---
id: content.copy-audit
collection: content
type: content-foundation
title: Copy Audit
summary: Defines how existing production copy is audited against Design Language rules, including running the audit on a frontend codebase, the audit item and finding shapes, content types and their decision owners, priority model, mechanical fixes, rewrite through a copy brief, and how gaps return to the owning guideline.
knowledge_state: unverified
document_maturity: draft
related:
  - content.content-guidelines
  - content.copy-brief
  - content.terminology
  - content.product-voice
topics:
  - copy-audit
  - ux-writing
  - terminology
  - persian
---

# Copy audit

این سند روش آدیت copy فعلی پروداکشن است. قرارداد machine-readable در
[`copy-audit.yml`](copy-audit.yml) و caseهای قطعی در
[`../../ai/evals/content/audit/copy-audit-cases.yml`](../../ai/evals/content/audit/copy-audit-cases.yml)
قرار دارند.

موجودی صفحه‌ها، findingهای واقعی و گزارش‌های تاریخ‌دار در این مخزن نگهداری
نمی‌شوند؛ آن‌ها در موجودی بیرونی و سامانهٔ پیگیری کار می‌مانند. این مخزن فقط
روش، قواعد و ابزار را نگه می‌دارد.

## قرارداد قطعی

<!-- generated:content-rules source=copy-audit.yml -->
<!-- این بخش از فایل YAML تولید می‌شود؛ دستی ویرایش نکنید. پس از تغییر قواعد اجرا کنید: python tooling/generate_content_rule_sections.py generate -->

### باید

- `AUD-001` هر finding یا ID قاعدهٔ نقض‌شده را ذکر کند یا guideline_gap مشخص داشته باشد.
- `AUD-002` برچسب forbidden یا legacy فقط به برچسب مصوب همان مفهوم در واژه‌نامه نگاشت شود، نه به برچسب حدسی.
- `AUD-004` copy پیشنهادی از یک copy brief ساخته شود تا fact نامعلوم به سؤال تبدیل شود، نه به ادعا.
- `AUD-005` هر مورد نوع متن مشخص داشته باشد و مالک تصمیم finding از همان نوع بیاید؛ ادعای محصولی بی‌منبع در هر نوع به PM برود.

### نباید

- `AUD-003` موردی که context کامل ندارد یا محصولش لایهٔ هویت کلامی ندارد قضاوت نشود و needs_context بگیرد.
- `AUD-006` محتوای بازاریابی یا حقوقی فراتر از قواعد مجاز نوع خودش قضاوت یا بازنویسی نشود.

<!-- /generated:content-rules -->

## نوع متن و مالک تصمیم

هر مورد یک `content_type` دارد. نوع متن مشخص می‌کند finding پیش چه کسی
می‌رود و چه اندازه تغییر مجاز است. اولویت همچنان از `priority_model` می‌آید؛
نوع متن مدل اولویت دوم نمی‌سازد.

| `content_type` | نام | مالک تصمیم | قواعد قضاوت‌شده | بازنویسی |
|---|---|---|---|---|
| `interface` | متن رابط | `designer` | همهٔ قواعد | بله، از راه copy brief |
| `marketing` | محتوای بازاریابی | `marketing` | بومی‌سازی، نگارش (`VOICE-002`)، ادعا (`VOICE-003`، `VOICE-005`) و واژه (`VOICE-007`، `VOICE-010`) | نه؛ برچسب مصوب خودش اصلاح است |
| `legal` | متن حقوقی | `legal` | بومی‌سازی، نگارش و واژه | نه |

- متن رابط همان دامنهٔ اصلی این گایدلاین است. محتوای بازاریابی و حقوقی مالک
  دیگری دارند؛ آدیت فقط آنچه را این مخزن مالکش است برایشان گزارش می‌کند.
- **ادعای محصولی نوع متن نیست.** ادعا در هر نوعی می‌آید، از تیتر لندینگ تا
  دیالوگ رابط. finding با dimension `product_truth`، یا پاسخ evaluator با
  `unsupported_product_or_runtime_claim`، در هر نوع متن مالک `product_manager`
  می‌گیرد تا fact تأیید شود.
- موردی که نوع متن ندارد یا نوعش ناشناخته است `needs_context` می‌گیرد؛ ابزار
  نوع را حدس نمی‌زند.
- متن راهنما (مقاله‌های کمک) هنوز نوع جدا ندارد. پرسش‌های متداول سئو
  `marketing` است.

## مراحل

1. **استخراج:** هر copy با context کامل و نوع متن ثبت می‌شود (`audit_item`).
2. **بررسی قطعی:** برچسب‌های forbidden و legacy مفهوم‌های مورد از روی
   واژه‌نامهٔ همان محصول (مثلاً [`jobvision.yml`](terminology/jobvision.yml)) پیدا و به برچسب مصوب نگاشت می‌شوند.
3. **بررسی معنایی:** copy با [evaluator معنایی](../../ai/evals/README.md) در
   برابر قواعد قرارداد مالک سنجیده می‌شود.
4. **اولویت‌بندی:** از `priority_model`.
5. **بازبینی انسانی:** مالک تصمیم (`decision_owner`) finding، اولویت و copy
   پیشنهادی را تأیید یا رد می‌کند. finding مکانیکی فهرستی بازبینی می‌شود
   (بخش [بازبینی و اجرا](#بازبینی-و-اجرا)).
6. **تیکت:** finding تأییدشده در سامانهٔ پیگیری کار ثبت می‌شود.
7. **برگشت شکاف:** هر `guideline_gap` یا برچسب قدیمی تازه از مسیر
   [Evolve the system](../../playbooks/evolve-the-system/README.md) به سند مالک
   برمی‌گردد. برچسب قدیمی به `legacy_labels` همان مدخل اضافه می‌شود، نه فهرست
   صفحه‌ها.

## اجرا روی کدبیس

وقتی آدیت مستقیم روی کد فرانت اجرا می‌شود، واحد کار **منبع متن** است: جایی که
متن نوشته شده و اصلاح در آن انجام می‌شود. همهٔ متن‌ها کلید ترجمه ندارند؛ متن
داخل کد هم یک منبع است.

| `source_kind` | `location` | اثر اصلاح |
|---|---|---|
| `i18n_key` | فایل ترجمه و کلید | همهٔ جاهایی که کلید را می‌خوانند |
| `inline` | فایل و نام کامپوننت | همهٔ صفحه‌هایی که کامپوننت را نشان می‌دهند |
| `backend` | سرویس یا endpoint، اگر معلوم است | در فرانت اصلاح نمی‌شود؛ فقط ثبت می‌شود |

1. **پیدا کردن متن‌ها:** فایل‌های ترجمه، متن داخل template و کامپوننت، و
   پیام‌هایی که از سرور نمایش داده می‌شوند. دادهٔ نمونه و محتوای کاربر آدیت
   نمی‌شوند.
2. **ثبت هر منبع یک بار:** با `usages`، یعنی صفحه‌ها یا routeهایی که آن را نشان
   می‌دهند. شمارهٔ خط در `location` نمی‌آید، چون با هر تغییر کد جابه‌جا می‌شود؛
   متن فعلی برای پیدا کردن دقیق کافی است.
3. **متن یکسان در چند منبع** چند ردیف است؛ این ردیف‌ها در سند خروجی کنار هم
   می‌آیند تا یکدست اصلاح شوند.
4. **context از روی کد:** `content_type` و برای متن رابط `contract`، `state` و
   `slot` از کدی تعیین می‌شود که متن را نشان می‌دهد. اگر از کد معلوم نشود، مورد
   `needs_context` می‌گیرد.
5. **سنجش اثر:** copy پیشنهادی باید برای همهٔ `usages` منبع درست باشد. اگر
   نیست، برای آن جا منبع جدا پیشنهاد می‌شود: کلید جدا، یا ورودی جدا برای
   کامپوننت.

انتقال متن داخل کد به فایل ترجمه جزو آدیت نیست؛ متن در همان منبعی اصلاح
می‌شود که هست.

### سند خروجی

سند خروجی آدیت کدبیس برای هر finding این ستون‌ها را دارد. ستون‌های تصمیم را
بازبین پر می‌کند و سند بازبینی‌شده همان فهرست اجرای اصلاح است.

| ستون | از کجا |
|---|---|
| منبع | `source_kind` و `location` |
| جای استفاده | `usages` |
| متن فعلی | `observed_text` |
| متن پیشنهادی AI | خروجی copy brief؛ برای سؤال PM، سؤال به‌جای متن |
| قاعده و دلیل | `rule_ids` یا `guideline_gap`، با یک جمله دلیل |
| اولویت | `priority` |
| نوع متن و مالک تصمیم | `content_type` و `decision_owner` |
| تصمیم | بازبین: تأیید، ویرایش، رد یا سؤال PM |
| متن نهایی | بازبین، فقط برای «ویرایش» |

### بازبینی و اجرا

- **اصلاح مکانیکی:** finding که همهٔ قواعدش در `review_model.mechanical_rules`
  است (نگارش و قالب، بدون تغییر واژه یا جمله) `mechanical` می‌گیرد. این
  findingها فهرستی بازبینی می‌شوند، نه تک‌تک.
- اصلاح مکانیکی **همیشه اعمال می‌شود**، حتی وقتی تصمیم محتوایی همان متن رد
  شده یا منتظر fact است. فقط وقتی متن حذف شود اعمال نمی‌شود.
- «تأیید» یعنی copy پیشنهادی همان‌طور اعمال شود؛ «ویرایش» یعنی متن نهایی
  بازبین اعمال شود.

## ورودی: audit item

| فیلد | الزام | مقدار |
|---|---|---|
| `id`، `observed_text` | لازم | شناسه و متن دقیق دیده‌شده |
| `location` | لازم | منبع متن (فایل و کلید، یا فایل و کامپوننت) یا شناسهٔ مبهم موجودی بیرونی؛ URL و شمارهٔ خط ممنوع |
| `captured_on` | لازم | تاریخ دیده‌شدن، `YYYY-MM-DD` |
| `product`، `audience`، `surface`، `content_type` | لازم برای قضاوت | واژگان [copy brief](copy-brief.md) و جدول نوع متن |
| `contract`، `state`، `slot` | لازم برای `interface` | همان واژگان copy brief |
| `source_kind`، `usages` | اختیاری؛ در آدیت کدبیس لازم | نوع منبع و جاهای استفاده |
| `concepts`، `product_facts`، `notes` | اختیاری | ID مدخل‌ها و factهای منبع‌دار |

موردی که یکی از فیلدهای context لازم برای نوع خودش را ندارد، یا محصولش لایهٔ
هویت کلامی ندارد، `needs_context` می‌گیرد و قضاوت نمی‌شود.

## خروجی: finding

| فیلد | محتوا |
|---|---|
| `status` | `finding`، `no_issue` یا `needs_context` |
| `source_kind`، `usages` | از audit item، برای سند خروجی |
| `mechanical` | true وقتی finding فقط اصلاح نگارش و قالب است |
| `content_type`، `decision_owner` | نوع متن و مالک تصمیم؛ ادعای بی‌منبع مالک `product_manager` می‌گیرد |
| `rule_ids` | قواعد نقض‌شده؛ برچسب نادرست به `VOICE-007` نگاشت می‌شود |
| `guideline_gap` | مشکل واقعی‌ای که هیچ قاعده‌ای آن را پوشش نمی‌دهد |
| `label_findings` | برچسب یافته‌شده، نوع (forbidden یا legacy)، برچسب‌های مصوب و `needs_review` |
| `priority` | `P1` تا `P4` |
| `rewrite_brief` | copy brief برای تولید copy پیشنهادی؛ فقط برای `interface` |
| `context_gaps` | فیلدهای غایب، `product_layer_missing`، `unknown_content_type` یا `unknown_contract` |

`needs_review` یعنی برچسب ممنوع scope محدودتری از concept دارد (مثلاً
`entity_label`) و فقط بازبین انسانی می‌تواند بگوید در این متن واقعاً نادرست است.
برچسب‌های مصوب هر مفهوم پیش از جست‌وجو حذف می‌شوند، تا «درخواست» داخل «درخواست
شغلی» گزارش نشود.

## اولویت

اولویت برابر است با رتبهٔ پایین‌ترین dimension نقض‌شده به‌علاوهٔ جابه‌جایی
surface، و حداکثر `P4` است:

| dimension | رتبه |
|---|---|
| `product_truth`، `accessibility`، `disclosure` | 1 |
| `clarity`، `action`، `structure`، `interaction`، `classification`، `localization` | 2 |
| `terminology` | 3 |
| `tone` | 4 |

surface برابر `public` جابه‌جایی صفر دارد و بقیهٔ surfaceها یک. بازبین انسانی
می‌تواند اولویت را با دلیل تغییر دهد.

## ابزار

```bash
python tooling/audit/run_copy_audit.py check --items <items.jsonl> --output <findings.jsonl>
python tooling/audit/run_copy_audit.py prepare --items <items.jsonl> --repository-commit <sha> --output <tasks.jsonl>
python tooling/audit/run_copy_audit.py summarize --findings <findings.jsonl> --semantic <responses.jsonl> --report-json <report.json> --report-markdown <report.md>
```

ورودی و خروجی این دستورها بیرون از مخزن نگهداری می‌شوند. بخش معنایی
report-only است و پاسخ‌های evaluator را فقط با findingها ادغام می‌کند. هر
task معنایی قواعد قضاوت‌شدهٔ نوع متن را در `judged_rules` دارد، و `summarize`
violation بیرون از آن قواعد را کنار می‌گذارد.

```bash
python tooling/validators/check_copy_audit.py
```

اعتبارسنج قرارداد را بررسی می‌کند، checker واقعی را روی caseهای نمونه اجرا و با
نتیجهٔ مورد انتظار مقایسه می‌کند، هر rewrite brief را با validator copy brief
می‌سنجد و پوشش همهٔ قواعد blocking `AUD` را کنترل می‌کند.

## محدودیت فعلی

`legacy_labels` در واژه‌نامه هنوز هیچ مدخلی ندارد، پس بررسی قطعی فعلاً فقط
برچسب‌های forbidden را می‌یابد. هر برچسب قدیمی که در آدیت دیده شود از مرحلهٔ ۷
به واژه‌نامه اضافه می‌شود.
