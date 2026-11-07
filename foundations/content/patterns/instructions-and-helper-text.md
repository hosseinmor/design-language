---
id: content.pattern.instructions-and-helper-text
collection: content
type: content-pattern
title: Instructions and Helper Text
summary: Defines the roles, timing, wording, and validation boundary for labels, instructions, helper text, placeholders, examples, and requirement indicators; programmatic association and required-state semantics are referenced from Accessibility.
knowledge_state: verified
document_maturity: draft
related:
  - content.product-voice
  - content.terminology
  - content.pattern.error
  - design-system.accessibility.forms
  - design-system.accessibility.content
  - design-system.experience-rule.contextual-guidance
  - design-system.component.text-input
  - design-system.component.textarea
topics:
  - instructions
  - helper-text
  - labels
  - placeholders
  - examples
  - required-optional
  - forms
  - accessibility
  - ux-writing
  - persian
---

# دستورالعمل‌ها و متن راهنما

این سند قرارداد انسانی Label، Instruction، Helper Text، Placeholder، Example و
Required/Optional wording است. قواعد machine-readable در
[`instructions-and-helper-text.yml`](instructions-and-helper-text.yml) و
نمونه‌های regression در
[`../../../ai/evals/content/instruction-helper-cases.yml`](../../../ai/evals/content/instruction-helper-cases.yml)
قرار دارند.

## هدف

کاربر باید پیش از آنکه به یک requirement برسد، بداند:

1. کنترل یا گروه چه اطلاعاتی می‌خواهد؛
2. قالب، محدودیت یا شرط واقعی چیست؛
3. چرا اطلاعات لازم است، اگر دانستن آن به تصمیم کمک می‌کند؛
4. کدام اطلاعات الزامی یا اختیاری‌اند؛
5. یک مقدار قابل‌قبول چگونه به نظر می‌رسد، اگر مثال لازم است.

هدف راهنما پیشگیری از خطاست؛ Error بعد از تشخیص failure وارد می‌شود.

## نقش هر نوع محتوا

| نوع | وظیفه | ماندگاری |
|---|---|---|
| Label | نام و purpose کنترل یا گروه | باید مستقل از مقدار ورودی قابل‌دریافت بماند |
| Instruction | اطلاعات لازم برای انجام task یا چند کنترل | پیش از نیاز و تا زمان مرتبط‌بودن در دسترس |
| Helper Text | context یا راهنمای کوتاه و field-specific | هنگام تکمیل فیلد قابل‌مشاهده |
| Placeholder | hint، example یا قالب تکمیلی | با ورود مقدار ناپدید می‌شود؛ منبع ضروری نیست |
| Example | نمونهٔ concrete از مقدار قابل‌قبول | در Placeholder یا Helper، با نقش روشن |
| Error | مشکل تشخیص‌داده‌شده و recovery | پس از validation؛ متعلق به Error pattern |
| Count | metadata دربارهٔ مقدار فعلی و limit | مستقل از Helper/Error و بر اساس واحد واقعی |

### Label

Label می‌گوید «این کنترل چیست؟»، نه اینکه همهٔ قواعد آن چیست.

```text
خوب: عنوان شغلی
خوب: شماره موبایل
بد: اینجا عنوان شغلی خود را وارد کنید
```

Label دیداری منبع معمول accessible name است. مخفی‌کردن Label فقط وقتی مجاز است
که composition منبع نام معتبر دیگری داشته باشد؛ Placeholder جای آن نیست.

### Instruction

Instruction برای requirementی است که کاربر برای تکمیل task، form، step یا group
باید بداند. آن را پیش از کنترل‌های مربوط قرار دهید و در Tooltip یا surface
گذرا پنهان نکنید.

```text
برای ادامه، سوابق شغلی ۵ سال اخیر را وارد کنید.
```

این جمله فقط وقتی مجاز است که بازهٔ ۵ سال واقعاً requirement محصول باشد.

### Helper Text

Helper اطلاعات کوتاه، غیرخطا و field-specific است که هنگام ورود مقدار مفید
می‌ماند. Helper می‌تواند قالب، محدودیت، دلیل یا اثر معلوم را توضیح دهد.

