---
id: content.component.button
collection: content
type: content-component
title: Button Content
summary: Defines how Persian Button labels name actions, outcomes, objects, exits, destructive consequences, and loading states without duplicating the Design System Button contract.
knowledge_state: verified
document_maturity: draft
related:
  - content.product-voice
  - content.terminology
  - content.localization
  - content.pattern.confirmation
  - content.pattern.loading-and-progress
  - design-system.experience-rule.action-hierarchy
  - button
topics:
  - button
  - action-label
  - call-to-action
  - destructive-action
  - loading
  - accessibility
  - persian
---

# محتوای Button

این سند قرارداد انسانی برچسب Button است. قواعد machine-readable در
[`button.yml`](button.yml) و نمونه‌های regression در
[`../../../ai/evals/content/button-content-cases.yml`](../../../ai/evals/content/button-content-cases.yml) قرار
دارند.

## مرز منبع و تصمیم

### قواعد تأییدشده در Design System

قرارداد canonical کامپوننت Button این موارد را تثبیت کرده است:

- Button برای action است؛ navigation باید Link semantics داشته باشد.
- Button استاندارد در حالت عادی label دیداری دارد؛ action فقط‌آیکن متعلق به
  Icon Button است.
- label باید کوتاه، یک‌خطی و توصیف‌کنندهٔ نتیجهٔ activation باشد.
- نام قابل‌دسترس Button معمولاً از همان label دیداری می‌آید.
- یک action group معمولاً یک رهبر دیداری دارد؛ Brand، Primary و Danger فقط با
  معنی و hierarchy تأییدشده انتخاب می‌شوند.
- Loading هویت action را تغییر نمی‌دهد، فعال‌سازی تکراری را متوقف می‌کند و
  فضای label را برای جلوگیری از layout shift حفظ می‌کند.
- Danger فقط برای intent واقعاً مخرب است، نه صرفاً یک فعل منفی.

### تصمیم‌های اجرایی Product Content

قواعد نگارش، میزان صراحت، الگوهای label، disambiguation و مثال‌های فارسی این
سند تصمیم Product Content System هستند. این قواعد رفتار business را تعیین
نمی‌کنند و نباید action، recoverability یا نتیجه‌ای را که در محصول تأیید نشده
است اختراع کنند.

## مدل انتخاب label

پیش از نوشتن، پنج ورودی را مشخص کنید:

```text
action واقعی
+ object یا scope لازم
+ نتیجه یا مقصد
+ context پیرامون
+ consequence / recoverability تأییدشده
→ label Button
```

اگر یکی از این ورودی‌ها برای صحت label لازم است اما معلوم نیست، متن را با حدس
کامل نکنید؛ تصمیم را به Product Knowledge یا owner همان flow برگردانید.

## ساختار پایهٔ برچسب فارسی

در فارسی معمولاً label طبیعی به شکل زیر است:

```text
[فعل یا عمل]
[فعل + موضوع]
[فعل + دامنه/نتیجه]
```

نمونه‌ها:

```text
ذخیره
ذخیرهٔ تغییرات
ارسال رزومه
افزودن کارجو
حذف آگهی
ادامهٔ ویرایش
```

کوتاه‌ترین label را انتخاب کنید که در همان context دقیق و متمایز باشد. object
را وقتی حذف کنید که heading، field یا action group بدون ابهام آن را تعیین
می‌کند. اختصار نباید چند Button هم‌نام یا نتیجه‌ای مبهم بسازد.

## نتیجه را نام ببرید، نه gesture یا نیت مبهم را

label باید بگوید activation چه کاری انجام می‌دهد یا کاربر را به کدام مرحلهٔ
شناخته‌شده می‌برد.

| مبهم | روشن‌تر |
|---|---|
| تأیید | ذخیرهٔ تغییرات |
| بله | حذف آگهی |
| انجام | ارسال درخواست شغلی |
| کلیک کنید | مشاهدهٔ رزومه |
| بعدی | ادامه به اطلاعات تماس |

«ادامه» زمانی معتبر است که destination بعدی از ساختار flow روشن باشد. در یک
تصمیم پیامددار یا میان چند مسیر، مقصد یا نتیجه را به label اضافه کنید.

label پیش از activation نباید completion را اعلام کند. «ذخیره شد» feedback
است؛ action درست «ذخیره» یا «ذخیرهٔ تغییرات» است.

