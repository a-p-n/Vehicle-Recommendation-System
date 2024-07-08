<template>
    <div>
      <h1>Select the cars you like</h1>
      <div class="comp-div">
        <ul class="comp-ul">
          <li class="comp" v-for="car in randomCars" :key="car.id" @click="selectCar(car.id)">
            <img :src="car.photo" alt="Car Photo" />
            {{ car.id }} {{ car.make }} {{ car.model }} ({{ car.year }})
          </li>
        </ul>
      </div>
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
      selectCar(carId) {
        axios.post('http://localhost:8000/select-car/', { id: carId })
          .then(response => {
            console.log('Car selected:', response.data);
          })
          .catch(error => {
            console.error('Error selecting car:', error);
          });
      },
    },
  };
  </script>
  
  <style scoped>
  .comp-div {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
  }
  .comp {
    list-style-type: none;
    margin: 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    cursor: pointer;  /* Add pointer cursor to indicate clickable items */
  }
  .comp-ul {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }
  </style>
  