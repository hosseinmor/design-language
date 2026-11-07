---
id: content.component.text-input
collection: content
type: content-component
title: Text Input Content
summary: Defines the Persian content contract for a single-line Text Input across label, placeholder, helper, error, requiredness, values, states, adornment actions, and accessible relationships.
knowledge_state: verified
document_maturity: draft
related:
  - content.product-voice
  - content.terminology
  - content.localization
  - content.pattern.instructions-and-helper-text
  - content.pattern.error
  - design-system.component.text-input
  - design-system.accessibility.forms
topics:
  - text-input
  - forms
  - labels
  - placeholder
  - helper-text
  - validation
  - accessibility
  - persian
---

# محتوای Text Input

این سند قرارداد محتوایی یک ورودی متن تک‌خطی است. قواعد machine-readable در
[`text-input.yml`](text-input.yml) و نمونه‌های regression در
[`../../../ai/evals/content/text-input-content-cases.yml`](../../../ai/evals/content/text-input-content-cases.yml)
قرار دارند.

## مرز منبع و تصمیم

### قواعد تأییدشده

قرارداد Design System و Accessibility این موارد را تثبیت کرده است:

- Text Input برای مقدار تک‌خطی است و بر رفتار native input تکیه دارد.
- هر input به accessible name معنادار نیاز دارد؛ Label دیداری منبع معمول آن
  است و Placeholder جای Label نیست.
- Label، Placeholder، Value، Helper و Error نقش‌های مستقل دارند.
- Error باید متنی و برنامه‌وار مرتبط باشد؛ border قرمز به‌تنهایی کافی نیست.
- Helper و Error در supporting-content region قرار می‌گیرند و Error در حالت
  invalid جای treatment عادی Helper را می‌گیرد.
- Required، Read only، Disabled و Invalid stateهای متمایزند و semantics
  برنامه‌وار متناظر می‌خواهند.
- محتوای لازم برای تکمیل field نباید فقط پشت Info یا Tooltip پنهان شود.
- RTL، متن دوجهته، paste، autofill و ویرایش native باید حفظ شوند.

### تصمیم‌های اجرایی Product Content

الگوی نوشتن Label، Placeholder، Helper و Error، حذف تکرار بین آن‌ها، حفظ
requirement هنگام انتقال به Error و مثال‌های فارسی این سند تصمیم Product
Content System هستند. این سند مشخص نمی‌کند کدام field اجباری است، validation چه
زمانی اجرا می‌شود یا چه input type و autocomplete tokenی برای یک field واقعی
درست است.

### قواعد ارثی

قواعد عمومی Label، Placeholder، Helper، Example، requiredness و حفظ requirement
هنگام Error مالکشان [الگوی دستورالعمل و متن راهنما](../patterns/instructions-and-helper-text.md)
است (`INS-004`، `INS-005`، `INS-007`، `INS-009`، `INS-010`، `INS-011`، `INS-014`،
`INS-020`) و حفظ اصطلاح Label در Error مالکش [الگوی خطا](../patterns/errors.md)
است (`ERR-003`). ارتباط برنامه‌وار accessible name، Helper و Error با input در
[Accessibility forms](../../../accessibility/forms.md) تعریف شده است. این سند
فقط قیدهای مخصوص Text Input را اضافه می‌کند؛ بخش‌های زیر نمونه‌های همان قواعد
در anatomy این component هستند.

## ابتدا roleها را جدا کنید

```text
Label
→ این field چیست؟

Placeholder
→ مثال یا قالب تکمیلیِ غیرضروری چیست؟

Helper
→ پیش از خطا چه context یا requirement کوتاهی مفید است؟

Value
→ مقدار واقعی کاربر یا سیستم چیست؟

Error
→ کدام شرط نقض شده و اصلاح معلوم چیست؟
```

هر رشته فقط یک وظیفهٔ اصلی دارد. یک عبارت را هم‌زمان در Label، Placeholder و
Helper تکرار نکنید.

## Label

Label باید purpose فیلد را با اصطلاح canonical همان مخاطب نام ببرد:

```text
نام
ایمیل
شماره موبایل
عنوان شغلی
```

Label instruction یا جمله نیست:

```text
بد: لطفاً عنوان شغلی خود را اینجا وارد کنید
خوب: عنوان شغلی
```

Label دیداری حالت پیش‌فرض است. مخفی‌کردن آن فقط در compositionی مجاز است که
accessible name معتبر دیگری وجود دارد و purpose فیلد بدون اتکا به Placeholder
قابل‌فهم می‌ماند.

## Placeholder

Placeholder اختیاری است. فقط وقتی از آن استفاده کنید که اطلاعاتی افزون بر Label
بدهد، مانند example یا format hint غیرضروری:

```text
Label: ایمیل
Placeholder: name@example.com

Label: عنوان شغلی
Placeholder: مثال: طراح محصول
```

