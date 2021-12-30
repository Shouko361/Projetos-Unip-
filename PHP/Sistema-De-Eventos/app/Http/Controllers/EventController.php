<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Event;
use App\Models\User;
class EventController extends Controller
{
    public function index() {

        $search = request('search');

        if ($search) {

            $events = Event::where([
                ['title', 'like', '%'.$search.'%']
            ])->get();

        }else{

            $events = Event::all();

        }

        return view('welcome', ['events' => $events, 'search' => $search]);
    }

    public function create() {
     
        return view('events.create');
    
    }

    public function store(Request $request){

        $event = new Event;

        $event->title = $request->title;
        $event->date = $request->date;
        $event->city = $request->city;
        $event->private = $request->private;
        $event->description = $request->description;
        $event->items = $request->items;

        //image
        if($request->hasFile('image') && $request->file('image')->isValid()){
            $requestImage = $request->image;
            $extension = $requestImage->extension();
            $imageName = sha1($requestImage->getClientOriginalName() . strtotime("now")). "." . $extension;
            $request->image->move(public_path('/img/events'), $imageName);
            $event->image = $imageName;
        }

        $user = auth()->user();
        $event->user_id = $user->id;
        
        $event->save();

        return redirect('/')->with('msg', 'Evento criado com sucesso!');

    }

    public function show($id){
        
        $event = Event::findOrFail($id);

        $user = auth()->user();
        $hasUserJoined = false;

        if($user){

            $userEvents = $user->eventsAsParticipants->toArray();

            foreach($userEvents as $userEvent){

                if($userEvent['id'] == $id){

                    $hasUserJoined = true;

                }

            }

        }

        $eventOwner = User::where('id', $event->user_id)->first()->toArray();

        return view('events.show', ['event' => $event, 'eventOwner' => $eventOwner, 'hasUserJoined' => $hasUserJoined]);

    }

    public function dashboard(){

        $user = auth()->user();

        $events = $user->events;

        $eventsAsParticipant = $user->eventsAsParticipants;

        return view('events.dashboard', ['events' => $events, 'eventsasparticipant' => $eventsAsParticipant]);    
    }

    public function destroy($id){

        $user = auth()->user();

        $events = $user->events;

        $eventsAsParticipant = $user->eventsAsParticipants;

        if(count($eventsAsParticipant) > 0){

            return redirect('/dashboard')->with('msg', 'Existem pessoas neste evento');    
        
        }else{

            Event::findOrFail($id)->delete();
        
        }

        return redirect('/dashboard')->with('msg', 'Evento excluido com sucesso!');

    }

    public function edit($id){

        $user = auth()->user();

        $event = Event::findOrFail($id);

        if($user->id != $event->user_id){
            return redirect('/dashboard')->with('msg', 'Você não pode editar esse evento');
        }

        return view('events.edit', ['events' => $event]);

    }

    public function update(Request $request){

        $data = $request->all();
            
            //image
            if($request->hasFile('image') && $request->file('image')->isValid()){
                $requestImage = $request->image;
                $extension = $requestImage->extension();
                $imageName = sha1($requestImage->getClientOriginalName() . strtotime("now")). "." . $extension;
                $request->image->move(public_path('/img/events'), $imageName);
                $data['image'] = $imageName;
            }

        Event::findOrFail($request->id)->update($data);

        return redirect('/dashboard')->with('msg', 'Evento alterado com sucesso!');

    }

    public function joinEvent($id){

        $user = auth()->user();

        $user->eventsAsParticipants()->attach($id);

        $events = Event::findOrFail($id);

        return redirect('/')->with('msg', 'Presença confirmada!');

    }

    public function leaveEvent($id){

        $user = auth()->user();

        $user->eventsAsParticipants()->detach($id);

        $events = Event::findOrFail($id);

        return redirect('/dashboard')->with('msg', 'Sua presença foi cancelada!');

    }
}