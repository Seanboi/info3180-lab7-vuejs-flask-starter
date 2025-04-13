<template>
    <div class="add-movie-form-container">
      <h1 class="form-title">Add a New Movie</h1>
      <MovieForm />
    </div>
  </template>
  
  <script setup>
  import MovieForm from '../components/MovieForm.vue';
  </script>
  
  <style scoped>
  .add-movie-form-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  }
  
  .form-title {
    text-align: center;
    margin-bottom: 20px;
    font-size: 28px;
    color: #333;
  }
  </style>