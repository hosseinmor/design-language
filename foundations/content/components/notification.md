---
id: content.component.notification
collection: content
type: content-component
title: Notification Content
summary: Defines how outcome and status wording maps into the distinct Inline Notification and Toast anatomies (message roles, action labels, dismiss wording); presentation, severity set, action count, focus and announcements are referenced from the Design System and Accessibility.
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

## مرز مالکیت

[`../patterns/notifications.md`](../patterns/notifications.md) wording و ساختار
پیام نتیجه و معنی هر severity برای نوشتن را تعیین می‌کند. این سند تعیین می‌کند
همان پیام چگونه در anatomy تأییدشدهٔ Inline Notification یا Toast قرار می‌گیرد.

این تصمیم‌ها از منبع مالک خوانده می‌شوند و این‌جا تکرار نمی‌شوند:

- انتخاب Inline Notification، Toast یا in-place feedback، تعداد action و
  ماندگاری action → [Design System Notifications](../../../design-system/patterns/notifications.md)؛
- مجموعهٔ severity، `Danger` و `High`، anatomy، Dismiss و Timeout indicator →
  [Notification component](../../../design-system/components/notification.md)؛
- urgency، focus، autofocus و بازخورد تکراری →
  [Dynamic content and feedback](../../../accessibility/dynamic-content-and-feedback.md).

Inline Notification و Toast دو component مستقل‌اند، نه یک component با axis
مشترک `Type`. runtime timing، stacking، placement و default dismissibility
شکاف‌های باز Design System هستند و این contract آن‌ها را اختراع نمی‌کند.

## Wording هر severity

