$(document).ready(function() {
    async function fetchPokemon(id) {
      try {
        // Mostrar el spinner antes de hacer la solicitud del Pokémon
        const spinner = $('<div class="spinner">Cargando...</div>');
        $('#pokemon-list').append(spinner);

        await new Promise(resolve => setTimeout(resolve, 2000)); // Simular un retraso de 3 segundos

        const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${id}`);
        const pokemonData = await response.json();

        // Obtener la URL de la imagen del Pokémon
        const pokemonImageUrl = pokemonData.sprites.other['official-artwork'].front_default;

        // Crear un elemento <li> para mostrar la información del Pokémon
        const listItem = $('<li>');

        // Crear un elemento <img> para mostrar la imagen del Pokémon
        const pokemonImage = $('<img>').attr('src', pokemonImageUrl).attr('alt', pokemonData.name);

        // Ocultar el spinner y mostrar la imagen una vez que se haya cargado
        pokemonImage.on('load', function() {
          spinner.remove(); // Eliminar el spinner una vez que la imagen se ha cargado
          listItem.append(pokemonImage); // Agregar la imagen al elemento <li>
        });

        // Agregar el elemento <li> a la lista de Pokémon
        $('#pokemon-list').append(listItem);
      } catch (error) {
        console.error('Error fetching Pokémon data:', error);
      }
    }

    async function fetchPokemons() {
      try {
        // Iterar desde el ID 1 hasta el ID 10 (para cargar los primeros 10 Pokémon)
        for (let i = 1; i <= 6; i++) {
          await fetchPokemon(i);
        }
      } catch (error) {
        console.error('Error fetching Pokémon data:', error);
      }
    }

    // Llamar a la función para cargar datos de los Pokémon cuando la página se carga
    fetchPokemons();
  });