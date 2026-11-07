---
id: content.component.modal
collection: content
type: content-component
title: Modal Content
summary: Defines the Persian content contract for focused blocking dialogs across titles, body copy, actions, dismissal wording, confirmations, forms, loading, errors, and accessible naming.
knowledge_state: verified
document_maturity: draft
related:
  - content.product-voice
  - content.terminology
  - content.localization
  - content.component.button
  - content.component.text-input
  - content.pattern.confirmation
  - content.pattern.error
  - content.pattern.loading-and-progress
  - design-system.component.modal
  - design-system.accessibility.focus-management
topics:
  - modal
  - dialog
  - confirmation
  - forms
  - actions
  - errors
  - accessibility
  - persian
---

# محتوای Dialog

> برای سازگاری با ارجاع‌های موجود، شناسهٔ `content.component.modal` و نام فایل
> فعلاً حفظ شده‌اند. نام canonical کامپوننت **Dialog** است؛ **Modal** فقط alias
> قدیمی و توصیف رفتار blocking است. برای کار جدید از Dialog استفاده کنید.

این سند قرارداد محتوای یک context موقت و blocking است. قواعد machine-readable
در [`modal.yml`](modal.yml) و نمونه‌های regression در
[`../../../ai/evals/content/modal-content-cases.yml`](../../../ai/evals/content/modal-content-cases.yml) قرار
دارند.

## وضعیت منبع و مرز تصمیم

سند canonical کامپوننت Dialog در Design System اکنون `canonical/reviewed` است و
هدف، anatomy، size و responsive behavior، رفتار `Escape` و backdrop، focus،
scroll و مرز Confirmation/Alert را تعریف می‌کند. سند legacy Modal فقط redirect
سازگاری است. وضعیت runtime، Storybook mapping و آزمون‌های اجراشده همچنان
`unregistered/unverified` است؛ این سند از روی تأیید طراحی، shipped بودن را نتیجه
نمی‌گیرد.

قواعد تأییدشدهٔ موجود می‌گویند:

- Dialog یک interaction context موقت و blocking برای task یا تصمیم متمرکز است.
- عنوان روشن لازم است و معمولاً accessible name از همان عنوان دیده‌شده می‌آید.
- محتوای اصلی باید بدون مراجعه به صفحهٔ پوشیدهٔ پشت Dialog قابل‌فهم باشد.
- feedback منفعل، disclosure ساده، task طولانی یا navigation-heavy معمولاً Dialog
  نیست.
- actionها از Button hierarchy و Confirmation pattern پیروی می‌کنند؛ Dialog
  Button style تازه نمی‌سازد.
- هنگام submit نباید Dialog بدون product policy معتبر خوش‌بینانه بسته شود و
  recovery را از دسترس خارج کند.

الگوهای فارسی Title، Body، acknowledgement، dismissal wording و transitionهای
content تصمیم Product Content System هستند.

## ابتدا نوع Dialog را مشخص کنید

| نوع | هدف محتوا | اجزای معمول |
|---|---|---|
| Confirmation | مکث برای تصمیم پیامددار | Title پرسشی، consequence، action اصلی، خروج امن |
| Focused task/form | انجام task کوتاه در context موقت | Title عملی، fieldها، action submit، خروج |
| Response-required information | فهم اطلاعات مهم و پاسخ صریح | Title موضوعی، توضیح لازم، acknowledgement/action |

اگر content فقط نتیجه‌ای منفعل را گزارش می‌کند، Notification یا Toast را بررسی
کنید. اگر task چندمرحله‌ای، طولانی، navigation-heavy یا نیازمند URL/history است،
page یا flow مستقل مناسب‌تر است.

## Anatomy محتوایی

```text
Title            required
Body             conditional
Task content     conditional
Inline feedback  conditional
Actions          when response is required
Dismiss control  only when flow is dismissible
```

هر بخش فقط یک وظیفهٔ اصلی دارد. Title نام task یا decision است؛ Body context،
consequence یا requirement لازم را می‌دهد؛ actionها نتیجهٔ activation را نام
می‌برند.

لحن با نوع Dialog تغییر می‌کند: form کوتاه از لحن راهنمای form، confirmation
خنثی یا مخرب از پروفایل همان confirmation و information response-required از
لحن informational پیروی می‌کند. هیچ‌کدام مجوز فشار احساسی یا بیان تبلیغاتی
نیستند.

## Title

Title باید به‌تنهایی شروع قابل‌فهمی برای context جدید بسازد:

```text
ویرایش اطلاعات تماس
افزودن سابقهٔ شغلی
آگهی را حذف می‌کنید؟
تغییرات ذخیره‌نشده را کنار می‌گذارید؟
```

از عنوان‌های generic زیر استفاده نکنید:

```text
توجه
هشدار
پیام
تأیید
مطمئن هستید؟
```

