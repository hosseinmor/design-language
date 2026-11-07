---
id: content.copy-brief
collection: content
type: content-foundation
title: Copy Brief
summary: Defines the structured input for AI copy generation and its output contract, including how missing or draft product facts and products without a verbal-identity layer are handled.
knowledge_state: unverified
document_maturity: draft
related:
  - content.content-guidelines
  - content.product-voice
  - content.terminology
  - content.localization
topics:
  - copy-brief
  - ai-generation
  - ux-writing
  - product-truth
  - persian
---

# Copy brief

copy brief ورودی ساخت‌یافتهٔ تولید copy با AI است. قرارداد machine-readable در
[`copy-brief.yml`](copy-brief.yml) و caseهای تولید در
[`../../ai/evals/content/generation/copy-generation-cases.yml`](../../ai/evals/content/generation/copy-generation-cases.yml)
قرار دارند.

brief فقط ارجاع می‌دهد. قرارداد مالک (pattern یا component)، برچسب‌ها
(واژه‌نامه)، لحن (tone profile همان قرارداد) و قواعد نوشتن را از Design Language
می‌گیرد و factهای محصول را با منبع از Product Knowledge. هیچ معنی، رفتار یا
قاعدهٔ محصولی در brief تعریف نمی‌شود.

## چه کسی می‌سازد و کجا می‌ماند

brief قالب میانی کار AI است، نه سندی که انسان بنویسد.

- **سازنده:** ابزار هماهنگی کار (Product Development Harness) brief را از منابع
  همان کار می‌سازد. جزئیات این جریان مال هارنس است، نه این مخزن.
- **خوراک:** طرح Figma برای `contract`، `states`، `slots` و `surface`؛ سند
  Product Knowledge همان feature برای `product_facts` با منبع؛ تیکت یا PRD برای
  `audience` و `context`؛ واژه‌نامه برای `concepts`. حداقل خوراک طرح و سند PK
  است. هر چیزی که منبع ندارد `unknown` می‌شود و سؤال برمی‌گرداند.
- **سهم انسان:** فقط پاسخ به `open_questions`.
- **ذخیره:** brief جایی نگهداری نمی‌شود. هر بار از منابع از نو ساخته می‌شود، از
  جمله پس از تغییر دیزاین، و فقط copyهای متأثر دوباره نوشته می‌شوند.
- **پاسخ سؤال‌ها:** پاسخ هر سؤال fact محصول است و در سند Product Knowledge همان
  feature ثبت می‌شود. تا آن زمان در تیکت همان کار می‌ماند. پاسخی که جایی ثبت
  نشود در ساخت بعدی دوباره پرسیده می‌شود.

تنها briefهای این مخزن caseهای eval هستند.

## قرارداد قطعی

<!-- generated:content-rules source=copy-brief.yml -->
<!-- این بخش از فایل YAML تولید می‌شود؛ دستی ویرایش نکنید. پس از تغییر قواعد اجرا کنید: python tooling/generate_content_rule_sections.py generate -->

### باید

- `BRF-001` copy فقط از brief، قراردادهای Design Language و factهای ارجاع‌شده ساخته شود؛ هیچ ادعای محصولی دیگری اضافه نشود.
- `BRF-003` هر slot که به fact با status برابر draft تکیه دارد در draft_dependencies ثبت شود.
- `BRF-004` برچسب هر concept از واژه‌نامه و متناسب با audience و surface انتخاب شود؛ برچسب forbidden یا legacy در copy تازه نیاید.

### نباید

- `BRF-002` fact با status برابر unknown در copy ادعا یا القا نشود و در open_questions به سؤال تبدیل شود.
- `BRF-005` برای محصولی که لایهٔ هویت کلامی آن موجود نیست copy تولید نشود؛ outcome برابر blocked با دلیل برگردد.

<!-- /generated:content-rules -->

## ورودی

