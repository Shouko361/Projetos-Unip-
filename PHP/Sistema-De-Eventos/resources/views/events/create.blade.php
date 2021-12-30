@extends('layouts.main')

@section('title', 'Criar Evento')

@section('content')
        <div id="event-create-container" class="col-md-6 offset-md-3">
                <h1>Crie o seu evento</h1><br>
                <form action="/events" method="POST" enctype="multipart/form-data">
                        @csrf
                        <div class="form-group">
                                <label for="title">Evento: </label>
                                <input type="text" class="form-control" id="title" name="title" placeholder="Nome do Evento" required>
                        </div><br>
                        <div class="form-group">
                                <label for="date">Data do evento: </label>
                                <input type="datetime-local" class="form-control" id="date" name="date" required>
                        </div><br>
                        <div class="form-group">
                                <label for="title">Local: </label>
                                <input type="text" class="form-control" id="city" name="city" placeholder="Local do Evento" required>
                        </div><br>
                        <div class="form-group">
                                <label for="title">O evento é privado?</label>
                                <input type="radio" name="private" value="0">
                                <label for="">Não</label>
                                <input type="radio" name="private" value="1" checked>
                                <label for="">Sim</label>
                        </div><br>
                        <div class="form-group">
                                <label for="title">Descrição: </label>
                                <textarea name="description" id="description" class="form-control" placeholder="O que vai acontecer no evento?"></textarea>
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
                                <label for="image">Imagem do evento: </label>
                                <input type="file" class="form-control-file" id="image" name="image" required>
                        </div><br>
                        <input type="submit" class="btn btn-primary" value="Criar Evento">
                </form>
        </div>
@endsection