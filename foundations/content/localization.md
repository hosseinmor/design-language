---
id: content.localization
collection: content
type: content-guideline
title: Persian Localization
summary: Defines the source-backed Persian language, RTL, mixed-direction text, locale formatting, translation, product-name, and dynamic-variable contract for product content.
knowledge_state: verified
document_maturity: draft
related:
  - content.content-guidelines
  - content.product-voice
  - content.terminology
  - content.pattern.instructions-and-helper-text
  - design-system.accessibility.content
  - design-system.accessibility.forms
  - design-system.experience-rule.contextual-guidance
topics:
  - localization
  - persian
  - rtl
  - bidi
  - numbers
  - dates
  - variables
  - translation
---

# بومی‌سازی فارسی

این سند قرارداد مشترک بومی‌سازی محتوای محصول را برای انسان و AI تعریف می‌کند.
منبع machine-readable آن در [`localization.yml`](localization.yml) و evalهای آن
در [`../../ai/evals/content/localization-cases.yml`](../../ai/evals/content/localization-cases.yml) قرار دارد.

Localization فقط ترجمهٔ واژه‌ها نیست. زبان، جهت، قالب عدد و زمان، واحد، نام
محصول و متغیرهای runtime باید در کنار هم معنای درست و خوانایی قابل‌اعتماد بسازند.

## مرز شواهد و تصمیم‌ها

### تثبیت‌شده در منابع فعلی

- زبان پایهٔ محتوای محصول جاب‌ویژن فارسی معیار نوشتاری و خطاب کاربر «شما» است.
- صفحه باید زبان پایه را برنامه‌وار اعلام کند و تغییر زبانِ بخش معنادار نیز مشخص
  شود.
- تجربهٔ فارسی RTL است و layout باید از semantics منطقی Start/End استفاده کند.
- متن دوجهته، نام کاربر، URL، ایمیل، کد و محتوای runtime باید بدون به‌هم‌ریختن
  ترتیب و نشانه‌گذاری نمایش داده شوند.
- اصطلاحات از واژه‌نامه و نام‌های رسمی محصول می‌آیند؛ ترجمهٔ لفظ‌به‌لفظ concept
  جدید نمی‌سازد.
- عدد، تاریخ، زمان، درصد و واحد باید با formatter آگاه از locale ساخته شوند، نه
  با چسباندن رشته‌های ثابت.

### تصمیم اجرایی Product Content در این سند

- `fa-IR` شناسهٔ زبان پایهٔ محتوای فارسی است.
- هر مقدار پویا قبل از ورود به جمله باید بر اساس نوعش format شود و محدودهٔ bidi
  خودش را داشته باشد.
- identifierهایی مانند ایمیل، URL، شمارهٔ پیگیری و کد نباید با تبدیل عمومی رقم
  یا نشانه‌گذاری تغییر کنند.
- جملهٔ قابل‌ترجمه باید یک واحد معنایی کامل باشد؛ fragmentهای قابل‌چسباندن قرارداد
  ترجمه نیستند.
- fallback نباید متن دو زبان را در یک جمله ترکیب یا واژهٔ ناقص تولید کند.

### هنوز تصمیم Product یا Engineering لازم دارد

- زبان‌های واقعاً پشتیبانی‌شده در هر محصول و سطح
- رقم فارسی یا لاتین برای هر surface و نوع داده
- تقویم هجری شمسی یا میلادی برای هر concept و flow
- timezone مرجع و سیاست تبدیل زمان
- نمایش ریال، تومان و گردکردن مبلغ در هر محصول
- library و API canonical برای formatting و plural/select
- سیاست normalization ورودی‌های کاربر و جست‌وجو
- fallback ترجمه و رفتار رشتهٔ گمشده در runtime

تا زمان تصمیم، AI و نویسنده نباید یک انتخاب را به همهٔ محصولات تعمیم دهند.

## زبان و نگارش پایه

- متن رابط فارسی با `fa-IR` و جهت RTL ارائه شود.
- فارسی معیار نوشتاری، نیم‌فاصله و نویسه‌های فارسی «ی» و «ک» در copy تألیفی
  رعایت شوند.
- دادهٔ واردشدهٔ کاربر صرفاً برای یکدست‌کردن ظاهر بازنویسی نشود؛ normalization
  ذخیره یا جست‌وجو یک تصمیم Engineering/Product است.
- تغییر زبانِ عبارت یا passage وقتی برای پردازش و تلفظ معنادار است با language
  metadata مشخص شود؛ صرف لاتین‌بودن یک نام تجاری همیشه به معنی تغییر زبان نیست.
- متن accessibility، label و accessible name باید همان زبان و معنی نسخهٔ دیداری
  را حفظ کنند.

نمونهٔ وب:

```html
<html lang="fa-IR" dir="rtl">
  <p>راهنمای <span lang="en" dir="ltr">GitHub</span></p>
</html>
```

## RTL و متن دوجهته

