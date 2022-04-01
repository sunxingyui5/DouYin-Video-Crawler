import requests
import re


class DouYin_Downloader():
    def __init__(self, url):
        self.url = url
        self.headers = {
                        'cookie': 'douyin.com; ttcid=be0e4c72ddac477998e093a240602ab719; ttwid=1%7CzCUAumsJLs5saY5D8bn7dI_X83RllITT15UpYe3ipo0%7C1637395882%7C364bf27783fe82923c5cccad2dac9c5ff32b3c291d30199c937c84eaab37b5d7; _tea_utm_cache_6383=undefined; MONITOR_WEB_ID=572de40d-1fff-4dc0-836b-44602750dc34; _tea_utm_cache_1300=undefined; passport_csrf_token_default=dd2988387b03b0773031755a2075362f; passport_csrf_token=dd2988387b03b0773031755a2075362f; n_mh=fxMGxUII0nrBEe6Ohr1FoUZfRGlBDBAaChEVJm8nhLw; sso_uid_tt=431643b7ae0a16e36948eaa4aa2fe0b8; sso_uid_tt_ss=431643b7ae0a16e36948eaa4aa2fe0b8; toutiao_sso_user=a6a32f4d3abd7f5cb1eb0d7eeabc84ae; toutiao_sso_user_ss=a6a32f4d3abd7f5cb1eb0d7eeabc84ae; odin_tt=c7d78d63f431f8c1e00e8485858263b58517378bcc76989d41f95a286edf145a24fcc6619fb54291391fe759ddb14183232da50c003e508cb62704e1655bf862; passport_auth_status_ss=411c4ce005860d1e47ae548b3d79891e%2C; sid_guard=170aabb93cd0ea3eaf455af0ebb02145%7C1637396118%7C5183999%7CWed%2C+19-Jan-2022+08%3A15%3A17+GMT; uid_tt=a079d0ed3a5f1cc20ac7df76ab3f771b; uid_tt_ss=a079d0ed3a5f1cc20ac7df76ab3f771b; sid_tt=170aabb93cd0ea3eaf455af0ebb02145; sessionid=170aabb93cd0ea3eaf455af0ebb02145; sessionid_ss=170aabb93cd0ea3eaf455af0ebb02145; sid_ucp_v1=1.0.0-KDM0ODMxYjI2MWZjZmEyOGQxODY1YTVjZTA1NmRmMGU4Y2I4ZGJkNGIKFwj-yaDfrPSnBxCW3eKMBhjvMTgGQPQHGgJobCIgMTcwYWFiYjkzY2QwZWEzZWFmNDU1YWYwZWJiMDIxNDU; ssid_ucp_v1=1.0.0-KDM0ODMxYjI2MWZjZmEyOGQxODY1YTVjZTA1NmRmMGU4Y2I4ZGJkNGIKFwj-yaDfrPSnBxCW3eKMBhjvMTgGQPQHGgJobCIgMTcwYWFiYjkzY2QwZWEzZWFmNDU1YWYwZWJiMDIxNDU; passport_auth_status=411c4ce005860d1e47ae548b3d79891e%2C; __ac_nonce=06199f5620065ae56f208; __ac_signature=_02B4Z6wo00f01zXQoHQAAIDDtdJaNVT9We819KTAAKz4E9gQs3vJPZfIoRD8mx-QJL-EU8pQPmUm00Hbx9IagiMBd-pmRH3pvT6ggFtdKm1nTnr9mNQ5kieWCKvz2tKcdqz4X0KRer6BBdFre3; douyin.com; s_v_web_id=verify_kw8xnlj5_8y3BLFlW_B5ca_45LT_8ppb_jfJU5qu9V9Fr; msToken=q3LpmVgozuLxZu1J26Ygd2uJ-NEm08J03SWFEp5p19c3kENTBcHPQ4Pci1G-3kUt8IvmnZI2QX7o9GE7Kfd8h92iHl5qTgfD_qOFqct2IikUtpSZA46xZWsAoA==; msToken=SdRjdYoFLEpaFsvHhGFNVA4c3TOj2BVyb0iO8GpzjS5n47A9Ziv5aNAbDI3uUqSkYWagXM1tIS4SakirPiSM0m-E9vwN1urTp6eM2MQ6wdZsb-MC_x5wig==; tt_scid=n.SR2EXQsnCoS52o0b6sEoX8j2W6Zjp8vEp8WuuaKfgHE6S5wBV4QKudldzcLitOae57',
                        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
                        }
        self.text = requests.get(url=self.url, headers=self.headers).text

    def getTitle(self):
        return re.findall('<title data-react-helmet="true">(.*?)</title>', self.text)[0]

    def getVideoUrl(self):
        herf = re.findall('src(.*?)vr%3D%2', self.text)[1]
        video_url = requests.utils.unquote(herf).replace('":"', 'https:')
        return video_url

    def downloadVideo(self):
        title = self.getTitle()
        video_url = self.getVideoUrl()
        video_content = requests.get(url=video_url).content
        with open(title + '.mp4', mode='wb') as f:
            f.write(video_content)

    def getComment(self):
        decode_comment_url = requests.utils.unquote(self.text)
        comment = re.findall('"text":"(.*?)"', decode_comment_url)
        return comment

    def getLikeNum(self):
        likeNum = re.findall('<span class="CE7XkkTw">(.*?)</span>', self.text)[0]
        return likeNum

    def getCollectNum(self):
        collectNum = re.findall('<span class="CE7XkkTw">(.*?)</span>', self.text)[1]
        return collectNum

if __name__ == "__main__":
    url = 'https://www.douyin.com/video/7080711567834238240'
    DY = DouYin_Downloader(url)
    print("得到标题：", DY.getTitle())
    # DY.downloadVideo()
    print("得到评论：", DY.getComment())
    print("得到点赞数：", DY.getLikeNum())
    print("得到评论数：", DY.getCollectNum())