- requirement ضروری را فقط در Placeholder قرار ندهید؛ با ورود Value ناپدید
  می‌شود.
- Label را تکرار نکنید.
- متن بلند، چندمرحله‌ای یا دارای consequence را در Placeholder نگذارید.
- exampleی که ممکن است value واقعی برداشت شود با «مثال:» یا context روشن
  مشخص شود.
- Placeholder را مانند value ازپیش‌پرشده نمایش ندهید.

## Helper

Helper کوتاه، field-specific و پیشگیرانه است. اطلاعات تازه‌ای مانند قالب، limit
تأییدشده، دلیل یا مقصد معلوم را پیش از failure نشان می‌دهد:

```text
حداکثر ۱۰۰ نویسه
این عنوان در رزومهٔ شما نمایش داده می‌شود.
```

Helper نباید:

- Label را با جمله‌ای طولانی‌تر تکرار کند؛
- Error احتمالی را پیشاپیش نمایش دهد؛
- limit، privacy، storage یا consequence تأییدنشده بسازد؛
- requirement حیاتی را فقط به Info/Tooltip منتقل کند.

اگر راهنما برای چند field یا کل step مشترک است، آن را به group یا form ببرید؛
در Helper هر field تکرار نکنید.

## Required و Optional

requiredness باید هم دیداری و هم برنامه‌وار قابل‌فهم باشد. `Required` در Figma
فقط مکانیزم marker را فراهم می‌کند؛ Product/Form تعیین می‌کند field واقعاً
اجباری است یا نه.

- یک convention ثابت در محدودهٔ form نگه دارید.
- اگر `*` استفاده می‌شود و معنی آن ممکن است مبهم باشد، convention را توضیح دهید.
- Required یا Optional را فقط در Placeholder ننویسید.
- optional بودن را وقتی بنویسید که به تصمیم کاربر کمک می‌کند؛ همهٔ fieldها را
  با metadata غیرضروری شلوغ نکنید.

policy سراسری JobVision/Cando برای «همهٔ requiredها را mark کنیم یا فقط
optionalها» هنوز تأیید نشده است.

## Value

Value دادهٔ واقعی است، نه copy نمونه. محتوای کاربر را صرفاً برای هماهنگی با لحن
برند بازنویسی نکنید.

- type و purpose field را حفظ کنید؛ quantity، identifier، email و free text
  formatting یکسان ندارند.
- مقدار mixed-direction را با قرارداد Localization نمایش دهید.
- Placeholder و Value نباید در runtime با authoring property به نام `Filled`
  اشتباه شوند؛ وجود Value state واقعی را تعیین می‌کند.
- خطای قابل‌بازیابی نباید دادهٔ معتبر و نامرتبط را پاک کند.

## Error و انتقال state

در حالت invalid، Error باید شرط نقض‌شده و راه اصلاح معلوم را بیان کند:

```text
Label: ایمیل
Error: ایمیل را با قالب name@example.com وارد کنید.
```

```text
Label: شماره موبایل
Error: شماره موبایل را وارد کنید.
```

Error باید همان نام field را حفظ کند، با input برنامه‌وار مرتبط باشد و invalid
state فقط با رنگ منتقل نشود.

وقتی Error جای Helper treatment را می‌گیرد، requirement ضروری نباید ناپدید
شود. آن requirement باید در خود Error، یک Instruction ماندگار یا context معتبر
دیگری باقی بماند. زمان validation، متن دقیق business rule و strategy تمرکز به
Form/Product تعلق دارند.

## Disabled و Read only

این دو state را با copy یا ظاهر یکسان نکنید:

- `Disabled` یعنی کنترل در دسترس interaction نیست.
- `Read only` یعنی Value همچنان خواندنی و بخشی از form است اما ویرایش نمی‌شود.

دلیل state را فقط وقتی بیان کنید که برای تکمیل task لازم است و آن دلیل از
product truth معلوم است. Helper نباید برای توجیه state نامعلوم حدس بزند.

## Info و adornmentها

Info فقط برای توضیح supplementary است. requirement لازم، Error، consequence یا
policy را تنها پشت آن نگذارید.

Leading icon معمولاً تزئینی است و نباید نام field را دوباره announce کند. اگر
Trailing به action تعاملی مانند پاک‌کردن مقدار تبدیل شود:

- action و نتیجهٔ آن باید معلوم باشد؛
- accessible name معنادار لازم است؛
- نام action با Label field اشتباه نشود؛
- focus، keyboard behavior و hit target را component/implementation تخصصی
  تعیین کند.

## Localization و input purpose

- Label، Helper و Error فارسی از جهت پایهٔ RTL پیروی می‌کنند.
- ایمیل، URL، کد، شمارهٔ پیگیری و free text پویا باید با isolation و field
  contract مناسب نمایش داده شوند.
