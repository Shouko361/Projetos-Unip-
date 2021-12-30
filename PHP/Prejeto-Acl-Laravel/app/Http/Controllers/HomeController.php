<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Gate;
use App\Models\Post;

class HomeController extends Controller
{
    /**
     * Create a new controller instance.
     *
     * @return void
     */
    public function __construct()
    {
        $this->middleware('auth');
    }

    /**
     * Show the application dashboard.
     *
     * @return \Illuminate\Contracts\Support\Renderable
     */
    public function index(Post $post)
    {
        $posts = $post->all();
        return view('home', compact('posts'));
    }

    public function update($idPost, Post $post){

        $post = Post::find($idPost);

        if(Gate::denies('update-post', $post))
            abort(403, 'Não autorizado');

        return view('update-post', compact('post'));

    }

    public function rolesPermission(){
       $nameUser = auth()->user()->name;
       var_dump("<h1>{$nameUser}</h1>");
    }
}
