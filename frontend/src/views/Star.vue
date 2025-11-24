<template>

  <div class="home">
    <h1 class="title">七星彩摇号</h1>

    <el-row display="margin-top:10px">
      <el-button type="primary" @click="generateLottery(1)" style="float:left; margin: 2px;">机选1注</el-button>
      <el-button type="primary" @click="generateLottery(5)" style="float:left; margin: 2px;">机选5注</el-button>
      <el-button type="primary" @click="generateLottery(10)" style="float:left; margin: 2px;">机选10注</el-button>
    </el-row>

    <el-row>
      <el-table :data="tableData" style="width: 100%" border>
        <el-table-column label="注数" min-width="100" :header-cell-style="{fontWeight: 'bold'}"
                         :cell-style="{fontWeight: 'bold'}">
          <template v-slot:default="scope">
            <span>{{ scope.$index + 1 }}</span>
          </template>
        </el-table-column>

        <el-table-column label="前区结果" min-width="100" :header-cell-style="{fontWeight: 'bold'}"
                         :cell-style="{fontWeight: 'bold'}">
          <template v-slot:default="scope">
            <span>{{ scope.row.front_list }}</span>
          </template>
        </el-table-column>

        <el-table-column label="后区结果" min-width="100" :header-cell-style="{fontWeight: 'bold'}"
                         :cell-style="{fontWeight: 'bold'}">
          <template v-slot:default="scope">
            <span>{{ scope.row.behind_list }}</span>
          </template>
        </el-table-column>
      </el-table>
    </el-row>

  </div>

</template>


<script>
import axios from "axios";

export default {
  name: 'home',
  computed: {},
  data() {
    return {
      tableData: []
    }
  },
  mounted: function () {
  },

  methods: {
    generateLottery(num) {
      axios.get('http://127.0.0.1:9999/star/?num=' + num)
        .then((response) => {
          var res = response.data
          if (res.result === 1) {
            this.$message.error(res.msg);
          } else {
            this.tableData = res.data;
          }
        })
        .catch((error) => {
          console.error(error)
          this.$message.error('请求失败，请检查网络连接或服务器状态')
        })
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


h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>


