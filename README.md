# Cryptocurrency Analyzer

> داشبورد تحلیل لحظه‌ای ارزهای دیجیتال — bilingual (فارسی / English)

## Overview / مرور

A single-file, client-side cryptocurrency analysis dashboard. It pulls live market data directly from Binance public REST APIs (`ticker`, `klines`, `fundingRate`, `premiumIndex`, `longShortRatio`) and calculates technical indicators (`RSI 14`, `SMA 20/50`, `MACD`) without any backend server.

> داشبورد تحلیل ارز دیجیتال در یک فایل HTML. داده‌ها مستقیماً از API عمومی بایننس دریافت می‌شوند و هیچ سرور یا پایگاه داده خارجی لازم نیست.

## Features / ویژگی‌ها

- **Live Price & Chart** — قیمت لحظه‌ای و نمودار کندل با تایم‌فریم قابل تغییر (۱۵ دقیقه، ۱ ساعت، ۴ ساعت، ۱ روزه).
- **Multi-Crypto Support** — انتخاب از بین: BTC, ETH, SOL, XRP, DOGE (`USDT` pairs).
- **Technical Indicators** — RSI, SMA, MACD محاسبه‌شده بر اساس داده‌های ۴ ساعته (یا تایم‌فریم انتخابی).
- **Market Sentiment** — Funding Rate, Premium Index, Top Trader Long/Short Ratios.
- **Algorithmic Signal Engine** — خروجی الگوریتمی `LONG` / `SHORT` / `WAIT` بر اساس ترکیب شاخص‌ها و داده‌های بازار (بدون مشاوره مالی).
- **Interactive Trade Calculator** — محاسبه حجم پوزیشن، ریسک، سود/ضرر احتمالی و نسبت ریسک/پاداش بر اساس قیمت فرضی، حد ضرر، حد سود و لوریج انتخابی.
- **Bilingual UI** — قابل تغییر بین فارسی (`fa`) و انگلیسی (`en`) با یک کلیک.
- **No Server Required** — فایل HTML استاتیک؛ مستقیماً در مرورگر باز می‌شود یا روی GitHub Pages / Vercel / Netlify دیپلوی می‌شود.

## How to Use / نحوه استفاده

1. **Direct** — فایل `Cryptocurrency_Analyzer.html` را در مرورگر خود باز کنید.
2. **Online (GitHub Pages)** — فایل را در مخزن GitHub آپلود کنید و از تنظیمات مخزن (`Settings → Pages`) آن را فعال کنید.
3. **Online (Vercel / Netlify)** — فایل را مستقیماً در داشبورد سرویس آپلود کنید؛ لینک زنده (`https://...`) در چند ثانیه آماده می‌شود.

**Note:** Because it uses `fetch()` to call `api.binance.com`, opening as `file://` works in most modern browsers, but for full reliability (especially mobile), hosting on `https://` (GitHub Pages / Vercel) is recommended.

> **نکته:** از آنجایی که از `fetch()` برای دریافت داده از بایننس استفاده می‌شود، باز کردن فایل با `file://` در اکثر مرورگرهای مدرن کار می‌کند؛ اما برای اطمینان کامل (به‌ویژه در موبایل)، میزبانی روی `https://` (GitHub Pages / Vercel) توصیه می‌شود.

## Data Sources / منابع داده

| Source | Endpoint | Purpose |
|--------|----------|---------|
| Binance Spot | `/api/v3/ticker/24hr` | قیمت لحظه‌ای و تغییر ۲۴ ساعته |
| Binance Spot | `/api/v3/klines` | کندل‌های تاریخی برای تحلیل تکنیکال |
| Binance Futures | `/fapi/v1/fundingRate` | نرخ فاندینگ |
| Binance Futures | `/fapi/v1/premiumIndex` | شاخص پریمیوم |
| Binance Futures | `/futures/data/topLongShortPositionRatio` | نسبت لانگ/شورت برترین تریدرها |
| Binance Futures | `/futures/data/globalLongShortAccountRatio` | نسبت حساب لانگ/شورت |

All endpoints are **public** and require no authentication.

## File Structure / ساختار فایل

```
Cryptocurrency_Analyzer.html   # تنها فایل پروژه (HTML + CSS + JS)
README.md                        # این فایل
```

No build step, no dependencies, no package manager (`npm` / `yarn`) required.

## Security / امنیت

- **No API keys or tokens are embedded** in the source code. The dashboard uses Binance **public** endpoints only.
- **Do not share any personal access tokens** (e.g., `ghp_*`, `gho_*`) with AI models or public chats. If a token was previously exposed, revoke it immediately via `GitHub → Settings → Developer settings → Personal access tokens`.

## Disclaimer / سلب مسئولیت

> This dashboard is purely educational and informational. It does **not** provide financial advice, investment recommendations, or guaranteed trading signals. Cryptocurrency markets are highly volatile; you may lose part or all of your capital. Always perform your own analysis and risk management before entering any trade. Leverage above 5x–10x significantly increases liquidation risk.

> این داشبورد صرفاً آموزشی و اطلاعاتی است و مشاوره مالی، توصیه سرمایه‌گذاری یا سیگنال تضمینی ارائه نمی‌دهد. بازار ارزهای دیجیتال بسیار پرنوسان است؛ همیشه تحلیل و مدیریت ریسک شخصی خود را انجام دهید. لوریج بالا ریسک لیکویید شدن را به شدت افزایش می‌دهد.

## License / مجوز

Open for personal and educational use.
