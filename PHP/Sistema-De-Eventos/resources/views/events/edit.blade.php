
@extends('layouts.main')

@section('title', 'Editando: '. $events->title)

@section('content')

<div id="event-create-container" class="col-md-6 offset-md-3">
    <h1>Editando o evento: {{ $events->title }}</h1><br>
    <form action="/events/update/{{ $events->id }}" method="POST" enctype="multipart/form-data">
            @csrf
            @method('PUT')
            <div class="form-group">
                    <label for="title">Evento: </label>
                    <input type="text" class="form-control" id="title" name="title" placeholder="Nome do Evento" value="{{ $events->title }}" required>
            </div><br>
            <div class="form-group">
                    <label for="date">Data do evento: </label>
                    <input type="datetime" class="form-control" id="date" name="date" value="{{ $events->date->format('Y-m-d H:i') }}" required>
                </div><br>
            <div class="form-group">
                    <label for="title">Local: </label>
                    <input type="text" class="form-control" id="city" name="city" placeholder="Local do Evento" value="{{ $events->city }}" required>
            </div><br>
            <div class="form-group">
                    <label for="title">O evento é privado?</label>
                    <input type="radio" name="private" value="0" {{ $events->private == 0 ? "checked='checked'" : "" }}>
                    <label for="">Não</label>
                    <input type="radio" name="private" value="1" {{ $events->private == 1 ? "checked='checked'" : "" }}>
                    <label for="">Sim</label>
            </div><br>
            <div class="form-group">
                    <label for="title">Descrição: </label>
                    <textarea name="description" id="description" class="form-control" placeholder="O que vai acontecer no evento?">{{ $events->description }}</textarea>
            </div><br>
            <div class="form-group">
                    <label for="title">Adicione items de infraestrutura: </label>
                    <div class="form-group">
                            <input type="checkbox" name="items[]" value="Cadeiras"> Cadeiras
                    </div>
                    <div class="form-group">
                            <input type="checkbox" name="items[]" value="Palco"> Palco
                    </div>
                    <div class="form-group">
                            <input type="checkbox" name="items[]" value="Open Bar"> Open Bar
                    </div>
                    <div class="form-group">
                            <input type="checkbox" name="items[]" value="Brindes"> Brindes
                    </div>
            </div><br>
            <div class="form-group">
                    <label for="#">Imagem atual do evento: </label>
                    <img src="/img/events/{{ $events->image }}" alt="{{ $events->title }}" class="img-preview"><br>
                    <label for="image">Imagem do evento: </label>
                    <input type="file" class="form-control-file" id="image" name="image" required>
            </div><br>
            <input type="submit" class="btn btn-primary" value="Alterar Evento">
    </form>
</div>

@endsection