## Action، Navigation و انتخاب کامپوننت

- تغییر state، submit، confirm یا اجرای عملیات → Button.
- رفتن به destination مستقل → Link semantics، حتی اگر treatment ظاهری شبیه
  Button باشد.
- بازکردن menu یا control تخصصی → قرارداد همان کنترل؛ label نباید ماهیت کنترل
  را پنهان کند.
- action فقط‌آیکن → Icon Button با accessible name و Tooltip لازم؛ این سند
  اجازهٔ حذف label از Button استاندارد را نمی‌دهد.

## رابطه با hierarchy و style

copy نباید با لحن پرهیجان ضعف hierarchy را جبران کند. اول action اصلی flow را
از Product Knowledge و `action-hierarchy` تعیین کنید، سپس label آن را بنویسید.

- Brand به‌معنی «هر CTA مهم» نیست؛ فقط برای لحظهٔ conversion یا ورود
  محصول‌تعریف‌شده و تأییدشده است.
- Primary action اصلی operational است.
- Ghost معمولاً برای خروج‌هایی مانند «انصراف»، «بازگشت» یا «فعلاً نه» است.
- Danger فقط وقتی consequence مخرب یا دشواربازگشت تأیید شده باشد.

از واژه‌هایی مانند «ویژه»، «فوری»، «هوشمند» یا «رایگان» برای قوی‌ترکردن CTA
استفاده نکنید، مگر همان ادعا بخشی از product truth و برای تصمیم کاربر ضروری
باشد.

## Confirmation و خروج امن

در confirmation، label اصلی action و object را نام می‌برد و label ثانویه راه
خروج امن را روشن می‌کند:

```text
[حذف آگهی] [انصراف]
[خروج بدون ذخیره] [ادامهٔ ویرایش]
```

«بله/خیر»، «تأیید/لغو» یا دو label هم‌معنا برای تصمیم پیامددار کافی نیستند.
اگر action اصلی خود «لغو» است، safe exit را نیز «لغو» ننامید؛ از «انصراف»،
«بازگشت» یا label دقیق task استفاده کنید.

## Loading و stateهای action

شروع Loading معنی action را عوض نمی‌کند. label پایه باید همان action باقی
بماند و کامپوننت فضای آن را حفظ کند. برای جلوگیری از تغییر عرض، label را به
«در حال ذخیره…» یا متن طولانی دیگری جایگزین نکنید.

اگر یک عملیات طولانی یا ناحیه‌ای به status دیداری/برنامه‌وار نیاز دارد، آن پیام
را مطابق pattern Loading در جای مناسب ارائه کنید. Button نباید success یا
failure را پیش از state واقعی اعلام کند.

```text
idle label: ذخیرهٔ تغییرات
loading identity: ذخیرهٔ تغییرات
success feedback: تغییرات ذخیره شد
error feedback: تغییرات ذخیره نشد. دوباره تلاش کنید.
```

## واژگان، متغیرها و جهت متن

- object را با preferred term همان audience و surface بنویسید.
- implementation name، API field یا نام داخلی را به label منتقل نکنید.
- label حاوی نام، تعداد یا identifier پویا باید از قرارداد variable و bidi در
  Localization پیروی کند.
- مقدار پویا را فقط وقتی در label بیاورید که scope تصمیم را روشن‌تر می‌کند و
  طول آن قابل‌کنترل است؛ نام آزاد کاربر معمولاً در title یا body امن‌تر است.
- سیستم ارقام، نیم‌فاصله و جهت متن را به‌صورت موردی در رشته hard-code نکنید.

## شکل نوشتاری

- label را مانند یک عبارت کوتاه بنویسید، نه جملهٔ توضیحی.
- در پایان label نقطه، دونقطه یا علامت سؤال نگذارید.
- ellipsis را فقط برای نمایش Loading یا وعدهٔ dialog آینده به‌صورت تزئینی به
  label اضافه نکنید؛ state و behavior باید از component/flow معلوم باشد.
- از emoji، ALL CAPS و تکرار علامت تعجب برای جلب توجه استفاده نکنید.
- لحن Button مستقیم، معیار و خنثی است؛ خطاب «لطفاً ...» را داخل label نیاورید.

## دسترس‌پذیری

