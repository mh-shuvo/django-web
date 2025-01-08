from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from timetracking.models import TimeLog
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/login')
def home(request):
    # Assuming the logged-in user is the one for whom we need the durations
    user_id = request.user.id

    # Get durations from TimeLog model methods
    today_duration = TimeLog.get_today_total_work_duration(user_id)
    week_duration = TimeLog.get_current_week_work_duration(user_id)
    month_duration = TimeLog.get_current_month_work_duration(user_id)
    year_duration = TimeLog.get_current_year_work_duration(user_id)

    # Pass the data to the template
    context = {
        'today_duration': today_duration,
        'week_duration': week_duration,
        'month_duration': month_duration,
        'year_duration': year_duration,
    }

    return render(request, 'moderator/home.html', context)