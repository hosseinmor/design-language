---
id: content.pattern.confirmation
collection: content
type: content-pattern
title: Confirmations and Destructive Actions
summary: Defines when confirmation is necessary and how to name actions, consequences, recoverability, scope, and safe exits.
knowledge_state: verified
document_maturity: draft
related:
  - content.product-voice
  - content.terminology
  - content.pattern.error
  - design-system.pattern.confirmation
  - design-system.pattern.destructive-actions
  - design-system.experience-rule.action-hierarchy
  - design-system.component.modal
  - button
topics:
  - confirmation
  - destructive-actions
  - action-labels
  - modal-content
  - ux-writing
  - persian
---

# تأیید و اقدام مخرب

این سند قرارداد انسانی پیام‌های confirmation است. قواعد machine-readable در
[`confirmations.yml`](confirmations.yml) و نمونه‌های regression در
[`../../../ai/evals/content/confirmation-cases.yml`](../../../ai/evals/content/confirmation-cases.yml) قرار دارند.

## هدف

confirmation باید پیش از یک تصمیم پیامددار، چهار چیز را روشن کند:

1. چه عملی انجام می‌شود؛
2. روی چه چیزی یا چه کسانی اثر می‌گذارد؛
3. نتیجهٔ مستقیم آن چیست؛
4. آیا می‌توان آن را برگرداند یا بازیابی کرد.

هدف confirmation ایجاد مکث آگاهانه است، نه ترساندن کاربر یا گرفتن یک «بله».

## ابتدا تصمیم بگیرید confirmation لازم است یا نه

| وضعیت | الگو |
|---|---|
| کم‌ریسک، مورد انتظار و به‌آسانی قابل‌بازگشت | اقدام مستقیم؛ در صورت نیاز بازخورد یا Undo |
| پیامددار ولی غیرمخرب | confirmation خنثی |
| حذف داده، حذف دسترسی، لغو برگشت‌ناپذیر یا پیامد جدی دشواربازگشت | confirmation مخرب |

سبک Button هر نوع confirmation (مثلاً Danger Primary) تصمیم presentation است و
از [Destructive Actions](../../../design-system/patterns/destructive-actions.md) و
[Action Hierarchy](../../interaction/action-hierarchy.md) خوانده می‌شود.

فعل منفی به‌تنهایی تعیین‌کننده نیست. «ردکردن»، «بستن» یا «غیرفعال‌کردن» فقط
وقتی مخرب‌اند که رفتار واقعی محصول پیامد جدی و دشواربازگشت داشته باشد.

اگر Undo امن، واضح و واقعاً در دسترس است، ممکن است از confirmation بهتر باشد؛
اما متن نباید قابلیت Undo را قبل از اثبات رفتار محصول وعده دهد.

## قرارداد قطعی

<!-- generated:content-rules source=confirmations.yml -->
<!-- این بخش از فایل YAML تولید می‌شود؛ دستی ویرایش نکنید. پس از تغییر قواعد اجرا کنید: python tooling/generate_content_rule_sections.py generate -->

### باید

- `CNF-001` confirmation فقط برای تصمیمی استفاده شود که پیامد، ریسک یا ابهام معنادار دارد.
- `CNF-002` عمل و موضوع آن را مشخص کنید.
- `CNF-003` نتیجهٔ مستقیم و مهم اقدام را توضیح دهید.
- `CNF-004` امکان بازگشت، بازیابی یا دائمی‌بودن را مطابق رفتار واقعی محصول روشن کنید.
- `CNF-005` برچسب اقدام اصلی باید نتیجهٔ فعال‌سازی را توصیف کند.
- `CNF-006` اقدام ثانویه باید راه خروج امن یا ادامهٔ task را بدون ابهام نشان دهد.
- `CNF-010` در اقدام گروهی یا چندموضوعی، تعداد و دامنهٔ اثر را مشخص کنید.
- `CNF-012` کاربر باید بتواند پیش از اجرا جزئیات لازم را بخواند و از تصمیم خارج شود.

### نباید

- `CNF-008` با ترساندن، شرم، فوریت ساختگی یا لحن تبلیغاتی کاربر را به تصمیم هل ندهید.
- `CNF-011` متن پیش از اقدام نباید انجام‌شدن یا موفقیت نتیجه را القا کند.

### بازنشسته (مالک فعلی)

- `CNF-009` → `design-system.pattern.destructive-actions`: انتخاب Danger برای اقدام مخرب تصمیم presentation و hierarchy در Design System است.
- `CNF-007` → `BTN-004`: برچسب عمومی برای action پیامددار قاعدهٔ Button است و confirmation فقط یکی از موارد آن است.

<!-- /generated:content-rules -->

## ساختار

```text
عنوان      → تصمیم: [object] را [action] می‌کنید؟
توضیح      → پیامد + دامنه + امکان بازگشت
اقدام اصلی → نتیجهٔ دقیق عمل
اقدام دوم  → خروج امن یا ادامهٔ task
```

عنوان و توضیح Modal باید بدون مراجعه به صفحهٔ پوشیدهٔ پشت آن قابل‌فهم باشند.

## حذف غیرقابل‌بازگشت

