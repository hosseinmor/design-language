---
id: content.pattern.notifications
collection: content
type: content-pattern
title: Notifications and Outcome Feedback
summary: Defines the wording and message structure of inline notifications, Toasts, and in-place outcome feedback; severity set, presentation choice, actions, focus, and announcements are referenced from the Design System and Accessibility.
knowledge_state: verified
document_maturity: draft
related:
  - content.product-voice
  - content.terminology
  - content.pattern.error
  - content.pattern.confirmation
  - content.pattern.empty-states
  - design-system.component.notification
  - design-system.pattern.notifications
  - design-system.accessibility.dynamic-content-and-feedback
topics:
  - notifications
  - success-feedback
  - toast
  - inline-notification
  - accessibility
  - ux-writing
  - persian
---

# اعلان‌ها و بازخورد نتیجه

این سند قرارداد انسانی محتوای Inline Notification، Toast و بازخورد درون‌صفحه‌ای
است. قواعد machine-readable در [`notifications.yml`](notifications.yml) و
نمونه‌های regression در
[`../../../ai/evals/content/notification-cases.yml`](../../../ai/evals/content/notification-cases.yml) قرار دارند.

## هدف

بازخورد نتیجه باید بدون قطع بی‌دلیل task روشن کند:

1. چه اتفاقی افتاده یا چه وضعیتی برقرار است؛
2. نتیجه به کدام object یا action مربوط است؛
3. اگر نتیجه روی ادامهٔ task اثر دارد، گام بعدی چیست.

## مرز مالکیت

این سند فقط **wording و ساختار پیام** را مالک است. تصمیم‌های زیر از منبع مالک
خوانده می‌شوند و این‌جا تکرار نمی‌شوند:

