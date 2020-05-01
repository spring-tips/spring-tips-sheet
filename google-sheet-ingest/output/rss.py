import datetime
import typing

import PyRSS2Gen

import episodes


def build_from_episodes(eps: typing.List[episodes.Episode]) -> str:
    print('writing RSS...')

    def build_rss_item_for_episode(episode: episodes.Episode) -> PyRSS2Gen.RSSItem:
        return PyRSS2Gen.RSSItem(title=episode.title, link=episode.blog_url, description='', pubDate=episode.date)

    items: typing.List[PyRSS2Gen.RSSItem] = [build_rss_item_for_episode(e) for e in eps]
    rss = PyRSS2Gen.RSS2(
        title="Spring Tips",
        link="http://bit.ly/spring-tips-playlist",
        description="Spring Tips is a YouTube playlist by Josh Long (@starbuxman) that "
                    "looks at different aspects of the wonderful and wide world of Springdom",
        lastBuildDate=datetime.datetime.now(),
        items=items
    )
    return rss.to_xml()
