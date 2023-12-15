<template>
  <div id="app" class="login-container">
    <h2 class="login-title">用户登录</h2>
    <form @submit.prevent="submitForm" class="login-form">
      <div class="form-group">
        <label for="username" class="form-label">用户:</label>
        <input type="text" id="username" v-model="username" class="form-input">
      </div>
      <div class="form-group">
        <label for="password" class="form-label">密码:</label>
        <input type="password" id="password" v-model="password" class="form-input">
      </div>
      <button type="submit" class="submit-button">Login</button>
    </form>
  </div>
</template>


<script>
export default {
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    submitForm() {
      // Handle the form submission here
      if (this.username === "" || this.password === "") {
        this.$message.warning("用户名或者密码不能为空")
      } else {
        this.$http.post('http://127.0.0.1:9999/signin/', {
          username: this.username,
          password: this.password
        }, {headers: {'Content-Type': 'application/json'}})
          .then((response) => {
              var res = JSON.parse(response.bodyText)
              if (res.result === 0) {
                this.$message.success(res.msg)
                localStorage.setItem('user', JSON.stringify(res.user))
                this.$router.push(this.$route.query.redirect || '/')
              } else {
                this.$message.error(res.msg)
              }
            }
          )
      }
    }
  }
}
</script>


<style scoped>

.login-container {
  width: 100%;
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  box-sizing: border-box;
  font-family: 'Roboto', sans-serif;
  background: linear-gradient(to right, #ff9966, #ff5e62);
  border-radius: 10px;
  box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.2);
  border: 1px solid #ccc;
}

.login-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 20px;
}

.form-input {
  padding: 10px;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  box-shadow: 0px 0px 5px 0px rgba(0,0,0,0.1);
}

.form-input:focus {
  box-shadow: 0px 0px 5px 0px rgba(0,0,0,0.2);
}

.submit-button {
  padding: 10px 20px;
  background-color: #007BFF;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease;
}

.submit-button:hover {
  background-color: #0056b3;
}
</style>



