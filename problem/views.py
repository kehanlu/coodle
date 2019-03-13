from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from problem.models import Problem, Submission
import markdown


def problem_list(request):
    context = {
        'problems': Problem.objects.all().order_by('-create_date')
    }
    return render(request, 'problem/list.html', context)


def problem(request, pid):
    # not found
    if not Problem.objects.filter(id=pid).exists():
        return HttpResponseNotFound()

    context = {
        'problem': Problem.objects.get(id=pid),
    }
    return render(request, 'problem/single.html', context)


def submission(request, pid):
    if not Problem.objects.filter(id=pid).exists():
        return HttpResponseNotFound()

    problem = Problem.objects.get(id=pid)

    context = {
        'submissions': problem.psub.all().order_by('-submit_date'),
    }
    return render(request, 'problem/submission.html', context)


def post(request):
    return render(request, 'problem/create.html', {})


def api_post(request):
    data = request.POST
    description = markdown.markdown(
        data['description'], extensions=['fenced_code'])

    problem = Problem.objects.create(user=request.user,
                                     title=data['title'],
                                     description=description,
                                     short_description=data['short_description'])
    return redirect('/problem/{}'.format(problem.id))


def api_submit(request, pid):
    # not found
    if not Problem.objects.filter(id=pid).exists():
        return HttpResponseNotFound()

    if request.method == "POST":
        data = request.POST
        problem = Problem.objects.get(id=pid)
        if len(data['code']) > 10:
            Submission.objects.create(
                problem=problem,
                user=request.user,
                code=data['code']
            )
        return redirect('/problem/{}'.format(pid))


def api_submission(request, sid):
    if not Submission.objects.filter(id=sid).exists():
        return HttpResponseNotFound()

    submission = Submission.objects.get(id=sid)

    return JsonResponse(
        {
            'code': submission.code,
        }
    )
