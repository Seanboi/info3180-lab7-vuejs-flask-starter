<template>
    <div class="movie-form-container">
      <form id="movieForm" @submit.prevent="saveMovie" class="movie-form">
        <h2 class="form-title">Add a New Movie</h2>
        <div class="form-group mb-3">
          <label for="title" class="form-label">Movie Title</label>
          <input type="text" v-model="title" class="form-control" required />
        </div>
        <div class="form-group mb-3">
          <label for="description" class="form-label">Description</label>
          <textarea v-model="description" class="form-control" required></textarea>
        </div>
        <div class="form-group mb-3">
          <label for="poster" class="form-label">Movie Poster</label>
          <input type="file" @change="onFileChange" class="form-control" required />
        </div>
        <button type="submit" class="btn btn-primary">Add Movie</button>
        <div v-if="message" class="alert alert-success mt-3">{{ message }}</div>
        <div v-if="errors.length" class="alert alert-danger mt-3">
          <ul>
            <li v-for="(error, index) in errors" :key="index">{{ error }}</li>
          </ul>
        </div>
      </form>
    </div>
  </template>
  
  <script setup>
    import { ref, onMounted } from 'vue';

    const title = ref('');
    const description = ref('');
    const poster = ref(null);
    const message = ref('');
    const errors = ref([]);
    const csrf_token = ref('');

    function getCsrfToken() {
    fetch('/api/v1/csrf-token')
    .then((response) => {
      if (!response.ok) {
        throw new Error(`Server error: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      console.log(data);
      csrf_token.value = data.csrf_token;
    })
    .catch(error => {
      console.error('Error fetching CSRF token:', error);
    });
};

    onMounted(() => {
        getCsrfToken();
});

  const onFileChange = (event) => {
    poster.value = event.target.files[0];
  };
  
  const saveMovie = async () => {
  let movieForm = document.getElementById('movieForm');
  let form_data = new FormData(movieForm);

  form_data.append('title', title.value);
  form_data.append('description', description.value);
  if (poster.value) {
    form_data.append('poster', poster.value);
  }
  
  try {
    const response = await fetch('/api/v1/movies', {
      method: 'POST',
      body: form_data,
      headers: {
        'X-CSRFToken': csrf_token.value
    }
    });
    const data = await response.json();
    
    if (response.ok) {
      // display a success message
      console.log(data);
      message.value = data.message || 'Movie added successfully!';
      errors.value = [];
      title.value = '';
      description.value = '';
      poster.value = null;
    } else {
      errors.value = data.errors || ['Failed to save the movie'];
      message.value = '';
    }
  } catch (error) {
    console.error('Error:', error);
    errors.value = ['An error occurred while saving the movie.'];
    message.value = '';
  }
};

  </script>
  
  <style scoped>
  .movie-form-container {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #f9f9f9;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  }
  
  .movie-form {
    display: flex;
    flex-direction: column;
  }
  
  .form-title {
    text-align: center;
    margin-bottom: 20px;
    font-size: 24px;
    color: #333;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  .form-label {
    font-weight: bold;
    margin-bottom: 5px;
  }
  
  .form-control {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 16px;
  }
  
  .form-control:focus {
    border-color: #007bff;
    outline: none;
    box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
  }
  
  .btn {
    padding: 10px 15px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
  }
  
  .btn:hover {
    background-color: #0056b3;
  }
  
  .alert {
    padding: 10px;
    border-radius: 4px;
    margin-top: 10px;
  }
  
  .alert-success {
    background-color: #d4edda;
    color: #155724;
    border: 1px solid #c3e6cb;
  }
  
  .alert-danger {
    background-color: #f8d7da;
    color: #721c24;
    border: 1px solid #f5c6cb;
  }
  </style>