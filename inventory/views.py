from django.shortcuts import render, get_object_or_404, redirect
from .models import Monument
from django.shortcuts import render, redirect
from .forms import MonumentForm
from django.utils import timezone
from django.db.models import Sum, Count


def add_lot(request):
    if request.method == 'POST':
        form = MonumentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('monument_list')  # Redirect to monument list after saving
    else:
        form = MonumentForm()

    return render(request, 'inventory/add_lot.html', {'form': form})

def monument_list(request):
    monuments = Monument.objects.all()
    return render(request, 'inventory/monument_list.html', {'monuments': monuments})

def transfer_monument(request, monument_id):
    monument = get_object_or_404(Monument, id=monument_id)

    if request.method == 'POST':
        new_name = request.POST.get('name')
        transferred_quantity = int(request.POST.get('transferred_quantity'))
        new_status = request.POST.get('new_status')

        # Ensure we do not transfer more than available quantity
        if transferred_quantity > monument.quantity:
            return render(request, 'inventory/transfer_monument.html', {
                'monument': monument,
                'error': 'Cannot transfer more than available quantity.'
            })

        # Update the quantity for the current section (reduce the quantity)
        monument.quantity -= transferred_quantity

        # Save the current monument
        monument.updated_at = timezone.now()
        monument.save()

        # Check if the same person (new_name) already has an entry for the same monument and status
        existing_entry = Monument.objects.filter(
            name=new_name,
            monument=monument.monument,
            status=new_status
        ).first()

        if existing_entry:
            # If an entry exists, update the quantity by adding the new transferred quantity
            existing_entry.quantity += transferred_quantity
            existing_entry.updated_at = timezone.now()  # Update the timestamp
            existing_entry.save()
        else:
            # Create a new monument entry for the transferred portion if no entry exists
            new_monument = Monument.objects.create(
                name=new_name,
                from_person=monument.name,
                monument=monument.monument,
                category=monument.category,
                weight=monument.weight,
                length=monument.length,
                width=monument.width,
                height=monument.height,
                quantity=transferred_quantity,
                status=new_status
            )

            # Set the created_at time for the new section
            current_time = timezone.now()
            if new_status == 'polisher':
                new_monument.polisher_created_at = current_time
            elif new_status == 'designer':
                new_monument.designer_created_at = current_time
            elif new_status == 'stock':
                new_monument.stock_created_at = current_time

            new_monument.save()

        return redirect('monument_list')

    return render(request, 'inventory/transfer_monument.html', {'monument': monument})


def dashboard(request):
    # Sum the total quantity of monuments in each stage
    owner_quantity = Monument.objects.filter(status='owner').aggregate(total=Sum('quantity'))['total'] or 0
    polisher_quantity = Monument.objects.filter(status='polisher').aggregate(total=Sum('quantity'))['total'] or 0
    designer_quantity = Monument.objects.filter(status='designer').aggregate(total=Sum('quantity'))['total'] or 0
    stock_quantity = Monument.objects.filter(status='stock').aggregate(total=Sum('quantity'))['total'] or 0

    # Get the list of all monuments with name and category for the table
    monument_list = Monument.objects.values('name', 'monument', 'category', 'status')

    context = {
        'owner_quantity': owner_quantity,
        'polisher_quantity': polisher_quantity,
        'designer_quantity': designer_quantity,
        'stock_quantity': stock_quantity,
        'monument_list': monument_list,
    }
    
    return render(request, 'inventory/dashboard.html', context)


def delete_monument(request, monument_id):
    monument = get_object_or_404(Monument, id=monument_id)
    
    if request.method == 'POST':
        monument.delete()
        return redirect('monument_list')

    return render(request, 'inventory/delete_monument.html', {'monument': monument})