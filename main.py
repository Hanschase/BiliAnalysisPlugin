from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *  # 导入事件类
import re
import requests
from mirai import Image,MessageChain

'''
当收到B站视频链接时，对B站链接进行分析并发送封面，标题，作者，等内容
'''
#注册插件
@register(name='BiliAnalysis', description='当收到B站视频链接时，对B站链接进行分析并发送封面，标题，作者，等内容', version='0.2', author="Hanschase")
class BiliAnalysisPlugin(BasePlugin):
    #插件加载时触发
    def __init__(self, host: APIHost):
        pass
    @handler(PersonNormalMessageReceived)
    async def on_person_normal_message(self, ctx: EventContext):
        msg = ctx.event.text_message
        #如果msg含有https://www.bilibili.com/video/字段则截取BV号
        match = re.search(r'https://www.bilibili.com/video/(BV\w+)', msg)
        if match:
            bv_id = match.group(1)
            #发送封面，标题，作者等信息
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
            }
            response = requests.get(f"https://api.bilibili.com/x/web-interface/view?bvid={bv_id}", headers=headers)
            data = response.json()
            if data['code'] == 0:
                video_data = data['data']
                cover_url = video_data['pic']
                author_name = video_data['owner']['name']
                video_url = "https://www.bilibili.com/video/" + bv_id
                title = video_data['title']
                await ctx.event.query.adapter.reply_message(ctx.event.query.message_event,MessageChain([f"B站视频解析成功喵~\n",
                                                                                                        "封面：",Image(url=cover_url),
                                                                                                        f"视频标题：{title}\n",
                                                                                                        f"UP主：{author_name}\n",
                                                                                                        f"视频链接：{video_url}"
                                                                                                        ]), False)
                ctx.prevent_default()
                ctx.prevent_postorder()
            else:
                ctx.add_return("reply", ["视频解析失败"])
                ctx.prevent_default()
                ctx.prevent_postorder()

    # 当收到群消息时触发
    @handler(GroupNormalMessageReceived)
    async def group_normal_message_received(self, ctx: EventContext):
        msg = ctx.event.text_message
        # 如果msg含有https://www.bilibili.com/video/字段则截取BV号
        match = re.search(r'https://www.bilibili.com/video/(BV\w+)', msg)
        if match:
            bv_id = match.group(1)
            # 发送封面，标题，作者等信息
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
            }
            response = requests.get(f"https://api.bilibili.com/x/web-interface/view?bvid={bv_id}", headers=headers)
            data = response.json()
            if data['code'] == 0:
                video_data = data['data']
                cover_url = video_data['pic']
                author_name = video_data['owner']['name']
                video_url = "https://www.bilibili.com/video/" + bv_id
                title = video_data['title']
                await ctx.event.query.adapter.reply_message(ctx.event.query.message_event,MessageChain([f"B站视频解析成功喵~\n",
                                                                                                        "封面：",Image(url=cover_url),
                                                                                                        f"视频标题：{title}\n",
                                                                                                        f"UP主：{author_name}\n",
                                                                                                        f"视频链接：{video_url}"
                                                                                                        ]), False)
                # 下面是垃圾代码防止以后有用先不删
                # send_text = (f"B站视频解析成功喵~\n"
                #              f"视频标题：{title}\n"
                #              f"UP主：{author_name}\n"
                #              f"视频链接：{video_url}")
                # ctx.add_return("reply",[send_text])
                ctx.prevent_default()
                ctx.prevent_postorder()
            else:
                ctx.add_return("reply", ["视频解析失败"])
                ctx.prevent_default()
                ctx.prevent_postorder()