- label دیداری باید نام action را منتقل کند و معمولاً همان accessible name
  باشد.
- accessible name متفاوت نباید با label دیداری دربارهٔ نتیجهٔ action تناقض
  داشته باشد.
- icon تزئینی کنار label نام action را دوباره announce نکند.
- دو Button هم‌نام که action یا object متفاوت دارند باید با label یا context
  برنامه‌وار کافی از هم متمایز شوند.
- فهم action نباید فقط به رنگ، style، icon یا جایگاه وابسته باشد.

## قرارداد قطعی

<!-- generated:content-rules source=button.yml -->
<!-- این بخش از فایل YAML تولید می‌شود؛ دستی ویرایش نکنید. پس از تغییر قواعد اجرا کنید: python tooling/generate_content_rule_sections.py generate -->

### باید

- `BTN-001` label باید action یا نتیجهٔ واقعی activation را روشن کند.
- `BTN-002` کوتاه‌ترین label دقیق و بدون ابهام در context واقعی انتخاب شود.
- `BTN-003` object یا scope هرجا برای فهم، تمایز یا consequence لازم است در label بیاید.
- `BTN-006` Button برای action استفاده شود و navigation مستقل Link semantics داشته باشد.
- `BTN-007` Brand، Primary و Danger از معنی، hierarchy و consequence تأییدشده انتخاب شوند، نه از شدت واژهٔ label.
- `BTN-009` object با اصطلاح canonical همان audience و surface نامیده شود.
- `BTN-011` در Loading هویت label پایه ثابت بماند و با status طولانی جایگزین نشود.
- `BTN-012` در confirmation، action اصلی و راه خروج امن labelهای صریح و غیرهم‌معنا داشته باشند.
- `BTN-013` label دیداری و accessible name باید از نظر نتیجهٔ action همسو باشند.
- `BTN-014` Buttonهای هم‌نام با action یا object متفاوت باید از طریق label یا context برنامه‌وار کافی متمایز شوند.
- `BTN-015` عدد، identifier و variable پویا در label باید از قرارداد localization و bidi پیروی کند.

### نباید

- `BTN-004` در action پیامددار، «بله»، «خیر»، «تأیید» یا «انجام» به‌تنهایی label نباشد.
- `BTN-005` label پیش از activation نباید completion، success یا failure را اعلام کند.
- `BTN-008` label نباید ادعای تبلیغاتی، فشار احساسی یا فوریت ساختگی را برای تقویت CTA اضافه کند.
- `BTN-010` implementation name، API field یا نام داخلی نباید به label کاربر منتقل شود.
- `BTN-016` label نباید جملهٔ توضیحی، punctuation پایانی، emoji یا تأکید تزئینی باشد.

<!-- /generated:content-rules -->

## چک‌لیست بازبینی

- [ ] action واقعی و owner رفتار معلوم است.
- [ ] label نتیجه یا مقصد را روشن می‌کند.
- [ ] object فقط در صورت بی‌نیازی واقعی از context حذف شده است.
- [ ] Button به‌جای Link یا کنترل تخصصی استفاده نشده است.
- [ ] hierarchy و style از معنی و consequence آمده‌اند، نه از شدت copy.
- [ ] اصطلاح، عدد و variable از قراردادهای مشترک پیروی می‌کنند.
- [ ] Loading هویت action را حفظ می‌کند.
- [ ] label دیداری و accessible name همسو و متمایزند.
- [ ] punctuation، تبلیغ، فشار و internal term وارد label نشده‌اند.

## مسائل باز

- حداکثر تعداد نویسه یا واژه برای Button به‌صورت سراسری تأیید نشده است؛ معیار
  فعلی یک‌خطی‌بودن در layout واقعی و وضوح در context است.
- policy سراسری برای نمایش نام یا count پویا داخل Button وجود ندارد.
- label دقیق Back/Continue در هر multi-step flow به مقصد و رفتار همان flow
  وابسته است.
- policy مربوط به labelهای دو‌زبانه یا transliteration باید در Localization و
  context محصول حل شود.

## ارزیابی

```bash
python tooling/validators/check_content_components.py
```

این بررسی ساختار source، شناسهٔ قواعد، ارتباط eval و پوشش همهٔ قواعد blocking
را کنترل می‌کند. تناسب طول و تمایز label باید در layout و flow واقعی نیز آزموده
شود.
