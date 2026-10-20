---
id: content.component.notification
collection: content
type: content-component
title: Notification Content
summary: Defines how outcome and status content maps into the distinct Inline Notification and Toast anatomies, including severity, message roles, actions, dismissal, timeout indicators, and accessible announcements.
knowledge_state: verified
document_maturity: draft
related:
  - content.product-voice
  - content.terminology
  - content.localization
  - content.component.button
  - content.pattern.notifications
  - content.pattern.error
  - content.pattern.confirmation
  - design-system.component.notification
  - design-system.accessibility.dynamic-content-and-feedback
topics:
  - notification
  - toast
  - inline-notification
  - feedback
  - severity
  - accessibility
  - persian
---

# محتوای Notification

این سند قرارداد component-specific برای `Inline Notification` و `Toast` است.
قواعد machine-readable در [`notification.yml`](notification.yml) و نمونه‌های
regression در
[`../../../ai/evals/content/notification-content-cases.yml`](../../../ai/evals/content/notification-content-cases.yml)
قرار دارند.

## مرز Pattern و Component

[`../patterns/notifications.md`](../patterns/notifications.md) تعیین می‌کند:

- آیا رویداد به feedback نیاز دارد؛
- severity معنایی چیست؛
- feedback درون‌صفحه‌ای، Inline Notification، Toast یا الگوی پاسخ‌خواه است؛
- پیام چه نتیجه، object و next stepی را منتقل می‌کند.

این سند تعیین می‌کند همان پیام چگونه در anatomy تأییدشدهٔ Inline Notification
یا Toast قرار می‌گیرد. runtime timing، stacking، placement، default
dismissibility و announcement implementation هنوز در منابع canonical کامل
نیستند و این contract آن‌ها را اختراع نمی‌کند.

## دو کامپوننت مستقل

```text
Inline Notification
→ persistent contextual feedback inside layout

Toast
→ transient floating feedback in a viewport-level region
```

این دو variant یک کامپوننت با axis مشترک `Type` نیستند. انتخاب آن‌ها از context،
persistence و نیاز به action می‌آید، نه فقط از severity.

| نیاز | presentation مناسب |
|---|---|
| پیام باید بماند یا برای ادامه خوانده شود | Inline Notification |
| پیام به section مشخص وابسته است | Inline Notification |
| recovery/action باید در دسترس بماند | Inline Notification یا in-place feedback |
| feedback کوتاه است و ازدست‌رفتن آن task را مختل نمی‌کند | Toast |
| تصمیم یا پاسخ پیش از ادامه لازم است | Modal/Confirmation، نه Notification |

## Severity

هر دو کامپوننت چهار severity مشترک دارند:

- `Info` — واقعیت یا تغییر خنثی مفید؛
- `Success` — outcome تأییدشده؛
- `Warning` — ریسک یا محدودیت قبل از شکست قطعی؛
- `Error` — failure واقعی.

`Danger` severity پنجم نیست. Danger نیت مخرب پیش از action را نشان می‌دهد؛ Error
شکست action را گزارش می‌کند. `High` در Toast نیز severity یا urgency نیست؛ فقط
contrast treatment است.

## Inline Notification anatomy

```text
Message       required
Description   optional
Action        optional; at most one
Dismiss       optional
```

### Message

Message نتیجه یا وضعیت اصلی را مستقل و کوتاه بیان می‌کند:

```text
اتصال ناپایدار است
بارگذاری رزومه ناموفق بود
دسترسی این بخش تغییر کرده است
```

### Description

Description فقط consequence، context یا recovery معناداری را اضافه می‌کند:

```text
ممکن است ذخیرهٔ تغییرات بیشتر طول بکشد.
اتصال اینترنت را بررسی و دوباره تلاش کنید.
```

Description helper metadata نیست و نباید Message را با wording دیگری تکرار
کند. اگر محتوا paragraph-like، طولانی یا reading-oriented است، container یا
pattern مناسب‌تری لازم است.

یک Inline Notification کوتاه همان component با Description خاموش است؛ برای آن
variant «one-line» جدا نسازید.

## Toast anatomy

```text
Title       optional
Message     required
Action      optional; at most one
Dismiss     optional
Timeout indicator optional
```

### Message

Message باید بدون Title نیز نتیجهٔ اصلی را منتقل کند:

```text
تغییرات رزومه ذخیره شد.
درخواست شغلی ارسال نشد. دوباره تلاش کنید.
```

### Title

Title فقط وقتی استفاده شود که اطلاعات را سریع‌تر دسته‌بندی یا object را روشن
می‌کند. Title نباید Message را تکرار کند:

```text
Title: تغییرات رزومه
Message: ذخیره شد.
```

اگر حذف Title چیزی از فهم کم نمی‌کند، آن را نشان ندهید. عنوان‌های generic مانند
«موفقیت»، «خطا»، «هشدار» یا «اطلاع» severity را تکرار می‌کنند و context تازه‌ای
نمی‌دهند.

Toast برای متن بلند، چند action، instruction حیاتی، confirmation یا recoveryای
که باید باقی بماند مناسب نیست.

## Action

هر Notification حداکثر یک action دارد:

- navigation یا مقصد مستقل → Link؛
- operation یا تغییر state → Button؛
- Undo → فقط وقتی واقعاً پیاده‌سازی، امن و در بازهٔ لازم در دسترس است.

