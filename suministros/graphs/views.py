from django.shortcuts import render

def graphs(request, graph=None):
    if graph != None:
        if graph == 'costumer':
            context = {
                'graph': 'costumer', 
            }
            return render(request, 'graphs/graphs.html', context)
        if graph == 'supplier':
            context = {
                'graph': 'supplier', 
            }
            return render(request, 'graphs/graphs.html', context)            
    return render(request, 'graphs/graphs.html', {})
