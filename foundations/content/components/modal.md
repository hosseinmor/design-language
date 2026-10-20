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

# محتوای Modal

این سند قرارداد محتوای یک context موقت و blocking است. قواعد machine-readable
در [`modal.yml`](modal.yml) و نمونه‌های regression در
[`../../../ai/evals/content/modal-content-cases.yml`](../../../ai/evals/content/modal-content-cases.yml) قرار
دارند.

## وضعیت منبع و مرز تصمیم

کامپوننت Modal در Design System هنوز `unverified/draft` است و تصمیم‌هایی مانند
size model، رفتار `Escape` و backdrop، initial-focus API، action layout و nested
Modal policy باز مانده‌اند. این سند آن‌ها را قطعی نمی‌کند.

قواعد تأییدشدهٔ موجود می‌گویند:

- Modal یک interaction context موقت و blocking برای task یا تصمیم متمرکز است.
- عنوان روشن لازم است و معمولاً accessible name از همان عنوان دیده‌شده می‌آید.
- محتوای اصلی باید بدون مراجعه به صفحهٔ پوشیدهٔ پشت Modal قابل‌فهم باشد.
- feedback منفعل، disclosure ساده، task طولانی یا navigation-heavy معمولاً Modal
  نیست.
- actionها از Button hierarchy و Confirmation pattern پیروی می‌کنند؛ Modal
  Button style تازه نمی‌سازد.
- هنگام submit نباید Modal بدون product policy معتبر خوش‌بینانه بسته شود و
  recovery را از دسترس خارج کند.

الگوهای فارسی Title، Body، acknowledgement، dismissal wording و transitionهای
content تصمیم Product Content System هستند.

## ابتدا نوع Modal را مشخص کنید

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

لحن با نوع Modal تغییر می‌کند: form کوتاه از لحن راهنمای form، confirmation
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

محتوا نباید به صفحهٔ unavailable پشت Modal ارجاع مبهم بدهد:

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
- requiredness، helper و error را به Modal-specific copy تبدیل نکنید.
- task طولانی یا چندمرحله‌ای را فقط با کوتاه‌کردن متن در Modal جا ندهید.
- اگر بستن باعث ازدست‌رفتن داده می‌شود، آن consequence باید مطابق Product truth
  مدیریت و در صورت نیاز confirmation شود.

## Information requiring a response

Modal فقط وقتی برای information مناسب است که کاربر باید پیش از بازگشت پاسخ
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

این سند تعیین نمی‌کند Close icon، `Escape` یا backdrop در همهٔ Modalها چه رفتاری
دارند. تا ثبت contract نهایی، copy نباید وعده‌ای مانند «برای خروج بیرون کادر
کلیک کنید» بدهد.

## Loading، success و error

هنگام submit:

- Button هویت action را در Loading حفظ می‌کند؛
- Modal context تا زمانی که flow نتیجهٔ دیگری را تأیید نکرده حفظ می‌شود؛
- completion یا success پیش از پاسخ واقعی اعلام نمی‌شود؛
- Modal فقط وقتی خودکار بسته می‌شود که behavior محصول این transition را تعریف
  کرده باشد.

Failure قابل‌بازیابی باید در همان context قابل‌فهم باشد، data معتبر را حفظ کند
و recovery معلوم را نشان دهد. Toast تنها نباید recovery لازم داخل Modal را از
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
- Modal نباید نام internal object یا placeholder خام نشان دهد.

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

### باید

- نوع Modal و ضرورت blocking context را پیش از نوشتن مشخص کنید.
- Title task، decision یا موضوع response را روشن نام ببرد.
- محتوا را مستقل از background قابل‌فهم نگه دارید.
- Body فقط context، consequence یا requirement لازم و تأییدشده را اضافه کند.
- action اصلی، خروج امن و dismissal action موجود را دقیق نام‌گذاری کنید.
- Loading، success و error را فقط از state واقعی flow بنویسید.
- terminology، variable formatting و accessible relationships را حفظ کنید.

### نباید

- feedback منفعل یا disclosure ساده را فقط برای تأکید داخل Modal ببرید.
- از Titleهای generic مانند «توجه»، «هشدار» یا «مطمئن هستید؟» استفاده کنید.
- Title، Body و actions را با wording تکراری پر کنید.
- consequence، recoverability، dismissal یا focus behavior را حدس بزنید.
- Modal را پیش از outcome واقعی موفق اعلام یا خوش‌بینانه ببندید.
- task طولانی و چندمرحله‌ای را به Modal عمومی تحمیل کنید.

## مسائل باز

- exact dismissibility contract برای Close، Escape و backdrop.
- initial-focus configuration و action-layout defaults.
- size، scrolling و sticky header/footer behavior.
- nested/stacked Modal policy.
- زمان و شرایط auto-close پس از success.
- مرز دقیق focused form با Drawer یا dedicated page در هر محصول.

## ارزیابی

```bash
python tooling/validators/check_content_components.py
```

اعتبارسنج identity، source evidence، rule IDها، eval link و پوشش همهٔ قواعد
blocking را کنترل می‌کند. focus، keyboard، screen reader، responsive layout و
dismissal باید در component و flow واقعی آزموده شوند.