`RTL` فقط راست‌چین‌کردن نیست. جهت paragraph، ترتیب inline، punctuation و
جای‌گذاری component باید مستقل اما هماهنگ باشند.

- در layout از `Start` و `End` استفاده کنید؛ در RTL، Start سمت راست و End سمت
  چپ است.
- رشتهٔ LTR شناخته‌شده مانند URL، ایمیل، کد، hash و شمارهٔ پیگیری را در محدودهٔ
  LTR مستقل نمایش دهید.
- برای متن runtime با جهت نامعلوم، از isolation semantic مانند `bdi` یا
  `dir="auto"` استفاده کنید.
- هر متغیر مستقل باید جداگانه isolate شود؛ isolate کردن کل جمله جای آن را نمی‌گیرد.
- کنترل‌نویسه‌های نامرئی bidi را به copy ثابت یا دادهٔ کاربر اضافه نکنید وقتی
  markup semantic در دسترس است.
- نویسه‌های دارای شکل mirrored مانند پرانتز را دستی جایگزین نکنید؛ direction و
  rendering باید آن را مدیریت کنند.

```html
<p>رزومهٔ <bdi>Alex Smith</bdi> دریافت شد.</p>
<p>ارسال به <span dir="ltr">name@example.com</span> انجام نشد.</p>
```

## عدد، درصد و واحد

- مقدار عددی در data model عدد باقی بماند؛ localized string را به‌عنوان مقدار
  محاسباتی ذخیره نکنید.
- نمایش عدد با locale و policy همان محصول format شود.
- یک token عددی نباید رقم فارسی و لاتین را مخلوط کند.
- جداکنندهٔ اعشار، گروه‌بندی، علامت منفی و درصد را دستی با replace عمومی نسازید.
- unit باید با مقدار و context قابل‌فهم باشد: «۱۰۰ نویسه»، «۵ مگابایت» یا
  «۳ درخواست شغلی»؛ انتخاب واحد از product truth می‌آید.
- identifier عددی با quantity یکی نیست. شماره موبایل، کد ملی، OTP، شمارهٔ پیگیری
  و نسخهٔ نرم‌افزار باید مطابق قرارداد همان فیلد حفظ شوند.
- عدد تقریبی، compact notation و گردکردن فقط وقتی مجاز است که دقت لازم و policy
  محصول معلوم باشد.

CLDR برای فارسی ایران دادهٔ locale، رقم فارسی و الگوهای عددی فراهم می‌کند؛ اما
محصول باید تعیین کند کدام numbering system برای هر surface فعال است.

## تاریخ و زمان

تاریخ چهار تصمیم مستقل دارد:

```text
Instant
→ Time zone
→ Calendar
→ Locale format
```

- ترتیب اجزا و نام ماه را با formatter locale-aware بسازید.
- تقویم را از زبان نتیجه نگیرید؛ فارسی‌بودن UI به‌تنهایی ثابت نمی‌کند هر تاریخ
  باید هجری شمسی باشد.
- زمان نسبی مانند «۳ روز پیش» فقط وقتی استفاده شود که دقت و تغییر آن با task
  سازگار است؛ برای deadline یا سابقهٔ حساس، تاریخ مطلق لازم است.
- وقتی کاربران یا رویدادها در timezoneهای متفاوت‌اند، timezone یا زمینهٔ کافی
  را نشان دهید.
- «امروز»، «فردا» و deadline باید از clock و timezone معتبر محصول بیایند.
- تاریخ و زمان را با fragmentهای دستی مانند `{day}/{month}/{year}` نسازید مگر
  قرارداد همان فیلد دقیقاً چنین قالبی را الزام کند.

CLDR برای `fa` نمونه‌های ترتیب تاریخ و زمان ۲۴ساعته دارد، اما انتخاب calendar،
timezone و سطح کوتاهی/بلندی همچنان تصمیم محصول است.

## ترجمه و fallback

- concept را ترجمه کنید، نه رشته را بدون context. Terminology و Product
  Knowledge معنی و label مخاطب را تعیین می‌کنند.
- رشتهٔ قابل‌ترجمه باید جمله یا پیام کامل باشد تا ترتیب اجزا، فعل و شمار در زبان
  مقصد قابل‌تغییر باشد.
- برای translator، surface، intent، نوع متغیر، محدودیت فضا و نتیجهٔ action را
  توضیح دهید.
- یک رشته را فقط به‌دلیل برابر بودن متن در دو context reuse نکنید؛ معنی و امکان
  تغییر مستقل را بررسی کنید.
- fallback باید در سطح کل پیام رخ دهد. ترکیب label فارسی، فعل انگلیسی و fragment
  گمشده خروجی معتبر نیست.
- متن منبع یا ترجمه نباید product behavior، محدودیت یا claim تازه بسازد.

## نام محصول، برند و اصطلاحات

- نام رسمی محصول یا قابلیت را از source canonical و واژه‌نامه بگیرید.
- نام برند، URL، handle، plan یا integration را فقط با تصمیم رسمی ترجمه یا
  transliterate کنید.
