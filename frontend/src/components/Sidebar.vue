<!-- Sidebar.vue -->
<template>
  <div id="sidebar">
    <h3>系统管理</h3>
    <ul>
      <li><router-link exact active-class="active" to="/">首页</router-link></li>
      <li><router-link active-class="active" to="/userinfo">用户管理</router-link></li>
      <li><router-link active-class="active" to="/textcheck">错别字检测</router-link></li>
      <li><router-link active-class="active" to="/apitest">接口测试</router-link></li>
      <li><router-link active-class="active" to="/about">关于</router-link></li>
    </ul>
  </div>
</template>

<style scoped>
#sidebar {
  width: 200px;
  height: 100vh;
  position: fixed;
  left: 0;
  top: 0;
  background-color: #343a40;
  padding: 20px;
  box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
  color: #f8f9fa;
}

#sidebar h3 {
  margin-bottom: 20px;
}

#sidebar ul {
  list-style-type: none;
  padding: 0;
}

#sidebar ul li {
  margin-bottom: 10px;
}

#sidebar ul li a {
  color: #f8f9fa;
  text-decoration: none;
  transition: color 0.3s ease;
  height: 50px;
  line-height: 50px;
}

#sidebar ul li a:hover,
#sidebar ul li a.active {
  color: #007bff;
}
</style>
<script setup>
</script>
