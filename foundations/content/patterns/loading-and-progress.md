---
id: content.pattern.loading-and-progress
collection: content
type: content-pattern
title: Loading and Progress Content
summary: Defines classification, status language, progress truth, transitions, and accessibility for asynchronous product operations.
knowledge_state: verified
document_maturity: draft
related:
  - content.product-voice
  - content.terminology
  - content.pattern.error
  - content.pattern.notifications
  - design-system.accessibility.dynamic-content-and-feedback
  - design-system.accessibility.focus-management
  - button
  - design-system.pattern.loading-and-progress
topics:
  - loading
  - progress
  - async-status
  - skeleton
  - accessibility
  - ux-writing
  - persian
---

# بارگذاری و پیشرفت

این سند قرارداد انسانی محتوای Loading و Progress است. قواعد machine-readable
در [`loading-and-progress.yml`](loading-and-progress.yml) و نمونه‌های regression
در [`../../../ai/evals/content/loading-progress-cases.yml`](../../../ai/evals/content/loading-progress-cases.yml)
قرار دارند.

## وضعیت منبع

اسناد `design-system.pattern.loading-and-progress` و
`design-system.experience-rule.loading` هنوز scaffold و unverified هستند.
قواعد قطعی این سند از قراردادهای canonical دسترس‌پذیری، Button و مرزهای الگوهای
Error و Notification می‌آیند. مدت انتظار، threshold نمایش، ETA، رفتار دقیق
Skeleton و امکان لغو را نباید از این سند استنتاج کرد.

## هدف

در یک عملیات async، کاربر باید به‌اندازهٔ لازم بفهمد:

1. چه action یا محتوایی در جریان است؛
2. آیا پیشرفت واقعاً قابل‌اندازه‌گیری است؛
3. آیا باید منتظر بماند، می‌تواند task دیگری انجام دهد یا action معتبری دارد؛
4. عملیات چه زمانی واقعاً پایان یافته یا شکست خورده است.

## ابتدا وضعیت را طبقه‌بندی کنید

| وضعیت | معنی | قرارداد محتوا |
|---|---|---|
| Loading محلی | یک کنترل یا action مشخص در حال اجراست | زمینهٔ action را حفظ کنید؛ متن جدا فقط در صورت نیاز |
| Busy ناحیه یا صفحه | محتوای اصلی یک محدوده هنوز آماده نیست | محدوده و محتوای در انتظار را قابل‌فهم نگه دارید |
| Progress معین | مقدار کل و مقدار انجام‌شده معتبر و قابل‌اندازه‌گیری‌اند | درصد، تعداد یا مرحله را فقط از state واقعی نشان دهید |
| Progress نامعین | عملیات در جریان است اما مقدار باقی‌مانده معتبر نیست | فعالیت جاری را بگویید؛ درصد یا زمان نسازید |

Loading، Disabled، Empty و Error چهار وضعیت متفاوت‌اند. Loading یعنی نتیجه هنوز
معلوم نیست؛ Empty یعنی نتیجه با موفقیت دریافت شده اما محتوا وجود ندارد؛ Error
یعنی عملیات شکست خورده است.

## چه زمانی متن لازم است؟

برای یک action کوتاه و محلی که trigger و spinner زمینه را روشن نگه می‌دارند،
متن دیداری جدا ممکن است لازم نباشد. متن وضعیت را اضافه کنید وقتی:

- object یا action بدون آن مبهم می‌شود؛
- یک ناحیه یا task اصلی در انتظار است؛
- عملیات طولانی به نظر می‌رسد یا ممکن است متوقف‌شده برداشت شود؛
- مقدار پیشرفت معتبر به تصمیم یا اطمینان کاربر کمک می‌کند؛
- کاربر باید بداند می‌تواند صفحه را ترک کند، منتظر بماند یا عملیات را لغو کند و
  این رفتار در product truth تأیید شده است.

threshold زمانی ثابت در منابع canonical تعریف نشده است. عددی مانند «بعد از ۲
ثانیه متن را نمایش دهید» تصمیم این pattern نیست.

## ساختار پیام

### نامعین

```text
[action جاری + object]…
```

```text
در حال ذخیرهٔ تغییرات رزومه…
در حال بارگذاری آگهی‌های شغلی…
```

اگر context از خود کنترل کاملاً روشن است، متن کوتاه‌تر می‌تواند کافی باشد؛ اما
«در حال پردازش…» یا «لطفاً منتظر بمانید» به‌تنهایی action و object را مشخص
نمی‌کنند.

### معین

```text
[action جاری + object] — [مقدار واقعی انجام‌شده از کل]
```

```text
در حال بارگذاری رزومه — ۳ از ۵ مگابایت
در حال پردازش ۲۴ رزومه — ۱۸ مورد انجام شد
```

درصد، تعداد، مرحله و زمان باقی‌مانده فقط وقتی مجازند که از state واقعی و قابل
اعتماد بیایند. spinner تکرارشونده یا animation زمان‌محور، پیشرفت واقعی نیست.

## زمان و انتظار

- مدت یا زمان پایان را فقط با منبع معتبر محصول اعلام کنید.
- «چند لحظه»، «به‌زودی» و «تقریباً تمام شد» نیز ادعای زمانی‌اند؛ آن‌ها را صرفاً
  برای دلگرمی اضافه نکنید.