- نام code-only و internal را به‌دلیل نبود ترجمه وارد UI نکنید.
- نام رسمی را در وسط جمله طوری تغییر ندهید که identity یا امکان جست‌وجوی آن از
  بین برود.
- ترجمهٔ نام concept نباید تمایزهایی مانند آگهی شغلی/موقعیت شغلی/فرصت شغلی یا
  جذب/استخدام را collapse کند.

## متغیرها و محتوای پویا

هر متغیر باید contract داشته باشد:

| ویژگی | سؤال |
|---|---|
| type | شخص، object، count، amount، date، time، identifier یا free text؟ |
| source | از product truth، کاربر یا سرویس بیرونی می‌آید؟ |
| formatter | کدام locale، calendar، timezone یا unit policy را دارد؟ |
| grammar | آیا شمار، select یا ترتیب جمله با مقدار تغییر می‌کند؟ |
| bidi | جهت معلوم است یا isolation خودکار لازم دارد؟ |
| fallback | نبودن یا نامعتبر بودن مقدار چه خروجی تأییدشده‌ای دارد؟ |

- نام placeholder باید معنایی باشد: `{candidate_name}` نه `{0}`.
- مقدار پویا escape شود و هرگز markup یا دستور ترجمه را کنترل نکند.
- count با سازوکار plural/select formatter مدیریت شود؛ شرط‌های دست‌ساز روی رشتهٔ
  نهایی ننویسید.
- punctuation و فاصله بخشی از template محلی‌اند، نه بخشی از مقدار متغیر.
- متغیر ناموجود نباید placeholder خام، `null` یا جملهٔ شکسته به کاربر نشان دهد.
- نام و free text کاربر از نظر bidi isolate شوند و بدون دلیل زبانی بازنویسی نشوند.

```text
درست
{count, plural, one {# درخواست شغلی} other {# درخواست شغلی}}

نادرست
{count} + " درخواست شغلی"
```

syntax بالا illustrative است؛ library نهایی هنوز باید توسط Engineering ثبت شود.

## قرارداد قطعی

### باید

- زبان و جهت پایهٔ surface را برنامه‌وار مشخص کنید.
- بخش معنادار با زبان یا جهت متفاوت را با semantics مناسب مشخص کنید.
- عدد، تاریخ، زمان، درصد و واحد را بر اساس type و locale format کنید.
- متغیرهای runtime را type-aware، escaped و bidi-isolated نگه دارید.
- terminology و نام رسمی محصول را در ترجمه حفظ کنید.
- انتخاب‌های حل‌نشدهٔ calendar، digit، timezone و currency را صریح نگه دارید.

### نباید

- RTL را فقط با text alignment پیاده کنید.
- identifier را مانند quantity تبدیل یا گروه‌بندی کنید.
- جملهٔ ترجمه‌پذیر را از fragmentهای مستقل بسازید.
- نویسهٔ bidi نامرئی را جای semantics قابل‌مشاهده و قابل‌نگهداری بگذارید.
- از زبان UI، نوع تقویم یا timezone را حدس بزنید.
- placeholder خام یا fallback دوزبانه به کاربر نشان دهید.

## چک‌لیست بازبینی

- [ ] زبان پایه و تغییر زبان passageها مشخص است.
- [ ] layout و inline content در RTL و LTR واقعی آزموده شده‌اند.
- [ ] نام، ایمیل، URL، کد و مقدار runtime punctuation را به‌هم نمی‌ریزند.
- [ ] عدد و واحد از formatter و policy معتبر می‌آیند.
- [ ] calendar، timezone و precision تاریخ/زمان معلوم یا صریحاً unresolved است.
- [ ] رشتهٔ ترجمه یک واحد معنایی کامل دارد.
- [ ] نام‌های رسمی و اصطلاحات canonical حفظ شده‌اند.
- [ ] متغیرها type، formatter، bidi و fallback مشخص دارند.
- [ ] missing value باعث placeholder خام یا جملهٔ ناقص نمی‌شود.

## ارزیابی

```bash
python tooling/validators/check_content_localization.py
```

اعتبارسنج، ساختار منبع machine-readable، شناسه و evidence ruleها، اتصال eval و
پوشش قواعد blocking را کنترل می‌کند. صحت rendering، formatter runtime و
screen-reader output همچنان باید در محصول واقعی آزموده شود.

## منابع

- [W3C: Declaring language in HTML](https://www.w3.org/International/questions/qa-html-language-declarations.html)
- [W3C: Inline markup and bidirectional text](https://www.w3.org/International/articles/inline-bidi-markup/)
- [W3C: Strings and bidi](https://www.w3.org/International/articles/strings-and-bidi/)
- [Unicode CLDR: Persian guidance](https://cldr.unicode.org/translation/language-specific/persian)
- [Unicode CLDR: Persian locale data](https://www.unicode.org/cldr/charts/latest/summary/fa.html)