```text
حداکثر ۱۰۰ نویسه
فقط فایل PDF تا حجم ۵ مگابایت
این عنوان در رزومهٔ شما نمایش داده می‌شود.
```

مقادیر، نوع فایل، مقصد نمایش یا هر consequence باید از product truth بیایند.

### Placeholder

Placeholder می‌تواند example، hint یا expected format تکمیلی باشد، اما:

- Label را تکرار یا جایگزین نمی‌کند؛
- requirement ضروری را حمل نمی‌کند؛
- متن بلند و چندبخشی نیست؛
- نباید طوری نوشته شود که با value واقعی اشتباه شود.

```text
Label: ایمیل
Placeholder: name@example.com

Label: عنوان شغلی
Placeholder: مثال: طراح محصول
```

اگر ممکن است example با مقدار ازپیش‌پرشده اشتباه شود، «مثال:» را صریح بنویسید.

## Required و Optional

- requiredness با wording قابل‌فهم بیان می‌شود؛ semantics برنامه‌وار آن در
  [Accessibility forms](../../../accessibility/forms.md) تعریف شده است.
- رنگ یا `*` به‌تنهایی کافی نیست وقتی معنی آن برای کاربر روشن نشده است.
- در یک form، convention باید یکدست باشد: اگر همهٔ فیلدها الزامی‌اند، optionalها
  را با «اختیاری» مشخص کنید؛ اگر ترکیب فرم ابهام دارد، راهنمای کلی یا marker
  توضیح‌داده‌شده ارائه کنید.
- «الزامی» یا «اختیاری» را داخل Placeholder نگذارید؛ با ورود مقدار ناپدید می‌شود.
- business rule تعیین می‌کند فیلد required است؛ content آن را حدس نمی‌زند.

## محدودیت، قالب و مثال

### قالب

قالب را با نمونه یا rule قابل‌فهم بیان کنید:

```text
ایمیل را با قالب name@example.com وارد کنید.
تاریخ را به‌شکل ۱۴۰۵/۰۷/۰۹ وارد کنید.
```

فرمت تاریخ، عدد، شماره و locale باید با localization و implementation واقعی
سازگار باشد. نمونه نباید فرمتی را پیشنهاد دهد که parser نمی‌پذیرد.

### محدودیت

محدودیت سخت را پیش از رسیدن به آن نشان دهید:

```text
حداکثر ۵ مگابایت
بین ۸ تا ۶۴ نویسه
حداکثر ۱۰۰ نویسه
```

اگر limit فقط توصیه است، آن را به‌صورت الزام ننویسید. اگر شمارنده وجود دارد،
واحد آن—نویسه، واژه، فایل یا مورد—باید روشن باشد.

### دلیل یا استفاده

«چرا» را فقط وقتی اضافه کنید که به اعتماد یا انتخاب کمک می‌کند:

```text
این عنوان در رزومهٔ شما نمایش داده می‌شود.
```

از توجیه‌های مبهم مثل «برای تجربه بهتر» یا ادعاهای privacy و security بی‌منبع
پرهیز کنید.

## مرز Helper و Error

Helper پیش از خطا requirement را توضیح می‌دهد. Error پس از validation، شرط
برآورده‌نشده و راه اصلاح را نام می‌برد.

```text
Helper: رمز عبور باید حداقل ۸ نویسه داشته باشد.
Error: رمز عبور باید حداقل ۸ نویسه داشته باشد.
```

ممکن است wording مشابه باشد، اما state و نقش semantic متفاوت است. در کامپوننت
Text Input و Textarea، Error می‌تواند treatment معمول Helper را جایگزین کند.
اگر Helper چند requirement ضروری دارد، هنگام خطا باید شرط مرتبط در Error یا یک
Instruction ماندگار باقی بماند؛ اطلاعات حیاتی نباید ناپدید شود.

قواعد کامل Error در [`errors.md`](errors.md) قرار دارند.

## جلوگیری از تکرار

هر لایه باید اطلاعات جدیدی اضافه کند:

```text
بد
Label: ایمیل
Placeholder: ایمیل
Helper: ایمیل خود را وارد کنید

خوب
Label: ایمیل
Placeholder: name@example.com
Helper: نتیجهٔ بازیابی حساب به این ایمیل ارسال می‌شود.  ← فقط اگر رفتار تأیید شده است
```

