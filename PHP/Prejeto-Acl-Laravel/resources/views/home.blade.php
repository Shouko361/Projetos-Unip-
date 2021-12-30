@extends('layouts.app')

@section('content')
<div class="container">
    @forelse ($posts as $post)
    <p>{{ $post->name }}</p>

        @can('view_post', $post)
            <h1>{{ $post->title }}</h1>
            <p>{{ $post->description }}</p>
            <b>Author: {{ $post->user->name }}</b>
            @can('edit_post', $post)
                <a href="/post/{{ $post->id }}/update">Editar</a>
            @endcan
        @endcan
    @empty
        <p>Nenhuma postagem encontrada!</p>
    @endforelse
</div>
@endsection
