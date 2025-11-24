<!-- Sidebar.vue -->
<template>
  <div id="sidebar">
    <h3>系统管理</h3>
    <ul>
      <li>
        <router-link exact active-class="active" to="/">首页</router-link>
      </li>
      <li>
        <router-link active-class="active" to="/userinfo">用户管理</router-link>
      </li>
      <li>
        <router-link active-class="active" to="/textcheck">错别字检测</router-link>
      </li>
      <li>
        <router-link active-class="active" to="/apitest">接口测试</router-link>
      </li>
      <li>
        <router-link active-class="active" to="/lottery">大乐透选号</router-link>
      </li>
      <li>
        <router-link active-class="active" to="/ball">双色球选号</router-link>
      </li>
      <li>
        <router-link active-class="active" to="/star">七星彩选号</router-link>
      </li>
      <li>
        <router-link active-class="active" to="/about">关于</router-link>
      </li>
      <li>
        <button class="logout-button" @click="logout()">退出登录</button>
      </li>
    </ul>
  </div>
</template>

<script>

import {MessageBox} from "element-ui";

export default {
  methods: {
    logout() {
      MessageBox.confirm('确认退出登录吗?', '提示', {
        confirmButtonText: '确认退出',
        cancelButtonText: '取消',
        type: "warning"
      }).then(() => {
        this.$http.post('http://127.0.0.1:9999/signout/')
          .then(response => {
            var res = JSON.parse(response.bodyText)
            if (res.result === 0) {
              this.$message.success(res.msg);
              localStorage.removeItem('user');
              this.$router.push('/login');
            } else {
              this.$message.error("登出失败");
            }
          })
      }).catch(() => {
        }
      )
    }
  }
}
</script>

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

.logout-button {
  background-color: #007bff;
  color: #ffffff;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.logout-button:hover {
  background-color: #0056b3;
}
</style>
<script setup>
</script>
