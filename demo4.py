import time

print(time.strftime("%y%m%d %H:%M:%S", time.localtime()))

print(time.strftime('%Y{y}%m{m}%d{d}%H{h}%M{f}%S{s}').format(y='年', m='月', d='日', h='时', f='分', s='秒'))

dict = {"data": [
    {"id": 585, "isSave": "false", "status": 0, "title": "图片发送", "type": 2, "userUpdateDate": "2021-07-14T03:39:55.003Z",
     "image": "https://s3.cn-northwest-1.amazonaws.com.cn/juzi-work-material-prod/public/7f8f1221-4aa2-480e-a549-36d0be5ad10d_1111.jpg"},
    {"id": 586, "isSave": "false", "status": 0, "title": "图片发送2", "type": 2, "userUpdateDate": "2021-07-14T04:07:54.526Z",
     "image": "https://s3.cn-northwest-1.amazonaws.com.cn/juzi-work-material-prod/public/01213207-eec7-4296-a616-56a800b30317_6666.jpg"},
    {"id": 587, "isSave": "false", "status": 0, "title": "3333", "type": 2, "userUpdateDate": "2021-07-14T05:49:04.174Z",
     "image": "https://s3.cn-northwest-1.amazonaws.com.cn/juzi-work-material-prod/public/8561ceef-e416-43fa-b246-5c80f16bf887_9999.jpg"},
    {"id": 590, "isSave": "false", "status": 0, "title": "5555", "type": 2, "userUpdateDate": "2021-07-14T06:06:34.164Z",
     "image": "https://s3.cn-northwest-1.amazonaws.com.cn/juzi-work-material-prod/public/52bef14f-7cb7-40ea-86b8-aeafb0d61d03_9999.jpg"},
    {"id": 591, "isSave": "false", "status": 0, "title": "图文1", "type": 5, "userUpdateDate": "2021-07-14T06:16:55.292Z",
     "link": {"desc": "请为今天的课程打分，并留下你的建议或意见，我们将根据你的反馈来调整授课方式、内容等。",
              "picurl": "https://s3.cn-northwest-1.amazonaws.com.cn/juzi-work-material-prod/public/momentImg/juziwork_rc-upload-e96c2dde-fcd1-4bf1-ba9d-d6e33ad09065-1626243402805.jpg",
              "title": "句子互动测试用", "url": "https://jinshuju.net/f/sqdDMu"}},
    {"id": 592, "isSave": "false", "status": 0, "title": "表单话术1", "type": 7, "userUpdateDate": "2021-07-14T06:38:46.265Z",
     "form": {"id": 167, "title": "信息收集", "description": "为了给您提供更好的服务，我们需要收集您的个人信息",
              "finishWord": "感谢您提交问卷, 我们将尽快处理并联系您",
              "items": [{"id": 505, "name": "企业", "required": "true", "placeholder": "请输入企业"},
                        {"id": 504, "name": "手机号", "required": "true", "placeholder": "请输入手机号"},
                        {"id": 503, "name": "姓名", "required": "true", "placeholder": "请输入姓名"}]}}],
        "page": {"current": 1, "total": 6}}

print(dict["data"]["id"])
