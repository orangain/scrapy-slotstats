# coding: utf-8

from __future__ import print_function, unicode_literals

import itertools
import logging
from datetime import datetime
from statistics import mean, median, stdev

from scrapy import signals

logger = logging.getLogger(__name__)


class SlotStats(object):

    def __init__(self, crawler):
        crawler.signals.connect(self.response_downloaded, signal=signals.response_downloaded)
        crawler.signals.connect(self.spider_closed, signal=signals.spider_closed)
        self.stats = []

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def response_downloaded(self, response, request, spider):
        self.stats.append({
            'time': datetime.now(),
            'slot': request.meta['download_slot'],
            'url': request.url,
        })

    def spider_closed(self, spider, reason):
        lines = []
        keyfunc = lambda s: s['slot']
        sorted_stats = list(sorted(self.stats, key=keyfunc))
        for slot, stats in itertools.groupby(sorted_stats, keyfunc):
            prev_time = None
            for stat in stats:
                stat['delay'] = (stat['time'] - prev_time).total_seconds() if prev_time else None
                prev_time = stat['time']
                lines.append('{slot}\t{delay}\t{time}\t{url}'.format(**stat))

        logger.debug('Slot details:\n%s', '\n'.join(lines))

        lines = []
        for slot, stats in itertools.groupby(sorted_stats, keyfunc):
            delays = [stat['delay'] for stat in stats if stat['delay'] is not None]
            if len(delays) == 0:
                lines.append('{0}\tcount:{1}'.format(slot, len(delays)))
                continue

            lines.append('{0}\tcount:{1}\tmin:{2}\tmax:{3}\tmean:{4}\tmedian:{5}\tstdev:{6}'.format(
                slot, len(delays), min(delays), max(delays), mean(delays), median(delays),
                stdev(delays) if len(delays) >= 2 else None))

        logger.info('Slot delay stats:\n%s', '\n'.join(lines))
