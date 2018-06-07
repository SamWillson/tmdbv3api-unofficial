from tmdbv3api.tmdb import TMDb
from tmdbv3api.as_obj import AsObj

try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote


class Season(TMDb):
    _urls = {
        'details': '/tv/%s/season/%s',
        'changes': '/tv/season/%s/changes',
        'account_states': '/tv/%s/season/%s/account_states',
        'credits': '/tv/%s/season/%s/credits',
        'external_ids': '/tv/%s/season/%s/external_ids',
        'images': '/tv/%s/season/%s/images',
        'videos': '/tv/%s/season/%s/videos',
    }

    def details(self, tv_id, season_num, append_to_response="append_to_response=trailers,images,casts,translations"):
        """
        Get the TV season details by id.
        :param tv_id:
        :param season_num:
        :param append_to_response:
        :return:
        """
        return AsObj(**self._call(self._urls['details'] % (str(tv_id), str(season_num)), append_to_response))

    def changes(self, season_id, append_to_response="append_to_response=trailers,images,casts,translations"):
        """
        Get the changes for a TV season. By default only the last 24 hours are returned.
        :param season_id:
        :return:
        """
        return AsObj(**self._call(self._urls['changes'] % str(season_id), append_to_response))