- اگر عملیات ادامهٔ پس‌زمینه‌ای، خروج امن یا notification پس از پایان دارد، فقط
  رفتار تأییدشده را بگویید.
- برای تحمل‌پذیرکردن انتظار از شوخی، شعار، rotating copy یا وعده استفاده نکنید.

## Action و لغو

- فعال‌سازی تکراری action در حال اجرا باید متوقف شود.
- Loading را از نظر معنا و ظاهر با Disabled یکی نکنید؛ action در جریان است، نه
  لزوماً غیرمجاز.
- «لغو» فقط وقتی نمایش داده شود که cancellation واقعاً پشتیبانی می‌شود و نتیجهٔ
  آن برای داده و task معلوم است.
- actionهای رقیب را فقط بر اساس policy همان flow محدود کنید؛ content pattern
  تصمیم سراسری برای غیرفعال‌کردن آن‌ها نمی‌سازد.

## پایان، شکست و توقف

```text
idle → loading/progress → success | error | cancelled
```

- Success فقط پس از نتیجهٔ تأییدشده و با
  [`notifications.md`](notifications.md) نوشته می‌شود.
- Failure از [`errors.md`](errors.md) و recovery تأییدشده پیروی می‌کند.
- اگر عملیات متوقف، در صف یا در پس‌زمینه ادامه دارد، فقط state واقعی را نام ببرید
  و آن را Success یا Error فرض نکنید.
- متن Loading قبلی نباید بعد از پایان در دسترس‌پذیری یا UI باقی بماند و با نتیجه
  تناقض بسازد.

## Skeleton و placeholder

Skeleton یک treatment دیداری برای ساختار در انتظار است، نه یک state تجاری یا
دادهٔ واقعی. آن را به‌عنوان variant کنترل‌هایی مانند Checkbox یا Text Input
تعریف نکنید. استفاده از Skeleton نیاز به busy/status درست را، هرجا برای فهم
کاربر لازم است، حذف نمی‌کند.

جزئیات انتخاب Skeleton در برابر spinner و شکل دقیق placeholder هنوز در pattern
canonical Design System تثبیت نشده است؛ این سند آن‌ها را اختراع نمی‌کند.

## دسترس‌پذیری

- وضعیت مهمی که بدون تغییر فوکوس رخ می‌دهد باید برنامه‌وار قابل دریافت باشد.
- `aria-busy`، progress semantics یا status message فقط وقتی استفاده شوند که
  state واقعی را درست توصیف می‌کنند.
- برای ظاهرشدن spinner یا progress indicator فوکوس را جابه‌جا نکنید، مگر خود
  progress به context تعاملی لازم تبدیل شده باشد.
- اگر trigger متمرکز باقی می‌ماند، فوکوس را تا حد ممکن حفظ و فعال‌سازی تکراری را
  متوقف کنید.
- progress پیوسته را در هر تغییر کوچک announce نکنید؛ milestone معنادار یا
  تغییر ضروری را با کم‌مزاحمت‌ترین روش کافی اعلام کنید.
- معنی پیشرفت نباید فقط به motion وابسته باشد.

## قرارداد قطعی

### باید

- scope و نوع progress را پیش از نوشتن مشخص کنید.
- در صورت نیاز به متن، action و object واقعی را نام ببرید.
- مقدار progress را از state قابل‌اعتماد محصول بگیرید.
- اصطلاحات همان سطح و مخاطب را حفظ کنید.
- transition به Success، Error یا Cancelled را فقط پس از state واقعی انجام دهید.
- focus، busy semantics و announcement را متناسب با همان flow نگه دارید.

### نباید

- برای progress نامعین درصد، تعداد، مرحله یا ETA بسازید.
- «لطفاً منتظر بمانید» یا «در حال پردازش» را بدون زمینه کل پیام قرار دهید.
- زمان پایان یا نزدیک‌بودن آن را حدس بزنید.
- Loading را به Disabled، Empty یا Error تبدیل کنید.
- برای سرگرم‌کردن کاربر متن تبلیغاتی، ایموجی یا پیام‌های چرخشی اضافه کنید.
- هر تغییر جزئی progress را به‌صورت مزاحم announce کنید.
- cancellation، ادامهٔ پس‌زمینه‌ای یا threshold نمایش را بدون product truth
  وعده دهید.

## چک‌لیست بازبینی

- [ ] Loading محلی/ناحیه‌ای و progress معین/نامعین مشخص شده‌اند.
- [ ] action و object در صورت نیاز روشن‌اند.
- [ ] عدد، درصد و ETA از state واقعی می‌آیند.
- [ ] Loading با Disabled، Empty یا Error اشتباه نشده است.
- [ ] تکرار action متوقف و focus حفظ شده است.
- [ ] announcement کم‌مزاحمت و غیرتکراری است.
- [ ] Success، Error و Cancelled فقط از نتیجهٔ واقعی آمده‌اند.
- [ ] رفتار تعریف‌نشدهٔ runtime یا Skeleton اختراع نشده است.

## ارزیابی

```bash
python tooling/validators/check_content_patterns.py
```

اعتبارسنج ساختار pattern، tone profile، rule IDها و پوشش قواعد blocking در
evalها را کنترل می‌کند. زمان‌سنجی و کیفیت تجربه باید در محصول واقعی نیز آزموده
شوند.
