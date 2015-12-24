# scrapy-slotstats
Scrapy extension to show statistics of downloader slots.

## Usage

Add following settings to your project's `settings.py`:

```py
EXTENSIONS = {
    'scrapy_slotstats.SlotStats': 0,
}
```
