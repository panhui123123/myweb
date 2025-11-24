<template>
  <div id="app">
    <nav v-if="$route.name !== 'login'">
      <Sidebar/>
    </nav>
    <div id="navbar" v-if="$route.name !== 'login'">
      <div id="breadcrumbs">
        <span v-for="(route, index) in $route.matched" :key="index">
          <router-link :to="route.path">{{ route.meta.breadcrumb }}</router-link>
          <span v-if="index < $route.matched.length - 1"> / </span>
        </span>
      </div>
    </div>
    <router-view/>
  </div>
</template>

<script>
import Sidebar from './components/Sidebar.vue'

export default {
  components: {
    Sidebar
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

#navbar {
  position: fixed;
  right: 0;
  top: 0;
  width: calc(100% - 240px); /* Adjust as needed */
  background-color: dodgerblue;
  height: 50px;
}

#navbar ul {
  list-style-type: none;
  padding: 0;
  display: flex;
  justify-content: space-around;
}

#navbar li {
  padding: 8px;
  margin-bottom: 7px;
  background-color: dodgerblue;
  color: #ffffff;
  box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
}

#navbar li:hover {
  background-color: #0099cc;
}

#breadcrumbs {
  padding: 10px;
  text-align: left;
}
</style>
