<template>
    <div class="movies-container">
      <h1 class="page-title">Movies</h1>
      
      <div v-if="loading" class="loading">
        Loading movies...
      </div>
      
      <div v-else-if="error" class="error-message">
        {{ error }}
      </div>
      
      <div v-else-if="movies.length === 0" class="no-movies">
        No movies found. Add some movies to see them here!
      </div>
      
      <div v-else class="movies-list">
        <div v-for="(movie, index) in movies" :key="movie.id" class="movie-card" :class="{ 'right-column': index % 2 !== 0 }">
          <div class="movie-poster">
            <img :src="movie.poster" :alt="movie.title" class="poster-image">
          </div>
          <div class="movie-info">
            <h3 class="movie-title">{{ movie.title }}</h3>
            <p class="movie-description">{{ movie.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  
  const movies = ref([]);
  const loading = ref(true);
  const error = ref(null);
  
  const fetchMovies = async () => {
    try {
      const response = await fetch('/api/v1/movies');
      
      if (!response.ok) {
        throw new Error(`Server error: ${response.status}`);
      }
      
      const data = await response.json();
      movies.value = data.movies;
      loading.value = false;
    } catch (err) {
      console.error('Error fetching movies:', err);
      error.value = 'Failed to fetch movies. Please try again later.';
      loading.value = false;
    }
  };
  
  onMounted(() => {
    fetchMovies();
  });
  </script>
  
  <style scoped>
  .movies-container {
    padding: 20px;
    max-width: 1200px;
    margin: 0 auto;
  }
  
  .page-title {
    margin-bottom: 30px;
    color: #333;
    font-size: 24px;
    font-weight: bold;
  }
  
  .loading, .error-message, .no-movies {
    text-align: center;
    padding: 20px;
    font-size: 18px;
  }
  
  .error-message {
    color: #721c24;
    background-color: #f8d7da;
    border-radius: 4px;
    padding: 15px;
  }
  
  .movies-list {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
  }
  
  .movie-card {
    display: flex;
    border: 1px solid #ddd;
    border-radius: 4px;
    overflow: hidden;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .movie-poster {
    flex: 0 0 130px;
    height: 180px;
  }
  
  .poster-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  
  .movie-info {
    flex: 1;
    padding: 15px;
  }
  
  .movie-title {
    font-size: 18px;
    margin-bottom: 10px;
    color: #333;
  }
  
  .movie-description {
    color: #666;
    line-height: 1.4;
    font-size: 14px;
  }
  
  @media (max-width: 768px) {
    .movies-list {
      grid-template-columns: 1fr;
    }
  }
  </style>