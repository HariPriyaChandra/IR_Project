from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .service import RetrieveResults


# Create your views here.

def search(request):
    return render(request, 'search.html')

def results(request):
    if request.method == 'POST':
        query = request.POST['query']
        scoring_model= request.POST['scoring_model']
        
        print(query, scoring_model)
        get_results = RetrieveResults()
        if scoring_model == 'yes':
            results = get_results.get_results_by_bm25(query)

        if scoring_model == 'no':
            results = get_results.get_results_by_jelinekMercer(query)

        
        # print(results)
        
        # for result in results:
        #     print(result['title'])
        
        return render(request, 'results.html', {'query':query, 'data':results})




