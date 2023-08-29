from flask import Flask,json,jsonify,request
app=Flask(__name__)

animee= [
    {
    "id": 1,
    "titulo": "Gintama THE FINAL",
    "categoria": ["Accion","Comedia","Drama","Ciencia ficcion"],
    "rating": 91,
    "reviews": 33633,
    "season": "Invierno 2021",
    "tipo": "pelicula",
    "portada":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx114129-RLgSuh6YbeYx.jpg"
    },
    {
    "id": 2,
    "titulo": "Gintama",
    "categoria": ["accion","comedia","drama","ciencia ficcion"],
    "rating": 90,
    "reviews": 87963,
    "season": "Primavera 2015",
    "tipo": "serie",
    "portada":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx20996-kBEGEGdeK1r7.jpg"
    },
    {
    "id": 3,
    "titulo": "Cesta de frutas: la final",
    "categoria": ["comedia","drama","psicologico"],
    "rating": 90,
    "reviews": 118020,
    "season": "Primavera 2021",
    "tipo": "serie",
    "portada":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx124194-pWfBqp3GgjOx.jpg"
    },
    {
    "id": 4,
    "titulo": "Hagane no Renkinjutsushi: ALQUIMISTA DE METAL",
    "categoria": ["accion","aventura","drama","fantasia"],
    "rating": 90,
    "reviews": 494524,
    "season": "Primavera 2009",
    "tipo": "serie",
    "portada":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx5114-KJTQz9AIm6Wk.jpg"
    },
    {
    "id":5,
    "titulo":"Kaguya-sama wa Kokurasetai: Ultra Romantic",
    "categoria":["comedy","psychological","romance","sci-fi"],
    "rating":90,
    "reviews":176923,
    "season":"Primavera 2019",
    "tipo":"TV Show",
    "portada":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/bx125367-bl5vGalMH2cC.png",
    },
    {
    "id":6,
    "titulo":"Shingeki no Kyojin 3 Part 2",
    "categoria":["action","drama","fantasy","mystery"],
    "rating":90,
    "reviews":411090,
    "season":"Otoño 2017",
    "tipo":"TV Show",
    "portada":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/bx104578-LaZYFkmhinfB.jpg",
    },
    {
    "id":7,
    "titulo":"3-gatsu no Lion 2",
    "categoria":["drama","sci-fi"],
    "rating":89,
    "reviews":102391,
    "season":"2011 - 2014",
    "tipo":"TV Show",
    "portada":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/bx98478-dF3mpSKiZkQu.jpg",
    },
    {
    "id":8,
    "titulo":"HUNTERHUNTER (2011)",
    "categoria":["action","adventure","fantasy"],
    "rating":89,
    "reviews":575350,
    "season":"Verano 2017",
    "tipo":"TV Show",
    "portada":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/bx11061-sIpBprNRfzCe.png",
    },
    {
    "id":9,
    "titulo":"Owarimonogatari (Ge)",
    "categoria":["comedy","mystery","psychological","romance","supernatural"],
    "rating":89,
    "reviews":92090,
    "season":"Primavera 2011",
    "tipo":"TV Show",
    "portada":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/bx21745-vHwC1VKoL6zf.png",
    },
    {
    "id":10,
    "titulo":"Steins;Gate",
    "categoria":["drama","psychological","sci-fi","thriller"],
    "rating":89,
    "reviews":410650,
    "season":"Otoño 2020",
    "tipo":"TV Show",
    "portada":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/bx9253-7pdcVzQSkKxT.jpg",
    }
]

@app.route("/", methods=["GET"])
def inicio():  
    return "Bienvenidos a la lista de animes"

@app.route("/anime", methods=["GET"])
def leer():  
    return jsonify(animee)

@app.route("/anime", methods=["POST"])
def crear():  
    nuevo_anime = {
        "id": len(animee) + 1,  # id nuevo
        "titulo": request.json.get("titulo"),  
        "categoria":request.json.get("categoria"),
        "rating":request.json.get("rating"),
        "reviews":request.json.get("reviews"),
        "season":request.json.get("season"),
        "tipo":request.json.get("tipo"),
        "portada": request.json.get("portada"),
    }
    animee.append(nuevo_anime)
    return jsonify(nuevo_anime), 201 

@app.route("/anime/<int:id>", methods=["GET"])
def animeId(id):
    anime_id = next((anime for anime in animee if anime['id'] == int(id)), None)
    if anime_id:
        return jsonify(anime_id)
    else:
        return "Anime no encontrado", 404

@app.route("/anime/<int:id>", methods=["DELETE"])
def deleteanimeId(id):
    anime_id = next((anime for anime in animee if anime['id'] == int(id)), None)
    if anime_id:
        animee.remove(anime_id)  # Elimina
        return "Anime eliminado",200
    else:
        return "Anime no encontrado", 404
    
@app.route("/anime/<int:id>", methods=["PUT"])
def anime_update(id):
    anime_id = next((anime for anime in animee if anime['id'] == int(id)), None)
    if anime_id:
        anime_id.update(request.json)  #Actualiza
        return jsonify(anime_id), 200
    else:
        return "Anime no encontrado", 404

@app.route("/anime/<int:id>", methods=["PATCH"])
def anime_patch(id):
    anime_id = next((anime for anime in animee if anime['id'] == int(id)), None)
    if anime_id:
        dat = request.json
        for key, value in dat.items():
            if key in anime_id:
                anime_id[key] = value  # Actualiza específico
        return jsonify(anime_id), 200
    else:
        return "Anime no encontrado", 404
    

if __name__ == '__main__':
    app.run(debug=True)
