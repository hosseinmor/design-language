---
id: content.copy-audit
collection: content
type: content-foundation
title: Copy Audit
summary: Defines how existing production copy is audited against Design Language rules, including the audit item and finding shapes, priority model, rewrite through a copy brief, and how gaps return to the owning guideline.
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

### نباید

- `AUD-003` موردی که context کامل ندارد یا محصولش لایهٔ هویت کلامی ندارد قضاوت نشود و needs_context بگیرد.

<!-- /generated:content-rules -->

## مراحل

1. **استخراج:** هر copy با context کامل یک slot ثبت می‌شود (`audit_item`).
2. **بررسی قطعی:** برچسب‌های forbidden و legacy مفهوم‌های مورد از روی
   واژه‌نامهٔ همان محصول (مثلاً [`jobvision.yml`](terminology/jobvision.yml)) پیدا و به برچسب مصوب نگاشت می‌شوند.
3. **بررسی معنایی:** copy با [evaluator معنایی](../../ai/evals/README.md) در
   برابر قواعد قرارداد مالک سنجیده می‌شود.
4. **اولویت‌بندی:** از `priority_model`.
5. **بازبینی انسانی:** finding، اولویت و copy پیشنهادی تأیید یا رد می‌شود.
6. **تیکت:** finding تأییدشده در سامانهٔ پیگیری کار ثبت می‌شود.
7. **برگشت شکاف:** هر `guideline_gap` یا برچسب قدیمی تازه از مسیر
   [Evolve the system](../../playbooks/evolve-the-system/README.md) به سند مالک
   برمی‌گردد. برچسب قدیمی به `legacy_labels` همان مدخل اضافه می‌شود، نه فهرست
   صفحه‌ها.

## ورودی: audit item

| فیلد | الزام | مقدار |
|---|---|---|
| `id`، `observed_text` | لازم | شناسه و متن دقیق دیده‌شده |
| `location` | لازم | شناسهٔ مبهم مورد در موجودی بیرونی؛ URL ممنوع |
| `captured_on` | لازم | تاریخ دیده‌شدن، `YYYY-MM-DD` |
| `product`، `audience`، `surface`، `contract`، `state`، `slot` | لازم برای قضاوت | همان واژگان [copy brief](copy-brief.md) |
| `concepts`، `product_facts`، `notes` | اختیاری | ID مدخل‌ها و factهای منبع‌دار |

موردی که یکی از فیلدهای context را ندارد، یا محصولش لایهٔ هویت کلامی ندارد،
`needs_context` می‌گیرد و قضاوت نمی‌شود.

## خروجی: finding

| فیلد | محتوا |
|---|---|
| `status` | `finding`، `no_issue` یا `needs_context` |
| `rule_ids` | قواعد نقض‌شده؛ برچسب نادرست به `VOICE-007` نگاشت می‌شود |
| `guideline_gap` | مشکل واقعی‌ای که هیچ قاعده‌ای آن را پوشش نمی‌دهد |
| `label_findings` | برچسب یافته‌شده، نوع (forbidden یا legacy)، برچسب‌های مصوب و `needs_review` |
| `priority` | `P1` تا `P4` |
| `rewrite_brief` | copy brief برای تولید copy پیشنهادی |
| `context_gaps` | فیلدهای غایب یا `product_layer_missing` |

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
report-only است و پاسخ‌های evaluator را فقط با findingها ادغام می‌کند.

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