| تصمیم | مالک |
|---|---|
| مجموعهٔ severityها، کنارگذاشتن Danger و treatment دیداری | [Design System Notifications](../../../design-system/patterns/notifications.md) |
| انتخاب درون‌صفحه‌ای، Inline Notification، Toast یا Modal | [Design System Notifications](../../../design-system/patterns/notifications.md#presentation-choice) |
| تعداد action، Link یا Button و ماندگاری action در Toast | [Design System Notifications](../../../design-system/patterns/notifications.md#actions) |
| anatomy، Action Slot، Dismiss و Timeout indicator | [Notification component](../../../design-system/components/notification.md) |
| فوریت announcement، focus و جلوگیری از بازخورد تکراری | [Dynamic content and feedback](../../../accessibility/dynamic-content-and-feedback.md) |

شکل نمایش ورودی نوشتن است: ابتدا تصمیم presentation را از Design System بگیرید،
سپس متن را برای همان presentation بنویسید. قرارداد محتوایی anatomy هر component
در [`../components/notification.md`](../components/notification.md) است.

## معنی severity برای نوشتن

Design System مجموعهٔ severityها را تعیین می‌کند و مالکیت معنی و wording آن‌ها را
به Content واگذار کرده است. متن باید با معنی severity انتخاب‌شده هم‌خوان باشد:

- **Info:** یک واقعیت یا تغییر وضعیت خنثی که دانستن آن برای task مفید است.
- **Success:** action واقعاً کامل شده و نتیجهٔ مورد انتظار ثبت یا اعمال شده است.
- **Warning:** ریسک، محدودیت یا وضعیت ناپایداری که هنوز به شکست قطعی تبدیل نشده
  است و توجه کاربر می‌تواند مهم باشد.
- **Error:** action یا سیستم شکست خورده است. ساختار و recovery را از
  [`errors.md`](errors.md) بگیرید.

هشدار دربارهٔ اقدام مخرب پیش از action در قالب اعلان نوشته نمی‌شود؛ wording آن
متعلق به [`confirmations.md`](confirmations.md) است.

## قرارداد قطعی

<!-- generated:content-rules source=notifications.yml -->
<!-- این بخش از فایل YAML تولید می‌شود؛ دستی ویرایش نکنید. پس از تغییر قواعد اجرا کنید: python tooling/generate_content_rule_sections.py generate -->

### باید

- `NTF-001` رویداد، severity معنایی و نیاز به ماندگاری پیش از نوشتن مشخص شود.
- `NTF-003` نتیجه یا وضعیت واقعی با action و object قابل‌فهم نام برده شود.
- `NTF-005` Success فقط پس از تأیید کامل‌شدن action اعلام شود.
- `NTF-006` اگر نتیجه روی ادامهٔ task اثر دارد، پیامد یا گام بعدی معلوم بیان شود.
- `NTF-015` Error فقط پس از failure تأییدشده اعلام شود؛ وقتی نتیجه هنوز نامعلوم است، شکست قطعی گزارش نشود.

### نباید

- `NTF-008` عبارت کلی مانند «عملیات با موفقیت انجام شد» بدون نام نتیجه کل پیام نباشد.
- `NTF-009` موفقیت معمولی با تحسین، هیجان، شعار یا ایموجی بزرگ‌نمایی نشود.
- `NTF-014` زمان نمایش، محل، stacking یا dismissibility تعریف‌نشده اختراع نشود.

### بازنشسته (مالک فعلی)

- `NTF-002` → `design-system.pattern.notifications`: انتخاب درون‌صفحه‌ای، Inline Notification یا Toast تصمیم presentation در Design System است.
- `NTF-004` → `VOICE-007`: تکرار قاعدهٔ عمومی اصطلاح canonical در product voice؛ عین LDP-008.
- `NTF-007` → `design-system.pattern.notifications`: سقف تعداد action تصمیم composition در Design System است.
- `NTF-010` → `design-system.pattern.notifications`، `content.pattern.confirmation`: کنارگذاشتن Danger از severityها تصمیم Design System است؛ هشدار پیش از action متعلق به confirmation است.
- `NTF-011` → `design-system.pattern.notifications`، `design-system.accessibility.dynamic-content-and-feedback`: فوریت announcement سازوکار دسترس‌پذیری است، نه wording.
- `NTF-012` → `design-system.pattern.notifications`، `design-system.accessibility.dynamic-content-and-feedback`: رفتار focus هنگام ظاهرشدن Toast متعلق به Design System و accessibility است.
- `NTF-013` → `design-system.pattern.notifications`، `design-system.accessibility.dynamic-content-and-feedback`: هماهنگی focus، live announcement و Toast سازوکار تعاملی است، نه wording.

<!-- /generated:content-rules -->

## ساختار پیام

```text
[نتیجه یا وضعیت مشخص]. [پیامد مهم یا گام بعدیِ معلوم].
```

بخش دوم فقط وقتی اضافه می‌شود که برای ادامه یا تصمیم کاربر مفید باشد.

```text
خوب: تغییرات رزومه ذخیره شد.
خوب: درخواست شغلی ارسال شد.
خوب: اتصال ناپایدار است؛ ممکن است ذخیرهٔ تغییرات بیشتر طول بکشد.

بد: عملیات با موفقیت انجام شد.
بد: عالی بود! درخواستتان با موفقیت ارسال شد 🎉
بد: درخواست شغلی ارسال شد.   ← وقتی سیستم هنوز نتیجه را تأیید نکرده است
```

## برچسب action و Undo

تعداد action و انتخاب Link یا Button را Design System تعیین می‌کند. این الگو فقط
wording را مالک است:

- برچسب action نتیجهٔ واقعی activation را نام می‌برد؛ قواعد برچسب در
  [`../components/button.md`](../components/button.md) هستند.
- «بازگردانی» فقط وقتی نوشته شود که بازیابی واقعاً پیاده‌سازی، امن و در بازهٔ
  لازم قابل‌دسترسی است.

```text
پیام: آگهی از ذخیره‌شده‌ها حذف شد.
اقدام: بازگردانی
```

این نمونه فقط وقتی معتبر است که «بازگردانی» واقعاً در همان تجربه کار کند.

## مرز با الگوهای دیگر

- confirmation پیش از action است؛ اعلان نتیجه پس از action یا هنگام تغییر
  وضعیت ظاهر می‌شود.
- پیام شکست از قواعد [`errors.md`](errors.md) پیروی می‌کند؛ این سند ساختار
  پیام نتیجه را روشن می‌کند.
- وضعیت خالی، موفقیت حذف آخرین آیتم نیست. بازخورد action و وضعیت خالی نقش‌های
  جدا دارند و می‌توانند بدون تکرار بیایند.
- Loading و progress نشان می‌دهند کار هنوز در جریان است؛ Success پایان تأییدشده
  را گزارش می‌کند.

## دسترس‌پذیری

فوریت announcement، رفتار focus، زمان‌بندی پیام گذرا و جلوگیری از بازخورد تکراری
در [Dynamic content and feedback](../../../accessibility/dynamic-content-and-feedback.md)
و [Design System Notifications](../../../design-system/patterns/notifications.md#accessibility)
تعریف شده‌اند. سهم محتوا:

- متن پیام بدون اتکا به رنگ یا severity دیداری قابل‌فهم است؛
- برچسب فارسی dismiss برابر «بستن» است.

مدت دقیق، تعداد هم‌زمان، جای‌گذاری، stacking و dismissibility پیش‌فرض شکاف‌های
باز Design System هستند و در copy پر نمی‌شوند.

## چک‌لیست بازبینی

- [ ] رویداد، نتیجه و severity درست طبقه‌بندی شده‌اند و presentation از Design System آمده است.
- [ ] پیام action و object واقعی را با اصطلاح همان surface نام می‌برد.
- [ ] Success فقط پس از تأیید نتیجه و Error فقط پس از failure واقعی است.
- [ ] برچسب action نتیجه‌محور است و Undo فقط با بازیابی واقعی آمده است.
- [ ] متن کلی، تبلیغاتی، کدی یا تکراری نیست.
- [ ] رفتار تعریف‌نشدهٔ runtime اختراع نشده است.

## ارزیابی

```bash
python tooling/validators/check_content_patterns.py
```

اعتبارسنج ساختار pattern، tone profileها، rule IDها و پوشش قواعد blocking در
evalها را کنترل می‌کند. کیفیت معنایی و تطابق با رفتار واقعی محصول همچنان به
مرور انسانی و آزمون محصول نیاز دارد.
