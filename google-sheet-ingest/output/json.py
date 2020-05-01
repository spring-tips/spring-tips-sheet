import typing
import episodes

import jsons


def build_from_episodes(eps: typing.List[episodes.Episode]) -> str:
    print('writing JSON...')
    return jsons.dumps(eps)
