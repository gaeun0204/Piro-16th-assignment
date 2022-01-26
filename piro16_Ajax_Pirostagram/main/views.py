from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def post_list(request):
	posts = Post.objects.all()
	ctx = {'posts' : posts}
	return render(request, template_name = 'list.html', context = ctx)

def post_create(request):
	if request.method == 'POST':
		form = PostForm(request.POST) 
		if form.is_valid():
			form = form.save()
			return redirect('main:list')
	else:
		form = PostForm() 
		ctx = {'form' : form}
		return render(request, template_name = 'post_form.html', context = ctx)

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

{% csrf_token %}
@csrf_exempt # Ajax나 CDV?? 사용할때 꼭 써줘야함. 보안무시한다는 의미.
def like_ajax(request):
	req = json.loads(request.body) # 클라이언트에게 받은 {'id':1, 'type':like}를 파이썬 딕셔너리 형태로 저장
	post_id = req['id']
	button_type = req['type']

	print(poist_id, button_type)

	post = Post.objects.get(id=post_id)

	if button_type == 'like':
		post.like += 1
	else:
		post.dislike += 1

	post.save() # 꼭 save해줘야 DB에 저장된다
# 여기까진 바뀐값 DB에 저장만하고 사용자에겐 안 보여줌

# reload없이 바뀐값 알려줌.
# JsonResponse Json형태로 변환
	return JsonResponse({'id':post_id, 'type':button_type}) # 클라이언트에게 응답 {'id':1, 'type':like} 전송 - 화면에 출력