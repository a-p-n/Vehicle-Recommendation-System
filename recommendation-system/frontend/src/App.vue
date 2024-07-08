<template>
  <div id="app">
    <RandomCarList />
  </div>
</template>

<script>
import RandomCarList from './components/randomCarList.vue';

export default {
  name: 'App',
  components: {
    RandomCarList,
  },
};
</script>

<style>
  body {
    font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #ffffff;
    margin: 0;
    padding: 0;
  }
</style>
