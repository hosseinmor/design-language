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
  Product Knowledge برای رفتار فعلی و PRD جاری برای رفتار تازه، هر دو برای
  `product_facts` با منبع؛ تیکت یا PRD برای
  `audience` و `context`؛ واژه‌نامهٔ DL و گلاسری PK برای `concepts`. حداقل خوراک طرح و سند PK
  است؛ وقتی کار رفتار تازه می‌سازد، PRD هم لازم است. هر چیزی که منبع ندارد `unknown` می‌شود و سؤال برمی‌گرداند.
- **سهم انسان:** فقط پاسخ به `open_questions`.
- **ذخیره:** brief جایی نگهداری نمی‌شود. هر بار از منابع از نو ساخته می‌شود، از
  جمله پس از تغییر دیزاین، و فقط copyهای متأثر دوباره نوشته می‌شوند.
- **پاسخ سؤال‌ها:** Product Knowledge از کد پروداکشن استخراج می‌شود و منبع نهایی
  حقیقت است؛ کسی آن را دستی نمی‌نویسد. پس پاسخ هر سؤال این‌طور می‌رود:
  - رفتار **تازه‌ای** که همین کار می‌سازد → PRD جاری، با تصمیم PM. بعد از
    publish، استخراج PK آن را برمی‌دارد.
  - رفتار **فعلی** که PK آن را ندارد → درخواست تغییر برای مالک PK (شکاف
    استخراج). تا رفع آن، پاسخ در تیکت یا PRD همان کار می‌ماند.

  پاسخی که جایی ثبت نشود در ساخت بعدی دوباره پرسیده می‌شود.

تنها briefهای این مخزن caseهای eval هستند.

## قرارداد قطعی

<!-- generated:content-rules source=copy-brief.yml -->
<!-- این بخش از فایل YAML تولید می‌شود؛ دستی ویرایش نکنید. پس از تغییر قواعد اجرا کنید: python tooling/generate_content_rule_sections.py generate -->

### باید

- `BRF-001` copy فقط از brief، قراردادهای Design Language و factهای ارجاع‌شده ساخته شود؛ هیچ ادعای محصولی دیگری اضافه نشود.
- `BRF-003` هر slot که به fact با status برابر draft تکیه دارد در draft_dependencies ثبت شود.
- `BRF-004` برچسب هر concept متناسب با audience و surface از منبع برچسب آن بیاید (برچسب هدف واژه‌نامه، وگرنه برچسب PK؛ برای مفهوم تازه قواعد NAM با ثبت در draft_dependencies) و برچسب forbidden یا legacy در copy تازه نیاید.

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
| `concepts` | اختیاری | ID مدخل واژه‌نامه، مفهوم PK (`{kind: product_knowledge, product, page, label}`) یا مفهوم تازه (`{kind: new_concept, id, source}`)؛ بخش «منبع برچسب» |
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
    source:
      kind: product_knowledge
      product: jobvision
      page: <source-native page name>
      state: verified
```

### وضعیت fact

| status | منبع | اثر روی copy |
|---|---|---|
| `verified` | منبعی که خودش verified است | می‌تواند در copy بیاید |
| `draft` | هر منبع مجاز | می‌تواند بیاید، ولی slot وابسته در `draft_dependencies` ثبت می‌شود |
| `unknown` | ندارد؛ `question` لازم است | ادعا یا القا نمی‌شود؛ در `open_questions` برمی‌گردد |

status یک fact نمی‌تواند از بلوغ منبع آن بالاتر باشد. سه شکل منبع مجاز است:

| شکل | معنی | بالاترین status |
|---|---|---|
| ID یکی از `sources` واژه‌نامه | منبع ثبت‌شده | همان `state` منبع |
| `{kind: product_knowledge, product, page, state}` | صفحهٔ Product Knowledge با نام source-native آن؛ `product` باید همان محصول brief باشد | همان `state` صفحه هنگام خواندن |
| `{kind: prd, ref, decision}` | PRD جاری همین کار؛ `decision` برابر `accepted` یا `proposed` | `verified` فقط با `accepted`؛ در غیر این صورت `draft` |

fact یک محصول از Product Knowledge محصول دیگر گرفته نمی‌شود. `eval_fixture`
فقط در fixtureهای eval مجاز است، تا caseهای آزمایشی ادعایی را به منبع واقعی
نسبت ندهند.

### منبع برچسب

| مفهوم | برچسب از کجا | اثر روی خروجی |
|---|---|---|
| مدخل [واژه‌نامهٔ DL](terminology/terms.yml) دارد | برچسب هدف همان مدخل | — |
| مدخل ندارد ولی در PK هست | `label` ثبت‌شده در PK | — |
| تازه است (`new_concept`) | نام‌گذاری با [قواعد NAM](naming.md)؛ wording مال Designer است | slot وابسته در `draft_dependencies` با `concept` ثبت می‌شود |

در دورهٔ گذار، واژه‌نامهٔ DL فقط برای مفهوم‌هایی برچسب هدف نگه می‌دارد که
پروداکشن هنوز با گایدلاین هم‌راستا نیست. مفهوم تازه در واژه‌نامه ثبت نمی‌شود:
نامش در PRD یا Design Artifact می‌آید و بعد از publish وارد PK می‌شود.
`source` مفهوم تازه یک ارجاع PRD است (`{kind: prd, ref, decision}`).

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
