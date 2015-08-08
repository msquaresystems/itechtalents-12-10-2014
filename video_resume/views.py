import json

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.conf import settings

from video_resume.models import VideoResume


def create_video(request):
	guid = request.GET.get("guid", "")
	if request.is_ajax() and guid:
		try:
			video = VideoResume.objects.create(
				user=request.user,
				guid=guid,
				title="Test Video"
			)
			data = {
			   "success": True,
			   "id": video.id
			}
		except Exception as err:
			data = {
				"success": False,
				"err": str(err)
			}
		return HttpResponse(
			json.dumps(data),
			content_type="application/json",
		)

	template_name = "video-resume-create.html"
	context = {
    	"nimbb": settings.NIMBB
    }
	return render_to_response(template_name, context)

def view_video(request, id):

	video = VideoResume.objects.get(
		id = id
	)
	template_name = "video-resume-play.html"
	context = {
    	#"nimbb": settings.NIMBB,
    	"video": video
    }
	return render_to_response(template_name, context)