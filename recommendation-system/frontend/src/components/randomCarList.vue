<!-- frontend/src/components/RandomCarList.vue -->

<template>
    <div>
      <h1>Random Car List</h1>
      <ul>
        <li v-for="car in randomCars" :key="car.id">
          <img :src="car.photo" alt="Car Photo" />
          {{ car.make }} {{ car.model }} ({{ car.year }})
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        randomCars: [],
      };
    },
    mounted() {
      this.fetchRandomCars();
    },
    methods: {
      fetchRandomCars() {
        axios.get('http://localhost:8000/random-car-list/')
          .then(response => {
            this.randomCars = response.data.cars;  // Corrected JSON key
          })
          .catch(error => {
            console.error('Error fetching random cars:', error);
          });
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add your component-specific styles here */
  </style>
  