اگر Label به‌تنهایی کافی است، Placeholder و Helper را حذف کنید. فضای خالی نیاز
به copy ساختگی ایجاد نمی‌کند.

## راهنمای تکمیلی و Progressive Disclosure

- instruction ضروری باید persistent و پیش از نیاز باشد.
- Info affordance، Toggletip و documentation برای توضیح supplementary مناسب‌اند.
- Tooltip تنها مسیر دسترسی به requirement، Error، consequence یا legal/policy
  content نیست.
- متن بلند را به نزدیک‌ترین سطح معنادار ببرید: group instruction، Toggletip،
  Popover یا documentation؛ Helper را به پاراگراف راهنما تبدیل نکنید.
- Link راهنما باید destination یا purpose قابل‌فهم داشته باشد؛ «بیشتر» یا
  «اینجا» به‌تنهایی کافی نیست.

## گروه‌ها و فیلدهای شرطی

- سؤال یا requirement مشترک Radio/Checkbox group در سطح group نوشته می‌شود، نه
  زیر هر option.
- instruction فیلد شرطی هنگام ظاهرشدن باید همراه همان context و در ترتیب منطقی
  در دسترس باشد.
- فیلد پنهان نباید requirement پنهانی ایجاد کند که submission را مسدود کند.
- از تکرار instruction گروه برای تک‌تک کنترل‌ها پرهیز کنید.

## Password، Upload و ورودی‌های محدود

### Password

- قواعد واقعی رمز عبور را پیش از ورود نشان دهید.
- paste و password manager را مجاز معرفی کنید، مگر محدودیت امنیتیِ مستند و
  توجیه‌شده وجود داشته باشد.
- برای «امنیت بیشتر» requirement ساختگی اضافه نکنید.

### Upload

اگر implementation محدودیت دارد، نوع، حجم و تعداد فایل را پیش از انتخاب بنویسید:

```text
فقط فایل PDF، حداکثر ۵ مگابایت
```

اگر resize، تبدیل، ذخیره یا اشتراک‌گذاری فایل معلوم نیست، دربارهٔ آن ادعا نکنید.

### Count

Count metadata است، نه Helper یا Error. `۲۴ از ۱۰۰ نویسه` فقط وقتی معتبر است که
حد، واحد و رفتار عبور از limit معلوم باشند. تغییر هر نویسه را به‌صورت assertive
announce نکنید.

## لحن و نگارش

- کوتاه، مستقیم و خنثی بنویسید.
- action یا constraint را مثبت بیان کنید: «فقط فایل PDF» به‌جای فهرست طولانی
  فایل‌های غیرمجاز.
- از «لطفاً» برای نرم‌کردن requirement استفاده نکنید؛ requirement را روشن کنید.
- کاربر را با «واضح است»، «به‌سادگی» یا «فقط کافی است» قضاوت نکنید.
- اصطلاح همان Label، surface و audience را حفظ کنید.

## دسترس‌پذیری

حداقل الزام WCAG برای Label، instruction و link purpose در
[Accessible content](../../../accessibility/content.md) و ارتباط برنامه‌وار
Helper، Error و group instruction با کنترل و required state در
[Accessibility forms](../../../accessibility/forms.md) تعریف شده‌اند. این سند آن‌ها
را بازتعریف نمی‌کند و فقط wording و توزیع نقش‌ها را مالک است:

- Placeholder تنها label یا تنها carrier requirement نیست (`INS-004`، `INS-005`)؛
- محتوای ضروری در Tooltip یا surface گذرا پنهان نمی‌شود (`INS-007`)؛
- requiredness با wording یکدست بیان می‌شود (`INS-010`)؛
- Link راهنما purpose قابل‌فهم دارد (`INS-017`).

## قرارداد قطعی

<!-- generated:content-rules source=instructions-and-helper-text.yml -->
<!-- این بخش از فایل YAML تولید می‌شود؛ دستی ویرایش نکنید. پس از تغییر قواعد اجرا کنید: python tooling/generate_content_rule_sections.py generate -->

### باید

