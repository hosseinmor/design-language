---
id: content.pattern.error
collection: content
type: content-pattern
title: Error Messages
summary: Defines the wording, tone, recovery, and evaluation contract for product error messages; placement, focus, and programmatic error semantics are referenced from the Design System and Accessibility.
knowledge_state: verified
document_maturity: draft
related:
  - content.product-voice
  - content.terminology
  - design-system.accessibility.content
  - design-system.component.text-input
  - design-system.component.notification
  - design-system.component.dialog
  - design-system.pattern.notifications
  - design-system.accessibility.forms
  - design-system.accessibility.dynamic-content-and-feedback
topics:
  - errors
  - validation
  - recovery
  - ux-writing
  - accessibility
  - persian
---

# پیام‌های خطا

این سند قرارداد انسانی الگوی خطاست. منبع machine-readable قواعد در
[`errors.yml`](errors.yml) و نمونه‌های regression در
[`../../../ai/evals/content/error-cases.yml`](../../../ai/evals/content/error-cases.yml) قرار دارند.

## هدف

پیام خطا باید به کاربر کمک کند task را ادامه دهد. کاربر باید بفهمد:

1. چه چیزی مانع ادامه شده است؛
2. خطا به کدام فیلد، شیء یا اقدام مربوط است؛
3. اگر راه بازیابی معلوم است، قدم بعدی چیست.

خطا جای نمایش شخصیت برند نیست. پروفایل لحن آن وضوح حداکثری، گرمی کم و انگیزش
و بیان برند صفر است.

## قرارداد قطعی

<!-- generated:content-rules source=errors.yml -->
<!-- این بخش از فایل YAML تولید می‌شود؛ دستی ویرایش نکنید. پس از تغییر قواعد اجرا کنید: python tooling/generate_content_rule_sections.py generate -->

### باید

- `ERR-001` مشکل یا وضعیت ناموفق را مشخص کنید.
- `ERR-002` وقتی راه بازیابی معلوم و مجاز است، اقدام بعدی را بگویید.
- `ERR-003` نام فیلد، شیء یا اقدام را با همان اصطلاحی بنویسید که در UI دیده می‌شود.
- `ERR-007` علت، نتیجه یا امکان بازیابی را فقط در حدی بیان کنید که محصول تأیید می‌کند.
- `ERR-009` پس از خطای قابل‌بازیابی، دادهٔ معتبر و نامرتبط کاربر حفظ شود.
- `ERR-010` خطا در متن بیان شود و مشکل و موضوع آن بدون اتکا به رنگ، آیکن یا محل نمایش قابل‌فهم باشد.

### نباید

- `ERR-004` کاربر را سرزنش نکنید و خطا را به شخصیت یا توانایی او نسبت ندهید.
- `ERR-005` «نامعتبر است» یا «خطایی رخ داد» نباید کل پیام باشد.
- `ERR-006` کد خطا، نام سرویس یا اصطلاح داخلی نباید جای توضیح کاربرفهم را بگیرد.
- `ERR-008` شوخی، شعار، ایموجی و انگیزش را به پیام خطا اضافه نکنید.

<!-- /generated:content-rules -->

## ساختار پیام

```text
[مشکل یا وضعیت ناموفق]. [راه اصلاح یا اقدام بعدی].
```

در خطای یک فیلد، مشکل و راه اصلاح اغلب در یک جمله جمع می‌شوند:

```text
ایمیل را با قالب name@example.com وارد کنید.
رمز عبور باید حداقل ۸ نویسه داشته باشد.
```

در خطای عملیات:

```text
درخواست شغلی ارسال نشد. اتصال اینترنت را بررسی و دوباره تلاش کنید.
```

اگر علت معلوم نیست، فقط نتیجهٔ مشاهده‌شده را بیان کنید:

```text
تغییرات ذخیره نشد. دوباره تلاش کنید.
```

نوشتن «سرور پاسخ نداد» فقط وقتی مجاز است که این علت برای محصول قطعی، قابل‌فهم
و مفید باشد.

## wording برای هر scope

محل و شکل نمایش خطا تصمیم این الگو نیست؛ آن را از منبع مالک بگیرید و متن را
برای همان scope بنویسید:

