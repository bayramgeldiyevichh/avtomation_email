from .models import ControlVideo, VideoEdit
from .models import User
from django.core.mail import EmailMessage
import time
import schedule




def sendEmail():
    video = ControlVideo.objects.all()
    for i in video:
        if i.gorulen_aralayk != i.doly_wagty:
            emailSubject = "Ýönekeý H.K-y"
            message = "Wideony doly gormegi maslahat beryaris, size gyzykly maglumatlar garashyar"
            email = EmailMessage(
                emailSubject,
                message,
                to=[i.user.email]
            )
            email.send()



def controlVideo(videoId, userId, fullTime, stopTime):
    if float(stopTime) == float(fullTime):
        pass
    else:
        video = ControlVideo.objects.all()
        videoID = VideoEdit.objects.get(id=videoId)
        user = User.objects.get(id=userId)
        if len(video) == 0:
            video = ControlVideo.objects.create(
                user=user,
                video_name=videoID,
                doly_wagty=fullTime,
                gorulen_aralayk=stopTime
            )
            video.save()
        else:
            for i in video:
                if i.user == user and i.video_name == videoID:
                    i.gorulen_aralayk = stopTime
                    i.save()
                else:
                    video = ControlVideo.objects.create(
                        user=user,
                        video_name=videoID,
                        doly_wagty=fullTime,
                        gorulen_aralayk=stopTime
                    )
                    video.save()
        sendEmail()


# schedule.every(10).seconds.do(sendEmail)

# while 1:
#     schedule.run_pending()
#     time.sleep(1)