- `INS-001` نقش هر متن به‌عنوان Label، Instruction، Helper، Placeholder، Example، Count یا Error پیش از نوشتن مشخص شود.
- `INS-002` Label purpose کنترل یا گروه را مستقل از Placeholder و مقدار ورودی مشخص کند.
- `INS-003` instruction لازم برای تکمیل task پیش از نیاز و تا زمان مرتبط‌بودن در دسترس باشد.
- `INS-006` قالب، limit، واحد، نوع فایل، دلیل، مقصد و consequence فقط مطابق product truth نوشته شود.
- `INS-008` Helper کوتاه، مرتبط با همان field و دارای اطلاعاتی فراتر از Label باشد.
- `INS-010` requiredness با wording یکدست و قابل‌فهم، مانند «اختیاری» یا marker توضیح‌داده‌شده، بیان شود.
- `INS-011` Example وقتی ممکن است با value واقعی اشتباه شود با نشانه‌ای مانند «مثال:» از مقدار جدا شود.
- `INS-012` نام field، object، action و واحد با terminology همان surface و audience هماهنگ بماند.
- `INS-013` Helper requirement را پیش از failure توضیح دهد و Error پس از validation شرط نقض‌شده و recovery را بیان کند.
- `INS-014` وقتی Error جای Helper treatment را می‌گیرد، requirement ضروری در Error یا Instruction ماندگار باقی بماند.
- `INS-017` Link یا action راهنما purpose یا destination قابل‌فهم داشته باشد و «بیشتر»، «اینجا» یا «ادامه» بدون context کافی به‌تنهایی برچسب نباشد.
- `INS-018` Count فقط با limit، واحد و رفتار واقعی استفاده شود و واحد آن در context قابل‌فهم باشد.

### نباید

- `INS-004` Placeholder جای Label یا accessible name استفاده نشود.
- `INS-005` requirement، consequence یا instruction ضروری فقط در Placeholder قرار نگیرد.
- `INS-007` requirement، Error، consequence یا policy ضروری فقط پشت Tooltip، Info یا surface گذرا پنهان نشود.
- `INS-009` Label، Placeholder و Helper با یک wording تکراری پر نشوند.
- `INS-015` محدودیت امنیتی، دلیل جمع‌آوری، privacy، storage یا رفتار فایل بدون منبع معتبر ادعا نشود.
- `INS-016` instruction کاربر را سرزنش نکند و task را با «واضح»، «ساده» یا «فقط کافی است» قضاوت نکند.
- `INS-020` paste، autofill یا password manager بدون محدودیت مشخص و توجیه‌شده ممنوع معرفی نشود.

### بازنشسته (مالک فعلی)

- `INS-019` → `design-system.accessibility.forms`: ارتباط برنامه‌وار Helper، Error و group instruction با کنترل سازوکار accessibility است، نه wording.
- `INS-021` → `INS-017`: نسخهٔ منفی همان قاعدهٔ purpose برای Link و action راهنما؛ در INS-017 ادغام شد.

<!-- /generated:content-rules -->

## چک‌لیست بازبینی

- [ ] هر متن نقش مشخص Label، Instruction، Helper، Placeholder، Example یا Error دارد.
- [ ] Label مستقل از Placeholder قابل‌فهم است.
- [ ] requirement قبل از نیاز و خارج از Tooltip گذرا در دسترس است.
- [ ] محدودیت و قالب با implementation واقعی منطبق‌اند.
- [ ] Required/Optional convention روشن و یکدست است.
- [ ] Example با value واقعی اشتباه نمی‌شود.
- [ ] Helper اطلاعات جدیدی اضافه می‌کند و Label را تکرار نمی‌کند.
- [ ] Error شرط نقض‌شده را حفظ می‌کند و اطلاعات ضروری ناپدید نمی‌شوند.
- [ ] متن داخلی، سرزنش‌گر یا دارای ادعای privacy/security بی‌منبع نیست.

## ارزیابی

```bash
python tooling/validators/check_content_patterns.py
```

اعتبارسنج ساختار pattern، rule IDها، tone profile و پوشش قواعد blocking در
evalها را کنترل می‌کند. business requirement و validation هر field همچنان باید
از Product Area یا implementation معتبر بیاید.