severity یا icon جای موضوع نیست. Title نباید success را پیش از action اعلام
کند و نباید برای جلب توجه از ترس، فوریت ساختگی یا علامت تعجب استفاده کند.

## Body

Body فقط اطلاعاتی را اضافه می‌کند که برای تصمیم یا تکمیل task لازم است:

- consequence و recoverability؛
- scope و count؛
- requirement تأییدشده؛
- توضیحی که Title و controls به‌تنهایی منتقل نمی‌کنند.

Title را با جمله‌ای طولانی‌تر تکرار نکنید. اگر Title، controls و actionها task را
کامل روشن می‌کنند، Body می‌تواند حذف شود.

محتوا نباید به صفحهٔ unavailable پشت Dialog ارجاع مبهم بدهد:

```text
بد: مورد انتخاب‌شده را طبق اطلاعات زیر حذف کنید.
خوب: آگهی «کارشناس فروش» حذف می‌شود و امکان بازگردانی آن نیست.
```

## Confirmation

برای confirmation از pattern مشترک استفاده کنید:

```text
Title       → [object] را [action] می‌کنید؟
Body        → consequence + scope + recoverability
Primary     → نتیجهٔ دقیق action
Safe exit   → خروج یا بازگشت روشن
```

```text
آگهی را حذف می‌کنید؟
آگهی «کارشناس فروش» حذف می‌شود و امکان بازگردانی آن نیست.
[حذف آگهی] [انصراف]
```

«بله/خیر»، «تأیید/لغو» یا Title «مطمئن هستید؟» تصمیم را بدون context رها
می‌کنند. Danger فقط برای consequence واقعاً مخرب یا دشواربازگشت است.

## Focused task یا form

Title task و object را نام می‌برد؛ field content از قرارداد Text Input و pattern
Instruction/Error می‌آید:

```text
Title: ویرایش اطلاعات تماس
Fields: ایمیل، شماره موبایل
Primary: ذخیرهٔ تغییرات
Exit: انصراف
```

- instruction مشترک را یک بار در جای مناسب بیاورید، نه زیر همهٔ fieldها.
- requiredness، helper و error را به Dialog-specific copy تبدیل نکنید.
- task طولانی یا چندمرحله‌ای را فقط با کوتاه‌کردن متن در Dialog جا ندهید.
- اگر بستن باعث ازدست‌رفتن داده می‌شود، آن consequence باید مطابق Product truth
  مدیریت و در صورت نیاز confirmation شود.

## Information requiring a response

Dialog فقط وقتی برای information مناسب است که کاربر باید پیش از بازگشت پاسخ
صریحی بدهد. Title موضوع را نام می‌برد و Body اطلاعات ضروری را توضیح می‌دهد.

برای acknowledgement ساده، labelی مانند «متوجه شدم» می‌تواند معتبر باشد چون
نوع پاسخ را روشن می‌کند. «تأیید» یا «باشه» را وقتی معنی response را مبهم
می‌کنند استفاده نکنید. اگر response لازم نیست، از feedback یا disclosure
غیربلوکه‌کننده استفاده کنید.

## Actionها و خروج

- action اصلی نتیجهٔ واقعی را نام می‌برد.
- خروج امن با «انصراف»، «بازگشت»، «ادامهٔ ویرایش» یا label دقیق task بیان می‌شود.
- Close icon، اگر flow dismissible است، accessible name معنادار مانند «بستن»
  دارد.
- اگر Close و Cancel نتیجهٔ متفاوت دارند، تفاوت باید در behavior و naming روشن
  باشد؛ ظاهر مشابه یا label یکسان کافی نیست.
- Brand، Primary و Danger از hierarchy و consequence می‌آیند، نه از شدت copy.

رفتار Close، `Escape` و backdrop را سند canonical Dialog تعیین می‌کند. این سند
آن رفتارها را بازتعریف نمی‌کند و copy نباید با آن‌ها تعارض داشته باشد یا از روی
طراحی، API و وضعیت پیاده‌سازی runtime را حدس بزند.

## Loading، success و error

هنگام submit:

- Button هویت action را در Loading حفظ می‌کند؛
- Dialog context تا زمانی که flow نتیجهٔ دیگری را تأیید نکرده حفظ می‌شود؛
- completion یا success پیش از پاسخ واقعی اعلام نمی‌شود؛
- Dialog فقط وقتی خودکار بسته می‌شود که behavior محصول این transition را تعریف
  کرده باشد.

Failure قابل‌بازیابی باید در همان context قابل‌فهم باشد، data معتبر را حفظ کند
و recovery معلوم را نشان دهد. Toast تنها نباید recovery لازم داخل Dialog را از
دسترس خارج کند.

```text
اطلاعات تماس ذخیره نشد. دوباره تلاش کنید.
```

