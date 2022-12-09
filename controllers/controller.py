from flask import render_template, request, redirect # request, redirect ADDED
from app import app
from models.event_list import events
from models.event import Event

@app.route('/events')
def index():
    return render_template("index.html", title="Events planner", events=events)

@app.route('/events', methods=['POST'])
def create():
    event_name = request.form["event_name"]
    room_location = request.form["room_location"]
    no_guests = request.form["no_guests"]
    description = request.form["description"]
    date = str(request.form["date"])
    recurring = bool(request.form["recurring"])
    new_event = Event(date, event_name, no_guests, room_location, description, recurring)
    events.append(new_event)
    return redirect('/events')

@app.route('/events/delete', methods=['POST'])
def remove():
    delete_event_name = request.form[delete_event_name]
    for event in events:
        if event.event_name == delete_event_name:
            events.remove(event)
    return redirect('/events')