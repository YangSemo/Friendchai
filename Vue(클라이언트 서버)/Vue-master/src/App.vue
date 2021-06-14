<template>
  <div id="app">
    <Header/>
    <!-- Header 크기 - Footer크기 -->
    <b-container fluid>
        <b-row style="height: 5vh;"></b-row>
    </b-container>
    <router-view style="background-color: #EDECEA"></router-view>

    <Footer />
    
  </div>   
</template>

<script>
import Header from '@/components/Layout/Header'
import Footer from '@/components/Layout/Footer'

export default {
  name: 'App',
  components: {
    Header,
    Footer,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
</style>
