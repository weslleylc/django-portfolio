from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from portfolio.models import Project, Review, Profile
from django.http import HttpResponseRedirect
from .forms import ReviewForm



def project_index(request):
    projects = Project.objects.all()
    reviews = Review.objects.all()
    # My user
    wes = User.objects.get(id=1)


    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            comment = Review(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                score=form.cleaned_data["score"],
            )
            comment.save()
            form.cleaned_data["author"] = ""
            form.cleaned_data["body"] = ""
            form.cleaned_data["score"] = 0
            return HttpResponseRedirect("/portfolio")

    context = {"projects": projects, "form": form, 'reviews': reviews, "wes": wes}

    return render(request, "portfolio/project_index.html", context)

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    context = {"project": project}
    return render(request, "portfolio/portfolio-details.html", context)
