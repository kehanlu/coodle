from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from problem.models import Problem, Submission


def problem_list(request):
    context = {
        'problems': Problem.objects.all()
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
        'submissions': problem.psub.all(),
    }
    return render(request, 'problem/submission.html', context)


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