Action label باید نتیجه را نام ببرد: «تلاش دوباره»، «مشاهدهٔ درخواست»،
«بازگردانی». از «بیشتر»، «اینجا» یا «کلیک کنید» استفاده نکنید.

Action ضروری را به Toast خودکارپنهان‌شونده وابسته نکنید، مگر runtime زمان کافی،
pause و دسترسی پایدار را تضمین کند. High Toast فعلاً inverse Button تأییدشده
ندارد؛ تا رفع gap، action عملیاتی Button در آن handoff-ready نیست و Link
Inverse تأییدشده باقی می‌ماند.

## Dismiss

Dismiss از Icon Button مشترک استفاده می‌کند. برای UI فارسی:

```text
accessible name: بستن
Tooltip: بستن
```

Tooltip جای accessible name نیست. `Dismissible=False` یعنی کنترل نمایش داده
نمی‌شود؛ copy نباید از نبود یا وجود آن default سراسری بسازد.

بستن Notification نباید با Undo، Cancel business action یا رفع علت اشتباه شود.
اگر dismissal نتیجه یا داده‌ای فراتر از پنهان‌کردن feedback دارد، آن behavior
باید در Product truth ثبت شود.

## Timeout indicator

Timeout indicator فقط باقی‌ماندهٔ عمر auto-dismiss Toast را نشان می‌دهد؛ progress
عملیات نیست. متن نباید آن را «پیشرفت»، «در حال تکمیل» یا درصد outcome بنامد.

- Timed Toast می‌تواند indicator داشته باشد.
- Persistent Toast indicator ندارد.
- مدت دقیق timeout هنوز runtime-owned و unverified است.
- content نباید عددی مانند «۵ ثانیه دیگر بسته می‌شود» بسازد مگر runtime همان
  مقدار را به‌صورت معتبر expose کرده باشد.

## Announcement و focus

visual severity و announcement urgency دو تصمیم مستقل‌اند:

- Error همیشه `alert` نیست.
- Success معمولی باید non-interruptive بماند.
- focus فقط به‌دلیل ظاهرشدن Toast جابه‌جا نمی‌شود.
- action داخل Notification keyboard-accessible است اما autofocus نمی‌گیرد.
- یک event را بی‌دلیل با Toast، focus move و live announcement تکرار نکنید.
- اگر پیام خودکار ناپدید می‌شود، runtime باید فرصت کافی برای خواندن و action را
  فراهم کند.

این سند semantic role یا politeness ثابت برای هر severity تعیین نمی‌کند.

## State truth

- Success فقط پس از outcome تأییدشده نوشته می‌شود.
- Warning شکست قطعی نیست و نباید به Error تبدیل شود.
- Error از pattern خطا، مشکل و recovery معلوم را می‌گیرد.
- Loading/Progress با Notification success اشتباه نمی‌شود.
- pre-action destructive warning از Danger semantics استفاده می‌کند، نه Error
  feedback.

```text
پیش از حذف: این اقدام آگهی را برای همیشه حذف می‌کند. → Danger callout
پس از شکست: آگهی حذف نشد. دوباره تلاش کنید. → Error notification
```

## Terminology و Localization

- action و object را با terminology همان audience و surface نام ببرید.
- count، amount، date و variable را با formatter معتبر نمایش دهید.
- identifier، نام کاربر و متن دوجهته را isolate کنید.
- internal code، raw placeholder یا نام سرویس را جای پیام کاربر نشان ندهید.
- Message، Description و action را fragmentهای ناسازگار یا دوزبانه نسازید.

## قرارداد قطعی

### باید

- Inline Notification و Toast را بر اساس persistence و context انتخاب کنید.
- severity را از معنی outcome یا state تعیین کنید.
- Message نتیجه یا وضعیت واقعی را مستقل و روشن نام ببرد.
- Description یا Title فقط اطلاعات تازه اضافه کند.
- action واحد، معنادار و واقعاً قابل‌استفاده باشد.
- Dismiss موجود نام «بستن» و accessible relationship درست داشته باشد.
- announcement را مستقل از severity و با کم‌مزاحمت‌ترین روش کافی تعیین کنید.

### نباید

- Inline Notification و Toast را یک `Type` مشترک فرض کنید.
- Danger یا High contrast را severity پنجم در نظر بگیرید.
- Title/Description را برای تکرار Message استفاده کنید.
- متن بلند، confirmation یا recovery حیاتی را در Toast گذرا قرار دهید.
- focus را برای ظاهرشدن Toast جابه‌جا کنید.
- timeout، stacking، placement یا dismissibility تعریف‌نشده بسازید.
- success را پیش از outcome واقعی یا با hype اعلام کنید.

## مسائل باز

- exact Toast timeout duration.
- stacking، queue و maximum simultaneous Toasts.
- responsive placement.
- default dismissibility/persistence هر feedback class.
- actionable Toast timing و fallback behavior.
- executable live-region/screen-reader tests.
- inverse Button و Icon Button treatment برای High Toast.

## ارزیابی

```bash
python tooling/validators/check_content_components.py
```

اعتبارسنج identity، source evidence، rule IDها، eval link و پوشش قواعد blocking
را کنترل می‌کند. timing، placement، announcement output و keyboard interaction
باید در runtime واقعی آزموده شوند.
