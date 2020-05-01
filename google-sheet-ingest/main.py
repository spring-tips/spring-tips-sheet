import datetime
import json
import os
import sys

import episodes
from sheets import *
import importlib


def main(args):
    spreadsheet_id = '13EoEqvqr3dR4eVW6twNTooxBl3ayNhlyKO7ip0zykKE'
    with open('credentials.json', 'r') as json_file:
        client_config = json.load(json_file)
    sheet = GSheet(client_config, spreadsheet_id)
    values = sheet.read_values('Published!A1:E')
    episodes_list = []
    for title, season, blog_url, date, youtube_id in values:
        print('title:', title, 'season:', season, 'blog_url:', blog_url, 'date:', date, 'youtube_id:', youtube_id)
        m, d, y = [int(x) for x in date.split('/')]
        date = datetime.datetime(y, m, d)
        episode = episodes.Episode(title, int(season), blog_url, date, youtube_id)
        episodes_list.append(episode)

    emitters = ['rss', 'json']
    for e in emitters:
        output_fn = os.environ[('%s_FN' % e).upper()]
        the_module = importlib.import_module('output.%s' % e, '.')
        the_write_fn = getattr(the_module, 'build_from_episodes')
        result = the_write_fn(episodes_list)
        with open(output_fn, 'w') as out:
            out.write(result)


if __name__ == '__main__':
    main(sys.argv)