| scope خطا | مالک محل و رفتار | قاعدهٔ محتوایی |
|---|---|---|
| یک ورودی مشخص | [Text Input](../../../design-system/components/text-input.md)، [Accessibility forms](../../../accessibility/forms.md) | نام فیلد و شرط اصلاح را بگویید. |
| فرم طولانی یا چند خطا | [Accessibility forms](../../../accessibility/forms.md)، [Form submission](../../../design-system/patterns/form-submission.md) | هر خطا را مستقل و با نام همان فیلد بنویسید. |
| یک بخش یا عملیات | [Design System Notifications](../../../design-system/patterns/notifications.md) | نتیجهٔ ناموفق و بازیابی را در همان زمینه نام ببرید. |
| context مسدودکننده و نیازمند پاسخ | [Dialog](../../../design-system/components/dialog.md) | مشکل و تصمیم لازم را بدون اتکا به background بنویسید. |
| بارگیری‌نشدن task اصلی | Product Knowledge و component همان صفحه | task ناموفق و مسیر retry یا جایگزین را روشن کنید. |

## خطای اعتبارسنجی

### فیلد الزامی

```text
بد: الزامی
بد: این فیلد نمی‌تواند خالی باشد
خوب: شماره موبایل را وارد کنید.
```

### قالب نامعتبر

```text
بد: ایمیل نامعتبر است
بد: شما ایمیل را اشتباه وارد کرده‌اید
خوب: ایمیل را با قالب name@example.com وارد کنید.
```

### محدودیت

```text
بد: رمز عبور ضعیف است
خوب: رمز عبور باید حداقل ۸ نویسه داشته باشد.
```

اگر چند شرط هم‌زمان لازم است، آن‌ها را پیش از ورود یا در helper توضیح دهید و
در خطا فقط شرط برآورده‌نشده را مشخص کنید. کاربر نباید با آزمون‌وخطا قواعد پنهان
را کشف کند.

## خطای سیستم یا شبکه

- نتیجهٔ ناموفق را با نام همان اقدام بگویید: «رزومه بارگذاری نشد».
- اگر retry امن است، اقدام مشخص بدهید: «دوباره تلاش کنید».
- اگر داده حفظ شده، فقط در صورت تأیید محصول آن را بگویید.
- اگر مشکل ادامه‌دار است، فقط مسیر پشتیبانی تأییدشده را معرفی کنید؛ عبارت کلی
  «با پشتیبانی تماس بگیرید» بدون مسیر قابل‌دسترسی کافی نیست.
- شناسهٔ فنی می‌تواند برای پشتیبانی به‌صورت اطلاعات ثانویه نمایش داده شود، اما
  نباید متن اصلی پیام باشد.

## خطا و واژه‌نامه

متن خطا اصطلاح جدید نمی‌سازد. اگر label فیلد «درخواست شغلی» است، پیام نباید آن
را «اپلیکیشن» یا «ارسال رزومه» بنامد. ابتدا concept و مخاطب را در
[`../terminology/terms.yml`](../terminology/terms.yml) پیدا کنید، سپس همان label
را در مشکل و راه بازیابی نگه دارید.

## دسترس‌پذیری

حداقل الزام WCAG برای متن خطا در [Accessible content](../../../accessibility/content.md#form-copy)
است و ارتباط برنامه‌وار، وضعیت invalid، مسیر focus پس از submit و فوریت
announcement در [Accessibility forms](../../../accessibility/forms.md) و
[Dynamic content and feedback](../../../accessibility/dynamic-content-and-feedback.md)
تعریف شده‌اند. این سند آن‌ها را بازتعریف نمی‌کند. سهم محتوا:

- خطا در متن بیان می‌شود و رنگ قرمز یا آیکن به‌تنهایی آن را منتقل نمی‌کند (`ERR-010`)؛
- خطای قابل‌بازیابی دادهٔ معتبر و نامرتبط را پاک نمی‌کند (`ERR-009`).

## چک‌لیست بازبینی

- [ ] مشکل مشخص است.
- [ ] شیء یا فیلد با همان label رابط نام‌گذاری شده است.
- [ ] راه بازیابیِ معلوم و امن ذکر شده است.
- [ ] علت یا نتیجه‌ای حدس زده نشده است.
- [ ] متن سرزنش‌گر، کلی، تبلیغاتی یا کدی نیست.
- [ ] متن برای scope و محل نمایشِ تعیین‌شده در Design System نوشته شده است.
- [ ] خطا بدون اتکا به رنگ یا آیکن قابل‌فهم است.

## ارزیابی

```bash
python tooling/validators/check_content_patterns.py
```

این بررسی ساختار مدل صدا، rule IDها، tone profileها، ارجاع‌های eval و پوشش
قواعد blocking را کنترل می‌کند. تشخیص کیفیت معنایی مثال‌های جدید همچنان به
مرور محتوا و آزمون محصول نیاز دارد.
