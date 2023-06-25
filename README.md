# Universal API-Based Multiplayer Concept
    
 I have been thinking about this concept for a while. Currently, if you want to make a multiplayer game with Unreal, you need a server(or a host), and clients all made with unreal. Same goes for Gamemaker, and although I haven't digged deep into networking in Unity, I assume it would be similar.
    
 So I thought 'Why not make a open standard for game-networking-protocol so that games using different engines can communicate with each other?' This way, not only game engines, but applications that are not made with game engines can utilize in-game data without extra hassle (for applications like live navigation maps on mobile phones in Euro truck simulator, etc...).
    
 Although this might be a rough draft in the current state, I would be coming back to this when I get more ideas. Feel free to help me out, as I feel this might help not only open source game engines, but to a wide variety of use cases.
    
----

### Repository Explanation
    
 API_Concept_Server contains the server project, written in python. You have to run this first.
 API_Concept_Godot contains the game project, made with Godot. You can run the project in the editor and check the output to see what's going on.
 API_Concept_Client contains the client project, written in python. This proves that this concept can be applied to other programs/applications that doesn't use game engines as well.

I would like to include Unreal/Unity projects as well, but for now, I think this is enough to prove my point. I'll add other game engines later when I can make some time.