علت، retry، حفظ داده یا زمان رفع را بدون source معتبر ادعا نکنید.

## Variables و Localization

- object، person، count و amount را با terminology و formatter معتبر وارد کنید.
- count عملیات گروهی باید با selection واقعی همگام بماند.
- نام، identifier، email و متن دوجهته را isolate کنید.
- Title، Body و Button labels باید در zoom و عرض واقعی بدون حذف اطلاعات ضروری
  قابل‌فهم بمانند.
- Dialog نباید نام internal object یا placeholder خام نشان دهد.

## دسترس‌پذیری محتوایی

- visible Title و accessible name از نظر معنی همسو باشند.
- description برنامه‌وار فقط Body مرتبط را در بر بگیرد؛ محتوای طولانی یا
  interactive را بی‌دلیل به یک announcement بزرگ تبدیل نکنید.
- Close و actionهای icon-only نام قابل‌دسترسی دارند.
- معنی تصمیم فقط به رنگ Danger، icon یا ترتیب Buttonها وابسته نیست.
- متن آغازین باید بدون نگاه به background قابل‌فهم باشد.

Focus entry، containment، restoration و initial target متعلق به Design System و
flow هستند. متن نباید یک target همیشگی مانند «همیشه دکمهٔ اصلی را focus کنید»
تعریف کند.

## قرارداد قطعی

<!-- generated:content-rules source=modal.yml -->
<!-- این بخش از فایل YAML تولید می‌شود؛ دستی ویرایش نکنید. پس از تغییر قواعد اجرا کنید: python tooling/generate_content_rule_sections.py generate -->

### باید

- `MOD-001` Dialog فقط برای task، decision یا response متمرکزی استفاده شود که واقعاً context blocking می‌خواهد.
- `MOD-002` Title باید task، decision یا موضوع response را روشن نام ببرد.
- `MOD-004` Title و content اصلی بدون مراجعه به background پوشیده‌شده قابل‌فهم باشند.
- `MOD-005` visible Title و accessible name Dialog از نظر معنی همسو و برنامه‌وار مرتبط باشند.
- `MOD-006` Body فقط context، consequence یا requirement لازم و تأییدشده‌ای فراتر از Title اضافه کند.
- `MOD-008` Confirmation باید action، object، consequence، scope و recoverability معلوم را روشن کند.
- `MOD-009` action اصلی نتیجهٔ activation و action ثانویه خروج امن یا بازگشت را صریح نام ببرند.
- `MOD-011` dismiss control موجود accessible name معنادار داشته باشد و با safe exit متفاوت اشتباه نشود.
- `MOD-013` اگر خروج باعث data loss می‌شود، consequence و مسیر تصمیم مطابق product truth روشن شوند.
- `MOD-014` در Loading هویت action و Dialog context تا outcome یا transition تأییدشده حفظ شوند.
- `MOD-016` Failure قابل‌بازیابی با دادهٔ معتبر و recovery معلوم در همان context قابل‌فهم بماند.
- `MOD-017` object، field و action با terminology همان surface و audience نامیده شوند.
- `MOD-018` نام، count، amount، identifier و متن دوجهته با formatter و bidi contract معتبر نمایش داده شوند.

### نباید

- `MOD-003` «توجه»، «هشدار»، «پیام»، «تأیید» یا «مطمئن هستید؟» به‌تنهایی Title نباشند.
- `MOD-007` Title، Body و actionها با wording تکراری پر نشوند.
- `MOD-010` برای تصمیم پیامددار از «بله»، «خیر»، «تأیید» یا «ادامه» به‌تنهایی استفاده نشود.
- `MOD-012` Escape، backdrop، auto-close، initial focus یا non-dismissible behavior بدون contract معتبر وعده داده نشود.
- `MOD-015` success اعلام نشود و Dialog پیش از outcome واقعی و policy تأییدشده بسته نشود.
- `MOD-019` task طولانی، چندمرحله‌ای یا navigation-heavy به Dialog عمومی تحمیل نشود.
- `MOD-020` Title، Body یا actionها با ترس، فوریت ساختگی، فشار احساسی یا success زودهنگام تصمیم را جهت ندهند.

<!-- /generated:content-rules -->

## مسائل باز

- ثبت runtime package، Storybook mapping و آزمون‌های اجراشدهٔ Dialog.
- زمان و شرایط product-specific برای auto-close پس از success.
- مرز دقیق focused form با Drawer یا dedicated page در هر محصول.
- برنامهٔ مهاجرت مصرف‌کنندگان و ارجاع‌های legacy Modal.

## ارزیابی

```bash
python tooling/validators/check_content_components.py
```

اعتبارسنج identity، source evidence، rule IDها، eval link و پوشش همهٔ قواعد
blocking را کنترل می‌کند. focus، keyboard، screen reader، responsive layout و
dismissal باید در component و flow واقعی آزموده شوند.
