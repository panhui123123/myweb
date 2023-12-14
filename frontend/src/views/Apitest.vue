<template>
  <div class="home">
    <h1 class="title">接口测试平台</h1>

    <el-row display="margin-top:10px">
      <el-input v-model="url" placeholder="请输入接口URL"
                style="display:inline-table; width: 30%; float:left"></el-input>
      <el-select v-model="method" placeholder="选择请求类型">
        <el-option label="GET" value="get"></el-option>
        <el-option label="POST" value="post"></el-option>
      </el-select>
      <el-button type="primary" @click="sendRequest()" style="float:left; margin: 2px;">发送请求</el-button>
    </el-row>

    <el-row>
      <el-table :data="tableData" style="width: 100%" border>
        <el-table-column label="请求URL" min-width="100">
          <template v-slot:default="scope">
            <span>{{scope.row.url}}</span>
          </template>
        </el-table-column>

        <el-table-column label="请求类型" min-width="100">
          <template v-slot:default="scope">
            <span>{{scope.row.method}}</span>
          </template>
        </el-table-column>

        <el-table-column label="返回结果" min-width="100">
          <template v-slot:default="scope">
            <span>{{scope.row.result}}</span>
          </template>
        </el-table-column>
      </el-table>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'home',
  data() {
    return {
      url: '',
      method: '',
      tableData: []
    }
  },
  methods: {
    sendRequest() {
      if (this.url === '' || this.method === '') {
        this.$message.warning("URL和请求类型不能为空");
      } else {
        this.$http[this.method](this.url)
          .then((response) => {
            this.tableData.push({url: this.url, method: this.method, result: JSON.stringify(response.body)})
          })
          .catch((error) => {
            this.$message.error('请求失败')
            console.log(error)
          })
      }
    }
  }
}
</script>

<style scoped>
.title {
  font-size: 2em;
  color: #333;
  margin-bottom: 20px;
}

.home {
  padding: 20px;
  box-sizing: border-box;
  margin-left: 300px;
}
</style>
