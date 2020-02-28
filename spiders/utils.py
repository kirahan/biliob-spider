
from db import redis_connect_string, redis_connection
import redis
from time import sleep

sub_channel_2_channel = {
    'ASMR': '生活',
    'GMV': '游戏',
    'Korea相关': '娱乐',
    'MAD·AMV': '动画',
    'MMD·3D': '动画',
    'Mugen': '游戏',
    'OP/ED/OST': '音乐',
    'VOCALOID·UTAU': '音乐',
    '三次元舞蹈': '舞蹈',
    '三次元音乐': '音乐',
    '人力VOCALOID': '鬼畜',
    '人文·历史': '纪录片',
    '健身': '时尚',
    '其他': '生活',
    '其他国家': '电影',
    '军事': '纪录片',
    '动物圈': '生活',
    '华语电影': '电影',
    '单机游戏': '游戏',
    '原创音乐': '音乐',
    '国产剧': '电视剧',
    '国产动画': '国创',
    '国产原创相关': '国创',
    '宅舞': '舞蹈',
    '完结动画': '番剧',
    '官方延伸': '番剧',
    '布袋戏': '国创',
    '广告': '广告',
    '影视剪辑': '影视',
    '影视杂谈': '影视',
    '手工': '生活',
    '手机游戏': '游戏',
    '搞笑': '生活',
    '教程演示': '鬼畜',
    '数码': '数码',
    '日常': '生活',
    '明星': '娱乐',
    '星海': '科技',
    '服饰': '时尚',
    '机械': '科技',
    '桌游棋牌': '游戏',
    '欧美电影': '电影',
    '汽车': '科技',
    '海外剧': '电视剧',
    '演奏': '音乐',
    '演讲·公开课': '科技',
    '特摄': '影视',
    '电子竞技': '游戏',
    '短片': '影视',
    '短片·手书·配音': '动画',
    '社会·美食·旅行': '纪录片',
    '科学·探索·自然': '纪录片',
    '绘画': '生活',
    '综合': '动画',
    '综艺': '娱乐',
    '网络游戏': '游戏',
    '美妆': '时尚',
    '美食圈': '生活',
    '翻唱': '音乐',
    '舞蹈教程': '舞蹈',
    '资讯': '国创',
    '趣味科普人文': '科技',
    '运动': '生活',
    '连载动画': '番剧',
    '野生技术协会': '科技',
    '音MAD': '鬼畜',
    '音乐选集': '音乐',
    '音游': '游戏',
    '预告 资讯': '影视',
    '预告·资讯': '影视',
    '单机联机': '游戏',
    '鬼畜调教': '鬼畜',
    '演讲• 公开课': '科技',
    '国产电影': '电影',
    '日本电影': '电影',
    '番剧': '番剧',
    '国创': '国创',
    '鬼畜': '鬼畜',
    '电视剧': '电视剧',
    '动画': '动画',
    '时尚': '时尚',
    '娱乐': '娱乐',
    '电影': '电影',
    '舞蹈': '舞蹈',
    '舞蹈综合': '舞蹈',
    '科技': '科技',
    '生活': '生活',
    '音乐': '音乐',
    '纪录片': '纪录片',
    '手机平板': '数码',
    '电脑装机': '数码',
    '影音智能': '数码',
    '摄影摄像': '数码',
    '风尚标': '时尚',
    '电音': '音乐',
    '音乐综合': '音乐',
    'MV': '音乐',
    '音乐现场': '音乐',
    '游戏': '游戏',
    'T台': '时尚',
    '动态漫·广播剧': '国创',
    '明星舞蹈': '舞蹈',
    '街舞': '舞蹈',
    '中国舞': '舞蹈',
}


def get_url_from_redis(key, redis_connection=redis_connection):
  while True:
    try:
      url = redis_connection.lpop(key)
    except Exception:
      redis_connection = redis.from_url(redis_connect_string)
      url = redis_connection.lpop(key)
    if url != None:
      return url
    else:
      sleep(1)