- format example را به‌صورت دستی از digit/calendar policy حل‌نشده نسازید.
- input type، input purpose و autocomplete metadata باید از معنای واقعی field
  بیایند؛ content writer نباید token فنی را حدس بزند.
- paste، autofill یا password manager را بدون محدودیت تأییدشده ممنوع نکنید.

## انتخاب component

- متن تک‌خطی → Text Input.
- متن چندخطی → Textarea.
- انتخاب از optionهای تعریف‌شده → Select، Radio، Checkbox یا کنترل انتخابی.
- password با reveal/hide و رفتار authentication → Password Input.
- query با رفتار تخصصی search → Search.
- مقدار immutable که input semantics لازم ندارد → محتوای خواندنی عادی.

Placeholder یا copy نباید component اشتباه را قابل‌قبول جلوه دهد.

## قرارداد قطعی

<!-- generated:content-rules source=text-input.yml -->
<!-- این بخش از فایل YAML تولید می‌شود؛ دستی ویرایش نکنید. پس از تغییر قواعد اجرا کنید: python tooling/generate_content_rule_sections.py generate -->

### باید

- `TXT-001` نقش Label، Placeholder، Helper، Value و Error پیش از نوشتن مشخص شود.
- `TXT-002` Label purpose field را با اصطلاح همان surface مستقل از Placeholder و Value نام ببرد.
- `TXT-004` Placeholder فقط در صورت افزودن example یا format hint کوتاه و غیرضروری استفاده شود.
- `TXT-006` Helper کوتاه، field-specific، غیرتکراری و شامل context تأییدشده‌ای فراتر از Label باشد.
- `TXT-008` limit، format، reason، privacy، storage، consequence و validation فقط از product truth نوشته شوند.
- `TXT-011` Error شرط نقض‌شده و اصلاح معلوم را متنی و بدون اتکا به رنگ بیان کند.
- `TXT-015` Value واقعی کاربر یا سیستم مطابق type field حفظ شود و برای لحن برند بازنویسی نشود.
- `TXT-016` Disabled و Read only مطابق state واقعی و semantics متمایز استفاده شوند.
- `TXT-017` Trailing تعاملی action و accessible name معنادار داشته باشد و از icon تزئینی متمایز شود.
- `TXT-018` email، URL، identifier، quantity و free text بر اساس type و قرارداد localization و bidi نمایش داده شوند.

### نباید

- `TXT-019` متن چندخطی، optionهای ثابت یا رفتار تخصصی به Text Input عمومی تحمیل نشود.
- `TXT-021` Warning، normalization، input purpose یا state حل‌نشده به‌عنوان policy قطعی ساخته نشود.

### بازنشسته (مالک فعلی)

- `TXT-003` → `INS-004`، `INS-005`: تکرار قواعد الگوی instruction دربارهٔ Placeholder.
- `TXT-005` → `INS-011`: تکرار قاعدهٔ الگوی instruction دربارهٔ جداکردن Example.
- `TXT-007` → `INS-007`: تکرار قاعدهٔ الگوی instruction دربارهٔ پنهان‌نکردن محتوای ضروری.
- `TXT-009` → `INS-010`: تکرار قاعدهٔ الگوی instruction دربارهٔ requiredness.
- `TXT-010` → `INS-009`: عین قاعدهٔ الگوی instruction دربارهٔ تکرار wording.
- `TXT-012` → `INS-014`: عین قاعدهٔ الگوی instruction دربارهٔ حفظ requirement هنگام Error.
- `TXT-013` → `design-system.accessibility.forms`: ارتباط برنامه‌وار name، Helper و Error با input سازوکار accessibility است.
- `TXT-014` → `ERR-003`: تکرار قاعدهٔ الگوی خطا دربارهٔ حفظ اصطلاح Label.
- `TXT-020` → `INS-020`: عین قاعدهٔ الگوی instruction دربارهٔ paste، autofill و password manager.

<!-- /generated:content-rules -->

## مسائل باز

- convention سراسری Required/Optional هر product form.
- validation timing و focus strategy هر Form/Product.
- input type و autocomplete token هر field تا زمان ثبت source معتبر.
- policy normalization برای ارقام، فاصله، حروف عربی/فارسی و search input.
- Warning state برای Text Input تا زمان وجود use case تأییدشده.
- semantics و copy actionهای تعاملی Trailing برای componentهای تخصصی.

## ارزیابی

```bash
python tooling/validators/check_content_components.py
```

اعتبارسنج، identity، source evidence، rule IDها، eval link و پوشش همهٔ قواعد
blocking را کنترل می‌کند. خوانایی در layout، zoom، keyboard، screen reader،
autofill و رفتار واقعی validation باید در محصول نیز آزموده شود.