```text
عنوان: آگهی را حذف می‌کنید؟
توضیح: آگهی «کارشناس فروش» حذف می‌شود و امکان بازگردانی آن نیست.
اقدام اصلی: حذف آگهی
اقدام دوم: انصراف
```

در این نمونه حذف دائمی مطابق product truth فرض شده است. اگر محصول archive یا
بازیابی دارد، متن باید تغییر کند و نوع confirmation دوباره از Destructive Actions
تعیین شود.

## تغییرات ذخیره‌نشده

```text
عنوان: تغییرات ذخیره‌نشده را کنار می‌گذارید؟
توضیح: اگر خارج شوید، تغییرات این صفحه ذخیره نمی‌شود.
اقدام اصلی: خروج بدون ذخیره
اقدام دوم: ادامهٔ ویرایش
```

«ادامهٔ ویرایش» از «لغو» روشن‌تر است، چون کاربر می‌فهمد با انتخاب آن به چه
taskی برمی‌گردد.

## حذف دسترسی

```text
عنوان: دسترسی مریم احمدی را حذف می‌کنید؟
توضیح: مریم احمدی دیگر به پنل سازمان دسترسی نخواهد داشت. برای بازگرداندن
دسترسی باید دوباره او را دعوت کنید.
اقدام اصلی: حذف دسترسی
اقدام دوم: انصراف
```

اگر مسیر دعوت دوباره تأیید نشده است، جملهٔ دوم را ننویسید و product truth را
پیش از انتشار تکمیل کنید.

## اقدام گروهی

```text
بد
این موارد حذف می‌شوند. ادامه می‌دهید؟
[بله] [خیر]

خوب
۳ درخواست شغلی را حذف می‌کنید؟
این اقدام روی هر ۳ درخواست شغلی اثر می‌گذارد و امکان بازگردانی آن‌ها نیست.
[حذف ۳ درخواست شغلی] [انصراف]
```

تعداد باید از همان انتخابی بیاید که کاربر می‌بیند. اگر شمارش تغییر می‌کند، متن
و برچسب اقدام باید پیش از اجرا به‌روز بمانند.

## «لغو» با دو معنای متفاوت

اگر action اصلی لغو یک رویداد یا فرایند است، action دوم را نیز «لغو» ننامید:

```text
مبهم
[لغو مصاحبه] [لغو]

روشن
[لغو مصاحبه] [انصراف]
```

در اینجا «لغو مصاحبه» نتیجهٔ business action است و «انصراف» از confirmation
خارج می‌شود.

## مرز با خطا و بازخورد

- confirmation پیش از action و برای تصمیم آگاهانه است.
- success یا error پس از action، نتیجهٔ واقعی را گزارش می‌کند.
- Toast برای گرفتن confirmation مناسب نیست؛ می‌تواند پس از action بازخورد یا
  Undo ارائه کند.
- Danger نیت مخرب را پیش از action نشان می‌دهد؛ Error شکست action را پس از آن.

اگر عملیات ناموفق شد، از [`errors.md`](errors.md) استفاده کنید و confirmation
را با پیام خطا مخلوط نکنید.

## دسترس‌پذیری و رفتار

سهم محتوا دو چیز است:

- عنوان دیده‌شده نام قابل‌دسترس Dialog می‌شود، پس باید بدون صفحهٔ پشت آن تصمیم را
  روشن کند.
- رنگ Danger به‌تنهایی پیامد را منتقل نمی‌کند؛ عنوان، توضیح و label لازم‌اند.

رفتار مال Design System است و این‌جا تکرار نمی‌شود:

- semantics، هدف اولیهٔ فوکوس (در confirmation مخرب: اقدام امن)، containment و
  بازگشت فوکوس: [Dialog](../../../design-system/components/dialog.md)؛
- Loading، جلوگیری از فعال‌سازی تکراری و حفظ عرض و فوکوس Button:
  [Button](../../../design-system/components/button.md)؛
- انتخاب confirmation مخرب و ترکیب آن:
  [Destructive Actions](../../../design-system/patterns/destructive-actions.md) و
  [Confirmation](../../../design-system/patterns/confirmation.md).

## چک‌لیست بازبینی

- [ ] confirmation واقعاً لازم است و جایگزین ساده‌تری مانند Undo بررسی شده است.
- [ ] action، object، consequence و recoverability روشن‌اند.
- [ ] scope و تعداد در عملیات گروهی مشخص‌اند.
- [ ] دکمهٔ اصلی نتیجه را نام می‌برد و دکمهٔ دوم خروج امن را نشان می‌دهد.
- [ ] «بله/خیر/تأیید/ادامه» جای label دقیق را نگرفته‌اند.
- [ ] متن پیامد مخرب را فقط وقتی می‌گوید که product truth آن را تأیید کرده است.
- [ ] متن نه سرزنش‌گر است، نه تبلیغاتی و نه پیشاپیش موفقیت را اعلام می‌کند.
- [ ] رفتار Modal، فوکوس و Loading با Design System سازگار است.

## ارزیابی

```bash
python tooling/validators/check_content_patterns.py
```

اعتبارسنج rule IDها، ساختار pattern، ارجاع‌های tone profile و پوشش همهٔ قواعد
blocking در evalها را کنترل می‌کند.
