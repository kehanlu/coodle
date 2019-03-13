import random
from django.shortcuts import render
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.contrib.auth.models import User
from users.models import Profile


def submission(request):
    context = {
        'submissions': request.user.usub.all()
    }
    return render(request, 'problem/submission.html', context)


@receiver(user_signed_up)
def sign_up(request, user, **kwargs):
    animals = set(["匿名變色龍", "匿名地鼠", "匿名雪貂", "匿名烏鴉", "匿名鴨嘴獸", "匿名海狸", "匿名孤狼", "匿名青蛙", "匿名水豚", "匿名浣熊", "匿名猴子", "匿名鬣蜥", "匿名奇異鳥", "匿名澳洲野犬", "匿名臭鼬", "匿名獨角鯨", "匿名蝙蝠", "匿名短尾矮袋鼠", "匿名蠑螈", "匿名恐龍", "匿名企鵝", "匿名灰熊", "匿名水滴魚", "匿名毛絲鼠", "匿名海豚",
                   "匿名鴨子", "匿名烏龜", "匿名犀牛", "匿名老虎", "匿名河馬", "匿名食蟻獸", "匿名花栗鼠", "匿名長頸鹿", "匿名草原狼", "匿名獅虎", "匿名列報", "匿名野生山羊", "匿名獾", "匿名袋鼠", "匿名鹿角兔", "匿名海牛", "匿名羊駝", "匿名鵝", "匿名狐猴", "匿名無尾熊", "匿名水牛", "匿名鱷魚", "匿名蟒蛇", "匿名兔子", "匿名水貂", "匿名海象", "匿名刺蝟"])
    used_animals = set([user.profile.nickname for user in User.objects.all()])
    nickname = random.choice(list(animals-used_animals))
    Profile.objects.create(user=user, nickname=nickname)
