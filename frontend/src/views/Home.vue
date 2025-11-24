<template>
  <div class="home">
    <h1 class="title">欢迎来到我的个人主页,我将用最真诚的服务, 来给用户带来最极致的体验</h1>
    <p class="description">在这里，您可以找到我们产品的最新消息、更新和功能。我们致力于为用户提供最好的服务和体验。</p>
    <div class="features">
      <h2 class="subtitle">Features</h2>
      <ul>
        <li>我们可以提供足浴按摩</li>
        <li>我们可以提供双色球大乐透选号</li>
        <li>我们可以提供肯德基代吃服务</li>
      </ul>
    </div>
    <div class="buttons">
      <button class="btn" @click="goToAbout">关于我们</button>
      <button class="btn" @click="goToAbout">关于他们</button>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    goToAbout() {
      this.$router.push('/about');
    },
  }
}
</script>

<style scoped>
.home {
  text-align: center;
  color: #333;
  font-family: 'Helvetica Neue', Arial, sans-serif;
  padding: 20px;
}

.title {
  color: #007BFF;
  font-size: 2em;
  margin-bottom: 20px;
}

.description {
  font-size: 1.2em;
  margin-bottom: 40px;
}

.subtitle {
  color: #007BFF;
  font-size: 1.5em;
  margin-bottom: 20px;
}

.features ul {
  list-style-type: none;
  padding: 0;
}

.buttons {
  margin: 40px 0;
}

.btn {
  margin: 10px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  background-color: #007BFF;
  color: white;
  border: none;
  border-radius: 4px;
  transition: background-color 0.3s ease;
}

.btn:hover {
  background-color: #0056b3;
}

.features ul li {
  margin: 10px 0;
}

</style>