| فیلد | الزام | مقدار |
|---|---|---|
| `id` | لازم | شناسهٔ snake_case |
| `product` | لازم | کلید یکی از `product_layers` |
| `audience` | لازم | ID مدخل‌های نقش در [واژه‌نامه](terminology/terms.yml) (`role`، `persona`، `internal_role`) |
| `surface` | لازم | یکی از مقادیر `visibility` در واژه‌نامه |
| `contract` | لازم | ID قرارداد محتوایی pattern یا component |
| `states` | لازم | فهرست `{id, slots}`؛ slotها از anatomy همان قرارداد |
| `concepts` | اختیاری | ID مدخل‌های واژه‌نامه |
| `product_facts` | اختیاری | فهرست `{id, statement, status, source}` یا `{id, statement, status: unknown, question}` |
| `context` | اختیاری | توضیح آزاد موقعیت؛ fact محصولی نیست |
| `constraints` | اختیاری | محدودیت دقیق، فقط از Figma یا قرارداد component |

```yaml
id: delete_job_post
product: jobvision
audience: [employer_actor]
surface: public
contract: content.pattern.confirmation
states:
  - id: destructive_confirmation
    slots: [title, consequence, recoverability, primary_action, safe_exit]
concepts: [job_post]
product_facts:
  - id: deleted_job_post_is_permanent
    statement: آگهی حذف‌شده قابل بازگردانی نیست.
    status: verified
    source: <registered source id>
```

### وضعیت fact

| status | منبع | اثر روی copy |
|---|---|---|
| `verified` | منبع ثبت‌شده با state برابر verified | می‌تواند در copy بیاید |
| `draft` | منبع ثبت‌شده | می‌تواند بیاید، ولی slot وابسته در `draft_dependencies` ثبت می‌شود |
| `unknown` | ندارد؛ `question` لازم است | ادعا یا القا نمی‌شود؛ در `open_questions` برمی‌گردد |

status یک fact نمی‌تواند از state منبع آن بالاتر باشد. منبع‌ها همان
`sources` ثبت‌شده در واژه‌نامه‌اند. `eval_fixture` فقط در fixtureهای eval مجاز
است، تا caseهای آزمایشی ادعایی را به منبع واقعی نسبت ندهند.

### لایهٔ محصول

ساختار «پایهٔ مشترک + لایهٔ هر محصول» است. `product_layers` در
[`copy-brief.yml`](copy-brief.yml) نشان می‌دهد کدام محصول لایهٔ هویت کلامی دارد.
JobVision از [`product-voice.md`](product-voice.md) استفاده می‌کند. Cando لایه
ندارد و تا ثبت منبع آن، تولید با `outcome: blocked` متوقف می‌شود.

## خروجی

| فیلد | الزام | محتوا |
|---|---|---|
| `brief_id` | لازم | همان `id` brief |
| `outcome` | لازم | `copy` یا `blocked` |
| `checked_rules` | لازم | ID قواعدی که copy در برابر آن‌ها نوشته شده |
| `copy` | با `copy` | نگاشت state → slot → متن |
| `open_questions` | برای هر fact نامعلوم | `{fact, question}` |
| `draft_dependencies` | برای هر وابستگی draft | `{fact, slots}` |
| `blocked_reason` | با `blocked` | دلیل توقف |

slotی که به fact نامعلوم نیاز دارد خالی می‌ماند؛ متن جایگزین حدسی نوشته نمی‌شود.

## ارزیابی

```bash
python tooling/validators/check_copy_briefs.py
python tooling/evals/run_content_generation_eval.py validate
```

اعتبارسنج schema هر brief در fixtureها، ارجاع به قرارداد، anatomy، واژه‌نامه و
منابع، و پوشش همهٔ قواعد blocking `BRF` را کنترل می‌کند. ارزیابی خروجی مدل
report-only است و در CI اجرا نمی‌شود؛ جزئیات در [`../../ai/evals/README.md`](../../ai/evals/README.md).