Message باید با معنی severity انتخاب‌شده هم‌خوان باشد (`NTC-003`): Warning ریسک
یا محدودیت را می‌گوید نه شکست را، و Info نتیجهٔ Success یا Error را القا نمی‌کند.
معنی severityها در [الگوی اعلان‌ها](../patterns/notifications.md#معنی-severity-برای-نوشتن) است.

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

متن Toast فقط بازخورد کوتاه و خودبسنده است و confirmation، instruction حیاتی یا
recovery ماندگار را حمل نمی‌کند (`NTC-008`). اگر چنین محتوایی لازم است، انتخاب
presentation ماندگار را از Design System بگیرید.

## Action

تعداد action، انتخاب Link یا Button و ماندگاری action در Toast را
[Design System Notifications](../../../design-system/patterns/notifications.md#actions)
تعیین می‌کند. سهم محتوا wording است:

- Action label نتیجه را نام می‌برد: «تلاش دوباره»، «مشاهدهٔ درخواست»،
  «بازگردانی». از «بیشتر»، «اینجا» یا «کلیک کنید» استفاده نکنید.
- Undo فقط وقتی نوشته می‌شود که واقعاً پیاده‌سازی، امن و در بازهٔ لازم در دسترس است.

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

معنی Timeout indicator در [Notification component](../../../design-system/components/notification.md#timeout-indicator)
تعریف شده است. سهم محتوا wording است: copy یا accessible name آن را «پیشرفت»،
«در حال تکمیل» یا درصد outcome نمی‌نامد (`NTC-014`)، و copy نباید عددی مانند «۵ ثانیه دیگر بسته می‌شود» بسازد مگر
runtime همان مقدار را به‌صورت معتبر expose کرده باشد.

## State truth

- Success فقط پس از outcome تأییدشده و Error فقط پس از failure واقعی نوشته
  می‌شود (`NTF-005`، `NTF-015`).
- Error از pattern خطا، مشکل و recovery معلوم را می‌گیرد.
- Loading/Progress با Notification success اشتباه نمی‌شود.
- هشدار مخرب پیش از action متعلق به [الگوی confirmation](../patterns/confirmations.md) است.

## Terminology و Localization

- action و object را با terminology همان audience و surface نام ببرید (`NTC-020`).
- count، amount، date و variable را با formatter معتبر نمایش دهید.
- identifier، نام کاربر و متن دوجهته را isolate کنید.
- internal code، raw placeholder یا نام سرویس را جای پیام کاربر نشان ندهید.
- Message، Description و action را fragmentهای ناسازگار یا دوزبانه نسازید.

## قرارداد قطعی

<!-- generated:content-rules source=notification.yml -->
<!-- این بخش از فایل YAML تولید می‌شود؛ دستی ویرایش نکنید. پس از تغییر قواعد اجرا کنید: python tooling/generate_content_rule_sections.py generate -->

### باید

- `NTC-003` Message با معنی severity انتخاب‌شده هم‌خوان باشد؛ Warning ریسک را بگوید نه شکست را، و Info نتیجهٔ Success یا Error را القا نکند.
- `NTC-005` Message required باشد و نتیجه یا وضعیت واقعی را مستقل و روشن نام ببرد.
- `NTC-006` Inline Description فقط context، consequence یا recovery تکمیلی و غیرتکراری اضافه کند.
- `NTC-007` Toast Title فقط در صورت افزودن دسته‌بندی یا object تازه استفاده شود و Message را تکرار نکند.
- `NTC-010` navigation از Link و operation از Button با label نتیجه‌محور استفاده کند.
- `NTC-011` Undo یا action ضروری فقط با behavior تأییدشده و فرصت دسترسی کافی ارائه شود.
- `NTC-012` Dismiss موجود accessible name و Tooltip فارسی «بستن» داشته باشد.
- `NTC-020` action و object با terminology همان audience و surface نامیده شوند.
- `NTC-021` count، amount، date، identifier، نام و متن دوجهته با formatter و bidi contract معتبر نمایش داده شوند.

### نباید

- `NTC-002` Inline Notification و Toast یک component با Type axis مشترک فرض نشوند.
- `NTC-008` متن Toast confirmation، instruction حیاتی یا recovery ماندگار را حمل نکند و فقط بازخورد کوتاه و خودبسنده باشد.
- `NTC-014` Timeout indicator در copy یا accessible name «پیشرفت»، «در حال تکمیل» یا درصد outcome نامیده نشود.

### بازنشسته (مالک فعلی)

- `NTC-001` → `design-system.pattern.notifications`: انتخاب Inline Notification یا Toast تصمیم presentation در Design System است.
- `NTC-004` → `design-system.pattern.notifications`، `design-system.component.notification`: Danger و High contrast به‌عنوان severity را Design System رد کرده است.
- `NTC-009` → `design-system.pattern.notifications`: سقف تعداد action تصمیم composition در Design System است؛ واقعی‌بودن action در NTC-011 می‌ماند.
- `NTC-013` → `NTF-014`: تکرار قاعدهٔ الگو دربارهٔ اختراع‌نکردن timing، stacking و dismissibility.
- `NTC-015` → `design-system.pattern.notifications`، `design-system.accessibility.dynamic-content-and-feedback`: فوریت announcement سازوکار دسترس‌پذیری است، نه wording.
- `NTC-016` → `design-system.pattern.notifications`، `design-system.accessibility.dynamic-content-and-feedback`: focus و autofocus در Toast رفتار تعاملی است؛ عین NTF-012.
- `NTC-017` → `design-system.pattern.notifications`، `design-system.accessibility.dynamic-content-and-feedback`: هماهنگی Toast، focus و live announcement سازوکار تعاملی است.
- `NTC-018` → `NTF-005`، `NTF-015`: تکرار قاعدهٔ الگو؛ NTF-005 برای Success و NTF-015 برای Error.
- `NTC-019` → `design-system.pattern.notifications`: ماندگاری recovery و action یک شکاف باز presentation در Design System است و در copy پر نمی‌شود.
- `NTC-022` → `NTF-008`، `NTF-009`: تکرار قواعد الگو دربارهٔ پیام کلی و هیجان‌زده.

<!-- /generated:content-rules -->

## مسائل باز

شکاف‌های timing، stacking، placement، dismissibility، actionable Toast و High
Toast در [Design System Notifications](../../../design-system/patterns/notifications.md#variations-and-gaps)
پیگیری می‌شوند و در copy پر نمی‌شوند.

## ارزیابی

```bash
python tooling/validators/check_content_components.py
```

اعتبارسنج identity، source evidence، rule IDها، eval link و پوشش قواعد blocking
را کنترل می‌کند. timing، placement، announcement output و keyboard interaction
باید در runtime واقعی آزموده شوند.
