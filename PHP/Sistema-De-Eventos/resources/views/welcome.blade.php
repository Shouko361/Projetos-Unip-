@extends('layouts.main')

@section('title', 'Página inicial')

@section('content')
        <div id="search-container" class="col-">
                <h1>Busque um evento</h1>
                <form action="/" method="GET" class="d-flex">
                        <input class="form-control me-2" name="search" type="search" placeholder="Procurar..." aria-label="Search">
                        <button class="btn btn-outline-success" type="submit">Buscar</button>
                </form>
        </div>
        <div id="events-container" class="col-">
                @if ($search)
                        <h2>Buscando por: {{ $search }}</h2><br>
                @else
                        <h2>Próximos Eventos</h2>
                        <p class="subtitle">Veja os eventos dos próximos dias</p>
                @endif
                <div id="cards-container" class="row">
                        @foreach ($events as $event)
                            <div class="card col-md-3">
                                <img src="/img/events/{{ $event->image }}" alt="{{ $event->title }}">
                                <div class="card-body">
                                        <p class="card-date">{{ date('d/m/Y H:i:s', strtotime($event->date)) }}</p>
                                        <h5 class="card-title">{{ $event->title }}</h5>
                                        <p class="card-participants">{{ count($event->users) }} participantes</p>
                                        <a href="/events/{{ $event->id }}" class="btn btn-primary">Saber mais</a>
                                </div>
                            </div>
                        @endforeach
                        @if (count($events) == 0 && $search)
                                <p>Não foi possível encontrar nenhum evento com {{ $search }}! <a href="/">Ver todos</a></p>
                        @elseif(count($events) == 0)
                                <p>Não existem eventos no momento!</p>
                        @endif
                </div>
        </div>
@endsection