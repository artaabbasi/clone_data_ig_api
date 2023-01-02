import requests, json, datetime
access_token = ""
ig_user_id = ""
basic_url = "https://graph.instagram.com/v15.0/"

sample_res = """
{
    "business_discovery": {
        "id": "17841401525860163",
        "ig_id": 10482862,
        "name": "J Balvin",
        "username": "jbalvin",
        "profile_picture_url": "https://scontent.fbaq2-2.fna.fbcdn.net/v/t51.2885-15/272307439_140470511724764_4263731586488463919_n.jpg?_nc_cat=1&ccb=1-5&_nc_sid=86c713&_nc_eui2=AeErYr-NceD1DvlTdMFw7QPcrlXwvFWx4ZOuVfC8VbHhkxGyDdL5-tOIFpeIU77PgqeJvRY6gXVRGSpdxBP8SxNL&_nc_ohc=RswtWyTHU8wAX_u4pcF&_nc_ht=scontent.fbaq2-2.fna&edm=AL-3X8kEAAAA&oh=00_AT8p18_oXvJsxCQV632bq6vmDcxMrJ9HHnQdk5E-s29bDw&oe=61F82A7A",
        "followers_count": 51214234,
        "media_count": 12940,
        "follows_count": 1927,
        "media": {
        "data": [
            {
            "comments_count": 1550,
            "like_count": 427154,
            "timestamp": "2023-01-01T17:34:22+00:00",
            "media_type": "CAROUSEL_ALBUM",
            "media_product_type": "FEED",
            "id": "17928326101919137"
            }
            ]
        }
    }
}
"""
def get_media( page:str):
    use_url = basic_url+page+"?fields={media{timestamp,comments_count,like_count,media_type}}&access_token="+access_token
    req = requests.get(use_url)
    dict_content = json.loads(req.content)
    # dict_content = json.loads(sample_res)

    need_medias = []
    now = datetime.datetime.now()
    for media in dict_content["business_discovery"]["media"]["data"]:
        post_timestamp = datetime.datetime.fromisoformat(media["timestamp"])
        timedelta =  now - post_timestamp.replace(tzinfo=None)
        if timedelta.days <= 30 :
            need_medias.append(media)
        else:
            break
    with open(page+"_clone.txt", "w") as f:
        f.write(json.dumps(need_medias))


