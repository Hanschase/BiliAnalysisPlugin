# BiliAnalysisPlugin

<!--
## 插件开发者详阅

### 开始

此仓库是 QChatGPT 插件模板，您可以直接在 GitHub 仓库中点击右上角的 "Use this template" 以创建你的插件。  
接下来按照以下步骤修改模板代码：

#### 修改模板代码

- 修改此文档顶部插件名称信息
- 将此文档下方的`<插件发布仓库地址>`改为你的插件在 GitHub· 上的地址
- 补充下方的`使用`章节内容
- 修改`main.py`中的`@register`中的插件 名称、描述、版本、作者 等信息
- 修改`main.py`中的`MyPlugin`类名为你的插件类名
- 将插件所需依赖库写到`requirements.txt`中
- 根据[插件开发教程](https://qchatgpt.rockchin.top/develop/plugin-dev.html)编写插件代码
- 删除 README.md 中的注释内容


#### 发布插件

推荐将插件上传到 GitHub 代码仓库，以便用户通过下方方式安装。   
欢迎[提issue](https://github.com/RockChinQ/QChatGPT/issues/new?assignees=&labels=%E7%8B%AC%E7%AB%8B%E6%8F%92%E4%BB%B6&projects=&template=submit-plugin.yml&title=%5BPlugin%5D%3A+%E8%AF%B7%E6%B1%82%E7%99%BB%E8%AE%B0%E6%96%B0%E6%8F%92%E4%BB%B6)，将您的插件提交到[插件列表](https://github.com/stars/RockChinQ/lists/qchatgpt-%E6%8F%92%E4%BB%B6)

下方是给用户看的内容，按需修改
-->

## 安装

配置完成 [QChatGPT](https://github.com/RockChinQ/QChatGPT) 主程序后使用管理员账号向机器人发送命令即可安装：

```
!plugin get https://github.com/Hanschase/BiliAnalysisPlugin
```
或查看详细的[插件安装说明](https://qchatgpt.rockchin.top/develop/plugin-intro.html#%E6%8F%92%E4%BB%B6%E7%94%A8%E6%B3%95)

## 说明
当收到B站视频链接时，对B站链接进行分析并发送封面，标题，作者等内容。
（自己逼逼：电脑看B站分享视频习惯直接发链接，但朋友看到链接一般不会点进去，虽然手机QQ也已经有了自动解析功能,就当做着练练手了）

## 使用
发送B站链接之后即可自动解析
![9892a35b356824efa8d34d41f717525](https://github.com/user-attachments/assets/37b3b577-d5dd-498f-a78a-6c8fed36a133)

<!-- 插件开发者自行填写插件使用说明 -->
